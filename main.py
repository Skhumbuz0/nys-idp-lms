import re
import json
from pathlib import Path
from datetime import datetime
from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import func
from database import Base, engine, get_db
from models import Participant, Question, QuizResponse, DailyResponse

app = FastAPI(title="NYS IDP LMS")

# FIX: Use Path object and explicit keyword arguments to prevent Jinja2 caching errors
templates = Jinja2Templates(directory=Path("templates"))

# ==========================================
# THE 30-DAY CURRICULUM ENGINE
# ==========================================
CURRICULUM = {
    1: {"week": 1, "title": "Start With Yourself", "questions": [
        {"id": "improve", "type": "checkbox", "label": "What do you currently want to improve most in your life?", "options": ["Education", "Career", "Employment", "Business", "Finances", "Leadership", "Skills", "Confidence", "Community impact", "Other"]},
        {"id": "satisfaction", "type": "scale", "label": "On a scale of 1–10, how satisfied are you with where you are currently in life?", "min": 1, "max": 10},
        {"id": "score_reason", "type": "paragraph", "label": "Why did you choose this score?"},
        {"id": "change_30", "type": "paragraph", "label": "What is one thing you want to change during the next 30 days?"}
    ], "action": "Complete your personal life audit.", "reflection": "What did you discover about yourself today?"},
    2: {"week": 1, "title": "Discover Your Vision", "questions": [
        {"id": "vision_1", "type": "paragraph", "label": "Imagine your life 10 years from now. Where are you living and what work are you doing?"},
        {"id": "vision_2", "type": "paragraph", "label": "What skills do you have, and what does your financial life look like?"},
        {"id": "vision_3", "type": "paragraph", "label": "Who are you helping, and what kind of person have you become?"},
        {"id": "ideal_future", "type": "paragraph", "label": "Describe your ideal future in your own words."}
    ], "action": "Write down your 10-year vision and place it where you will see it daily.", "reflection": "How did it feel to vividly imagine this future?"},
    3: {"week": 1, "title": "Find Your Definite Purpose", "questions": [
        {"id": "stand_for", "type": "paragraph", "label": "What do you want your life to stand for?"},
        {"id": "purpose_statement", "type": "paragraph", "label": "Complete this sentence: 'My purpose is to...'", "placeholder": "My purpose is to..."},
        {"id": "benefit", "type": "paragraph", "label": "Who will benefit from your purpose, and what problem do you want to help solve?"},
        {"id": "why_important", "type": "paragraph", "label": "Why is this important to you?"}
    ], "action": "Write your final Definite Purpose statement on a card.", "reflection": "How does having a clear purpose change your mindset?"},
    4: {"week": 1, "title": "Define Your Desire", "questions": [
        {"id": "exactly_what", "type": "paragraph", "label": "What exactly do you want to achieve?"},
        {"id": "why_want", "type": "paragraph", "label": "Why do you want it?"},
        {"id": "how_change", "type": "paragraph", "label": "How will achieving it change your life, and who else could benefit?"}
    ], "action": "Write down your biggest goal in one clear sentence.", "reflection": "Is this goal truly yours, or someone else's expectation?"},
    5: {"week": 1, "title": "Put a Number on Your Goal", "questions": [
        {"id": "amount", "type": "text", "label": "How much money do you want to earn/save/create? (R_______)"},
        {"id": "date", "type": "date", "label": "By what exact date will you achieve this?"},
        {"id": "give_return", "type": "paragraph", "label": "What will you give in return for achieving this goal? (Value exchange)"}
    ], "action": "Finalize your specific, measurable, time-bound goal.", "reflection": "Does the value you are offering match the reward you seek?"},
    6: {"week": 1, "title": "What Will You Give in Return?", "questions": [
        {"id": "value_type", "type": "checkbox", "label": "What skills, products, services or solutions can you offer?", "options": ["My knowledge", "My technical skills", "My creativity", "My labour", "My business", "My leadership", "My ability to solve problems", "My network", "Something else"]},
        {"id": "value_desc", "type": "paragraph", "label": "Describe the specific value you can create for other people."}
    ], "action": "Identify one person or group you can serve with this value this week.", "reflection": "How does focusing on service shift your perspective on making money?"},
    7: {"week": 1, "title": "Set the Deadline", "questions": [
        {"id": "goal_summary", "type": "paragraph", "label": "Goal & Amount/Outcome:"},
        {"id": "deadline", "type": "date", "label": "Deadline:"},
        {"id": "action_1", "type": "text", "label": "First action:"},
        {"id": "action_2", "type": "text", "label": "Second action:"},
        {"id": "action_3", "type": "text", "label": "Third action:"},
        {"id": "commitment", "type": "radio", "label": "Are you willing to commit to this goal?", "options": ["Yes", "I'm still deciding", "No"]}
    ], "action": "Sign and date your commitment.", "reflection": "What is the cost of NOT committing to this?"},
    8: {"week": 2, "title": "Faith", "questions": [
        {"id": "holding_back", "type": "paragraph", "label": "What belief about yourself is currently holding you back?"},
        {"id": "believe_instead", "type": "paragraph", "label": "What would you need to believe instead to move forward?"}
    ], "action": "Write down your new empowering belief and read it aloud 3 times.", "reflection": "Where did this limiting belief originally come from?"},
    9: {"week": 2, "title": "Visualization", "questions": [
        {"id": "visualize_where", "type": "paragraph", "label": "Describe yourself after achieving your goal. Where are you and what are you doing?"},
        {"id": "visualize_help", "type": "paragraph", "label": "Who are you helping, what have you learned, and what have you built?"}
    ], "action": "Spend 5 minutes in quiet visualization of this exact scene.", "reflection": "What emotions arose during your visualization?"},
    10: {"week": 2, "title": "Self-Talk", "questions": [
        {"id": "iam", "type": "text", "label": "'I am becoming...'", "placeholder": "I am becoming..."},
        {"id": "iwill", "type": "text", "label": "'I will...'", "placeholder": "I will..."},
        {"id": "ican", "type": "text", "label": "'I can...'", "placeholder": "I can..."},
        {"id": "igive", "type": "text", "label": "'I will give...'", "placeholder": "I will give..."},
        {"id": "mypurpose", "type": "text", "label": "'My purpose is...'", "placeholder": "My purpose is..."}
    ], "action": "Record yourself reading this declaration and listen to it tomorrow morning.", "reflection": "How does speaking these words aloud affect your confidence?"},
    11: {"week": 2, "title": "Control Your Inputs", "questions": [
        {"id": "consuming", "type": "checkbox", "label": "What are you currently consuming? (Select all that apply)", "options": ["Social media", "YouTube", "TikTok", "News", "Books", "Podcasts", "Friends", "Conversations"]},
        {"id": "helping", "type": "paragraph", "label": "Which influences are helping you?"},
        {"id": "holding_back", "type": "paragraph", "label": "Which influences are holding you back?"},
        {"id": "reduce_increase", "type": "paragraph", "label": "What will you reduce, and what will you increase?"}
    ], "action": "Unfollow or mute 3 negative influences today.", "reflection": "How much time did you reclaim by auditing your inputs?"},
    12: {"week": 2, "title": "Identify Knowledge Gaps", "questions": [
        {"id": "gap_1", "type": "paragraph", "label": "Gap 1: What I want to achieve | What I need to know | How I'll learn"},
        {"id": "gap_2", "type": "paragraph", "label": "Gap 2: What I want to achieve | What I need to know | How I'll learn"},
        {"id": "gap_3", "type": "paragraph", "label": "Gap 3: What I want to achieve | What I need to know | How I'll learn"}
    ], "action": "Enroll in one course, buy one book, or book one mentor call.", "reflection": "Why is it empowering to admit what you don't know?"},
    13: {"week": 2, "title": "Build Your Learning Plan", "questions": [
        {"id": "learn_1", "type": "paragraph", "label": "Knowledge Gap 1 → Resource → Person → Deadline"},
        {"id": "learn_2", "type": "paragraph", "label": "Knowledge Gap 2 → Resource → Person → Deadline"},
        {"id": "learn_3", "type": "paragraph", "label": "Knowledge Gap 3 → Resource → Person → Deadline"}
    ], "action": "Schedule your first learning session in your calendar.", "reflection": "What is the first step to executing this plan?"},
    14: {"week": 2, "title": "Exercise Your Imagination", "questions": [
        {"id": "community_problem", "type": "paragraph", "label": "Identify one real-world problem in your community."},
        {"id": "ten_solutions", "type": "paragraph", "label": "Write 10 possible solutions to this problem."}
    ], "action": "Share your best solution with one person for feedback.", "reflection": "Which of the 10 solutions excited you the most?"},
    15: {"week": 3, "title": "Choose Your Best Idea", "questions": [
        {"id": "score_importance", "type": "scale", "label": "Score (1-5): Importance", "min": 1, "max": 5},
        {"id": "score_people", "type": "scale", "label": "Score (1-5): Number of people affected", "min": 1, "max": 5},
        {"id": "score_feasibility", "type": "scale", "label": "Score (1-5): Feasibility", "min": 1, "max": 5},
        {"id": "score_affordability", "type": "scale", "label": "Score (1-5): Affordability", "min": 1, "max": 5},
        {"id": "score_value", "type": "scale", "label": "Score (1-5): Value", "min": 1, "max": 5},
        {"id": "score_interest", "type": "scale", "label": "Score (1-5): Personal interest", "min": 1, "max": 5},
        {"id": "score_growth", "type": "scale", "label": "Score (1-5): Growth potential", "min": 1, "max": 5}
    ], "action": "Select the highest-scoring idea to move forward with.", "reflection": "Why did this idea score the highest?"},
    16: {"week": 3, "title": "Define the Problem", "questions": [
        {"id": "prob_what", "type": "paragraph", "label": "What problem are you solving?"},
        {"id": "prob_who", "type": "paragraph", "label": "Who experiences it?"},
        {"id": "prob_current", "type": "paragraph", "label": "How are people currently solving it, and why isn't it good enough?"}
    ], "action": "Interview one person who experiences this problem.", "reflection": "What surprised you about their current struggle?"},
    17: {"week": 3, "title": "Design Your Solution", "questions": [
        {"id": "sol_offering", "type": "paragraph", "label": "What are you offering and who is the customer/user?"},
        {"id": "sol_how", "type": "paragraph", "label": "How does it work, and what resources/skills do you need?"},
        {"id": "sol_cost_value", "type": "paragraph", "label": "What could it cost, and how could it create income/value?"}
    ], "action": "Sketch a simple prototype or mockup of your solution.", "reflection": "What is the biggest risk in this solution?"},
    18: {"week": 3, "title": "Build Your Action Plan", "questions": [
        {"id": "plan_1", "type": "paragraph", "label": "Action 1 → Person responsible → Resources → Deadline → Measure"},
        {"id": "plan_2", "type": "paragraph", "label": "Action 2 → Person responsible → Resources → Deadline → Measure"},
        {"id": "plan_3", "type": "paragraph", "label": "Action 3 → Person responsible → Resources → Deadline → Measure"}
    ], "action": "Execute Action 1 today.", "reflection": "What friction did you encounter when planning?"},
    19: {"week": 3, "title": "Build Your Master Mind", "questions": [
        {"id": "mm_role", "type": "checkbox", "label": "Who can help you? (Select roles needed)", "options": ["Mentor", "Technical expert", "Business person", "Friend/accountability partner", "Industry contact", "Financial adviser", "Teacher/lecturer", "Community leader", "Other"]},
        {"id": "mm_contribute", "type": "paragraph", "label": "What can this person contribute?"},
        {"id": "mm_give", "type": "paragraph", "label": "What can YOU contribute to the relationship?"}
    ], "action": "Send a message to your first Master Mind candidate today.", "reflection": "Why is mutual value critical in a Master Mind?"},
    20: {"week": 3, "title": "Make a Decision", "questions": [
        {"id": "dec_postpone", "type": "paragraph", "label": "What important decision have you been postponing, and why?"},
        {"id": "dec_info", "type": "paragraph", "label": "What information do you still need?"},
        {"id": "dec_final", "type": "paragraph", "label": "My decision is: __________"}
    ], "action": "Communicate your decision to the relevant person.", "reflection": "How does it feel to finally decide?"},
    21: {"week": 3, "title": "TAKE ACTION", "questions": [
        {"id": "act_did", "type": "checkbox", "label": "What did you actually do?", "options": ["Called someone", "Sent an email", "Applied for something", "Registered", "Interviewed someone", "Started saving", "Built something", "Tested an idea", "Created a prototype", "Started learning", "Contacted a mentor", "Other"]},
        {"id": "act_desc", "type": "paragraph", "label": "Describe what happened."},
        {"id": "act_evidence", "type": "file", "label": "Upload evidence of your action (Image/PDF)"}
    ], "action": "Celebrate this win, no matter how small.", "reflection": "What did taking this action teach you about yourself?"},
    22: {"week": 4, "title": "Persistence", "questions": [
        {"id": "pers_purpose", "type": "scale", "label": "Score (1-10): Definite purpose", "min": 1, "max": 10},
        {"id": "pers_desire", "type": "scale", "label": "Score (1-10): Desire", "min": 1, "max": 10},
        {"id": "pers_self", "type": "scale", "label": "Score (1-10): Self-reliance", "min": 1, "max": 10},
        {"id": "pers_plan", "type": "scale", "label": "Score (1-10): Planning", "min": 1, "max": 10},
        {"id": "pers_know", "type": "scale", "label": "Score (1-10): Knowledge", "min": 1, "max": 10},
        {"id": "pers_coop", "type": "scale", "label": "Score (1-10): Cooperation", "min": 1, "max": 10},
        {"id": "pers_will", "type": "scale", "label": "Score (1-10): Willpower", "min": 1, "max": 10},
        {"id": "pers_disc", "type": "scale", "label": "Score (1-10): Discipline/habit", "min": 1, "max": 10},
        {"id": "pers_weak", "type": "paragraph", "label": "Which THREE areas are weakest, and what will you do to strengthen each one?"}
    ], "action": "Implement one habit to strengthen your weakest area.", "reflection": "Why is persistence a habit, not a trait?"},
    23: {"week": 4, "title": "Identify Your Excuses", "questions": [
        {"id": "excuse_use", "type": "radio", "label": "What excuse do you use most often?", "options": ["I don't have money", "I don't have time", "I don't know enough", "I'm waiting for the right opportunity", "I'm afraid of failing", "I'm afraid of what people will say", "I don't have connections", "I'll start tomorrow", "Other"]},
        {"id": "excuse_proof", "type": "paragraph", "label": "What action would prove that this excuse is not permanent?"}
    ], "action": "Take the action that proves your excuse wrong.", "reflection": "How does it feel to dismantle your own excuse?"},
    24: {"week": 4, "title": "Fear of Poverty", "questions": [
        {"id": "pov_mean", "type": "paragraph", "label": "What does financial insecurity mean to you?"},
        {"id": "pov_action", "type": "checkbox", "label": "What financial action will you take?", "options": ["Create a budget", "Start saving", "Reduce unnecessary spending", "Learn a new income skill", "Apply for work", "Start a small business activity", "Research an opportunity", "Speak to someone financially knowledgeable"]}
    ], "action": "Execute your chosen financial action today.", "reflection": "How does taking control reduce the fear?"},
    25: {"week": 4, "title": "Fear of Criticism", "questions": [
        {"id": "crit_avoid", "type": "paragraph", "label": "What are you currently avoiding because you are worried about what people will think?"},
        {"id": "crit_constructive", "type": "paragraph", "label": "What constructive action will you take anyway?"}
    ], "action": "Do the thing you are avoiding, despite the fear.", "reflection": "Was the criticism as bad as you imagined?"},
    26: {"week": 4, "title": "Beat Procrastination", "questions": [
        {"id": "proc_task", "type": "paragraph", "label": "Identify one task you've been postponing."},
        {"id": "proc_small", "type": "paragraph", "label": "What is the smallest action you can take in the next 5 minutes?"},
        {"id": "proc_did", "type": "radio", "label": "Did you do it?", "options": ["Yes", "No"]},
        {"id": "proc_happened", "type": "paragraph", "label": "What happened?"}
    ], "action": "Set a 5-minute timer and do it right now.", "reflection": "What is the true cost of procrastination?"},
    27: {"week": 4, "title": "Failure → Lesson → Action", "questions": [
        {"id": "fail_what", "type": "paragraph", "label": "What happened? (Describe a recent setback)"},
        {"id": "fail_learn", "type": "paragraph", "label": "What did I learn?"},
        {"id": "fail_diff", "type": "paragraph", "label": "What will I do differently?"},
        {"id": "fail_next", "type": "paragraph", "label": "What action will I take next?"}
    ], "action": "Apply the lesson to your current plan.", "reflection": "How is failure just data?"},
    28: {"week": 4, "title": "Master Mind Check", "questions": [
        {"id": "mm_spoke", "type": "paragraph", "label": "Who did you speak to about your goal?"},
        {"id": "mm_told", "type": "paragraph", "label": "What did they tell you, and what did you learn?"},
        {"id": "mm_change", "type": "paragraph", "label": "What will you change, and who else should you speak to?"}
    ], "action": "Schedule your next Master Mind check-in.", "reflection": "How has external input improved your plan?"},
    29: {"week": 4, "title": "Build Your 90-Day Plan", "questions": [
        {"id": "90_g1", "type": "paragraph", "label": "Goal 1: Outcome, Why, Actions, Resources, People, Deadline, Measurement"},
        {"id": "90_g2", "type": "paragraph", "label": "Goal 2: Outcome, Why, Actions, Resources, People, Deadline, Measurement"},
        {"id": "90_g3", "type": "paragraph", "label": "Goal 3: Outcome, Why, Actions, Resources, People, Deadline, Measurement"}
    ], "action": "Save this plan and review it every Sunday.", "reflection": "How does a 90-day horizon feel compared to 10 years?"},
    30: {"week": 4, "title": "Your Commitment", "questions": [
        {"id": "final_commit", "type": "paragraph", "label": "Congratulations. You have spent 30 days turning ideas into action. Write your final, unbreakable commitment to your future self."}
    ], "action": "Print or save your final commitment. The real work begins now.", "reflection": "Who have you become over the last 30 days?"}
}

