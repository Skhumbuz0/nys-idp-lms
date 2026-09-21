# employment_data.py

EMPLOYMENT_MODULES = [
    {
        "code": "EMP-M1", "title": "Module 1: Understanding Employability", "icon": "💼",
        "submodules": [
            {"number": "1.1", "title": "What is Employability?", "content_html": """
                <h3>What is Employability?</h3>
                <p>Employability is your ability to prepare for, find, enter, and continue developing within work. It is <strong>not</strong> only about having a qualification.</p>
                <p>Employers consider your: qualifications, technical skills, communication, teamwork, problem-solving, reliability, digital skills, work/volunteer experience, leadership, and ability to learn.</p>
                <p><strong>Key Lesson:</strong> Your qualification tells an employer what you studied. Your skills tell them what you can do. Your experience shows them what you have already done. Your application must connect all three to the employer's needs.</p>
            """},
            {"number": "1.2", "title": "Your Employment Value Proposition", "content_html": """
                <h3>Your Employment Value Proposition</h3>
                <p>Instead of saying "I have no experience," ask: "Where have I demonstrated skills that an employer may value?"</p>
                <p>Experience can come from: volunteering, community work, school activities, youth organisations, entrepreneurship, projects, internships, learnerships, temporary work, part-time work, family business activities, online projects, and training.</p>
                <div class="bg-blue-50 p-4 rounded-lg border-l-4 border-blue-500 mt-4">
                    <h4 class="font-bold text-blue-800">Activity: My Employment Value Statement</h4>
                    <p class="text-sm mt-2">Complete this sentence: <em>"I can contribute to an organisation by using my skills in __________, __________ and __________. I have developed these skills through __________, __________ and __________."</em></p>
                </div>
            """}
        ],
        "quiz": [
            {"q": "What does employability include?", "options": ["Only having a university qualification", "A combination of skills, knowledge, experience and work-related abilities", "Only having previous employment", "Having a professional social-media account"], "correct": 1},
            {"q": "Why should a participant identify experience gained through volunteering?", "options": ["Volunteer experience can demonstrate useful skills and responsibility", "Volunteer work automatically guarantees employment", "Volunteer work replaces qualifications", "Employers are required to hire volunteers"], "correct": 0},
            {"q": "What should a job seeker do before beginning a focused job search?", "options": ["Send the same CV everywhere", "Understand their skills and what type of work they want", "Apply only to government jobs", "Wait for an employer to contact them"], "correct": 1}
        ]
    },
    {
        "code": "EMP-M2", "title": "Module 2: Discover Your Skills & Experience", "icon": "🔍",
        "submodules": [
            {"number": "2.1", "title": "The Experience Inventory", "content_html": """
                <h3>You Have More Experience Than You Think</h3>
                <p>Many young people make the mistake of believing: <em>"I have never had a job, therefore I have no experience."</em> This is not necessarily true.</p>
                <p>Experience can come from formal employment, learning (internships, learnerships, short courses), community (volunteering, youth organisations), entrepreneurship, and projects.</p>
                <div class="bg-green-50 p-4 rounded-lg border-l-4 border-green-500 mt-4">
                    <h4 class="font-bold text-green-800">Activity: Experience Bank</h4>
                    <p class="text-sm mt-2">List 3 experiences. For each, note: What you did, the skill demonstrated, and the result. (e.g., Youth Centre Volunteer → Assisted with registration → Organisation → Programme delivered).</p>
                </div>
            """},
            {"number": "2.2", "title": "Skills Inventory & Evidence Test", "content_html": """
                <h3>Skills Inventory & Evidence Test</h3>
                <p>Divide your skills into:</p>
                <ul>
                    <li><strong>Technical/Digital Skills:</strong> Microsoft Excel, Data capturing, Social media management, Basic bookkeeping.</li>
                    <li><strong>Transferable Skills:</strong> Communication, Teamwork, Problem solving, Time management, Customer service.</li>
                </ul>
                <p><strong>Crucial Principle:</strong> Never claim a skill you cannot demonstrate. For every skill, ask: "Where did I demonstrate this skill?"</p>
            """}
        ],
        "quiz": [
            {"q": "Which can be included as relevant experience?", "options": ["Only permanent employment", "Only university employment", "Volunteer work, projects, internships and other relevant activities", "Only jobs where the participant received a salary"], "correct": 2},
            {"q": "Why should participants connect a skill to evidence?", "options": ["It helps demonstrate that the participant genuinely possesses the skill", "It makes the CV longer", "It guarantees an interview", "It replaces qualifications"], "correct": 0},
            {"q": "Which is an example of a technical skill?", "options": ["Microsoft Excel", "Being friendly", "Motivation", "Positive attitude"], "correct": 0}
        ]
    },
    {
        "code": "EMP-M3", "title": "Module 3: Understanding Job Advertisements", "icon": "📋",
        "submodules": [
            {"number": "3.1", "title": "A Job Advertisement is an Instruction Document", "content_html": """
                <h3>A Job Advertisement is an Instruction Document</h3>
                <p>A job advert tells you what an employer is looking for. Before applying, identify: job title, employer, location, closing date, minimum qualifications, required experience, required skills, duties, advantageous requirements, application method, reference number, and documents required.</p>
                <p><strong>Mandatory vs. Advantageous:</strong> Mandatory means you <em>must</em> have it. Advantageous strengthens your application but isn't strictly required.</p>
            """},
            {"number": "3.2", "title": "Job Advert Decoder Activity", "content_html": """
                <h3>Job Advert Decoder</h3>
                <p>Teach participants to distinguish between mandatory requirements, advantageous requirements, skills they already possess, and skills they can develop.</p>
                <div class="bg-yellow-50 p-4 rounded-lg border-l-4 border-yellow-500 mt-4">
                    <h4 class="font-bold text-yellow-800">Activity: Requirement Match</h4>
                    <p class="text-sm mt-2">Take a real job advert. Create a table: Requirement | Do I have it? (Yes/No) | Evidence. Finally, ask: "Based on the advertisement, is this an opportunity I should consider applying for?"</p>
                </div>
            """}
        ],
        "quiz": [
            {"q": "What should you do before applying for a job?", "options": ["Read and understand the job advertisement", "Immediately send your CV", "Ignore the closing date", "Remove qualifications that are not requested"], "correct": 0},
            {"q": "Why is the application method important?", "options": ["Employers may specify particular documents, formats or submission methods", "It determines the applicant's salary", "It replaces the CV", "It is only relevant to internships"], "correct": 0},
            {"q": "What is the purpose of matching your skills to job requirements?", "options": ["To identify relevant evidence you can present in your application", "To invent missing qualifications", "To guarantee selection", "To make every application identical"], "correct": 0}
        ]
    }
]