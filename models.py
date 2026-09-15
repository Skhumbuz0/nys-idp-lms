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