# ==========================================
# UTILITIES
# ==========================================
def generate_participant_id(db) -> str:
    highest = 0
    for (pid,) in db.query(Participant.participant_id).all():
        if pid:
            match = re.search(r'(\d+)$', pid)
            if match and int(match.group(1)) > highest:
                highest = int(match.group(1))
    return f"NYS-2026-{str(highest + 1).zfill(4)}"

def update_participant_progress(db, participant_id: str):
    p = db.query(Participant).filter(Participant.participant_id == participant_id).first()
    if not p: return
    
    progress = 5.0 if p.registration_complete else 0.0
    quizzes = db.query(QuizResponse).filter(QuizResponse.participant_id == participant_id).all()
    progress += len({q.week for q in quizzes}) * 11.25
    
    actions = db.query(DailyResponse).filter(DailyResponse.participant_id == participant_id).all()
    unique_days = len({a.day for a in actions})
    action_pct = min(100.0, (unique_days / 30.0) * 100)
    progress += (action_pct / 100.0) * 40.0
    
    if p.final_idp_complete: progress += 10.0
    progress = min(100.0, progress)
    
    p.overall_progress_pct = progress
    p.day30_action_progress_pct = action_pct
    p.day30_completed_days = unique_days
    
    if unique_days >= 7: p.week1_actions_complete = True
    if unique_days >= 14: p.week2_actions_complete = True
    if unique_days >= 21: p.week3_actions_complete = True
    if unique_days >= 30: p.week4_actions_complete = True
    
    if quizzes:
        p.overall_quiz_pct = (sum(q.score for q in quizzes) / sum(q.max_score for q in quizzes)) * 100
    
    if unique_days == 0 and not quizzes:
        p.risk_status, p.risk_reason = "Not Started", ""
    elif action_pct < 30 or (p.overall_quiz_pct or 0) < 40:
        p.risk_status, p.risk_reason = "At Risk", "Low engagement in actions or quizzes"
    elif action_pct < 60 or (p.overall_quiz_pct or 0) < 60:
        p.risk_status, p.risk_reason = "Needs Attention", "Below expected weekly threshold"
    else:
        p.risk_status, p.risk_reason = "On Track", ""
        
    p.last_activity = datetime.utcnow()
    db.commit()

