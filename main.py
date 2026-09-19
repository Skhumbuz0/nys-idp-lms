# main.py
import re
import json
import os
from pathlib import Path
from datetime import datetime, timedelta
from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy import func
from database import Base, engine, get_db
from models import Participant, Question, QuizResponse, DailyResponse, NemisaCourse, NemisaAssignment, NemisaWeeklyReport, Course, Enrollment
import resend

app = FastAPI(title="MAYO Learner Management System")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory=Path("templates"))

ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "MAYO2026!")
RESEND_API_KEY = os.getenv("RESEND_API_KEY", "")
FROM_EMAIL = os.getenv("FROM_EMAIL", "MAYO LMS <onboarding@resend.dev>")

# ==========================================
# EMAIL UTILITIES
# ==========================================
def send_email(to_email: str, subject: str, html_content: str) -> bool:
    if not RESEND_API_KEY:
        print(f"⚠️ WARNING: RESEND_API_KEY not set. Email to {to_email} not sent.")
        return False
    try:
        resend.api_key = RESEND_API_KEY
        resend.Emails.send({"from": FROM_EMAIL, "to": to_email, "subject": subject, "html": html_content})
        print(f"✅ Email sent to {to_email}: {subject}")
        return True
    except Exception as e:
        print(f"❌ Email error for {to_email}: {e}")
        return False

# (Keep your existing build_daily_action_email and build_final_report_email functions here)
# For brevity, assume they are pasted exactly as they were in your previous working version.
def build_daily_action_email(participant: Participant, day: int, day_data: dict, form_data: dict) -> tuple:
    qa_pairs = [{"question": q["label"], "answer": form_data.get(f"q_{q['id']}", "No answer provided")} for q in day_data["questions"]]
    action_status = form_data.get("action_status", "No")
    reflection = form_data.get("reflection", "No reflection provided")
    html = f"""<div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; background: #f9fafb;">
        <div style="background: #1f2937; color: white; padding: 20px; text-align: center;">
            <h1 style="margin: 0; font-size: 24px;">MAYO LMS</h1>
            <p style="margin: 5px 0 0 0; color: #9ca3af;">NYS IDP 30-Day Challenge</p>
        </div>
        <div style="background: white; padding: 30px; margin: 20px; border-radius: 8px;">
            <h2 style="color: #1f2937; margin-top: 0;">🎯 Day {day} Complete: {day_data['title']}</h2>
            <p style="color: #6b7280;">Hi {participant.full_name},</p>
            <div style="background: #eff6ff; border-left: 4px solid #3b82f6; padding: 15px; margin: 20px 0;">
                <h3 style="color: #1e40af; margin-top: 0;">📝 Your Responses</h3>"""
    for qa in qa_pairs:
        html += f"""<div style="margin-bottom: 15px;">
            <p style="color: #374151; font-weight: bold; margin-bottom: 5px;">{qa['question']}</p>
            <p style="color: #6b7280; margin: 0; padding-left: 15px; border-left: 2px solid #d1d5db;">{qa['answer']}</p></div>"""
    html += f"""</div>
            <div style="background: #f0fdf4; border-left: 4px solid #22c55e; padding: 15px; margin: 20px 0;">
                <h3 style="color: #166534; margin-top: 0;">🚀 Today's Action</h3>
                <p style="color: #374151; margin: 5px 0;"><strong>Task:</strong> {day_data['action']}</p>
                <p style="color: #374151; margin: 5px 0;"><strong>Status:</strong> {action_status}</p>
            </div>
            <div style="background: #fef3c7; border-left: 4px solid #f59e0b; padding: 15px; margin: 20px 0;">
                <h3 style="color: #92400e; margin-top: 0;">🔄 Your Reflection</h3>
                <p style="color: #374151; margin: 0; font-style: italic;">"{reflection}"</p>
            </div>
        </div>
        <div style="text-align: center; padding: 20px; color: #9ca3af; font-size: 12px;">
            <p>MAYO Learner Management System</p><p>Participant ID: {participant.participant_id}</p>
        </div></div>"""
    return f"Day {day} Complete: {day_data['title']} — MAYO LMS", html

def build_final_report_email(participant: Participant, db) -> tuple:
    # (Use your existing, working build_final_report_email function here)
    return "🎉 Your 30-Day Challenge Final Report — MAYO LMS", "<p>Report content here</p>" 


# ==========================================
# CURRICULUM & UTILITIES
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
        {"id": "score_interest", "type": "scale", "label": "SCURRICULUMcore (1-5): Personal interest", "min": 1, "max": 5},
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

WEEK_INFO = {
    1: {"title": "Discover", "chapters": [1,2,3,4], "max_score": 60, "description": "Chapters 1-4"},
    2: {"title": "Build Mindset", "chapters": [5,6,7,8], "max_score": 60, "description": "Chapters 5-8"},
    3: {"title": "Turn Ideas Into Plans", "chapters": [9,10,11,12], "max_score": 60, "description": "Chapters 9-12"},
    4: {"title": "Execute & Persist", "chapters": [13,14,15], "max_score": 45, "description": "Chapters 13-15"}
}

def generate_participant_id(db) -> str:
    highest = 0
    for (pid,) in db.query(Participant.participant_id).all():
        if pid:
            match = re.search(r'(\d+)$', pid)
            if match and int(match.group(1)) > highest: highest = int(match.group(1))
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
    if quizzes: p.overall_quiz_pct = (sum(q.score for q in quizzes) / sum(q.max_score for q in quizzes)) * 100
    if unique_days == 0 and not quizzes: p.risk_status, p.risk_reason = "Not Started", ""
    elif action_pct < 30 or (p.overall_quiz_pct or 0) < 40: p.risk_status, p.risk_reason = "At Risk", "Low engagement"
    elif action_pct < 60 or (p.overall_quiz_pct or 0) < 60: p.risk_status, p.risk_reason = "Needs Attention", "Below threshold"
    else: p.risk_status, p.risk_reason = "On Track", ""
    p.last_activity = datetime.utcnow()
    db.commit()

# ==========================================
# PUBLIC & AUTH ROUTES
# ==========================================
@app.get("/", response_class=HTMLResponse)
def home(request: Request): 
    return templates.TemplateResponse(request=request, name="home.html", context={})

@app.get("/register", response_class=HTMLResponse)
def register_form(request: Request): 
    return templates.TemplateResponse(request=request, name="register.html", context={})

@app.post("/register")
def process_register(request: Request, db = Depends(get_db), full_name: str = Form(...), email: str = Form(...), phone: str = Form(""), age_range: str = Form(...), main_goal: str = Form(...)):
    pid = generate_participant_id(db)
    new_p = Participant(participant_id=pid, full_name=full_name, email=email.lower(), phone=phone, age_range=age_range, main_goal=main_goal, registration_complete=True, last_activity=datetime.utcnow())
    db.add(new_p)
    
    # AUTO-ENROLL IN BOTH COURSES
    db.add(Enrollment(participant_id=pid, course_code="NYS-IDP", progress_pct=0.0))
    db.add(Enrollment(participant_id=pid, course_code="NEMISA-DIGITAL", progress_pct=0.0))
    
    db.commit()
    update_participant_progress(db, pid)
    return templates.TemplateResponse(request=request, name="register_success.html", context={"pid": pid, "name": full_name})

@app.get("/login", response_class=HTMLResponse)
def login_choice(request: Request): 
    return templates.TemplateResponse(request=request, name="login_choice.html", context={})

@app.get("/login/learner", response_class=HTMLResponse)
def learner_login_form(request: Request): 
    return templates.TemplateResponse(request=request, name="login.html", context={})

