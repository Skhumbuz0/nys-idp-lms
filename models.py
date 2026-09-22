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
    enrollments = relationship("Enrollment", back_populates="participant")
    ai_fluency_progress = relationship("AIFluencyProgress", back_populates="participant") # <-- MAKE SURE THIS IS HERE
    l2l_progress = relationship("L2LProgress", back_populates="participant")
    employment_profile = relationship("EmploymentProfile", back_populates="participant")

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
    evidence = Column(String, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    participant = relationship("Participant", back_populates="ai_fluency_progress")

class L2LProgress(Base):
    __tablename__ = "l2l_progress"
    id = Column(Integer, primary_key=True, index=True)
    participant_id = Column(String, ForeignKey("participants.participant_id"))
    module_code = Column(String)
    quiz_score = Column(Integer, default=0)
    quiz_max = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    participant = relationship("Participant")

# Add these to the bottom of models.py

class EmploymentProfile(Base):
    __tablename__ = "employment_profiles"
    id = Column(Integer, primary_key=True, index=True)
    participant_id = Column(String, ForeignKey("participants.participant_id"), unique=True)
    
    # Contact & Photo
    professional_name = Column(String, nullable=True)
    professional_email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    city = Column(String, nullable=True)
    province = Column(String, nullable=True)
    photo_path = Column(String, nullable=True)
    
    # Personal Details
    id_number = Column(String, nullable=True)
    nationality = Column(String, default="South African")
    gender = Column(String, nullable=True)
    marital_status = Column(String, nullable=True)
    health_status = Column(String, default="Good")
    criminal_record = Column(String, default="None")
    
    # Profile & Career
    professional_profile = Column(String, nullable=True)
    career_objective = Column(String, nullable=True)
    
    # Lists (stored as newline-separated text or JSON)
    core_competencies = Column(String, nullable=True)
    certifications = Column(String, nullable=True)
    skills = Column(String, nullable=True)
    references = Column(String, nullable=True) # Format: "Name - Title, Org | Phone | Email"
    
    profile_completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    participant = relationship("Participant")

class EmploymentExperience(Base):
    __tablename__ = "employment_experiences"
    id = Column(Integer, primary_key=True, index=True)
    participant_id = Column(String, ForeignKey("participants.participant_id"))
    experience_type = Column(String)
    organisation = Column(String)
    position = Column(String)
    start_date = Column(String)
    end_date = Column(String, nullable=True)
    description = Column(String)
    skills_used = Column(String, nullable=True)
    achievements = Column(String, nullable=True)
    currently_active = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    participant = relationship("Participant")

class JobOpportunity(Base):
    __tablename__ = "job_opportunities"
    id = Column(Integer, primary_key=True, index=True)
    participant_id = Column(String, ForeignKey("participants.participant_id"))
    employer = Column(String)
    position = Column(String)
    reference_number = Column(String, nullable=True)
    location = Column(String, nullable=True)
    source = Column(String)
    job_url = Column(String, nullable=True)
    closing_date = Column(String, nullable=True)
    requirements = Column(String)
    application_method = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    participant = relationship("Participant")
    applications = relationship("JobApplication", back_populates="opportunity")

class JobApplication(Base):
    __tablename__ = "job_applications"
    id = Column(Integer, primary_key=True, index=True)
    participant_id = Column(String, ForeignKey("participants.participant_id"))
    opportunity_id = Column(Integer, ForeignKey("job_opportunities.id"), nullable=True)
    date_applied = Column(String, nullable=True)
    status = Column(String, default="Preparing")
    follow_up_date = Column(String, nullable=True)
    response_date = Column(String, nullable=True)
    outcome = Column(String, nullable=True)
    notes = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    participant = relationship("Participant")
    opportunity = relationship("JobOpportunity", back_populates="applications")

class EmploymentWeeklyReport(Base):
    __tablename__ = "employment_weekly_reports"
    id = Column(Integer, primary_key=True, index=True)
    participant_id = Column(String, ForeignKey("participants.participant_id"))
    week_start = Column(String)
    week_end = Column(String)
    application_target = Column(Integer, default=5)
    jobs_found = Column(Integer, default=0)
    jobs_analysed = Column(Integer, default=0)
    cvs_tailored = Column(Integer, default=0)
    cover_letters_written = Column(Integer, default=0)
    applications_submitted = Column(Integer, default=0)
    followups_completed = Column(Integer, default=0)
    interviews_received = Column(Integer, default=0)
    responses_received = Column(Integer, default=0)
    reflection = Column(String, nullable=True)
    what_worked = Column(String, nullable=True)
    what_did_not_work = Column(String, nullable=True)
    lessons_learned = Column(String, nullable=True)
    next_week_action = Column(String, nullable=True)
    submitted = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    participant = relationship("Participant")

class EmploymentDocument(Base):
    __tablename__ = "employment_documents"
    id = Column(Integer, primary_key=True, index=True)
    participant_id = Column(String, ForeignKey("participants.participant_id"))
    document_type = Column(String)
    content = Column(String)
    job_opportunity_id = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    participant = relationship("Participant")
    
    class EmploymentProgress(Base):
        __tablename__ = "employment_progress"
        id = Column(Integer, primary_key=True, index=True)
        participant_id = Column(String, ForeignKey("participants.participant_id"))
        module_code = Column(String)
        quiz_score = Column(Integer, default=0)
        quiz_max = Column(Integer, default=0)
        completed = Column(Boolean, default=False)
        timestamp = Column(DateTime, default=datetime.utcnow)
        
        participant = relationship("Participant")
