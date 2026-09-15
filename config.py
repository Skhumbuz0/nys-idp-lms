# config.py
CONFIG = {
    "APP_NAME": "NYS IDP — Think and Grow Rich 30-Day Challenge",
    "WEEK_STRUCTURE": {
        1: {"chapters": [1, 2, 3, 4], "questions": 60, "max_marks": 60},
        2: {"chapters": [5, 6, 7, 8], "questions": 60, "max_marks": 60},
        3: {"chapters": [9, 10, 11, 12], "questions": 60, "max_marks": 60},
        4: {"chapters": [13, 14, 15], "questions": 45, "max_marks": 45}
    },
    "TOTAL_QUESTIONS": 225,
    "TOTAL_MARKS": 225,
    "AT_RISK_SCORE": 50,
    "NEEDS_ATTENTION_SCORE": 70,
    "CHAPTER_SCORE_LEVELS": {"EXCELLENT": 87, "VERY_GOOD": 73, "GOOD": 60, "NEEDS_REVIEW": 47}
}