@app.post("/login/learner")
def process_learner_login(request: Request, db = Depends(get_db), participant_id: str = Form(...)):
    pid = participant_id.strip().upper()
    p = db.query(Participant).filter(Participant.participant_id == pid).first()
    if not p: 
        return templates.TemplateResponse(request=request, name="login.html", context={"error": "Participant ID not found."})
    return templates.TemplateResponse(request=request, name="login_success.html", context={"pid": pid, "name": p.full_name})

@app.get("/login/facilitator", response_class=HTMLResponse)
def facilitator_login_form(request: Request): 
    return templates.TemplateResponse(request=request, name="facilitator_login.html", context={})

@app.post("/login/facilitator")
def process_facilitator_login(request: Request, password: str = Form(...)):
    if password.strip() == ADMIN_PASSWORD: 
        return templates.TemplateResponse(request=request, name="facilitator_login_success.html", context={})
    return templates.TemplateResponse(request=request, name="facilitator_login.html", context={"error": "Incorrect password."})

@app.get("/logout", response_class=HTMLResponse)
def logout(request: Request): 
    return templates.TemplateResponse(request=request, name="logout.html", context={})

# ==========================================
# LEARNER DASHBOARD & COURSE ROUTES
# ==========================================
@app.get("/learner-dashboard", response_class=HTMLResponse)
def learner_dashboard(request: Request): 
    return templates.TemplateResponse(request=request, name="learner_dashboard.html", context={})

@app.get("/api/learner-dashboard/{pid}")
def get_learner_dashboard_data(pid: str, db = Depends(get_db)):
    p = db.query(Participant).filter(Participant.participant_id == pid.upper()).first()
    if not p: raise HTTPException(status_code=404, detail="Participant not found")
    
    enrollments = db.query(Enrollment).filter(Enrollment.participant_id == pid.upper()).all()
    courses_data = []
    
    for e in enrollments:
        course = db.query(Course).filter(Course.code == e.course_code).first()
        if e.course_code == "NYS-IDP":
            progress = p.overall_progress_pct
        elif e.course_code == "NEMISA-DIGITAL":
            nemisa_assignments = db.query(NemisaAssignment).filter(NemisaAssignment.participant_id == pid.upper()).all()
            completed = sum(1 for a in nemisa_assignments if a.status == "COMPLETED")
            progress = int((completed / 12) * 100) if completed > 0 else 0
            e.progress_pct = progress
            db.commit()
        else:
            progress = e.progress_pct
            
        courses_data.append({
            "code": e.course_code,
            "title": course.title if course else e.course_code,
            "description": course.description if course else "",
            "progress": progress,
            "status": e.status
        })
        
    return {"participant": {"id": p.participant_id, "name": p.full_name}, "courses": courses_data}

@app.get("/my-progress", response_class=HTMLResponse)
def nys_idp_progress(request: Request): 
    # This is now the specific view for the NYS-IDP course
    return templates.TemplateResponse(request=request, name="my_progress.html", context={})

@app.get("/nemisa", response_class=HTMLResponse)
def nemisa_command_centre(request: Request, db = Depends(get_db)): 
    return templates.TemplateResponse(request=request, name="nemisa_command.html", context={})

# ==========================================
# QUIZ & DAILY ACTION ROUTES (Unchanged logic, just kept for NYS course)
# ==========================================
@app.get("/quizzes", response_class=HTMLResponse)
def quiz_hub(request: Request, db = Depends(get_db)): 
    return templates.TemplateResponse(request=request, name="quiz_hub.html", context={"week_info": WEEK_INFO})

@app.get("/quiz/{week}", response_class=HTMLResponse)
def quiz_form(request: Request, week: int, db = Depends(get_db)):
    if week < 1 or week > 4: raise HTTPException(status_code=404, detail="Week out of range")
    chapters = WEEK_INFO[week]["chapters"]
    questions = db.query(Question).filter(Question.chapter.in_(chapters)).order_by(Question.chapter, Question.id).all()
    return templates.TemplateResponse(request=request, name="quiz.html", context={"week": week, "week_title": WEEK_INFO[week]["title"], "week_description": WEEK_INFO[week]["description"], "questions": questions})

@app.post("/quiz/{week}")
async def process_quiz(week: int, request: Request, db = Depends(get_db)):
    form_data = await request.form()
    pid = str(form_data.get("participant_id", "")).strip().upper()
    p = db.query(Participant).filter(Participant.participant_id == pid).first()
    if not p: raise HTTPException(status_code=404, detail="Participant not found.")
    chapters = WEEK_INFO[week]["chapters"]
    max_score = WEEK_INFO[week]["max_score"]
    questions = db.query(Question).filter(Question.chapter.in_(chapters)).all()
    score = sum(q.marks for q in questions if str(form_data.get(f"q_{q.question_id}", "")).strip().lower() == str(q.correct_answer).strip().lower())
    pct = (score / max_score * 100) if max_score > 0 else 0
    existing_quiz = db.query(QuizResponse).filter(QuizResponse.participant_id == pid, QuizResponse.week == week).first()
    if existing_quiz: existing_quiz.score, existing_quiz.max_score, existing_quiz.percentage = score, max_score, pct
    else: db.add(QuizResponse(participant_id=pid, week=week, score=score, max_score=max_score, percentage=pct))
    setattr(p, f"week{week}_complete", True)
    db.commit(); update_participant_progress(db, pid)
    return RedirectResponse(url="/my-progress", status_code=303)

@app.get("/daily-action", response_class=HTMLResponse)
def daily_action_hub(request: Request, db = Depends(get_db)): 
    return templates.TemplateResponse(request=request, name="daily_action_hub.html", context={"curriculum": CURRICULUM})

@app.get("/daily-action/{day}", response_class=HTMLResponse)
def daily_action_form(request: Request, day: int):
    if day < 1 or day > 30: raise HTTPException(status_code=404, detail="Day out of range")
    return templates.TemplateResponse(request=request, name="daily_action.html", context={"day": day, "day_data": CURRICULUM[day]})

@app.post("/daily-action/{day}")
async def process_daily_action(day: int, request: Request, db = Depends(get_db)):
    form_data = await request.form()
    pid = str(form_data.get("participant_id", "")).strip().upper()
    p = db.query(Participant).filter(Participant.participant_id == pid).first()
    if not p: raise HTTPException(status_code=404, detail="Participant not found")
    responses = {key: value for key, value in form_data.items() if key.startswith("q_")}
    action_status = form_data.get("action_status", "No")
    reflection = form_data.get("reflection", "")
    evidence_file = form_data.get("evidence_file")
    filename = evidence_file.filename if evidence_file and hasattr(evidence_file, 'filename') and evidence_file.filename else None
    existing = db.query(DailyResponse).filter(DailyResponse.participant_id == pid, DailyResponse.day == day).first()
    if existing:
        existing.responses_json, existing.action_status, existing.reflection = json.dumps(responses), action_status, reflection
        if filename: existing.evidence_file = filename
    else:
        db.add(DailyResponse(participant_id=pid, day=day, responses_json=json.dumps(responses), action_status=action_status, reflection=reflection, evidence_file=filename))
    db.commit(); update_participant_progress(db, pid)
    if p.email and day in CURRICULUM:
        subject, html_content = build_daily_action_email(p, day, CURRICULUM[day], form_data)
        send_email(p.email, subject, html_content)
    next_day = day + 1
    return RedirectResponse(url=f"/daily-action/{next_day}" if next_day <= 30 else "/my-progress", status_code=303)

