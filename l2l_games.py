# l2l_games.py
import math
import re
from datetime import datetime

# =====================================================================
# MODULE 1 — Synaptic Pinball Game Logic
# =====================================================================
class SynapticPinballGame:
    def __init__(self):
        self.mode = "Focused"
        self.synaptic_strength = 10
        self.bdnf_points = 0
        self.dendritic_spines = 0
        self.consecutive_focus_attempts = 0

    def attempt_problem(self, problem_difficulty):
        if self.mode == "Focused":
            self.consecutive_focus_attempts += 1
            if problem_difficulty <= 5:
                self.synaptic_strength += 2
                return {"status": "SUCCESS", "mode": "Focused",
                        "message": "Direct hit! Tight bumpers solved the familiar problem.",
                        "strength": self.synaptic_strength}
            else:
                if self.consecutive_focus_attempts >= 2:
                    return {"status": "STUCK", "mode": "Focused",
                            "message": "Ball stuck! Switch to Diffuse Mode (Take a Break).",
                            "strength": self.synaptic_strength}
                return {"status": "RETRY", "mode": "Focused",
                        "message": "Bounced off tight bumpers. Try again or switch modes.",
                        "strength": self.synaptic_strength}
        else:
            self.consecutive_focus_attempts = 0
            self.bdnf_points += 15
            if self.bdnf_points >= 30:
                self.dendritic_spines += 1
                self.bdnf_points -= 30
            self.synaptic_strength += 5
            return {"status": "INSIGHT", "mode": "Diffuse",
                    "message": "Creative insight! Dendritic spines sprouting!",
                    "strength": self.synaptic_strength, "spines": self.dendritic_spines}

    def toggle_mode(self):
        self.mode = "Diffuse" if self.mode == "Focused" else "Focused"
        return self.mode


# =====================================================================
# MODULE 2 — Learner Audit Suite
# =====================================================================
class LearnerAuditSuite:
    @staticmethod
    def evaluate_audit(habits_score, locus_internal, locus_external, environment_score):
        if habits_score >= 7:
            orientation = "Deep Learner"
            habit_tip = "You actively search for principles. Keep elaborating with 'Why' questions."
        elif habits_score >= 5:
            orientation = "Strategic Learner"
            habit_tip = "Balance grades with understanding. Add more active elaboration."
        else:
            orientation = "Surface Learner"
            habit_tip = "Shift from memorization to explaining concepts in your own words."

        if locus_internal > locus_external:
            locus = "Internal"
            locus_tip = "You own your outcomes. Keep taking personal responsibility."
        else:
            locus = "External"
            locus_tip = "Focus on controllable daily actions rather than blaming luck."

        total = habits_score + min(locus_internal, 10) + environment_score
        if total >= 18:
            overall = "🟢 High-Performance Learner"
        elif total >= 12:
            overall = "🟡 Developing Learner"
        else:
            overall = "🔴 Needs Foundation Work"

        return {
            "orientation": orientation,
            "habit_tip": habit_tip,
            "locus": locus,
            "locus_tip": locus_tip,
            "overall": overall,
            "total_score": total
        }


# =====================================================================
# MODULE 3 — Fluency Illusion Simulator
# =====================================================================
class FluencyIllusionSimulator:
    @staticmethod
    def compare_methods(days_elapsed):
        rereading_retention = round(100 * math.exp(-0.8 * days_elapsed), 1)
        active_recall_retention = round(100 * math.exp(-0.15 * days_elapsed), 1)
        return {
            "days": days_elapsed,
            "rereading": {
                "retention": rereading_retention,
                "confidence": 85,
                "label": "Passive Rereading"
            },
            "active_recall": {
                "retention": active_recall_retention,
                "confidence": 65,
                "label": "Active Recall"
            },
            "insight": "Rereading feels easy but creates false confidence. Active recall feels harder but builds permanent neural pathways."
        }


# =====================================================================
# MODULE 4 — Learning Plan Generator
# =====================================================================
class LearningPlanGenerator:
    @staticmethod
    def generate_plan(total_hours, modules, exam_date_str):
        exploration = round(total_hours * 0.60, 1)
        fixation = round(total_hours * 0.30, 1)
        testing = round(total_hours * 0.10, 1)
        
        try:
            exam_date = datetime.strptime(exam_date_str, "%Y-%m-%d")
            days_left = (exam_date - datetime.now()).days
        except:
            days_left = 30
        
        return {
            "total_hours": total_hours,
            "allocation": {
                "exploration": exploration,
                "fixation": fixation,
                "testing": testing
            },
            "days_until_exam": days_left,
            "modules": modules,
            "recommendation": f"With {days_left} days left, prioritize Quadrant 2 (important but not urgent) activities."
        }

    @staticmethod
    def classify_task(urgent, important):
        if urgent and important:
            return {"quadrant": "Q1", "label": "DO NOW", "color": "red", "action": "Handle immediately"}
        elif not urgent and important:
            return {"quadrant": "Q2", "label": "SCHEDULE", "color": "green", "action": "Protect this time!"}
        elif urgent and not important:
            return {"quadrant": "Q3", "label": "DELEGATE", "color": "yellow", "action": "Batch or delegate"}
        else:
            return {"quadrant": "Q4", "label": "ELIMINATE", "color": "gray", "action": "Remove entirely"}


