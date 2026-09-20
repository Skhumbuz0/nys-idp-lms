# l2l_data.py

L2L_MODULES = [
    {
        "code": "L2L-M1", "title": "Module 1: Know Your Brain", "icon": "🧠",
        "content_html": """
            <h3>Sub-Module 1.1: The Building Blocks of the Brain</h3>
            <p><strong>Detailed Explanation:</strong> The human brain contains approximately 86 billion neurons. Each neuron is a specialized biological cell composed of a main cell body, branching input structures called <strong>dendrites</strong>, small projections on those dendrites called <strong>dendritic spines</strong>, and a long output transmitter called an <strong>axon</strong>. Neurons communicate by sending electrical signals down the axon that jump neurochemically across microscopic gaps called <strong>synapses</strong> to tickle the dendritic spines of adjoining neurons. Learning is not a vague abstract concept—it is the physical creation and strengthening of these synaptic links in long-term memory in the neocortex.</p>
            <p><strong>Real-World Example:</strong> When a learner practices multiplying numbers, electrical signals repeatedly fire across specific synaptic pathways. The first time a student encounters a new mathematical concept, the pathway is faint and weak. With repeated practice, the connection physically thickens, allowing signals to travel effortlessly.</p>

            <h3>Sub-Module 1.2: Brain Modes — Focused vs. Diffuse Thinking</h3>
            <p><strong>Detailed Explanation:</strong> The brain operates in two fundamentally distinct neural modes: <strong>Focused Mode</strong> and <strong>Diffuse Mode</strong>. Focused mode uses tightly spaced "pinball bumpers" across established neural pathways in the prefrontal cortex, ideal for analyzing familiar problems. Diffuse mode uses widely spaced bumpers across resting-state networks, allowing the mind to wander and connect distant neural nodes. You cannot be in both modes simultaneously for the same topic.</p>
            <p><strong>Real-World Example:</strong> Historical figures like Salvador Dalí and Thomas Edison harnessed the diffuse mode. When stuck on a complex invention, Edison would sit in a chair holding ball bearings over a brass plate and let himself drift off to sleep. As his hand relaxed and the balls clattered, he woke up, retrieving the creative, diffuse insights his brain had generated while relaxed.</p>

            <h3>Sub-Module 1.3: Memory Architecture — Working vs. Long-Term Memory</h3>
            <p><strong>Detailed Explanation:</strong> <strong>Working memory</strong> is the temporary workspace located in the prefrontal cortex, holding roughly 4 information "slots" or "tentacles of attention". It requires continuous metabolic energy to keep information active. <strong>Long-term memory</strong> is a vast, distributed storage warehouse located throughout the neocortex. Transitioning knowledge from working memory into long-term memory requires constructing "neural chunks"—compact ribbons of integrated information that can be easily pulled back into working memory without overloading its 4 slots.</p>
            <p><strong>Real-World Example:</strong> When a novice driver first learns to reverse a car, their 4 working memory slots are overloaded: checking mirrors, modulating the clutch, turning the wheel, and looking behind. After weeks of practice, these separate actions consolidate into a single "car reversing chunk," freeing working memory to listen to the radio or navigate.</p>

            <h3>Sub-Module 1.4: Brain Maintenance — Sleep, Waste Clearance, and Synaptic Mortar</h3>
            <p><strong>Detailed Explanation:</strong> Sleep is an active, essential phase of learning. During waking hours, metabolic activity generates toxic byproducts that accumulate between brain cells. When you sleep, brain cells shrink slightly, allowing cerebrospinal fluid to wash away these metabolic toxins like a "synaptic janitor". Furthermore, sleep allows the brain to review daytime lessons, drying the "synaptic mortar" between neural bricks and sprouting new dendritic spines overnight.</p>
            <p><strong>Real-World Example:</strong> If a student studies for 5 hours crammed into a single night without sleep, the un-set mortar crumbles, and metabolic waste blocks neural pathways. In contrast, studying 1 hour per day over 5 days with sleep in between allows the synaptic janitor to clear waste and build solid neural structures.</p>

            <h3>Sub-Module 1.5: Neurogenesis & Brain Fertilizer — Exercise and BDNF</h3>
            <p><strong>Detailed Explanation:</strong> Contrary to old myths, thousands of new neurons are born every single day in the hippocampus through a process called <strong>neurogenesis</strong>. Aerobic exercise releases a chemical called <strong>Brain-Derived Neurotrophic Factor (BDNF)</strong>, which acts as "brain fertilizer". BDNF stimulates existing neurons to sprout new dendritic spines and helps newly born neurons survive and integrate into learning networks.</p>
            <p><strong>Real-World Example:</strong> A student who takes a brisk 20-minute walk or engages in sports before studying sprinkles BDNF across their hippocampal neurons, making it significantly easier for new synaptic connections to form.</p>
        """,
        "quiz": [
            {"q": "What physically occurs in the brain when a student truly masters a new academic concept?", "options": ["The brain swells in overall volume.", "Axons and dendritic spines form new synapses, creating thick neural links in long-term networks.", "Working memory permanently expands from 4 to 12 slots.", "Existing neurons divide rapidly through mitosis."], "correct": 1},
            {"q": "Why does cramming for 5 hours the night before an exam produce poor long-term retention?", "options": ["The brain shuts down working memory after 18:00.", "Without intervals of sleep, synaptic mortar cannot dry, and unreinforced spines are swept away by synaptic janitors.", "Five hours exhausts the hippocampus's electrical voltage.", "Cramming causes working memory slots to shrink to zero."], "correct": 1},
            {"q": "How does physical exercise directly enhance the brain's ability to learn new material?", "options": ["It eliminates the need for sleep.", "It triggers the release of BDNF, causing new dendritic spines to sprout.", "It permanently switches the brain into Focused Mode.", "It converts short-term memory directly into gray matter."], "correct": 1},
            {"q": "Which metaphor best illustrates how the brain solves a completely unfamiliar problem type for the first time?", "options": ["A race car on a pre-paved highway.", "A pinball machine with widely spaced bumpers (Diffuse Mode).", "A filing cabinet opening a pre-labeled folder.", "An octopus holding four identical objects."], "correct": 1},
            {"q": "A student has been trying to solve a complex math proof for 45 minutes and feels frustrated. What is the scientifically optimal next step?", "options": ["Force themselves to stare at the equation for another two hours.", "Reread the textbook chapter five times.", "Step away and take a walk to allow Diffuse Mode to process the problem.", "Assume they lack the 'math gene' and give up."], "correct": 2}
        ]
    },
    {
        "code": "L2L-M2", "title": "Module 2: Know Yourself", "icon": "🪞",
        "content_html": """
            <h3>Sub-Module 2.1: Learning Orientations — Surface, Deep, and Strategic</h3>
            <p><strong>Detailed Explanation:</strong> Students approach learning with distinct cognitive orientations. <strong>Surface learning</strong> treats course content as isolated facts to be memorized for reproduction, leading to high anxiety and rapid forgetting. <strong>Deep learning</strong> seeks underlying meaning, actively questioning conclusions, relating new concepts to previous experience, and searching for underlying principles. <strong>Strategic learning</strong> focuses on organizing study time and methods specifically to achieve the highest possible grades.</p>
            <p><strong>Real-World Example:</strong> A surface learner memorizes the definition of Photosynthesis word-for-word to pass a quiz. A deep learner asks <em>why</em> plants require specific wavelengths of light, relates light energy to cellular currency, and explains how energy flows through the ecosystem.</p>

            <h3>Sub-Module 2.2: Locus of Control — Creator vs. Victim Language</h3>
            <p><strong>Detailed Explanation:</strong> <strong>Locus of Control</strong> reflects the degree to which learners believe they control their academic outcomes. <strong>Victims</strong> possess an External Locus of Control, blaming external factors ("The lecturer expects too much") and feeling helpless. <strong>Creators</strong> possess an Internal Locus of Control, using proactive language ("This module is demanding, so I will dedicate more time and seek help") to take responsibility for their progress.</p>
            <p><strong>Real-World Example:</strong> When receiving a low test score, a Victim says, "The test was unfair and the teacher hates me." A Creator says, "My study strategy was passive; I will switch to closed-book retrieval practice and consult a tutor."</p>

            <h3>Sub-Module 2.3: Multiple Intelligences & Personal Learning Audits</h3>
            <p><strong>Detailed Explanation:</strong> Intelligence is not a single static number; learners possess distinct intelligence profiles across 8 domains: Linguistic, Logical/Mathematical, Spatial/Visual, Bodily/Kinesthetic, Musical, Interpersonal, Intrapersonal, and Naturalist. Conducting self-audits on concentration, procrastination habits, and learning preferences allows students to tailor study strategies to their specific strengths.</p>
            <p><strong>Real-World Example:</strong> A student with high Bodily/Kinesthetic intelligence learns history better by pacing while reciting notes, whereas a Spatial/Visual learner builds detailed mind maps and color-coded diagrams.</p>

            <h3>Sub-Module 2.4: The Johari Window — Self-Awareness through Feedback</h3>
            <p><strong>Detailed Explanation:</strong> The <strong>Johari Window</strong> is a cognitive framework used to increase self-understanding across four quadrants: <em>Arena</em> (known to self and others), <em>Blind Spot</em> (known to others, unknown to self), <em>Hidden Area</em> (known to self, hidden from others), and <em>Unknown Area</em>. Seeking feedback from peers and instructors expands the Arena and shrinks the Blind Spot, exposing unexamined study flaws.</p>
            <p><strong>Real-World Example:</strong> A student may believe their summary notes are thorough, but peer feedback reveals they missed core concepts. This external feedback illuminates a blind spot, allowing the student to adjust.</p>

            <h3>Sub-Module 2.5: The 4 Study Environment Domains</h3>
            <p><strong>Detailed Explanation:</strong> Learning environment design spans four distinct domains: 1) <em>Human Environment:</em> Support from family and study groups. 2) <em>Non-Human Environment:</em> Physical study space, lighting, and noise control. 3) <em>Spiritual Environment:</em> Core values and connection to broader life goals. 4) <em>Internal Environment:</em> Self-belief, emotional regulation, and stress management.</p>
            <p><strong>Real-World Example:</strong> A student struggling with noise at home negotiates quiet study hours with their family (Human Domain) and arranges a dedicated, well-lit corner desk (Non-Human Domain).</p>
        """,
        "quiz": [
            {"q": "A student reads a biology chapter by highlighting every third sentence and memorizing definitions word-for-word without asking how systems interact. Which approach is this?", "options": ["Deep Learning", "Strategic Learning", "Surface Learning", "Metacognitive Mastery"], "correct": 2},
            {"q": "Why does multitasking significantly impair learning efficiency?", "options": ["Messages permanently erase long-term memory.", "Working memory has only ~4 slots; multitasking splits these, reducing chunking power.", "It causes the insular cortex to shut down.", "Working memory requires 10 slots for text messages."], "correct": 1},
            {"q": "A learner who believes their exam failure was entirely caused by 'unlucky questions' exhibits which orientation?", "options": ["Strong Internal Locus of Control", "Deep Learning Orientation", "External Locus of Control", "High Self-Efficacy"], "correct": 2},
            {"q": "According to the Johari Window, how can a learner discover hidden study flaws ('blind spots')?", "options": ["Studying in total isolation.", "Actively soliciting feedback and discussing habits with peers.", "Memorizing more definitions.", "Rereading notes three times."], "correct": 1},
            {"q": "Which of the following is part of the 'Non-Human' study environment domain?", "options": ["Family support", "Physical study space, lighting, and noise control", "Core values and life goals", "Self-belief and emotional regulation"], "correct": 1}
        ]
    },
    {
        "code": "L2L-M3", "title": "Module 3: Learn Better", "icon": "📚",
        "content_html": """
            <h3>Sub-Module 3.1: Active Recall vs. The Fluency Illusion</h3>
            <p><strong>Detailed Explanation:</strong> Passive study methods like highlighting or re-reading text create a false <strong>Fluency Illusion</strong>—the material looks familiar, so the brain assumes it is mastered. True mastery requires <strong>Active Recall</strong> (retrieval practice): closing the book and retrieving information from memory. Retrieval practice fires synaptic pathways, strengthening neural connections and clarifying conceptual boundaries.</p>
            <p><strong>Real-World Example:</strong> In research published in <em>Science</em>, students who spent 1 hour testing themselves using closed-book recall retained significantly more knowledge weeks later than those who spent the same time re-reading or creating concept maps.</p>

            <h3>Sub-Module 3.2: Spaced Repetition — Beating the Ebbinghaus Forgetting Curve</h3>
            <p><strong>Detailed Explanation:</strong> According to Hermann Ebbinghaus's research, unreinforced memory decays exponentially, losing over 50% of new information within 24 hours. <strong>Spaced repetition</strong> involves revisiting material at expanding intervals (e.g., 1 day, 1 week, 1 month). Each retrieval session flattens the decay curve, deepening the neural groove and converting volatile short-term memory into durable long-term storage.</p>
            <p><strong>Real-World Example:</strong> Reviewing notes for 15 minutes 24 hours after a lecture, 10 minutes a week later, and 5 minutes a month later requires far less total time than a 5-hour cramming session, while achieving near-permanent retention.</p>

            <h3>Sub-Module 3.3: Interleaving — Building Cognitive Agility</h3>
            <p><strong>Detailed Explanation:</strong> Instead of "blocked practice" (studying topic A repeatedly, then B, then C), <strong>interleaving</strong> alternates between different topics or problem types within a single session (A-B-C-A-B-C). While interleaving feels harder and more confusing initially, it trains the brain to recognize underlying structural patterns and select the correct solution strategy.</p>
            <p><strong>Real-World Example:</strong> When practicing mathematics, solving 10 calculus integration problems followed by 10 differentiation problems leads to rote mechanical repetition. Interleaving integration, differentiation, and algebraic problems forces the brain to identify <em>which</em> formula applies to each problem.</p>

            <h3>Sub-Module 3.4: Elaboration & Chunking — Connecting New Ideas to Schemas</h3>
            <p><strong>Detailed Explanation:</strong> <strong>Elaboration</strong> is the process of asking <em>Why</em> and using the 5 W's and 1 H to connect new information to existing mental schemas. <strong>Chunking</strong> compresses complex networks of details into unified mental ribbons, allowing working memory to process high-level concepts effortlessly.</p>
            <p><strong>Real-World Example:</strong> Instead of memorizing isolated historical dates, an elaborative learner asks <em>why</em> economic conditions led to a specific policy, linking political, economic, and social factors into a cohesive historical chunk.</p>

            <h3>Sub-Module 3.5: Dual Coding & Concrete Examples</h3>
            <p><strong>Detailed Explanation:</strong> <strong>Dual Coding</strong> combines verbal/textual information with visual representations (diagrams, doodles, mind maps). Processing information through both visual and auditory neural pathways creates dual retrieval hooks in memory. Translating abstract concepts into <strong>concrete real-world examples</strong> or analogies anchors theoretical ideas in everyday experience.</p>
            <p><strong>Real-World Example:</strong> A student learning computer programming draws a physical warehouse with labeled storage bins to visualize array indexing, combining visual imagery with technical code syntax.</p>
        """,
        "quiz": [
            {"q": "Which study technique yields the highest long-term exam retention?", "options": ["Rereading chapters three times.", "Highlighting key phrases.", "Retrieval practice (Active Recall) through closed-book self-testing.", "Drawing concept maps while looking at the book."], "correct": 2},
            {"q": "Why do students incorrectly believe rereading is effective?", "options": ["It activates BDNF in working memory.", "It creates an 'illusion of competence'—visual familiarity is mistaken for neural storage.", "It automatically engages Diffuse Mode.", "It builds thick links without sleep."], "correct": 1},
            {"q": "How does Interleaving improve math performance compared to Blocking?", "options": ["It reduces study time to 2 minutes.", "It trains the brain to discriminate between problem structures and select the correct strategy.", "It eliminates the need for working memory.", "It allows avoiding difficult topics."], "correct": 1},
            {"q": "What is the baseline recommended spacing schedule for reviewing complex concepts?", "options": ["Every 30 mins for 12 hours before the test.", "1 day after learning, 1 week later, and 1 month later.", "Once every 6 months.", "Only during sleep via audio."], "correct": 1},
            {"q": "Which activity represents Higher-Order Learning (Elaboration/Chunking)?", "options": ["Reciting a definition word-for-word.", "Creating a relatable analogy that explains an abstract process.", "Matching terms to definitions.", "Highlighting dates in history."], "correct": 1}
        ]
    },
    {
        "code": "L2L-M4", "title": "Module 4: Plan Your Learning", "icon": "📅",
        "content_html": """
            <h3>Sub-Module 4.1: The 60/30/10 Rule (EFT Process)</h3>
            <p><strong>Detailed Explanation:</strong> Effective study planning follows the <strong>EFT Process</strong>: <strong>60% Exploration (Planning):</strong> Skimming, framing questions, mapping structures, and setting goals. <strong>30% Fixation (Doing):</strong> Active note-making, problem-solving, and executing study tasks. <strong>10% Testing (Checking):</strong> Closed-book self-quizzing and evaluating knowledge gaps.</p>
            <p><strong>Real-World Example:</strong> Out of a 10-hour weekly study budget for a module, 6 hours are spent mapping content and previewing chapters, 3 hours performing active summarization, and 1 hour taking closed-book practice tests.</p>

            <h3>Sub-Module 4.2: Eisenhower Matrix — Protecting Quadrant 2</h3>
            <p><strong>Detailed Explanation:</strong> Tasks are categorized across four quadrants based on Urgency and Importance: <em>Q1 (Urgent & Important):</em> Crises and upcoming exam deadlines. <em>Q2 (Not Urgent but Important):</em> Strategic study planning, spaced review, and health maintenance. <em>Q3 (Urgent & Not Important):</em> Interruptions and phone notifications. <em>Q4 (Not Urgent & Not Important):</em> Mindless social media scrolling.</p>
            <p><strong>Real-World Example:</strong> Proactive students protect Q2 time by scheduling spaced revision weeks before exams, preventing Q2 tasks from exploding into Q1 crises.</p>

            <h3>Sub-Module 4.3: SMART Goal Setting & Regression Analysis</h3>
            <p><strong>Detailed Explanation:</strong> Goals must be <strong>SMART</strong>: <strong>S</strong>pecific, <strong>M</strong>easurable, <strong>A</strong>chievable, <strong>R</strong>easonable/Relevant, and <strong>T</strong>ime-bound. <strong>Regression analysis</strong> (working backward from the target completion date) breaks major qualification milestones into manageable weekly study units.</p>
            <p><strong>Real-World Example:</strong> Instead of a vague goal ("I want to do well"), a SMART goal specifies: "I will achieve a 70% average in Psychology by studying 8 hours per week and completing 2 practice essays by October 15th."</p>

            <h3>Sub-Module 4.4: Study Time Allocation & Master Scheduling</h3>
            <p><strong>Detailed Explanation:</strong> Full-time students require roughly 40 hours per week across 5 modules (8 hours/module/week), while part-time working adult learners must schedule up to 26 hours per week (2 hours/weeknight plus weekend sessions). Creating a master weekly schedule prevents time leaks.</p>
            <p><strong>Real-World Example:</strong> An adult student working 8:00–17:00 blocks 19:00–21:00 on weeknights and 08:00–14:00 on Saturdays, locking in 16 structured study hours without burning out.</p>

            <h3>Sub-Module 4.5: The Household & Family Negotiation Framework</h3>
            <p><strong>Detailed Explanation:</strong> Distance learners and school learners in busy households must proactively negotiate support. This involves communicating study goals to family members, explaining how academic success benefits the household, and negotiating uninterrupted study windows in exchange for shared responsibilities.</p>
            <p><strong>Real-World Example:</strong> A student signs a formal agreement with family members: "If you grant me 2 quiet hours between 18:00 and 20:00 every weeknight, I will handle all dinner dishwashing afterward."</p>
        """,
        "quiz": [
            {"q": "According to the 60/30/10 EFT Rule, how should a student allocate 10 hours of weekly study?", "options": ["1 hr planning, 8 hrs reading, 1 hr resting.", "6 hrs Exploration, 3 hrs Fixation, 1 hr Testing.", "10 hrs highlighting.", "9 hrs solving past papers without pre-reading."], "correct": 1},
            {"q": "In the Eisenhower Matrix, which quadrant should learners aggressively protect to prevent burnout?", "options": ["Quadrant 1 (Urgent & Important)", "Quadrant 2 (Not Urgent but Important)", "Quadrant 3 (Urgent & Not Important)", "Quadrant 4 (Not Urgent & Not Important)"], "correct": 1},
            {"q": "How should a full-time employed adult structure their weekly schedule to reach ~26 hours?", "options": ["26 continuous hours on Sunday.", "2 hours M-F (before/after work) and 6-8 hours Sat-Sun.", "10 mins during lunch only.", "Wait until two weeks before exams."], "correct": 1},
            {"q": "What is the main objective of the Family Negotiation Framework?", "options": ["Force family to take your exams.", "Secure dedicated quiet time and chore relief by communicating mutual benefits.", "Demand 24 hours of silence.", "Eliminate the need for a planner."], "correct": 1},
            {"q": "Which task falls into Quadrant 4 and should be strictly limited?", "options": ["Creating a weekly schedule.", "Mindlessly scrolling social media during study time.", "Attending a required class.", "Self-testing flashcards."], "correct": 1}
        ]
    },
    {
        "code": "L2L-M5", "title": "Module 5: Beat Procrastination", "icon": "⏱️",
        "content_html": """
            <h3>Sub-Module 5.1: The Neurobiology of Avoidance — Insular Cortex Pain</h3>
            <p><strong>Detailed Explanation:</strong> Procrastination is an emotional coping mechanism, not laziness or poor time management. When contemplating an uncomfortable, boring, or difficult task, the brain activates the <strong>insular cortex</strong>—the exact center that processes physical pain. To stop the pain, the brain redirects attention to a pleasant activity (social media, gaming), yielding immediate emotional relief.</p>
            <p><strong>Real-World Example:</strong> Looking at a dense textbook chapter triggers a spike in the insular cortex. The student picks up their phone, the pain centers deactivate, and the brain receives a dopamine hit, reinforcing the procrastination loop.</p>

            <h3>Sub-Module 5.2: Internal vs. External Causes of Procrastination</h3>
            <p><strong>Detailed Explanation:</strong> Procrastination stems from specific drivers. <em>Internal:</em> Fear of failure, perfectionism, task aversion, low self-efficacy, and self-handicapping. <em>External:</em> Poor study environments, ambiguous assignment instructions, or unrefined deadlines.</p>
            <p><strong>Real-World Example:</strong> A perfectionist student delays writing an essay draft because they fear their initial writing will be flawed. A self-handicapping student delays studying so that if they fail, they can blame lack of time rather than their intelligence.</p>

            <h3>Sub-Module 5.3: The 5-Minute Start Rule & The Zeigarnik Effect</h3>
            <p><strong>Detailed Explanation:</strong> Starting a task is the hardest part; once a task is underway, insular cortex pain deactivates within 20 minutes. The <strong>5-Minute Start Rule</strong> involves committing to work on a task for just 5 minutes. This leverages the <strong>Zeigarnik Effect</strong>—the brain's psychological drive to complete tasks it has already initiated.</p>
            <p><strong>Real-World Example:</strong> A student feeling overwhelmed by a 10-page paper commits to opening a blank document and writing for just 5 minutes. In 80% of cases, overcoming the starting friction carries them into a full 25-minute focus session.</p>

            <h3>Sub-Module 5.4: Process Focus & The Pomodoro Technique</h3>
            <p><strong>Detailed Explanation:</strong> Productive focus requires shifting from <em>outcome focus</em> ("I must finish this entire module tonight") to <em>process focus</em> ("I will execute 25 minutes of focused effort"). The <strong>Pomodoro Technique</strong> uses a 25-minute focus period followed by a 5-minute diffuse reward break.</p>
            <p><strong>Real-World Example:</strong> During a 25-minute Pomodoro, phone notifications are disabled. When thoughts of checking social media arise, the student lets them pass, focusing entirely on the process until the timer rings.</p>

            <h3>Sub-Module 5.5: The STAR Method & Reframing Mistakes</h3>
            <p><strong>Detailed Explanation:</strong> The <strong>STAR Method</strong> (<strong>S</strong>top, <strong>T</strong>hink, <strong>A</strong>ct, <strong>R</strong>eview) provides a cognitive pause before reacting impulsively to academic stress. Mistakes are reframed not as personal flaws, but as essential diagnostic feedback needed for neural development.</p>
            <p><strong>Real-World Example:</strong> When encountering a difficult math problem, a student applies STAR: <strong>Stop</strong> the impulse to close the book, <strong>Think</strong> about alternative approaches, <strong>Act</strong> by trying a practice step, and <strong>Review</strong> the outcome.</p>
        """,
        "quiz": [
            {"q": "What is the primary psychological principle behind the 5-Minute Start Rule?", "options": ["It forces long-term memory to double capacity.", "Overcoming starting friction triggers the Zeigarnik Effect (drive to complete initiated tasks).", "It eliminates the need for sleep.", "It permanently cures perfectionism."], "correct": 1},
            {"q": "When executing a 25-minute Pomodoro, what should the learner explicitly focus on?", "options": ["Finishing the entire assignment.", "The passage of time (working for 25 mins), rather than task completion.", "Checking phone every 5 mins.", "Rereading notes as fast as possible."], "correct": 1},
            {"q": "Why are app blockers effective short-term anti-procrastination tools?", "options": ["They rewire gray matter automatically.", "They introduce high friction to distractions, making access require more effort than staying focused.", "They eliminate the need for internal locus.", "They force continuous Diffuse Mode."], "correct": 1},
            {"q": "What does the 'S' stand for in the STAR method?", "options": ["Study", "Stop", "Summarize", "Speed-read"], "correct": 1},
            {"q": "A student procrastinates writing a paper because they fear it won't be flawless. What is driving this?", "options": ["External Locus of Control", "Perfectionism & Fear of Failure", "Lack of BDNF", "Short Sleep Gene"], "correct": 1}
        ]
    },
    {
        "code": "L2L-M6", "title": "Module 6: Remember More", "icon": "🏰",
        "content_html": """
            <h3>Sub-Module 6.1: The Leitner 5-Box Flashcard System</h3>
            <p><strong>Detailed Explanation:</strong> Sebastian Leitner's system organizes flashcards into 5 physical or digital boxes based on mastery: <em>Box 1:</em> Reviewed daily. <em>Box 2:</em> Reviewed every 3 days. <em>Box 3:</em> Reviewed weekly. <em>Box 4:</em> Reviewed bi-weekly. <em>Box 5:</em> Reviewed monthly. Correctly recalled cards move up a box; incorrect cards are demoted back to Box 1, ensuring maximum effort is spent on weak material.</p>
            <p><strong>Real-World Example:</strong> A medical student reviewing 200 anatomy flashcards moves mastered cards to Box 4 (reviewed every 2 weeks) while keeping difficult nerve pathways in Box 1 for daily review.</p>

            <h3>Sub-Module 6.2: The Method of Loci & Memory Palaces</h3>
            <p><strong>Detailed Explanation:</strong> Dating back to ancient Greece, the <strong>Method of Loci</strong> anchors abstract information to familiar physical locations along a mental journey (e.g., rooms in your house). Spatial memory in the hippocampus is biologically ancient and exceptionally strong.</p>
            <p><strong>Real-World Example:</strong> To remember a list of historical figures, a student visualizes the first figure standing on their front doormat, the second sitting on their kitchen counter, and the third in their shower.</p>

            <h3>Sub-Module 6.3: Peg Systems, Rhyme Keys, and Acronyms</h3>
            <p><strong>Detailed Explanation:</strong> <strong>Peg Systems</strong> link numbers to fixed rhyming "hangers" (1 = Sun, 2 = Shoe, 3 = Tree). <strong>Acronyms</strong> take the first letter of each word to create a memorable new word (e.g., BODMAS for math operations, PEN for Proton, Electron, Neutron).</p>
            <p><strong>Real-World Example:</strong> To remember the points of the compass in order (North, East, West, South), learners use the acronym NEWS.</p>

            <h3>Sub-Module 6.4: Chaining, Linking, & Mnemonic Exaggeration</h3>
            <p><strong>Detailed Explanation:</strong> <strong>Chaining</strong> links items in a list into an imaginative story where each element triggers the next. Memory retention increases dramatically when images incorporate <strong>synesthesia</strong> (blending senses), <strong>movement</strong>, and <strong>exaggeration</strong>.</p>
            <p><strong>Real-World Example:</strong> To remember "Fish, Coat, Table", visualize a giant glowing salmon wearing a bright red winter coat dancing on top of a dining table.</p>

            <h3>Sub-Module 6.5: Spaced Revision Calendars & Long-Term Memory Maintenance</h3>
            <p><strong>Detailed Explanation:</strong> Maintenance of long-term memory requires structured review schedules before decay occurs. Tracking revision dates on a monthly calendar ensures material is revisited before the "metabolic vampires" sweep weak neural patterns away.</p>
            <p><strong>Real-World Example:</strong> A student logs initial study on Feb 1, plans a 15-minute review on Feb 2, a 10-minute review on Feb 9, and a 5-minute refresh on March 9.</p>
        """,
        "quiz": [
            {"q": "In the Leitner system, what happens to a flashcard in Box 4 if answered incorrectly?", "options": ["Stays in Box 4.", "Moves to Box 5.", "Immediately demoted back to Box 1 for daily review.", "Permanently deleted."], "correct": 2},
            {"q": "Why is the Method of Loci (Memory Palace) so effective?", "options": ["Expands working memory to 50 slots.", "Leverages highly evolved spatial navigation networks in the hippocampus.", "Eliminates the need for sleep.", "Replaces Focused Mode."], "correct": 1},
            {"q": "Which combination of mnemonic attributes produces the highest retention?", "options": ["Small, realistic, monochrome text.", "Exaggerated, moving, multi-sensory, and absurd images.", "Abstract symbols without movement.", "Reread highlighted text."], "correct": 1},
            {"q": "What mindset shift regarding memory language builds cognitive self-efficacy?", "options": ["Saying 'My memory is full.'", "Saying 'I don't recall it right now' instead of 'I forgot.'", "Claiming to have a short sleep gene.", "Assuming intelligence is fixed."], "correct": 1},
            {"q": "When using flashcards for math formulas, what protocol should be followed?", "options": ["Stare at the front and immediately flip.", "Attempt closed-book free recall, then flip to verify.", "Reread 10 times without looking away.", "Highlight the formula."], "correct": 1}
        ]
    },
    {
        "code": "L2L-M7", "title": "Module 7: Prepare for Exams", "icon": "📝",
        "content_html": """
            <h3>Sub-Module 7.1: The Shewhart Cycle (PDSA)</h3>
            <p><strong>Detailed Explanation:</strong> Exam preparation utilizes the continuous improvement <strong>Shewhart Cycle</strong>: <strong>Plan:</strong> Schedule syllabus units across available weeks, reserving the final 2 weeks for testing. <strong>Do:</strong> Execute study plans using active note-taking. <strong>Study:</strong> Analyze self-test performance and identify weak areas. <strong>Act:</strong> Adjust study schedules to target knowledge gaps.</p>
            <p><strong>Real-World Example:</strong> A student allocates 4 weeks to cover 8 study units, tests themselves on week 3, discovers low scores in unit 4, and adjusts their week 4 schedule to re-study unit 4.</p>

            <h3>Sub-Module 7.2: Active Reading Systems — SQ3R & Surveying</h3>
            <p><strong>Detailed Explanation:</strong> Passive reading is ineffective. The <strong>SQ3R</strong> system ensures active engagement: 1) <strong>Survey:</strong> Skim headings, titles, and diagrams to get the big picture. 2) <strong>Question:</strong> Turn headings into test questions. 3) <strong>Read:</strong> Read actively to answer those questions. 4) <strong>Recite:</strong> Rephrase main ideas out loud in your own words. 5) <strong>Review:</strong> Perform periodic closed-book review.</p>
            <p><strong>Real-World Example:</strong> Before reading a chapter on Cell Biology, a student turns the heading "Mitochondria Function" into the question "How do mitochondria produce ATP?", creating a clear objective for reading.</p>

            <h3>Sub-Module 7.3: High-Impact Note-Taking — The Cornell Method & The 5 R's</h3>
            <p><strong>Detailed Explanation:</strong> Note-taking should follow Professor Walter Pauk's <strong>5 R's</strong>: 1) <em>Record:</em> Capture key concepts during lectures. 2) <em>Reduce:</em> Summarize notes in a left-hand cue column. 3) <em>Recite:</em> Cover notes and recite concepts from cues in your own words. 4) <em>Reflect:</em> Think deeply about practical applications. 5) <em>Review:</em> Perform weekly active reviews.</p>
            <p><strong>Real-World Example:</strong> The Cornell Note format divides the page into Cues (left), Class Notes (right), and Summary (bottom), forcing active reduction and reflection.</p>

            <h3>Sub-Module 7.4: Post-Exam Diagnostic Error Triage</h3>
            <p><strong>Detailed Explanation:</strong> After receiving test results, errors must be triaged into two categories: <em>Knowledge Gaps:</em> Concepts not fully understood or remembered. <em>Strategic/Testing Errors:</em> Misreading instructions, poor time management, or exam anxiety.</p>
            <p><strong>Real-World Example:</strong> A student realizes they lost 10 marks not because they didn't know the material, but because they spent too long on essay question 1 and ran out of time for question 2.</p>

            <h3>Sub-Module 7.5: Exam-Day Mindset & Managing Testing Anxiety</h3>
            <p><strong>Detailed Explanation:</strong> Exam anxiety is managed through physical regulation, positive self-talk ("I CAN!"), and proper physiological preparation (sleep, hydration, and steady nutrition).</p>
            <p><strong>Real-World Example:</strong> Arriving at the exam room 15 minutes early, taking deep diaphragmatic breaths to lower heart rate, and reading all instructions carefully before writing.</p>
        """,
        "quiz": [
            {"q": "In the Shewhart Cycle (PDSA), what occurs during the 'STUDY' phase?", "options": ["Highlighting for 5 hours.", "Evaluating mock test results, conducting error analysis, and reflecting.", "Setting initial due dates.", "Sleeping 12 hours."], "correct": 1},
            {"q": "Which note-taking layout features a Cue column, Main Notes, and a Summary Block?", "options": ["Mind Mapping", "The Cornell Method", "Linear Outline", "Flowchart"], "correct": 1},
            {"q": "What is the second step in the SQ3R reading method?", "options": ["Survey", "Question (turning headings into self-test questions)", "Read", "Recite"], "correct": 1},
            {"q": "A student misses a question because they failed to notice the word 'EXCEPT'. How should this be triaged?", "options": ["As a fundamental Knowledge Gap.", "As a Strategic/Testing Error caused by rushing past signal words.", "As proof of External Locus.", "As a biological flaw."], "correct": 1},
            {"q": "When planning a semester-long schedule, how much time should be reserved at the end for final cumulative testing?", "options": ["0 days.", "Exactly 2 weeks.", "6 months.", "1 hour on exam morning."], "correct": 1}
        ]
    },
    {
        "code": "L2L-M8", "title": "Module 8: Become Your Own Teacher", "icon": "🎓",
        "content_html": """
            <h3>Sub-Module 8.1: The Feynman Technique — Teaching to a 10-Year-Old</h3>
            <p><strong>Detailed Explanation:</strong> Named after physicist Richard Feynman, this metacognitive technique requires explaining a complex topic in simple language that a 10-year-old child could understand. Simplifying concepts strips away unparsed technical jargon and instantly exposes hidden gaps in understanding.</p>
            <p><strong>Real-World Example:</strong> When explaining Photosynthesis, instead of saying "Light-dependent reactions occur in the thylakoid membrane," explain: "The plant uses leaf solar panels to catch sunlight and split water into oxygen and plant food."</p>

            <h3>Sub-Module 8.2: Metacognitive Teach-Back & Gap Analysis</h3>
            <p><strong>Detailed Explanation:</strong> Metacognition is "thinking about thinking". The teach-back workflow requires learners to articulate a concept from memory, compare their explanation against authoritative source material, identify missing elements, and immediately relearn the missing gaps.</p>
            <p><strong>Real-World Example:</strong> After explaining a Python programming loop out loud, the student checks the textbook, realizes they forgot to mention termination conditions, and immediately re-studies that specific gap.</p>

            <h3>Sub-Module 8.3: Bloom's Cognitive Taxonomy — Moving Up the Staircase</h3>
            <p><strong>Detailed Explanation:</strong> Learning progresses across 6 hierarchical cognitive levels: 1) <em>Knowledge:</em> Remembering and recalling facts. 2) <em>Comprehension:</em> Translating and interpreting in own words. 3) <em>Application:</em> Applying knowledge to new contexts. 4) <em>Analysis:</em> Breaking concepts into underlying parts. 5) <em>Synthesis:</em> Combining ideas into new creative structures. 6) <em>Evaluation:</em> Critically judging arguments and evidence.</p>
            <p><strong>Real-World Example:</strong> True mastery requires moving beyond level 1 (reciting definitions) to level 3 (applying concepts to novel case studies) and level 6 (evaluating competing theories).</p>

            <h3>Sub-Module 8.4: Krathwohl's Affective Taxonomy & Value Internalisation</h3>
            <p><strong>Detailed Explanation:</strong> Learning also involves emotional and attitudinal growth across Krathwohl's affective domain: <em>Receiving</em> (being open to new ideas), <em>Responding</em> (actively participating), <em>Valuing</em> (attaching worth to learning), <em>Organization</em> (integrating values), and <em>Characterization</em> (internalizing habits into lifelong identity).</p>
            <p><strong>Real-World Example:</strong> A student transitions from studying solely because parents demand it (external motivation) to valuing personal intellectual growth as a core identity trait.</p>

            <h3>Sub-Module 8.5: Thorndike's Laws of Learning & Self-Assessment Systems</h3>
            <p><strong>Detailed Explanation:</strong> Edward Thorndike's foundational laws govern skill acquisition: <em>Law of Exercise:</em> Connections are strengthened with repeated practice ("use it or lose it"). <em>Law of Effect:</em> Learning accompanied by satisfying feelings or rewards is locked in, while negative experiences induce avoidance. <em>Law of Readiness:</em> Learning is most efficient when the learner is physically, emotionally, and mentally prepared.</p>
            <p><strong>Real-World Example:</strong> Building small rewards into every successful study session reinforces the Law of Effect, training the brain to associate focused learning with positive outcomes.</p>
        """,
        "quiz": [
            {"q": "What is the primary objective of Step 2 in the Feynman Technique (explaining to a 10-year-old)?", "options": ["To memorize definitions faster.", "To instantly expose hidden gaps where you rely on unparsed technical jargon.", "To shorten sleep requirements.", "To eliminate study groups."], "correct": 1},
            {"q": "Which level of Bloom's Taxonomy is engaged when evaluating the logical validity of opposing arguments?", "options": ["Knowledge", "Comprehension", "Evaluation", "Receiving"], "correct": 2},
            {"q": "According to Thorndike's Law of Intensity, how do students learn most effectively?", "options": ["By passively listening while multitasking.", "By engaging in vivid, active, real-world simulations.", "By reading a page five times in silence.", "By memorizing Box 1 flashcards."], "correct": 1},
            {"q": "Why are peer study groups powerful for metacognitive mastery?", "options": ["They allow one student to do all the work.", "Explaining concepts forces active thinking and provides immediate feedback on gaps.", "They eliminate individual study hours.", "They replace the 60/30/10 rule."], "correct": 1},
            {"q": "What cognitive state is achieved when explaining Photosynthesis using a 'kitchen baking' analogy from memory?", "options": ["Surface Rote Memorization", "Metacognitive Synthesis and Deep Conceptual Mastery", "Fluency Illusion", "External Locus of Control"], "correct": 1}
        ]
    }
]