# ==========================================
# FACILITATOR & INIT ROUTES
# ==========================================
@app.get("/facilitator", response_class=HTMLResponse)
def facilitator_dashboard(request: Request, db = Depends(get_db)):
    total = db.query(Participant).count()
    completed = db.query(Participant).filter(Participant.final_idp_complete == True).count()
    risk_counts = db.query(Participant.risk_status, func.count(Participant.id)).group_by(Participant.risk_status).all()
    risk_dict = {status: count for status, count in risk_counts}
    participants = db.query(Participant).all()
    priority = {"At Risk": 1, "Needs Attention": 2, "Not Started": 3, "On Track": 4, "Completed": 5}
    participants.sort(key=lambda x: priority.get(x.risk_status, 6))
    return templates.TemplateResponse(request=request, name="facilitator_dashboard.html", context={"total": total, "completed": completed, "risk_dict": risk_dict, "participants": participants})

@app.get("/init-db")
def init_db(db = Depends(get_db)):
    Base.metadata.create_all(bind=engine)
    # Seed Courses if empty
    if db.query(Course).count() == 0:
        db.add(Course(code="NYS-IDP", title="NYS IDP: Think & Grow Rich 30-Day Challenge", description="Master your mindset, build definite purpose, and take daily action over 30 days. Includes weekly knowledge quizzes."))
        db.add(Course(code="NEMISA-DIGITAL", title="NEMISA Digital Skills Programme", description="A comprehensive 12-course learning path covering GitHub, Power Platform, AI, Azure, Cybersecurity, and DevOps."))
        db.commit()
    return {"message": "Database initialized and courses seeded!"}

