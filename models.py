# models.py
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Participant(Base):
    __tablename__ = "participants"
    id = Column(Integer, primary_key=True, index=True)
    participant_id = Column(String, unique=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    full_name = Column(String)
    email = Column(String, unique=True, index=True)
    phone = Column(String, nullable=True)
    age_range = Column(String)
    main_goal = Column(String)
    programme_status = Column(String, default="Active")
    
    registration_complete = Column(Boolean, default=True)
    week1_complete = Column(Boolean, default=False)
    week2_complete = Column(Boolean, default=False)
    week3_complete = Column(Boolean, default=False)
    week4_complete = Column(Boolean, default=False)
    final_idp_complete = Column(Boolean, default=False)
    
    overall_progress_pct = Column(Float, default=0.0)
    overall_quiz_pct = Column(Float, default=0.0)
    risk_status = Column(String, default="Not Started")
    risk_reason = Column(String, nullable=True)
    last_activity = Column(DateTime, nullable=True)
    
    week1_actions_complete = Column(Boolean, default=False)
    week2_actions_complete = Column(Boolean, default=False)
    week3_actions_complete = Column(Boolean, default=False)
    week4_actions_complete = Column(Boolean, default=False)
    day30_action_points = Column(Integer, default=0)
    day30_action_progress_pct = Column(Float, default=0.0)
    day30_completed_days = Column(Integer, default=0)
    day30_current_streak = Column(Integer, default=0)
    
    daily_responses = relationship("DailyResponse", back_populates="participant")
    nemisa_assignments = relationship("NemisaAssignment", back_populates="participant")
    enrollments = relationship("Enrollment", back_populates="participant") # NEW

    ai_fluency_progress = relationship("AIFluencyProgress", back_populates="participant")

class Course(Base): # NEW
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)
    title = Column(String)
    description = Column(String)

class Enrollment(Base): # NEW
    __tablename__ = "enrollments"
    id = Column(Integer, primary_key=True, index=True)
    participant_id = Column(String, ForeignKey("participants.participant_id"))
    course_code = Column(String, ForeignKey("courses.code"))
    enrolled_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="Active")
    progress_pct = Column(Float, default=0.0)
    
    participant = relationship("Participant", back_populates="enrollments")

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(String, unique=True, index=True)
    chapter = Column(Integer)
    question_text = Column(String)
    option_a = Column(String)
    option_b = Column(String)
    option_c = Column(String)
    option_d = Column(String)
    correct_answer = Column(String)
    marks = Column(Integer, default=1)

class QuizResponse(Base):
    __tablename__ = "quiz_responses"
    id = Column(Integer, primary_key=True, index=True)
    participant_id = Column(String, ForeignKey("participants.participant_id"))
    week = Column(Integer)
    score = Column(Integer)
    max_score = Column(Integer)
    percentage = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

class DailyResponse(Base):
    __tablename__ = "daily_responses"
    id = Column(Integer, primary_key=True, index=True)
    participant_id = Column(String, ForeignKey("participants.participant_id"))
    day = Column(Integer)
    responses_json = Column(String)
    action_status = Column(String)
    reflection = Column(String)
    evidence_file = Column(String, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    participant = relationship("Participant", back_populates="daily_responses")

class NemisaCourse(Base):
    __tablename__ = "nemisa_courses"
    id = Column(Integer, primary_key=True, index=True)
    sequence = Column(Integer, unique=True)
    code = Column(String, unique=True, index=True)
    name = Column(String)
    track = Column(String)
    target_weeks = Column(Integer)

class NemisaAssignment(Base):
    __tablename__ = "nemisa_assignments"
    id = Column(Integer, primary_key=True, index=True)
    participant_id = Column(String, ForeignKey("participants.participant_id"))
    course_code = Column(String, ForeignKey("nemisa_courses.code"))
    sequence = Column(Integer, default=1)
    status = Column(String, default="NOT STARTED")
    progress_pct = Column(Integer, default=0)
    start_date = Column(DateTime, nullable=True)
    target_date = Column(DateTime, nullable=True)
    completion_date = Column(DateTime, nullable=True)
    exam_booked = Column(Boolean, default=False)
    exam_passed = Column(Boolean, default=False)
    participant = relationship("Participant", back_populates="nemisa_assignments")

class NemisaWeeklyReport(Base):
    __tablename__ = "nemisa_weekly_reports"
    id = Column(Integer, primary_key=True, index=True)
    participant_id = Column(String, ForeignKey("participants.participant_id"))
    week_number = Column(Integer)
    course_code = Column(String)
    accessed_nemisa = Column(Boolean, default=False)
    target_met = Column(String)
    progress_pct = Column(Integer, default=0)
    learnings = Column(String)
    practical_activity = Column(String)
    blockers = Column(String)
    support_needed = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

class AIFluencyProgress(Base):
    __tablename__ = "ai_fluency_progress"
    id = Column(Integer, primary_key=True, index=True)
    participant_id = Column(String, ForeignKey("participants.participant_id"))
    module_code = Column(String)
    module_name = Column(String)
    completed = Column(Boolean, default=False)
    evidence = Column(String, nullable=True)  # Text description of the project/evidence
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    participant = relationship("Participant")