# ==========================================
# ROUTES
# ==========================================
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(name="home.html", context={"request": request})

@app.get("/register", response_class=HTMLResponse)
def register_form(request: Request):
    return templates.TemplateResponse(name="register.html", context={"request": request})

@app.post("/register")
def process_register(request: Request, db = Depends(get_db), full_name: str = Form(...), email: str = Form(...), phone: str = Form(""), age_range: str = Form(...), main_goal: str = Form(...)):
    pid = generate_participant_id(db)
    new_p = Participant(
        participant_id=pid, full_name=full_name, email=email.lower(), phone=phone, 
        age_range=age_range, main_goal=main_goal, registration_complete=True, last_activity=datetime.utcnow()
    )
    db.add(new_p)
    db.commit()
    update_participant_progress(db, pid)
    return templates.TemplateResponse(name="register_success.html", context={"request": request, "pid": pid})

@app.get("/daily-action", response_class=HTMLResponse)
def daily_action_hub(request: Request, db = Depends(get_db)):
    return templates.TemplateResponse(name="daily_action_hub.html", context={"request": request, "curriculum": CURRICULUM})

@app.get("/daily-action/{day}", response_class=HTMLResponse)
def daily_action_form(request: Request, day: int):
    if day < 1 or day > 30:
        raise HTTPException(status_code=404, detail="Day out of range")
    return templates.TemplateResponse(name="daily_action.html", context={"request": request, "day": day, "day_data": CURRICULUM[day]})