@app.get("/seed-questions")
def seed_questions(db = Depends(get_db)):
    total = db.query(Question).count()
    if total >= 200:
        return {"message": f"Question bank is already fully populated with {total} questions!"}
    
    # Clear any partial/failed seeds to prevent duplicates
    db.query(Question).delete()
    
    # ALL 225 QUESTIONS
    raw_questions = [
        (1, 1, "What was Edwin C. Barnes' definite objective?", "To become rich through mining", "To become Thomas Edison's business associate", "To become Edison's employee", "To invent a new machine", "b"),
        (1, 2, "What did Barnes begin with?", "Large amounts of money", "A powerful family connection", "A definite purpose and determination", "A university qualification", "c"),
        (1, 3, "What does the chapter use Barnes' story to demonstrate?", "Wealth comes mainly from luck", "Achievement begins with a definite idea and purpose", "Education guarantees success", "People must inherit wealth", "b"),
        (1, 4, "What should a person do instead of simply wishing for success?", "Wait for an opportunity", "Define exactly what they want", "Avoid taking risks", "Find someone wealthy to support them", "b"),
        (1, 5, "Barnes' circumstances at the beginning were described as:", "Extremely wealthy", "Comfortable", "Limited", "Powerful", "c"),
        (1, 6, "What lesson does the chapter give about circumstances?", "Circumstances determine your future", "You should wait until circumstances improve", "You should determine what you can do despite circumstances", "Circumstances should be ignored completely", "c"),
        (1, 7, "What did Barnes do when he could not immediately become Edison's business associate?", "He gave up", "He started his own university", "He found a way to get into Edison's organisation", "He borrowed money", "c"),
        (1, 8, "What does the chapter teach about starting?", "Start only when everything is perfect", "Start wherever you can", "Start after becoming wealthy", "Start only after getting permission", "b"),
        (1, 9, "What should a person look for inside a problem?", "Someone to blame", "An opportunity", "An excuse", "A shortcut", "b"),
        (1, 10, "What is the lesson of 'Three Feet From Gold'?", "Gold is impossible to find", "Persistence can be defeated by quitting too soon", "Mining is the best business", "Luck determines success", "b"),
        (1, 11, "Temporary defeat should be interpreted as:", "Permanent failure", "Evidence that the goal is impossible", "A temporary condition", "A reason to quit", "c"),
        (1, 12, "According to the chapter, what can defeat often provide?", "An opportunity to learn", "Guaranteed wealth", "A reason to blame others", "A replacement for planning", "a"),
        (1, 13, "What must accompany a definite purpose?", "Wishful thinking", "Action and persistence", "Fear", "Indecision", "b"),
        (1, 14, "Barnes' example demonstrates the importance of:", "Waiting for perfect opportunities", "Taking the first practical step toward a definite objective", "Avoiding difficult situations", "Having wealthy parents", "b"),
        (1, 15, "What is one of the central lessons of the Introduction?", "Think positively and do nothing", "Definite purpose must be translated into action", "Money is the only measure of success", "Education is unnecessary", "b"),
        (2, 1, "What does Hill identify as the starting point of all achievement?", "Money", "Desire", "Education", "Luck", "b"),
        (2, 2, "What should you state first when applying the six-step formula?", "Your favourite career", "The exact amount of money you desire", "Your biggest fear", "Your current income", "b"),
        (2, 3, "What must you determine in addition to the amount of money?", "What you will give in return", "What other people earn", "Where you will live", "What university you attended", "a"),
        (2, 4, "What should you establish regarding time?", "A vague future intention", "A definite date by which you intend to possess the money", "A retirement age", "A weekly holiday", "b"),
        (2, 5, "What must you create for achieving the goal?", "A definite plan", "A dream board only", "A list of excuses", "A prediction", "a"),
        (2, 6, "What should you do with your plan?", "Begin immediately", "Wait until next year", "Keep it secret forever", "Give it to someone else", "a"),
        (2, 7, "What should be written down?", "Only the amount of money", "The complete statement of desire", "Other people's opinions", "Your past failures", "b"),
        (2, 8, "How often does Hill instruct the reader to read the statement aloud?", "Once a week", "Once a month", "Twice daily", "Once a year", "c"),
        (2, 9, "When should the statement be read?", "Morning and night", "Only at lunchtime", "Only on weekends", "Only when discouraged", "a"),
        (2, 10, "What should you do while reading the statement?", "Memorise the words without emotion", "See and feel yourself already in possession of the money", "Compare yourself with others", "Ignore the goal", "b"),
        (2, 11, "What else should you visualise?", "Yourself rendering the service or delivering the merchandise through which you intend to earn the money", "Someone giving you money", "Winning a lottery", "Avoiding work", "a"),
        (2, 12, "Why is the 'in return' part important?", "Hill presents achievement as an exchange involving value", "Money has no connection to service", "It removes the need for planning", "It guarantees success", "a"),
        (2, 13, "What is the difference between a wish and the desire described by Hill?", "Desire is vague", "Desire is backed by definiteness and a plan", "Desire requires no action", "Wish is more powerful", "b"),
        (2, 14, "Which sequence best represents Hill's six-step process?", "Wish → wait → hope → receive", "Amount → exchange → deadline → plan → write → repeat/visualise", "Education → job → salary → retirement", "Money → spending → debt → wealth", "b"),
        (2, 15, "What does Hill say should happen if you cannot yet see how the goal will be achieved?", "Abandon it", "Continue developing the desire and plan", "Lower the goal immediately", "Wait for someone else", "b"),
        (3, 1, "How does Hill define faith within his philosophy?", "Blind luck", "Visualization of and belief in attainment of desire", "Academic knowledge", "Financial planning", "b"),
        (3, 2, "What should be combined with desire?", "Doubt", "Faith", "Fear", "Indifference", "b"),
        (3, 3, "What role does visualization play?", "It helps create a mental picture of the desired outcome", "It replaces action", "It eliminates the need for knowledge", "It guarantees money", "a"),
        (3, 4, "According to Hill, faith can be:", "Deliberately developed", "Purchased", "Inherited only", "Avoided", "a"),
        (3, 5, "What should be added to repeated statements of desire?", "Emotion", "Confusion", "Fear", "Criticism", "a"),
        (3, 6, "What does Hill say faith influences?", "The subconscious mind", "The weather", "Other people's decisions", "The stock market automatically", "a"),
        (3, 7, "What should you picture yourself doing in relation to your goal?", "Already possessing the desired result", "Avoiding responsibility", "Waiting for someone else", "Giving up", "a"),
        (3, 8, "Which combination is most consistent with Hill's approach?", "Desire + faith + emotion", "Fear + doubt + procrastination", "Money + luck + waiting", "Criticism + indecision + avoidance", "a"),
        (3, 9, "Why does Hill emphasise emotion?", "He believes emotionally charged thoughts have greater influence on the subconscious", "Emotion removes the need for work", "Emotion guarantees wealth", "Emotion replaces specialised knowledge", "a"),
        (3, 10, "What can weaken faith?", "Repeated doubt", "Definite purpose", "Persistence", "Constructive imagination", "a"),
        (3, 11, "What should a person do when doubt appears?", "Strengthen belief through repeated constructive thought and action", "Abandon the goal", "Avoid planning", "Stop learning", "a"),
        (3, 12, "Faith is presented as something that can be strengthened through:", "Practice", "Gambling", "Complaining", "Avoidance", "a"),
        (3, 13, "What does Hill connect faith with in achieving desire?", "Turning desire into a mental certainty that supports action", "Avoiding action", "Eliminating knowledge", "Depending on luck", "a"),
        (3, 14, "What should a person repeatedly focus on?", "The desired outcome", "Past mistakes only", "Other people's failures", "Fear", "a"),
        (3, 15, "In Hill's framework, faith is primarily intended to help a person:", "Develop belief in the attainment of their definite desire", "Become dependent on others", "Avoid difficult decisions", "Stop making plans", "a"),
        (4, 1, "What does Hill describe auto-suggestion as?", "Self-suggestion", "Financial advice", "Physical exercise", "Formal education", "a"),
        (4, 2, "Auto-suggestion is described as the agency of communication between:", "Conscious thought and the subconscious mind", "Two businesses", "Two universities", "Employer and employee", "a"),
        (4, 3, "What kind of thoughts can influence the subconscious according to Hill?", "Dominating thoughts permitted to remain in the conscious mind", "Only thoughts written by other people", "Only academic thoughts", "No thoughts", "a"),
        (4, 4, "What does Hill compare the subconscious mind to?", "A fertile garden", "A bank account", "A factory machine", "A classroom", "a"),
        (4, 5, "What happens if desirable thoughts are not planted in the 'garden'?", "Undesirable thoughts may grow", "Nothing happens", "Wealth automatically appears", "Knowledge disappears", "a"),
        (4, 6, "What does Hill instruct the reader to read aloud twice daily?", "Their written statement of desire", "Their CV", "A newspaper", "Their financial statement", "a"),
        (4, 7, "What must accompany the words for auto-suggestion to be effective in Hill's framework?", "Emotion or feeling", "Anger", "Fear", "Silence", "a"),
        (4, 8, "Merely repeating words without emotion is described as:", "Insufficient", "Guaranteed to work", "The only requirement", "More powerful than faith", "a"),
        (4, 9, "What should a person deliberately feed the subconscious mind with?", "Constructive thoughts and desires", "Fear", "Jealousy", "Hatred", "a"),
        (4, 10, "What should the conscious mind act as?", "An outer guard to what reaches the subconscious", "A source of money", "A replacement for imagination", "A source of fear", "a"),
        (4, 11, "What is one purpose of repetition?", "To create thought habits", "To avoid planning", "To eliminate specialised knowledge", "To replace action", "a"),
        (4, 12, "Which emotion does Hill encourage in relation to desire?", "Faith", "Hatred", "Jealousy", "Revenge", "a"),
        (4, 13, "What does Hill say about negative thoughts?", "They can influence the subconscious if not controlled", "They are always harmless", "They should be encouraged", "They guarantee persistence", "a"),
        (4, 14, "What is the practical application of auto-suggestion in the course?", "Repeatedly and emotionally reinforce a definite purpose", "Stop thinking about goals", "Avoid writing goals", "Wait for circumstances to change", "a"),
        (4, 15, "Which statement best captures the chapter?", "Repeated, emotional thought can influence the subconscious and develop thought habits", "Money appears through repetition alone", "Planning is unnecessary", "Knowledge has no value", "a"),
        (5, 1, "What type of knowledge does Hill say is important for success?", "Specialized knowledge", "Every possible fact", "General gossip", "Unused information", "a"),
        (5, 2, "What is the difference between general and specialized knowledge?", "Specialized knowledge is organised around a specific purpose or field", "General knowledge is always useless", "Specialized knowledge cannot be learned", "There is no difference", "a"),
        (5, 3, "Does Hill say a person must personally possess all knowledge required for a major undertaking?", "No", "Yes, always", "Only if they are wealthy", "Only if they are young", "a"),
        (5, 4, "What can a person do when they lack specialised knowledge?", "Acquire it or organise people who possess it", "Abandon the goal", "Pretend to know it", "Ignore the gap", "a"),
        (5, 5, "What should knowledge ultimately be converted into?", "Plans and action", "Certificates only", "Arguments", "Entertainment", "a"),
        (5, 6, "Why is knowledge alone insufficient?", "It must be organised and applied toward a definite purpose", "Knowledge has no value", "It prevents imagination", "It creates fear", "a"),
        (5, 7, "Where can specialised knowledge come from?", "Education, experience and other knowledgeable people", "Luck only", "Money only", "Dreams only", "a"),
        (5, 8, "What should you do when you identify a knowledge gap?", "Determine where the required knowledge can be obtained", "Ignore it", "Blame someone", "Give up", "a"),
        (5, 9, "Which is an example of specialised knowledge?", "Technical knowledge needed to perform a specific task", "Random facts with no application", "Rumours", "Unverified opinions", "a"),
        (5, 10, "What role can other people play in filling knowledge gaps?", "They can provide knowledge and experience you do not possess", "They prevent learning", "They eliminate planning", "They guarantee wealth", "a"),
        (5, 11, "What should specialised knowledge support?", "Your definite purpose", "Procrastination", "Fear", "Indecision", "a"),
        (5, 12, "What does Hill emphasise about education?", "Education should help a person acquire and use useful knowledge", "Formal education automatically creates wealth", "Education is unnecessary", "Certificates are the same as specialised knowledge", "a"),
        (5, 13, "What should you do with knowledge once acquired?", "Organise it into practical plans", "Hide it", "Forget it", "Use it only for conversation", "a"),
        (5, 14, "Which person is better prepared to pursue a specialised goal?", "Someone who identifies and fills their knowledge gaps", "Someone who refuses to learn", "Someone who relies entirely on luck", "Someone who avoids experts", "a"),
        (5, 15, "What is the key lesson of the chapter?", "You need the right knowledge, whether acquired personally or through others, and must organise it for action", "You must know everything yourself", "General information guarantees wealth", "Learning should stop after school", "a"),
        (6, 1, "What does Hill call imagination?", "The workshop of the mind", "A form of financial accounting", "A type of education", "A business licence", "a"),
        (6, 2, "What can imagination combine?", "Existing knowledge and ideas", "Only money", "Only emotions", "Only memories", "a"),
        (6, 3, "What can imagination be used to create?", "Plans and solutions", "Fear", "Debt", "Excuses", "a"),
        (6, 4, "What is one purpose of creative imagination?", "To create new combinations of existing ideas", "To avoid thinking", "To replace specialised knowledge completely", "To eliminate action", "a"),
        (6, 5, "What should you do when an idea occurs to you?", "Capture and examine it", "Immediately forget it", "Assume it is impossible", "Hide it", "a"),
        (6, 6, "What can imagination help transform?", "Thought into practical plans", "Money into knowledge automatically", "Fear into wealth automatically", "Failure into success without action", "a"),
        (6, 7, "Which activity exercises imagination?", "Generating several possible solutions to a problem", "Repeating the same idea without thinking", "Avoiding problems", "Waiting for someone else", "a"),
        (6, 8, "Why is imagination important to entrepreneurship?", "Entrepreneurs must create new combinations and solutions", "Entrepreneurs do not need ideas", "It eliminates customers", "It replaces all knowledge", "a"),
        (6, 9, "What should imagination ultimately contribute to?", "Useful ideas and plans", "Confusion", "Procrastination", "Fear", "a"),
        (6, 10, "What should you do with an idea that appears promising?", "Develop and test it", "Assume it will work automatically", "Ignore it", "Wait indefinitely", "a"),
        (6, 11, "What is one way to develop imagination?", "Deliberately practise generating solutions", "Avoid new experiences", "Stop learning", "Avoid problems", "a"),
        (6, 12, "What is a 'new combination' in the context of imagination?", "Combining existing knowledge or concepts in a new way", "Memorising a fact", "Copying an idea without change", "Avoiding creativity", "a"),
        (6, 13, "What does imagination need to become useful?", "Direction and application", "No purpose", "No knowledge", "No action", "a"),
        (6, 14, "What should a person ask when facing a problem?", "What different solutions can I create?", "Who can I blame?", "Why should I quit?", "How can I avoid thinking?", "a"),
        (6, 15, "What is the central lesson of the chapter?", "Ideas can be developed through imagination and organised into useful plans", "Imagination is only entertainment", "Ideas have no economic value", "Imagination replaces persistence", "a"),
        (7, 1, "What does organized planning do to desire?", "Crystallizes desire into action", "Eliminates desire", "Delays action", "Replaces desire with fear", "a"),
        (7, 2, "What should a practical plan contain?", "Definite steps toward the objective", "Vague wishes", "Excuses", "Predictions only", "a"),
        (7, 3, "Who should you ally with when necessary?", "A group of people needed to create and carry out the plan", "Nobody", "Only competitors", "Only strangers", "a"),
        (7, 4, "What principle does Hill connect to this group?", "Master Mind", "Six Ghosts", "Auto-Suggestion", "Sixth Sense", "a"),
        (7, 5, "What should you determine before forming the Master Mind?", "What benefits you can offer members", "How to control members", "How to avoid cooperation", "How to work alone", "a"),
        (7, 6, "How often does Hill suggest the group meet while perfecting the plan?", "At least twice a week", "Once a year", "Once a month", "Never", "a"),
        (7, 7, "What must exist among Master Mind members?", "Harmony", "Competition", "Distrust", "Fear", "a"),
        (7, 8, "What should happen to plans that do not work?", "Replace them with new plans", "Abandon the goal immediately", "Blame others", "Hide the failure", "a"),
        (7, 9, "What does Hill identify as a major reason people fail with plans?", "Lack of persistence in creating new plans", "Too much learning", "Too much cooperation", "Too many ideas", "a"),
        (7, 10, "Why should other minds contribute to a plan?", "They bring experience, education, ability and knowledge", "They remove responsibility", "They guarantee success", "They replace the leader", "a"),
        (7, 11, "What should happen to plans developed by an individual?", "They should be checked and approved by the Master Mind when applicable", "They should never be questioned", "They should be hidden", "They should be abandoned", "a"),
        (7, 12, "What is the relationship between planning and persistence?", "Failed plans should be replaced rather than causing abandonment of the goal", "Failed plans mean the goal is impossible", "Planning eliminates persistence", "Persistence means never changing a plan", "a"),
        (7, 13, "What should compensation for cooperation be?", "It may take forms other than money", "It must always be cash", "It should never exist", "It is unnecessary", "a"),
        (7, 14, "What is the purpose of organised planning?", "To translate desire into practical action", "To create more wishes", "To postpone decisions", "To avoid people", "a"),
        (7, 15, "What is one of the chapter's most important lessons?", "Do not abandon the goal simply because the first plan fails", "Never change a plan", "Work alone", "Avoid criticism", "a"),
        (8, 1, "What does Hill identify as an important characteristic of successful people?", "Prompt decision-making", "Indecision", "Procrastination", "Avoidance", "a"),
        (8, 2, "What should decisions generally be made?", "Promptly", "After endless discussion", "Only when someone else decides", "Never", "a"),
        (8, 3, "What should changes to decisions generally be?", "Slow and deliberate", "Immediate and emotional", "Random", "Avoided completely", "a"),
        (8, 4, "What is one enemy of decision?", "Procrastination", "Knowledge", "Planning", "Persistence", "a"),
        (8, 5, "What should a person do before making an important decision?", "Quietly gather relevant facts", "Ask everyone for approval", "Ignore evidence", "Wait forever", "a"),
        (8, 6, "Who should have access to sensitive plans and decisions?", "Trusted members of the Master Mind", "Everyone", "Strangers", "Competitors", "a"),
        (8, 7, "What should criticism from others do to your definite purpose?", "It should not automatically control your direction", "It should always change your goal", "It should stop all action", "It should determine your career", "a"),
        (8, 8, "What does procrastination mean in this context?", "Delaying decisions or action unnecessarily", "Planning carefully", "Gathering facts", "Learning", "a"),
        (8, 9, "What should a person do once sufficient information has been gathered?", "Decide and act", "Keep researching forever", "Ask everyone else to decide", "Abandon the goal", "a"),
        (8, 10, "Which behaviour demonstrates indecision?", "Passing responsibility to others", "Making a considered decision", "Taking responsibility", "Acting on a plan", "a"),
        (8, 11, "Why does Hill emphasise prompt decisions?", "Indecision can create delay and weaken action", "Facts are unnecessary", "Planning is unnecessary", "Mistakes are impossible", "a"),
        (8, 12, "What should a person avoid when making decisions?", "Allowing fear and outside criticism to dominate the decision", "Gathering facts", "Thinking independently", "Consulting trusted people", "a"),
        (8, 13, "What does the chapter encourage?", "Independent thinking", "Blind conformity", "Endless waiting", "Avoidance", "a"),
        (8, 14, "Once a decision has been made, what should follow?", "Action", "Another year of hesitation", "Excuses", "Fear", "a"),
        (8, 15, "The title 'Mastery of Procrastination' suggests mastery over:", "Unnecessary delay", "Education", "Imagination", "Cooperation", "a"),
        (9, 1, "What does Hill say about persistence?", "It is a state of mind that can be cultivated", "It is impossible to develop", "It depends only on luck", "It is inherited", "a"),
        (9, 2, "Which factor is listed first among the eight causes of persistence?", "Definiteness of purpose", "Money", "Fame", "Age", "a"),
        (9, 3, "Why does desire support persistence?", "Strong desire motivates continued effort", "Desire eliminates work", "Desire guarantees success", "Desire removes the need for planning", "a"),
        (9, 4, "What does self-reliance contribute to persistence?", "Belief in one's ability to carry out a plan", "Dependence on others", "Fear of failure", "Indecision", "a"),
        (9, 5, "What type of plans encourage persistence?", "Definite plans", "Secret plans with no action", "Vague plans", "No plans", "a"),
        (9, 6, "What does accurate knowledge provide?", "Confidence that plans are based on sound information", "Guaranteed wealth", "An excuse to stop learning", "Fear", "a"),
        (9, 7, "What type of cooperation supports persistence?", "Sympathy, understanding and harmonious cooperation", "Conflict", "Competition within the team", "Distrust", "a"),
        (9, 8, "What does willpower involve?", "Concentrating thoughts on building plans for a definite purpose", "Avoiding decisions", "Depending on luck", "Ignoring goals", "a"),
        (9, 9, "What does Hill call the direct result of habit?", "Persistence", "Wealth", "Fear", "Knowledge", "a"),
        (9, 10, "What should a person do to understand their own persistence?", "Take an honest inventory of themselves", "Compare themselves with everyone else", "Ignore weaknesses", "Avoid self-analysis", "a"),
        (9, 11, "Which is a symptom of lack of persistence?", "Procrastination", "Definite purpose", "Self-reliance", "Accurate knowledge", "a"),
        (9, 12, "Which is another symptom of lack of persistence?", "Indecision", "Planning", "Desire", "Cooperation", "a"),
        (9, 13, "What does Hill recommend when a plan fails?", "Continue by developing another plan", "Abandon the goal", "Blame circumstances", "Stop learning", "a"),
        (9, 14, "How can fear be weakened according to the chapter?", "Through repeated acts of courage", "Through avoidance", "Through procrastination", "Through indecision", "a"),
        (9, 15, "What is the central lesson of persistence?", "Continue sustained effort toward a definite purpose despite temporary setbacks", "Never change plans", "Never experience failure", "Depend on motivation alone", "a"),
        (10, 1, "What is the Master Mind based upon?", "Coordinated knowledge and effort of two or more people", "Working completely alone", "Competition", "Financial wealth only", "a"),
        (10, 2, "Why does Hill believe people need a Master Mind?", "No individual possesses all the experience and knowledge needed for every major undertaking", "People cannot think independently", "It eliminates responsibility", "It guarantees success", "a"),
        (10, 3, "What should the group have?", "A definite objective", "No objective", "Conflicting objectives", "Secret objectives", "a"),
        (10, 4, "What is essential to a successful Master Mind?", "Harmony", "Fear", "Jealousy", "Distrust", "a"),
        (10, 5, "What can members contribute?", "Knowledge, experience, skills, contacts and ideas", "Only money", "Only criticism", "Nothing", "a"),
        (10, 6, "What happens when minds work together harmoniously?", "Their combined effort can create greater power than isolated effort", "Individual responsibility disappears", "Plans become unnecessary", "Fear increases automatically", "a"),
        (10, 7, "What should members gain from participating?", "Mutual benefit", "Nothing", "Guaranteed wealth", "Control over others", "a"),
        (10, 8, "What should a leader do when assembling a Master Mind?", "Identify the people whose knowledge and abilities are needed", "Choose people randomly", "Avoid skilled people", "Select only people who agree with everything", "a"),
        (10, 9, "What is the Master Mind not simply about?", "Having many friends", "Combining useful minds around a definite purpose", "Cooperation", "Shared knowledge", "a"),
        (10, 10, "Why is harmony important?", "Conflict can destroy the cooperative power of the group", "Harmony guarantees money", "Harmony removes the need for action", "Harmony replaces planning", "a"),
        (10, 11, "What should the Master Mind help transform?", "Knowledge into organised action", "Action into procrastination", "Plans into fear", "Desire into indecision", "a"),
        (10, 12, "Who benefits from a properly organised Master Mind?", "All participating members", "Only the leader", "Only the wealthiest person", "Nobody", "a"),
        (10, 13, "What should members bring to the relationship?", "Useful contribution", "Passive dependence", "Competition", "Secrecy", "a"),
        (10, 14, "What does the Master Mind strengthen?", "Collective problem-solving and organised effort", "Isolation", "Indecision", "Fear", "a"),
        (10, 15, "What is the central lesson?", "Combine capable people around a definite purpose and work in harmony", "Success must always be achieved alone", "Knowledge is unnecessary", "Teams eliminate responsibility", "a"),
        (11, 1, "What does Hill mean by 'transmutation' in this chapter?", "Changing or redirecting energy from one form into another", "Eliminating desire", "Avoiding creativity", "Removing emotion", "a"),
        (11, 2, "Which emotion does Hill describe as a powerful stimulus to the mind?", "Sex", "Indifference", "Boredom", "Laziness", "a"),
        (11, 3, "What does Hill suggest this energy can be redirected toward?", "Creative and constructive activities", "Procrastination", "Destruction", "Indifference", "a"),
        (11, 4, "Which is included among Hill's ten mind stimuli?", "Love", "Laziness", "Confusion", "Indifference", "a"),
        (11, 5, "Which is another mind stimulus listed by Hill?", "Music", "Boredom", "Sleep", "Silence", "a"),
        (11, 6, "What does Hill include as a mind stimulus involving cooperation?", "Master Mind alliance", "Isolation", "Competition", "Conflict", "a"),
        (11, 7, "Which substance does Hill include among the mind stimuli?", "Narcotics and alcohol", "Water", "Food", "Vitamins", "a"),
        (11, 8, "How does Hill distinguish constructive and destructive stimuli?", "He identifies some stimuli as constructive and others as destructive", "All stimuli are constructive", "All stimuli are destructive", "None influence the mind", "a"),
        (11, 9, "What does Hill associate sex transmutation with?", "Creative ability", "Procrastination", "Indecision", "Poverty", "a"),
        (11, 10, "What does Hill say strong emotion can stimulate?", "Creative imagination and action", "Laziness", "Indifference", "Fear only", "a"),
        (11, 11, "According to Hill, what should strong motivational energy be used for?", "Constructive achievement", "Destructive behaviour", "Avoiding goals", "Giving up", "a"),
        (11, 12, "What role does imagination play in Hill's framework?", "It helps direct powerful impulses into creative purposes", "It prevents creativity", "It eliminates desire", "It replaces specialised knowledge", "a"),
        (11, 13, "Which of these is NOT one of Hill's listed mind stimuli?", "Love", "Music", "Friendship", "Procrastination", "d"),
        (11, 14, "What is the practical lesson that can be extracted from the chapter for this course?", "Channel strong motivation and energy into constructive goals", "Suppress all emotion", "Avoid ambition", "Stop creating", "a"),
        (11, 15, "Hill presents sex transmutation primarily as a method of:", "Redirecting powerful emotion toward constructive achievement", "Avoiding relationships", "Eliminating desire", "Replacing planning", "a"),
        (12, 1, "How does Hill describe the subconscious mind?", "A connecting link between the conscious mind and what he calls Infinite Intelligence", "A financial institution", "A physical muscle", "A form of formal education", "a"),
        (12, 2, "Does Hill say the subconscious mind remains idle?", "No", "Yes", "Only during sleep", "Only during work", "a"),
        (12, 3, "What happens if desirable thoughts are not deliberately planted?", "The subconscious can be influenced by thoughts that reach it through other sources", "Nothing happens", "The mind stops functioning", "Knowledge disappears", "a"),
        (12, 4, "Which emotions does Hill encourage?", "Desire, faith, love, enthusiasm and hope", "Fear, hatred and revenge", "Jealousy and anger", "Indifference", "a"),
        (12, 5, "Which emotions does Hill identify as negative?", "Fear, jealousy, hatred and anger", "Hope and enthusiasm", "Love and faith", "Desire and romance", "a"),
        (12, 6, "What should dominate the subconscious mind?", "Constructive thoughts and definite desires", "Fear", "Poverty consciousness", "Revenge", "a"),
        (12, 7, "What role does persistence play?", "It helps establish thought habits", "It eliminates imagination", "It replaces desire", "It prevents learning", "a"),
        (12, 8, "What should thoughts be mixed with according to Hill?", "Feeling or emotion", "Confusion", "Fear", "Indifference", "a"),
        (12, 9, "What does Hill say everything man creates begins as?", "A thought impulse", "Money", "A physical object", "A business", "a"),
        (12, 10, "What does imagination do to thought impulses?", "It can assemble them into plans", "It destroys them", "It prevents action", "It removes desire", "a"),
        (12, 11, "What should a person do with negative mental impulses?", "Work to control and replace them with more desirable thoughts", "Encourage them", "Ignore them completely", "Turn them into excuses", "a"),
        (12, 12, "What does Hill connect with influencing the subconscious voluntarily?", "Habit", "Luck", "Wealth", "Age", "a"),
        (12, 13, "What is one reason Hill repeatedly emphasises a written desire?", "To make the desire clear and repeatedly impress it upon the mind", "To replace action", "To avoid planning", "To impress other people", "a"),
        (12, 14, "What should the subconscious be 'fed' with?", "Desirable, constructive thoughts", "Fear", "Jealousy", "Hatred", "a"),
        (12, 15, "What is the practical lesson of the chapter?", "Deliberately cultivate the thoughts and emotions that support your definite purpose", "Stop thinking about your goal", "Depend entirely on the subconscious", "Avoid emotion", "a"),
        (13, 1, "How does Hill describe the brain?", "A broadcasting and receiving station for thought", "A financial institution", "A computer in the modern technical sense", "A storage bank for money", "a"),
        (13, 2, "What does Hill believe the brain can receive?", "Thought impulses", "Money", "Physical products", "Qualifications", "a"),
        (13, 3, "What can stimulate the mind?", "Books, knowledgeable people, discussion and experience", "Isolation only", "Procrastination", "Fear", "a"),
        (13, 4, "Why should people associate with capable thinkers?", "Their ideas and knowledge can stimulate your own thinking", "They guarantee wealth", "They eliminate responsibility", "They replace imagination", "a"),
        (13, 5, "What can discussion with knowledgeable people produce?", "New ideas and solutions", "Guaranteed money", "Fear", "Indecision", "a"),
        (13, 6, "What does Hill encourage people to develop?", "Creative imagination", "Passive thinking", "Indifference", "Isolation", "a"),
        (13, 7, "What role can the brain play in the Master Mind principle?", "It can contribute to collective thinking and exchange of ideas", "It eliminates teamwork", "It replaces planning", "It removes knowledge", "a"),
        (13, 8, "What should a person expose their mind to?", "Useful and stimulating information", "Negative influences only", "Fear", "Gossip", "a"),
        (13, 9, "What can research provide?", "Information useful for solving problems and creating plans", "Guaranteed success", "Automatic wealth", "Elimination of risk", "a"),
        (13, 10, "What is the relationship between knowledge and imagination?", "Knowledge can provide material for imagination to work with", "They are unrelated", "Knowledge prevents imagination", "Imagination eliminates knowledge", "a"),
        (13, 11, "What should a person do when facing a difficult problem?", "Think, research and discuss possible solutions", "Avoid it", "Blame others", "Give up", "a"),
        (13, 12, "What type of people should you seek out?", "People whose knowledge can contribute to your development", "People who discourage you", "People who always agree", "People who avoid learning", "a"),
        (13, 13, "What can collective thinking help produce?", "New combinations of knowledge and ideas", "Less knowledge", "Automatic money", "Procrastination", "a"),
        (13, 14, "Hill's 'broadcasting and receiving' description should be understood in this course as:", "Part of Hill's philosophical framework", "An established modern scientific law", "A computer networking protocol", "A financial principle", "a"),
        (13, 15, "What is the practical lesson for participants?", "Feed your mind with quality knowledge and engage with capable thinkers", "Avoid learning from others", "Work entirely alone", "Stop developing imagination", "a"),
        (14, 1, "What does Hill call the Sixth Sense?", "Creative imagination", "Physical strength", "Financial knowledge", "Memory", "a"),
        (14, 2, "When does Hill say the Sixth Sense becomes more accessible?", "After mastering the preceding principles", "Before learning anything", "Without any effort", "Only through money", "a"),
        (14, 3, "What can the Sixth Sense provide according to Hill's framework?", "Hunches, inspiration and ideas", "Guaranteed financial returns", "Perfect predictions", "Freedom from all risk", "a"),
        (14, 4, "What should a person do with an idea or hunch?", "Examine and test it", "Automatically believe it", "Ignore every idea", "Treat it as guaranteed truth", "a"),
        (14, 5, "What mental faculty is particularly important to the Sixth Sense?", "Creative imagination", "Procrastination", "Fear", "Indifference", "a"),
        (14, 6, "What should precede reliance on the Sixth Sense?", "Development and application of the earlier principles", "Ignorance", "Indecision", "Avoidance", "a"),
        (14, 7, "What does Hill suggest can emerge during quiet reflection?", "Ideas and inspiration", "Guaranteed wealth", "Other people's thoughts", "Perfect certainty", "a"),
        (14, 8, "What are 'Invisible Counselors'?", "Imagined advisers based on admired people", "Government officials", "Financial institutions", "Actual employees", "a"),
        (14, 9, "Why might someone use the Invisible Counselors exercise?", "To stimulate imagination and seek imagined guidance from admired figures", "To replace real mentors permanently", "To avoid decisions", "To guarantee success", "a"),
        (14, 10, "What should a person do with useful inspiration?", "Convert it into constructive action", "Ignore it", "Wait indefinitely", "Hide it", "a"),
        (14, 11, "What can interfere with the Sixth Sense according to Hill?", "Indecision, doubt and fear", "Knowledge", "Persistence", "Desire", "a"),
        (14, 12, "What should participants do with intuitive ideas in a modern practical application?", "Test them against evidence and reality", "Accept every hunch as fact", "Reject every idea", "Stop researching", "a"),
        (14, 13, "What is the Sixth Sense connected to?", "Creative imagination and inspiration", "Physical strength", "Financial accounting", "Formal qualifications", "a"),
        (14, 14, "What is the purpose of mastering the earlier principles?", "To prepare the mind for the higher level of thinking Hill describes", "To eliminate planning", "To eliminate knowledge", "To avoid action", "a"),
        (14, 15, "What is the safest practical interpretation for the NYS course?", "Develop intuition and creativity, then test ideas before acting", "Treat every feeling as fact", "Stop gathering evidence", "Depend entirely on intuition", "a"),
        (15, 1, "What are the 'Six Ghosts of Fear'?", "Six major fears identified by Hill", "Six business competitors", "Six financial strategies", "Six types of imagination", "a"),
        (15, 2, "Which is the first fear listed by Hill?", "Fear of poverty", "Fear of education", "Fear of success", "Fear of travel", "a"),
        (15, 3, "Which fear concerns what other people think?", "Fear of criticism", "Fear of old age", "Fear of death", "Fear of ill health", "a"),
        (15, 4, "Which fear concerns physical wellbeing?", "Fear of ill health", "Fear of criticism", "Fear of poverty", "Fear of old age", "a"),
        (15, 5, "Which fear concerns relationships?", "Fear of loss of love", "Fear of poverty", "Fear of death", "Fear of criticism", "a"),
        (15, 6, "Which fear concerns getting older?", "Fear of old age", "Fear of criticism", "Fear of poverty", "Fear of ill health", "a"),
        (15, 7, "Which fear concerns mortality?", "Fear of death", "Fear of criticism", "Fear of poverty", "Fear of loss of love", "a"),
        (15, 8, "Which three negative forces does Hill place at the beginning of the chapter?", "Indecision, doubt and fear", "Desire, faith and hope", "Knowledge, imagination and planning", "Love, enthusiasm and romance", "a"),
        (15, 9, "According to Hill, what is the relationship between indecision, doubt and fear?", "Indecision can develop into doubt, which blends into fear", "They are completely unrelated", "Fear creates knowledge", "Doubt creates persistence", "a"),
        (15, 10, "What should participants do when studying the six fears?", "Examine themselves honestly to identify which fears may be affecting them", "Ignore them", "Blame others", "Pretend they do not exist", "a"),
        (15, 11, "What does Hill call these fears?", "Ghosts", "Opportunities", "Principles", "Assets", "a"),
        (15, 12, "Why does Hill call them 'ghosts'?", "He presents them as creations of the mind rather than physical beings", "They only occur at night", "They are supernatural creatures", "They are financial problems", "a"),
        (15, 13, "What can fear contribute to?", "Discouragement, procrastination and indecision", "Guaranteed success", "Better planning automatically", "Specialised knowledge", "a"),
        (15, 14, "What should a person replace worry with?", "Constructive decision and action", "More worry", "Avoidance", "Blame", "a"),
        (15, 15, "What is the overall purpose of the chapter?", "Identify and overcome the fears that interfere with purposeful action", "Eliminate all risk from life", "Avoid making decisions", "Stop pursuing goals", "a"),
    ]
    
    for ch, qn, q, a, b, c, d, corr in raw_questions:
        # Notice: chapter_question_num and correct_answer_text are REMOVED to match models.py perfectly
        db.add(Question(
            question_id=f"Q{ch}-{str(qn).zfill(2)}", 
            chapter=ch, 
            question_text=q, 
            option_a=a, 
            option_b=b, 
            option_c=c, 
            option_d=d,
            correct_answer=corr, 
            marks=1
        ))
    
    db.commit()
    return {"message": f"Successfully seeded all {len(raw_questions)} questions!"}

