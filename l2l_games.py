# ==========================================
# L2L INTERACTIVE GAMES API
# ==========================================
@app.get("/l2l/game/{module_code}", response_class=HTMLResponse)
def l2l_game_view(request: Request, module_code: str):
    module = next((m for m in L2L_MODULES if m["code"] == module_code), None)
    if not module:
        raise HTTPException(404, "Module not found")
    return templates.TemplateResponse(request=request, name="l2l_game.html", context={"module": module})

@app.post("/api/l2l/game/audit")
async def submit_l2l_audit(request: Request, db = Depends(get_db)):
    data = await request.json()
    pid = data.get("participant_id", "").strip().upper()
    result = LearnerAuditSuite.evaluate_audit(
        habits_score=data.get("habits_score", 0),
        locus_internal=data.get("locus_internal", 0),
        locus_external=data.get("locus_external", 0),
        environment_score=data.get("environment_score", 0)
    )
    return result

@app.post("/api/l2l/game/fluency")
async def simulate_fluency(request: Request):
    data = await request.json()
    days = int(data.get("days", 7))
    return FluencyIllusionSimulator.compare_methods(days)

@app.post("/api/l2l/game/plan")
async def generate_plan(request: Request):
    data = await request.json()
    return LearningPlanGenerator.generate_plan(
        total_hours=float(data.get("hours", 10)),
        modules=data.get("modules", []),
        exam_date_str=data.get("exam_date", "")
    )

@app.post("/api/l2l/game/eisenhower")
async def classify_task(request: Request):
    data = await request.json()
    return LearningPlanGenerator.classify_task(
        urgent=data.get("urgent", False),
        important=data.get("important", False)
    )

@app.post("/api/l2l/game/procrastination")
async def diagnose_procrastination(request: Request):
    data = await request.json()
    return ProcrastinationEngine.diagnose(data.get("trigger", "overwhelm"))

@app.post("/api/l2l/game/leitner")
async def process_leitner(request: Request):
    data = await request.json()
    return LeitnerFlashcardEngine.process_card(
        current_box=int(data.get("box", 1)),
        correct=data.get("correct", True)
    )

@app.post("/api/l2l/game/exam-strategy")
async def generate_exam_strategy(request: Request):
    data = await request.json()
    return ExamStrategyEngine.generate_strategy(
        subject=data.get("subject", "General"),
        days_remaining=int(data.get("days", 30)),
        confidence=int(data.get("confidence", 3))
    )

@app.post("/api/l2l/game/feynman")
async def evaluate_feynman(request: Request):
    data = await request.json()
    return MetacognitiveFeynmanEngine.evaluate_explanation(
        topic=data.get("topic", "photosynthesis"),
        learner_text=data.get("text", "")
    )