# =====================================================================
# MODULE 5 — Procrastination Engine
# =====================================================================
class ProcrastinationEngine:
    TRIGGERS = {
        "overwhelm": {
            "cause": "Task feels too massive",
            "action": "5-Minute Start Rule",
            "instruction": "Commit to working for EXACTLY 5 minutes. 80% of the time, overcoming starting friction keeps you going!",
            "icon": "🏔️"
        },
        "perfectionism": {
            "cause": "Fear of imperfect work",
            "action": "Rough Draft Dump",
            "instruction": "Give yourself permission to make an imperfect first attempt. Lower the bar to get words on paper.",
            "icon": "📝"
        },
        "distraction": {
            "cause": "Phone/social media pull",
            "action": "Environmental Friction",
            "instruction": "Put phone in another room. Add 20 seconds of effort to access distractions.",
            "icon": "📱"
        },
        "fear": {
            "cause": "Anticipated discomfort (insular cortex pain)",
            "action": "Pomodoro 25/5 Loop",
            "instruction": "Focus ONLY on the 25-minute timer, not the task completion. Pain disappears once in flow state.",
            "icon": "⏱️"
        }
    }

    @staticmethod
    def diagnose(trigger_key):
        return ProcrastinationEngine.TRIGGERS.get(trigger_key, {
            "cause": "General friction",
            "action": "Remove obstacles",
            "instruction": "Clear your desk and start with the easiest sub-task.",
            "icon": "🔧"
        })


# =====================================================================
# MODULE 6 — Leitner Flashcard Engine
# =====================================================================
class LeitnerFlashcardEngine:
    INTERVALS = {1: 1, 2: 3, 3: 7, 4: 14, 5: 30}

    @staticmethod
    def process_card(current_box, correct):
        if correct:
            new_box = min(5, current_box + 1)
            return {"new_box": new_box, "interval": LeitnerFlashcardEngine.INTERVALS[new_box],
                    "message": f"✅ Promoted to Box {new_box} (review in {LeitnerFlashcardEngine.INTERVALS[new_box]} days)"}
        else:
            return {"new_box": 1, "interval": 1,
                    "message": "❌ Demoted to Box 1 (review tomorrow)"}


# =====================================================================
# MODULE 7 — Exam Strategy Engine (PDSA)
# =====================================================================
class ExamStrategyEngine:
    @staticmethod
    def generate_strategy(subject, days_remaining, confidence):
        if confidence <= 2:
            focus = "Heavy Exploration (60% on core fundamentals)"
        elif confidence <= 4:
            focus = "Balanced Fixation (50% on active recall)"
        else:
            focus = "Targeted Testing (70% on past papers)"

        return {
            "subject": subject,
            "days_remaining": days_remaining,
            "confidence": confidence,
            "plan": f"Break syllabus into {max(1, days_remaining - 2)} daily chunks; reserve final 2 days for mock testing.",
            "do": "Apply SQ3R reading and 5 R's of Note-Taking.",
            "study": "Analyze mistakes: separate Knowledge Gaps from Testing Errors.",
            "act": f"Adjust schedule to target weak topics. Focus: {focus}",
            "priority": "Quadrant 2 strategic study"
        }


# =====================================================================
# MODULE 8 — Metacognitive Feynman Engine
# =====================================================================
class MetacognitiveFeynmanEngine:
    TOPICS = {
        "photosynthesis": ["sunlight", "chloroplast", "water", "carbon dioxide", "glucose", "oxygen"],
        "growth mindset": ["effort", "practice", "learn", "improve", "challenge", "yet"],
        "active recall": ["retrieve", "memory", "test", "practice", "close", "book"]
    }

    @staticmethod
    def evaluate_explanation(topic, learner_text):
        text_lower = learner_text.lower()
        key_concepts = MetacognitiveFeynmanEngine.TOPICS.get(topic, MetacognitiveFeynmanEngine.TOPICS["photosynthesis"])
        found = [c for c in key_concepts if c in text_lower]
        coverage = round((len(found) / len(key_concepts)) * 100, 1)

        words = [w for w in re.findall(r'\b\w+\b', text_lower) if len(w) > 2]
        avg_word_length = sum(len(w) for w in words) / max(1, len(words))
        word_count = len(words)

        jargon_words = [w for w in words if len(w) > 10]
        jargon_ratio = len(jargon_words) / max(1, word_count)

        if coverage >= 80 and avg_word_length < 6.0 and jargon_ratio < 0.05:
            level = "MASTERY"
            feedback = "🎓 Outstanding! You explained the concept simply without jargon. True metacognition!"
        elif coverage >= 50:
            level = "DEVELOPING"
            missing = set(key_concepts) - set(found)
            feedback = f"📚 Good progress ({coverage}%). Missing: {', '.join(missing)}. Use everyday analogies."
        else:
            level = "SURFACE"
            feedback = "🔄 Too brief or missing core mechanics. Try a kitchen/sports analogy for a 10-year-old."

        return {
            "coverage": coverage,
            "found_concepts": found,
            "missing_concepts": list(set(key_concepts) - set(found)),
            "word_count": word_count,
            "avg_word_length": round(avg_word_length, 2),
            "jargon_ratio": round(jargon_ratio * 100, 1),
            "level": level,
            "feedback": feedback
        }