@app.get("/seed-nemisa")
def seed_nemisa(db = Depends(get_db)):
    if db.query(NemisaCourse).count() >= 12: return {"message": "NEMISA courses already seeded."}
    NEMISA_COURSES_DATA = [
        (1, "GH-900", "GitHub Foundations", "Foundation", 2), (2, "PL-900", "Microsoft Power Platform Fundamentals", "Foundation", 2),
        (3, "AB-730", "AI Business Professional", "AI / Business", 2), (4, "AB-731", "AI Transformation Leader", "AI / Business", 2),
        (5, "COPILOT", "Microsoft 365 Copilot & Agent Admin Fundamentals", "AI / Productivity", 2), (6, "POWER-BI", "Microsoft Certified: Power BI Data Analyst Associate", "Data", 3),
        (7, "AZURE-AI", "Microsoft Certified: Azure AI Engineer Associate", "AI / Technical", 3), (8, "AZURE-DEV", "Microsoft Certified: Azure Developer Associate", "Development", 3),
        (9, "AZ-305", "Designing Microsoft Azure Infrastructure Solutions", "Architecture", 3), (10, "SEC-OPS", "Microsoft Certified: Security Operations Analyst Associate", "Security", 2),
        (11, "CYBER-ARCH", "Microsoft Certified: Cybersecurity Architect Expert", "Security Architecture", 3), (12, "DEVOPS", "Microsoft Certified: DevOps Engineer Expert", "DevOps", 3),
    ]
    for seq, code, name, track, weeks in NEMISA_COURSES_DATA:
        db.add(NemisaCourse(sequence=seq, code=code, name=name, track=track, target_weeks=weeks))
    db.commit()
    return {"message": "Successfully seeded 12 NEMISA courses!"}

