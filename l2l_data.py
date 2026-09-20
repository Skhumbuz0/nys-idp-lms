# l2l_data.py
L2L_MODULES = [
    {
        "code": "L2L-M1", "title": "Module 1: Know Your Brain", "icon": "🧠",
        "content_html": """
            <h3 class="text-xl font-bold mt-4 mb-2">What is Learning?</h3>
            <p>Learning is the physical creation and strengthening of connections between neurons. Your brain contains ~86 billion neurons. When you learn, neurons reach out across microscopic gaps called <strong>synapses</strong>. As you practice, these synaptic connections grow thicker, creating durable neural pathways in long-term memory.</p>
            <h3 class="text-xl font-bold mt-4 mb-2">Working Memory vs. Long-Term Memory</h3>
            <ul class="list-disc pl-6 mb-4">
                <li><strong>Working Memory:</strong> Located in the prefrontal cortex, it holds only about <strong>4 slots</strong> (tentacles of attention). Multitasking drastically reduces capacity.</li>
                <li><strong>Long-Term Memory:</strong> A vast storage network. To move info here, you must compress it into <strong>chunks</strong>—unified mental ribbons that occupy just a single working memory slot.</li>
            </ul>
            <h3 class="text-xl font-bold mt-4 mb-2">Focus Mode vs. Diffuse Mode</h3>
            <ul class="list-disc pl-6 mb-4">
                <li><strong>Focused Mode:</strong> Tightly spaced neural pathways for step-by-step logic and active concentration.</li>
                <li><strong>Diffuse Mode:</strong> Activated during relaxation. Allows thoughts to range widely and forge creative, big-picture connections.</li>
            </ul>
            <h3 class="text-xl font-bold mt-4 mb-2">Sleep & Exercise</h3>
            <p><strong>Sleep:</strong> Brain cells shrink during sleep, allowing fluid to wash away metabolic waste. Sleep is when new dendritic spines sprout and consolidate connections.</p>
            <p><strong>Exercise:</strong> Releases <strong>BDNF</strong> (Brain-Derived Neurotrophic Factor), a "brain fertilizer" that stimulates the birth of new neurons.</p>
        """,
        "quiz": [
            {"q": "What physically happens in the brain when a learner masters a new subject?", "options": ["Brain cells expand in size without changing structure.", "Synaptic connections form and dendritic spines thicken through practice.", "Working memory permanently expands to 20 slots.", "Old neurons die off."], "correct": 1},
            {"q": "Why is cramming all night scientifically counterproductive?", "options": ["The brain stops processing after 20:00.", "Without sleep, metabolic waste accumulates and unreinforced spines are swept away.", "Working memory slots lock permanently.", "Long-term memory only stores daylight info."], "correct": 1},
            {"q": "How many 'slots' does typical human working memory possess?", "options": ["10 to 12 slots.", "Exactly 1 slot.", "Approximately 4 slots.", "Unlimited."], "correct": 2},
            {"q": "When stuck on a difficult problem, what should you do next?", "options": ["Stare at it for 3 hours.", "Take a relaxing break to activate Diffuse Mode.", "Reread the chapter 10 times.", "Quit the course."], "correct": 1},
            {"q": "What chemical released during exercise acts as 'brain fertilizer'?", "options": ["Dopamine", "BDNF", "Cortisol", "Adrenaline"], "correct": 1}
        ]
    },
    {
        "code": "L2L-M2", "title": "Module 2: Know Yourself", "icon": "🪞",
        "content_html": """
            <h3 class="text-xl font-bold mt-4 mb-2">Mindsets (Carol Dweck)</h3>
            <ul class="list-disc pl-6 mb-4">
                <li><strong>Fixed Mindset:</strong> Believes intelligence is set in stone. Views effort as proof of low ability and avoids challenges.</li>
                <li><strong>Growth Mindset:</strong> Understands intellect is cultivated through effort. Setbacks are problems to be analyzed. Key shift: <strong>The Power of YET</strong> ("I can't do this *yet*").</li>
            </ul>
            <h3 class="text-xl font-bold mt-4 mb-2">Deep vs. Surface vs. Strategic Learning</h3>
            <ul class="list-disc pl-6 mb-4">
                <li><strong>Surface:</strong> Memorizing disconnected facts just to pass a test.</li>
                <li><strong>Deep:</strong> Seeking underlying meaning, identifying patterns, and relating new ideas to real-life contexts.</li>
                <li><strong>Strategic:</strong> Organizing time and effort strictly to achieve the highest grades.</li>
            </ul>
            <h3 class="text-xl font-bold mt-4 mb-2">Locus of Control & The 4 Environments</h3>
            <p>Shift from an <strong>External Locus</strong> (blaming teachers/luck) to an <strong>Internal Locus</strong> (taking personal responsibility). Audit your Human, Physical, Spiritual, and Internal environments to optimize learning.</p>
        """,
        "quiz": [
            {"q": "Saying 'I'm just not a math person' reflects which mindset and locus?", "options": ["Growth / Internal", "Fixed / External", "Deep / Strategic", "Diffuse / High Efficacy"], "correct": 1},
            {"q": "How does a Deep Learner approach a textbook chapter?", "options": ["Highlights every 3rd sentence.", "Memorizes definitions word-for-word.", "Looks for underlying patterns and relates concepts to prior knowledge.", "Skips reading entirely."], "correct": 2},
            {"q": "Using the 'Power of YET', how do you reframe 'I can't pass accounting'?", "options": ["Accounting is useless.", "I haven't mastered it YET, but with effort I will.", "I will cheat.", "I am naturally bad forever."], "correct": 1}
        ]
    },
    {
        "code": "L2L-M3", "title": "Module 3: Learn Better", "icon": "📚",
        "content_html": """
            <h3 class="text-xl font-bold mt-4 mb-2">The 6 Science-Backed Strategies</h3>
            <ol class="list-decimal pl-6 mb-4 space-y-2">
                <li><strong>Retrieval Practice:</strong> Forcing your brain to recall info without looking at notes. Rereading creates an <em>Illusion of Competence</em>.</li>
                <li><strong>Spaced Repetition:</strong> Distributing study over time (1 hr/day for 5 days) rather than cramming.</li>
                <li><strong>Interleaving:</strong> Alternating between different topics/problem types in one session to build cognitive flexibility.</li>
                <li><strong>Elaboration:</strong> Asking Why and How, and explaining concepts using the 5 W's.</li>
                <li><strong>Dual Coding:</strong> Combining text with visual diagrams/mind maps to double storage pathways.</li>
                <li><strong>Concrete Examples:</strong> Grounding abstract theories into real-world metaphors.</li>
            </ol>
        """,
        "quiz": [
            {"q": "Which method produces the highest long-term retention?", "options": ["Rereading 3 times.", "Highlighting.", "Retrieval Practice (Active Recall).", "Passive listening."], "correct": 2},
            {"q": "What is the 'Illusion of Competence'?", "options": ["Thinking you don't know it when you do.", "Mistaking the ease of reading text for actual mastery in long-term memory.", "Memorizing numbers fast.", "Believing sleep replaces study."], "correct": 1},
            {"q": "How should you apply Interleaving and Spacing?", "options": ["Study Topic A for 10 hours Sunday.", "Alternate shorter sessions of A, B, and C across several days.", "Study only easy topics.", "Reread notes every 10 mins."], "correct": 1},
            {"q": "What is Dual Coding?", "options": ["Coding in 2 languages.", "Combining text with visual diagrams.", "Listening to 2 podcasts.", "Translating to binary."], "correct": 1}
        ]
    },
    {
        "code": "L2L-M4", "title": "Module 4: Plan Your Learning", "icon": "📅",
        "content_html": """
            <h3 class="text-xl font-bold mt-4 mb-2">The 60/30/10 Principle</h3>
            <ul class="list-disc pl-6 mb-4">
                <li><strong>60% Exploration:</strong> Planning, SMART goals, surveying guides, mapping timelines.</li>
                <li><strong>30% Fixation:</strong> Active note-taking, solving problems, writing.</li>
                <li><strong>10% Testing:</strong> Self-testing and analyzing errors.</li>
            </ul>
            <h3 class="text-xl font-bold mt-4 mb-2">Regression Analysis & Eisenhower Matrix</h3>
            <p><strong>Regression (Backward Staircase):</strong> Start at the final exam date and work backward step-by-step to today to map milestones.</p>
            <p><strong>Eisenhower Matrix:</strong> Focus on <em>Quadrant 2</em> (Not Urgent but Important) for strategic planning and proactive studying.</p>
            <h3 class="text-xl font-bold mt-4 mb-2">Household Negotiation Framework</h3>
            <p>In busy homes, negotiate specific quiet windows by offering a clear trade-off (e.g., "I will do all chores before 16:30 if I get quiet focus time from 17:00-19:00").</p>
        """,
        "quiz": [
            {"q": "Where should 60% of your study time budget be invested?", "options": ["Cramming morning of exam.", "Exploration, planning, and goal setting.", "Socializing.", "Highlighting."], "correct": 1},
            {"q": "How does Regression Analysis help plan for an exam?", "options": ["Guessing from today.", "Starting at the exam date and working backward to map milestones.", "Delaying until 2 days before.", "Calculating IQ."], "correct": 1},
            {"q": "What is the core rule of the Household Negotiation Framework?", "options": ["Demanding family do chores.", "Studying near loud TV.", "Communicating goals, negotiating windows, and offering a fair trade-off.", "Giving up when noisy."], "correct": 2}
        ]
    },
    {
        "code": "L2L-M5", "title": "Module 5: Beat Procrastination", "icon": "⏱️",
        "content_html": """
            <h3 class="text-xl font-bold mt-4 mb-2">The Root Cause: Emotional Regulation</h3>
            <p>Procrastination is an emotional coping mechanism. Looking at a hard task activates the <strong>pain centers</strong> (insular cortex). Your brain seeks a quick dopamine fix via distraction to avoid the discomfort.</p>
            <h3 class="text-xl font-bold mt-4 mb-2">The STAR Method</h3>
            <ol class="list-decimal pl-6 mb-4">
                <li><strong>Stop:</strong> Pause the urge to switch tasks.</li>
                <li><strong>Think:</strong> Recognize pain centers are reacting to anticipated effort, not harm.</li>
                <li><strong>Act:</strong> Apply a low-friction start (5-Minute Rule).</li>
                <li><strong>Review:</strong> Notice how pain disappears once in flow state.</li>
            </ol>
            <h3 class="text-xl font-bold mt-4 mb-2">The Pomodoro Technique</h3>
            <p>Focus strictly on the <strong>time</strong> (25 minutes), not the emotional weight of finishing the whole task. This bypasses the pain center reaction.</p>
        """,
        "quiz": [
            {"q": "What neuroscientific reaction occurs when you look at a task you dislike?", "options": ["Pleasure centers overflow.", "Pain centers (insular cortex) physically activate.", "Long-term memory erases data.", "Working memory expands."], "correct": 1},
            {"q": "What is the core secret of the Pomodoro Technique?", "options": ["Finishing the whole task in 25 mins.", "Focusing strictly on the 25-minute time window, not the task completion.", "Skipping breaks.", "Checking phone every 2 mins."], "correct": 1},
            {"q": "What does the 'S' in STAR stand for?", "options": ["Study", "Stop", "Sleep", "Speed"], "correct": 1}
        ]
    },
    {
        "code": "L2L-M6", "title": "Module 6: Remember More", "icon": "🏰",
        "content_html": """
            <h3 class="text-xl font-bold mt-4 mb-2">Mnemonic Engines</h3>
            <ul class="list-disc pl-6 mb-4 space-y-2">
                <li><strong>Leitner 5-Box System:</strong> Flashcards move to higher boxes (longer review intervals) when correct. Incorrect cards drop immediately back to Box 1.</li>
                <li><strong>Method of Loci (Memory Palace):</strong> Anchoring items to a familiar physical path. Spatial memory in the hippocampus is biologically ancient and stronger than rote memory.</li>
                <li><strong>Acronyms & Acrostics:</strong> Compressing lists into words or vivid sentences.</li>
                <li><strong>Chaining:</strong> Linking items into an exaggerated, bizarre narrative.</li>
            </ul>
        """,
        "quiz": [
            {"q": "In the Leitner system, what happens if you miss a card in Box 4?", "options": ["Stays in Box 4.", "Moves to Box 5.", "Demoted back to Box 1.", "Deleted."], "correct": 2},
            {"q": "Why is the Method of Loci so effective?", "options": ["Human brains evolved powerful spatial memory pathways in the hippocampus.", "Allows sleeping during tests.", "Expands working memory to 50 slots.", "Replaces practice."], "correct": 0},
            {"q": "Why is an acronym like STAR a useful cognitive chunk?", "options": ["Replaces understanding.", "Compresses 4 steps into a single mental ribbon, freeing working memory.", "Eliminates long-term storage.", "Only works for languages."], "correct": 1}
        ]
    },
    {
        "code": "L2L-M7", "title": "Module 7: Prepare for Exams", "icon": "📝",
        "content_html": """
            <h3 class="text-xl font-bold mt-4 mb-2">The Shewhart Cycle (PDSA)</h3>
            <ol class="list-decimal pl-6 mb-4">
                <li><strong>Plan:</strong> Set targets, build backwards timetable.</li>
                <li><strong>Do:</strong> Execute active recall sessions.</li>
                <li><strong>Study:</strong> Review practice results and evaluate.</li>
                <li><strong>Act:</strong> Adjust tactics and re-allocate time to weak topics.</li>
            </ol>
            <h3 class="text-xl font-bold mt-4 mb-2">Post-Test Error Analysis</h3>
            <p>Categorize missed questions into:<br>
            <strong>Category A (Strategic Errors):</strong> Rushing, misreading directions.<br>
            <strong>Category B (Knowledge Gaps):</strong> Real conceptual misunderstandings requiring re-learning.</p>
        """,
        "quiz": [
            {"q": "What are the 4 steps of the Shewhart Cycle (PDSA)?", "options": ["Read, Highlight, Memorize, Repeat.", "Plan, Do, Study, Act.", "Stop, Think, Act, Review.", "Survey, Question, Read, Recite."], "correct": 1},
            {"q": "Why separate Strategic Errors from Knowledge Gaps?", "options": ["Strategic errors require fixing habits; Knowledge gaps require re-learning concepts.", "Strategic means drop the subject.", "Knowledge gaps can't be fixed.", "No difference."], "correct": 0},
            {"q": "In the 5 R's of Note Taking, what does 'Recite' require?", "options": ["Copying textbook word-for-word.", "Covering notes and stating concepts out loud in your own words.", "Reading silently with TV on.", "Typing fast without thinking."], "correct": 1}
        ]
    },
    {
        "code": "L2L-M8", "title": "Module 8: Become Your Own Teacher", "icon": "🎓",
        "content_html": """
            <h3 class="text-xl font-bold mt-4 mb-2">Metacognition & Bloom's Taxonomy</h3>
            <p><strong>Metacognition</strong> is "thinking about thinking"—monitoring and directing your own cognitive processes. Mastery occurs at Bloom's higher levels: <strong>Analysis, Synthesis, and Evaluation</strong> (Levels 4-6), rather than just Knowledge (Level 1).</p>
            <h3 class="text-xl font-bold mt-4 mb-2">The Feynman Technique</h3>
            <ol class="list-decimal pl-6 mb-4">
                <li>Choose a concept.</li>
                <li>Teach it to a 10-year-old using simple language and analogies (zero jargon).</li>
                <li>Identify where your explanation breaks down (this pinpoints your exact Knowledge Gap).</li>
                <li>Return to source material to refine understanding.</li>
            </ol>
        """,
        "quiz": [
            {"q": "What is Metacognition?", "options": ["Reading 2 books at once.", "Thinking about thinking—monitoring and evaluating your own learning.", "Memorizing without understanding.", "Skull bone growth."], "correct": 1},
            {"q": "What is the core test of the Feynman Technique?", "options": ["Writing an 80-page jargon dissertation.", "Explaining a concept simply so a 10-year-old can understand it.", "Rereading until asleep.", "Memorizing formulas."], "correct": 1},
            {"q": "Which Bloom's levels represent higher-order mastery?", "options": ["Knowledge (Level 1).", "Surface (Level 0).", "Analysis, Synthesis, and Evaluation (Levels 4, 5, 6).", "Passive Listening."], "correct": 2}
        ]
    }
]