@app.post("/daily-action/{day}")
async def process_daily_action(day: int, request: Request, db = Depends(get_db)):
    form_data = await request.form()
    pid = form_data.get("participant_id")
    
    responses = {}
    for key, value in form_data.items():
        if key.startswith("q_"):
            responses[key] = value
            
    action_status = form_data.get("action_status", "No")
    reflection = form_data.get("reflection", "")
    
    evidence_file = form_data.get("evidence_file")
    filename = None
    if evidence_file and hasattr(evidence_file, 'filename') and evidence_file.filename:
        filename = evidence_file.filename

    existing = db.query(DailyResponse).filter(DailyResponse.participant_id == pid, DailyResponse.day == day).first()
    
    if existing:
        existing.responses_json = json.dumps(responses)
        existing.action_status = action_status
        existing.reflection = reflection
        if filename: existing.evidence_file = filename
    else:
        new_response = DailyResponse(
            participant_id=pid, day=day, responses_json=json.dumps(responses),
            action_status=action_status, reflection=reflection, evidence_file=filename
        )
        db.add(new_response)
        
    db.commit()
    update_participant_progress(db, pid)
    
    next_day = day + 1
    if next_day <= 30:
        return RedirectResponse(url=f"/daily-action/{next_day}", status_code=303)
    return RedirectResponse(url="/dashboard", status_code=303)

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request, db = Depends(get_db)):
    total = db.query(Participant).count()
    completed = db.query(Participant).filter(Participant.final_idp_complete == True).count()
    
    risk_counts = db.query(Participant.risk_status, func.count(Participant.id)).group_by(Participant.risk_status).all()
    risk_dict = {status: count for status, count in risk_counts}
    
    participants = db.query(Participant).all()
    priority = {"At Risk": 1, "Needs Attention": 2, "Not Started": 3, "On Track": 4, "Completed": 5}
    participants.sort(key=lambda x: priority.get(x.risk_status, 6))
    
    return templates.TemplateResponse(
        name="dashboard.html", 
        context={
            "request": request, 
            "total": total, 
            "completed": completed,
            "risk_dict": risk_dict, 
            "participants": participants
        }
    )

@app.get("/init-db")
def init_db(db = Depends(get_db)):
    Base.metadata.create_all(bind=engine)
    return {"message": "Database initialized and seeded successfully!"}