def update_nemisa_sequence(db, participant_id: str):
    assignments = db.query(NemisaAssignment).filter(NemisaAssignment.participant_id == participant_id).order_by(NemisaAssignment.sequence).all()
    for i, assignment in enumerate(assignments):
        if assignment.progress_pct >= 100 and assignment.status != "COMPLETED":
            assignment.status, assignment.completion_date = "COMPLETED", datetime.utcnow()
            if i + 1 < len(assignments):
                next_course = assignments[i + 1]
                if next_course.status == "NOT STARTED":
                    next_course.status, next_course.start_date = "ACTIVE", datetime.utcnow()
                    next_course.target_date = datetime.utcnow() + timedelta(weeks=next_course.target_weeks)
    db.commit()

@app.get("/api/nemisa/{pid}")
def get_nemisa_data(pid: str, db = Depends(get_db)):
    p = db.query(Participant).filter(Participant.participant_id == pid.upper()).first()
    if not p: raise HTTPException(status_code=404, detail="Participant not found")
    assignments = db.query(NemisaAssignment).filter(NemisaAssignment.participant_id == pid.upper()).order_by(NemisaAssignment.sequence).all()
    reports = db.query(NemisaWeeklyReport).filter(NemisaWeeklyReport.participant_id == pid.upper()).order_by(NemisaWeeklyReport.week_number.desc()).all()
    completed_count = sum(1 for a in assignments if a.status == "COMPLETED")
    active_assignment = next((a for a in assignments if a.status == "ACTIVE"), None)
    return {
        "participant": {"id": p.participant_id, "name": p.full_name, "email": p.email, "status": p.risk_status},
        "progress": {"overall_pct": int((completed_count / 12) * 100) if completed_count > 0 else 0, "completed": completed_count, "remaining": 12 - completed_count, "current_course": active_assignment.course_code if active_assignment else "None", "current_progress": active_assignment.progress_pct if active_assignment else 0, "days_remaining": (active_assignment.target_date - datetime.utcnow()).days if active_assignment and active_assignment.target_date else 0},
        "journey": [{"sequence": a.sequence, "code": a.course_code, "name": db.query(NemisaCourse).filter(NemisaCourse.code == a.course_code).first().name if a.course_code else "Unknown", "status": a.status, "progress": a.progress_pct, "exam_passed": a.exam_passed} for a in assignments],
        "last_report": reports[0].timestamp.strftime("%Y-%m-%d") if reports else "Never"
    }

@app.get("/nemisa/report", response_class=HTMLResponse)
def nemisa_report_form(request: Request): return templates.TemplateResponse(request=request, name="nemisa_report.html", context={})

@app.post("/nemisa/report")
async def submit_nemisa_report(request: Request, db = Depends(get_db)):
    form_data = await request.form()
    pid = str(form_data.get("participant_id", "")).strip().upper()
    p = db.query(Participant).filter(Participant.participant_id == pid).first()
    if not p: raise HTTPException(status_code=404, detail="Participant not found")
    active_assignment = db.query(NemisaAssignment).filter(NemisaAssignment.participant_id == pid, NemisaAssignment.status == "ACTIVE").first()
    course_code = active_assignment.course_code if active_assignment else "GENERAL"
    if active_assignment:
        active_assignment.progress_pct = int(form_data.get("progress_pct", 0))
        update_nemisa_sequence(db, pid)
    db.add(NemisaWeeklyReport(participant_id=pid, week_number=int(form_data.get("week_number", 1)), course_code=course_code, accessed_nemisa=form_data.get("accessed") == "Yes", target_met=form_data.get("target_met", "No"), progress_pct=int(form_data.get("progress_pct", 0)), learnings=form_data.get("learnings", ""), practical_activity=form_data.get("practical", ""), blockers=form_data.get("blockers", ""), support_needed=form_data.get("support", "")))
    db.commit()
    send_email(p.email, f"NEMISA Weekly Report Submitted - Week {form_data.get('week_number')}", f"<div style='font-family: Arial; max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd;'><h2 style='color: #3b82f6;'>✅ NEMISA Weekly Report Received</h2><p>Hi {p.full_name},</p><p>Thank you for submitting your Week {form_data.get('week_number')} report for <strong>{course_code}</strong>.</p><p><strong>Progress:</strong> {form_data.get('progress_pct')}%</p><p>Keep up the 3-2-1 rhythm!</p></div>")
    return RedirectResponse(url="/nemisa", status_code=303)