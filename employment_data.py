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
                    <p class="text-sm mt-2">List 3 experiences. For each, note: What you did, the skill demonstrated, and the result. (e.g., Youth Centre Volunteer -> Assisted with registration -> Organisation -> Programme delivered).</p>
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
    },
    {
        "code": "EMP-M4", "title": "Module 4: Build Your Master CV", "icon": "📄",
        "submodules": [
            {"number": "4.1", "title": "The MAYO Master CV Structure", "content_html": """
                <h3>The MAYO Master CV</h3>
                <p>Your Master CV is your complete employment information database. It contains more information than you will necessarily send with every application. You then use it to create targeted CVs.</p>
                <p><strong>Section 1: Personal Info:</strong> Full name, mobile number, professional email (e.g., name.surname@gmail.com), Town/City, Province.</p>
                <p><strong>Section 2: Career/Profile Statement:</strong> 3-5 sentences explaining who you are, relevant skills/experience, and the type of opportunity you seek. Avoid generic phrases like "hardworking person looking for a job."</p>
            """},
            {"number": "4.2", "title": "Education, Skills & Experience", "content_html": """
                <h3>Education, Skills & Experience</h3>
                <p><strong>Education:</strong> Qualification | Institution | Year. Include both accredited and non-accredited training (e.g., MAYO NYS Digital Skills Programme).</p>
                <p><strong>Skills:</strong> Divide into Technical/Digital (e.g., MS Word, Data capturing) and Transferable (e.g., Communication, Teamwork). Never claim a skill you cannot demonstrate.</p>
                <p><strong>Experience:</strong> Use the format: Organisation - Position - Dates. Use bullet points for responsibilities.</p>
            """},
            {"number": "4.3", "title": "Achievements & References", "content_html": """
                <h3>Achievements & References</h3>
                <p><strong>Achievements:</strong> Convert duties into evidence using the formula: <em>Action + Task + Result</em>. (e.g., "Coordinated registration for 50 participants during a youth programme" instead of "Responsible for helping people").</p>
                <p><strong>References:</strong> Maintain a Reference Bank (previous employer, supervisor, lecturer, project leader). Always obtain permission before listing someone.</p>
                <div class="bg-red-50 p-4 rounded-lg border-l-4 border-red-500 mt-4">
                    <h4 class="font-bold text-red-800">CV Quality Check</h4>
                    <p class="text-sm mt-2">Before marking complete: Contact details correct? Email professional? Spelling/grammar checked? No false information? References have permission?</p>
                </div>
            """}
        ],
        "quiz": [
            {"q": "What is the purpose of a Master CV?", "options": ["To contain the participant's complete employment information for future tailoring", "To send unchanged to every employer", "To replace a cover letter", "To contain only qualifications"], "correct": 0},
            {"q": "Which information belongs in the education section?", "options": ["Qualifications and relevant educational achievements", "Favourite foods", "Personal opinions", "Passwords"], "correct": 0},
            {"q": "What should a participant do before submitting a CV?", "options": ["Proofread it and check that the information is accurate", "Add qualifications they do not have", "Remove their contact details", "Send it without checking"], "correct": 0}
        ]
    },
    {
        "code": "EMP-M5", "title": "Module 5: Tailor Your CV", "icon": "🎯",
        "submodules": [
            {"number": "5.1", "title": "One Master CV, Many Targeted CVs", "content_html": """
                <h3>One Master CV, Many Targeted CVs</h3>
                <p>Your Master CV is your information bank. Your targeted CV is the version you send to a particular employer. The Department of Employment and Labour specifically recommends changing the CV so relevant skills and experience are emphasised for the particular job.</p>
            """},
            {"number": "5.2", "title": "The 5-Step CV Tailoring Process", "content_html": """
                <h3>The 5-Step CV Tailoring Process</h3>
                <ol class="list-decimal pl-6 space-y-2">
                    <li><strong>Read</strong> the job advertisement carefully.</li>
                    <li><strong>Highlight</strong> important requirements and keywords.</li>
                    <li><strong>Find</strong> matching evidence in your Master CV.</li>
                    <li><strong>Move</strong> the most relevant information into prominent positions (e.g., top of the page).</li>
                    <li><strong>Remove</strong> or reduce information that is not relevant to this specific role.</li>
                </ol>
                <div class="bg-blue-50 p-4 rounded-lg border-l-4 border-blue-500 mt-4">
                    <h4 class="font-bold text-blue-800">Activity: Tailoring Practice</h4>
                    <p class="text-sm mt-2">Take your Master CV. Choose one real vacancy. Create a targeted CV. Then answer: "What did I change and why?"</p>
                </div>
            """}
        ],
        "quiz": [
            {"q": "Should the same CV always be sent to every employer?", "options": ["Yes", "No, it should be adapted to relevant opportunities", "Only when applying online", "Only when applying for internships"], "correct": 1},
            {"q": "What should be emphasised in a targeted CV?", "options": ["Relevant qualifications, skills and experience", "Completely unrelated hobbies", "Personal opinions", "Information that contradicts the job advert"], "correct": 0},
            {"q": "Should a participant claim a skill they do not have because it appears in a job advertisement?", "options": ["Yes", "No", "Only for online applications", "Only if the job is urgent"], "correct": 1}
        ]
    },
    {
        "code": "EMP-M6", "title": "Module 6: Write a Professional Cover Letter", "icon": "✉️",
        "submodules": [
            {"number": "6.1", "title": "What is a Cover Letter?", "content_html": """
                <h3>What is a Cover Letter?</h3>
                <p>A cover letter is a short, one-page document that introduces you to an employer and explains why you are applying and why your relevant qualifications, experience, and abilities make you a suitable candidate.</p>
                <p><strong>Important Lesson:</strong> A cover letter should not simply repeat the CV. It should show knowledge of the organisation and highlight specific relevant skills.</p>
            """},
            {"number": "6.2", "title": "The MAYO 4-Paragraph Cover Letter", "content_html": """
                <h3>The MAYO 4-Paragraph Cover Letter</h3>
                <ul class="list-disc pl-6 space-y-2">
                    <li><strong>Paragraph 1 (Introduction):</strong> State the position, organisation, where you found the vacancy, and reference number.</li>
                    <li><strong>Paragraph 2 (Your Value):</strong> Explain relevant qualification, experience, skills, and a specific achievement.</li>
                    <li><strong>Paragraph 3 (Why This Organisation):</strong> Show that you understand the organisation and why you are interested in this specific opportunity.</li>
                    <li><strong>Paragraph 4 (Close):</strong> State that your CV is attached, express appreciation, and state your willingness to attend an interview.</li>
                </ul>
            """}
        ],
        "quiz": [
            {"q": "What is the purpose of a cover letter?", "options": ["To introduce the applicant and explain relevant suitability for the position", "To replace the CV", "To provide a full autobiography", "To list unrelated hobbies"], "correct": 0},
            {"q": "Should a cover letter be adapted for different jobs?", "options": ["Yes", "No", "Only for government jobs", "Only for internships"], "correct": 0},
            {"q": "What should a cover letter avoid?", "options": ["Relevant skills", "Knowledge of the organisation", "Unsupported claims", "A professional closing"], "correct": 2}
        ]
    },
    {
        "code": "EMP-M7", "title": "Module 7: Build Your Employment Profile", "icon": "🌐",
        "submodules": [
            {"number": "7.1", "title": "Your Digital Employment Presence", "content_html": """
                <h3>Your Digital Employment Presence</h3>
                <p>Your employment profile is another way employers and employment services can understand what you offer. Participants should maintain relevant profiles and ensure that their information is current.</p>
                <p>The Department's <strong>ESSA</strong> system allows work seekers to register, search for opportunities, and capture a CV that can be matched with potential employers. <strong>SAYouth</strong> also stresses keeping employment profiles complete and updated.</p>
            """},
            {"number": "7.2", "title": "Employment Profile Audit Activity", "content_html": """
                <h3>Employment Profile Audit</h3>
                <p>Check your digital footprint. Ensure you have:</p>
                <ul class="list-disc pl-6 space-y-1">
                    <li>Professional email address</li>
                    <li>Correct phone number and location</li>
                    <li>Education and certificates uploaded</li>
                    <li>Skills and experience listed</li>
                    <li>SAYouth and/or ESSA profile updated</li>
                    <li>Professional online presence (e.g., LinkedIn where appropriate)</li>
                </ul>
                <div class="bg-yellow-50 p-4 rounded-lg border-l-4 border-yellow-500 mt-4">
                    <h4 class="font-bold text-yellow-800">Digital Professionalism Activity</h4>
                    <p class="text-sm mt-2">Search your own name online. Record: What public information did I find? Is it professional? Is there anything I should review or remove?</p>
                </div>
            """}
        ],
        "quiz": [
            {"q": "Why should an employment profile be kept updated?", "options": ["Employers and employment services may use profile information when considering opportunities", "It guarantees employment", "It replaces interviews", "It eliminates the need for qualifications"], "correct": 0},
            {"q": "What should a professional email address contain?", "options": ["A professional version of the person's name where possible", "Offensive language", "Random passwords", "False qualifications"], "correct": 0},
            {"q": "What is ESSA?", "options": ["A Department of Employment and Labour employment-services system", "A university degree", "A CV template", "A private bank"], "correct": 0}
        ]
    },
    {
        "code": "EMP-M8", "title": "Module 8: Finding Employment Opportunities", "icon": "🔎",
        "submodules": [
            {"number": "8.1", "title": "Build Multiple Job-Search Channels", "content_html": """
                <h3>Build Multiple Job-Search Channels</h3>
                <p>Do not rely on only one website. Expand your application avenues.</p>
                <p><strong>Online:</strong> SAYouth, ESSA, company career pages, recognised job portals, LinkedIn, recruitment agencies.</p>
                <p><strong>Offline:</strong> Labour Centres, employer open days, recruitment events, networking, community networks, direct employer enquiries.</p>
            """},
            {"number": "8.2", "title": "Target Employer List Activity", "content_html": """
                <h3>Target Employer List</h3>
                <p>Create a list of organisations you would like to work for. For each, note:</p>
                <ul class="list-disc pl-6 space-y-1">
                    <li>Employer Name & Industry</li>
                    <li>Target Role</li>
                    <li>Website/Source</li>
                    <li>Contact Person (if known)</li>
                </ul>
                <div class="bg-green-50 p-4 rounded-lg border-l-4 border-green-500 mt-4">
                    <h4 class="font-bold text-green-800">Opportunity Search Activity</h4>
                    <p class="text-sm mt-2">Find five legitimate opportunities. For each, record: Employer, Position, Location, Closing date, Source, Requirements, and Application method.</p>
                </div>
            """}
        ],
        "quiz": [
            {"q": "Why should job seekers use multiple employment channels?", "options": ["Different employers advertise opportunities through different channels", "It guarantees employment", "It means applications do not need to be tailored", "It eliminates interviews"], "correct": 0},
            {"q": "Which is an example of a direct employment channel?", "options": ["An employer's official careers page", "A random social-media message asking for money", "A password-sharing website", "An unrelated entertainment site"], "correct": 0},
            {"q": "What should a participant check before applying through a recruitment platform?", "options": ["That the opportunity and application process are legitimate and relevant", "That the recruiter asks for a password", "That payment is required before every application", "That qualifications can be invented"], "correct": 0}
        ]
    },
    {
        "code": "EMP-M9", "title": "Module 9: How to Submit a Professional Application", "icon": "📤",
        "submodules": [
            {"number": "9.1", "title": "Follow the Instructions Exactly", "content_html": """
                <h3>Follow the Instructions Exactly</h3>
                <p>A good CV cannot compensate for ignoring an employer's application instructions. Some South African public-sector advertisements specify exact requirements for: application forms, CV format, document combinations, email subject lines, reference numbers, and specific email addresses.</p>
                <p><strong>Failure to follow required application instructions can result in an application not being considered.</strong></p>
            """},
            {"number": "9.2", "title": "Application Quality Check & File Naming", "content_html": """
                <h3>Application Quality Check & File Naming</h3>
                <p><strong>Before applying, CHECK:</strong> Am I qualified? Do I meet mandatory requirements? Is my CV tailored? Is my cover letter tailored? Is the closing date valid?</p>
                <p><strong>File Naming Standard:</strong> Teach participants to use professional filenames.</p>
                <p>Instead of: <code>cvfinalfinal2.pdf</code></p>
                <p>Use: <code>John_Mokoena_CV_Administrative_Assistant.pdf</code></p>
            """}
        ],
        "quiz": [
            {"q": "What should you do if an advertisement specifies a particular application method?", "options": ["Follow the specified method", "Ignore it", "Send the application anywhere", "Wait until after the closing date"], "correct": 0},
            {"q": "Why should files have professional names?", "options": ["It helps identify the applicant and document clearly", "It guarantees an interview", "It changes the applicant's qualifications", "It replaces proofreading"], "correct": 0},
            {"q": "What should be recorded immediately after applying?", "options": ["Application details", "The employer's password", "A random job title", "Nothing"], "correct": 0}
        ]
    },
    {
        "code": "EMP-M10", "title": "Module 10: Track Every Application", "icon": "📊",
        "submodules": [
            {"number": "10.1", "title": "The Job Application Tracker", "content_html": """
                <h3>The Job Application Tracker</h3>
                <p>This turns job searching into a measurable process. Every application should become a record.</p>
                <p><strong>Recommended Database Fields:</strong> Application ID, Date Found, Employer, Position, Reference, Location, Source, Closing Date, CV Used, Cover Letter (Y/N), Date Applied, Method, Status, Follow-up Date, Response, Interview (Y/N), Outcome, Notes.</p>
            """},
            {"number": "10.2", "title": "Application Status Options", "content_html": """
                <h3>Application Status Options</h3>
                <p>Use controlled values to track progress accurately:</p>
                <ul class="list-disc pl-6 space-y-1">
                    <li>Saved / Preparing / Ready to Apply</li>
                    <li>Submitted</li>
                    <li>Follow-Up Due</li>
                    <li>Shortlisted / Interview / Offer</li>
                    <li>Unsuccessful / Withdrawn / Closed / No Response</li>
                </ul>
            """}
        ],
        "quiz": [
            {"q": "Why should applications be tracked?", "options": ["To know where, when and how you applied and what happened afterwards", "To guarantee employment", "To replace your CV", "To avoid applying for jobs"], "correct": 0},
            {"q": "Which is an appropriate application status after successfully submitting an application?", "options": ["Submitted", "Deleted", "Unknown", "Qualification"], "correct": 0},
            {"q": "What information should be recorded for follow-up?", "options": ["Follow-up date and application details", "The employer's password", "Private information unrelated to the application", "Nothing"], "correct": 0}
        ]
    },
    {
        "code": "EMP-M11", "title": "Module 11: Follow Up & Manage Applications", "icon": "🔔",
        "submodules": [
            {"number": "11.1", "title": "Applying is Not the End", "content_html": """
                <h3>Applying is Not the End</h3>
                <p>After submitting an application, record the date applied, employer, position, reference, closing date, follow-up date, and response.</p>
                <p>The participant should follow the communication instructions provided by the employer and avoid excessive or inappropriate contact.</p>
                        """},
            {"number": "11.2", "title": "Follow-Up Record & Automation", "content_html": """
                <h3>Follow-Up Record & Automation</h3>
                <p>After submitting an application, record the date applied, employer, position, reference, closing date, follow-up date, and response.</p>
                <p>The participant should follow the communication instructions provided by the employer and avoid excessive or inappropriate contact.</p>
                <div class="bg-blue-50 p-4 rounded-lg border-l-4 border-blue-500 mt-4">
                    <h4 class="font-bold text-blue-800">LMS Automation</h4>
                    <p class="text-sm mt-2">The MAYO LMS will identify: IF application status = "Submitted" AND follow_up_date <= TODAY, THEN show "Follow-up due" dashboard notification.</p>
                    <p class="text-sm mt-2 text-blue-700 italic">"Follow-up Reminder: You applied for Administrative Assistant at ABC Company 7 days ago. Check the application status and follow up if appropriate."</p>
                </div>
            """}
        ],
        "quiz": [
            {"q": "What should determine how a participant follows up?", "options": ["The employer's communication instructions and appropriate professional practice", "Sending messages every hour", "Calling random employees", "Sending unrelated documents"], "correct": 0},
            {"q": "Why should follow-up dates be recorded?", "options": ["To prevent important application tasks from being forgotten", "To guarantee selection", "To replace the application", "To change the applicant's qualifications"], "correct": 0},
            {"q": "What should a professional follow-up contain?", "options": ["Relevant application details and a polite request for an update where appropriate", "Threats", "Unrelated information", "False qualifications"], "correct": 0}
        ]
    },
    {
        "code": "EMP-M12", "title": "Module 12: Weekly Job Search System", "icon": "📅",
        "submodules": [
            {"number": "12.1", "title": "Treat Job Searching Like a Weekly Project", "content_html": """
                <h3>Treat Job Searching Like a Weekly Project</h3>
                <p>A job search should not depend on motivation alone. Create a routine.</p>
                <p><strong>Every week:</strong> SEARCH -> ANALYSE -> PREPARE -> APPLY -> TRACK -> FOLLOW UP -> REFLECT</p>
            """},
            {"number": "12.2", "title": "MAYO Weekly Employment Form", "content_html": """
                <h3>MAYO Weekly Employment Form</h3>
                <p>Participants answer weekly:</p>
                <ol class="list-decimal pl-6 space-y-1">
                    <li>How many applications did I submit?</li>
                    <li>How many were suitable for my qualifications?</li>
                    <li>How many required a CV / Cover letter?</li>
                    <li>How many responses/interviews did I receive?</li>
                    <li>What worked? What did not work?</li>
                    <li>What will I change next week?</li>
                </ol>
                <p><strong>LMS Dashboard Calculations:</strong> Application completion rate, CV tailoring rate, Cover-letter rate, Follow-up completion. These metrics measure job-search activity, not the participant's worth.</p>
            """}
        ],
        "quiz": [
            {"q": "What is the purpose of the weekly employment form?", "options": ["To review and improve the participant's job-search activity", "To guarantee employment", "To replace the CV", "To rank participants by personal worth"], "correct": 0},
            {"q": "Which sequence represents the MAYO job-search cycle?", "options": ["Search -> Analyse -> Prepare -> Apply -> Track -> Follow Up -> Reflect", "Apply -> Forget -> Wait", "Search -> Delete -> Stop", "Interview -> CV -> Search"], "correct": 0},
            {"q": "Why should application targets be treated as targets rather than guarantees?", "options": ["Suitable opportunities may not always be available", "Participants should never apply for jobs", "Applications are unnecessary", "Employers guarantee interviews"], "correct": 0}
        ]
    },
    {
        "code": "EMP-M13", "title": "Module 13: Interview Readiness", "icon": "🎤",
        "submodules": [
            {"number": "13.1", "title": "Your CV Opens the Door", "content_html": """
                <h3>Your CV Opens the Door</h3>
                <p>A CV and cover letter are not the final destination. They are part of the process that can lead to an interview. Once invited, the participant must be able to explain and provide evidence for the claims made in their application.</p>
            """},
            {"number": "13.2", "title": "The STAR Response Method", "content_html": """
                <h3>The STAR Response Method</h3>
                <p>Teach participants to structure their answers to behavioural questions:</p>
                <ul class="list-disc pl-6 space-y-2">
                    <li><strong>S - Situation:</strong> What was happening?</li>
                    <li><strong>T - Task:</strong> What needed to be done?</li>
                    <li><strong>A - Action:</strong> What did YOU do?</li>
                    <li><strong>R - Result:</strong> What happened? (Use numbers/metrics if possible)</li>
                </ul>
                <div class="bg-purple-50 p-4 rounded-lg border-l-4 border-purple-500 mt-4">
                    <h4 class="font-bold text-purple-800">Activity: STAR Preparation</h4>
                    <p class="text-sm mt-2">Question: "Tell us about a time you solved a problem." Prepare your Situation, Task, Action, and Result.</p>
                </div>
            """}
        ],
        "quiz": [
            {"q": "What does STAR stand for?", "options": ["Situation, Task, Action, Result", "Skills, Training, Application, Recruitment", "Search, Track, Apply, Respond", "Study, Test, Analyse, Review"], "correct": 0},
            {"q": "Why should interview examples match the CV?", "options": ["The participant should be able to explain and support information presented in the application", "Interviews replace qualifications", "Employers do not care about experience", "Examples are unnecessary"], "correct": 0},
            {"q": "What should a participant research before an interview?", "options": ["The organisation and position", "Random unrelated companies", "The interviewer's private information", "Nothing"], "correct": 0}
        ]
    },
    {
        "code": "EMP-M14", "title": "Module 14: 30-Day Employment Challenge", "icon": "🏆",
        "submodules": [
            {"number": "14.1", "title": "The 4-Week Challenge", "content_html": """
                <h3>The 4-Week Challenge</h3>
                <p>This is the final practical project. Participants must use everything they learned.</p>
                <ul class="list-disc pl-6 space-y-2">
                    <li><strong>Week 1 - BUILD:</strong> Skills inventory, Experience inventory, Professional email, Master CV, Employment profile.</li>
                    <li><strong>Week 2 - APPLY:</strong> Analyse 5 opportunities, tailor CVs, write cover letters, submit applications, record every application.</li>
                    <li><strong>Week 3 - IMPROVE:</strong> Review applications, CV quality, cover letters, responses, missing skills. Update documents based on lessons learned.</li>
                    <li><strong>Week 4 - PROFESSIONALISE:</strong> Submit further applications, follow up appropriately, update tracker, prepare for interviews, complete weekly reflection.</li>
                </ul>
                <p><strong>Final Target:</strong> 5+ quality applications or opportunities pursued, where suitable opportunities are available. The purpose is to build consistent job-search behaviour.</p>
            """},
            {"number": "14.2", "title": "Final Employability Portfolio", "content_html": """
                <h3>Final Employability Portfolio</h3>
                <p>To earn the <strong>MAYO EMPLOYMENT READY</strong> badge, the participant submits:</p>
                <ol class="list-decimal pl-6 space-y-1">
                    <li>Master CV</li>
                    <li>Targeted CV (for a real vacancy)</li>
                    <li>Cover Letter (tailored to the same vacancy)</li>
                    <li>Job Advertisement Analysis</li>
                    <li>Proof/details of submitted application</li>
                    <li>Application Tracker (minimum 5 recorded applications)</li>
                    <li>Weekly Employment Reports (minimum 4)</li>
                    <li>30-Day Employment Action Plan</li>
                </ol>
            """}
        ],
        "quiz": [
            {"q": "What is the purpose of the 30-day challenge?", "options": ["To demonstrate that the participant can apply the course skills in a real job search", "To guarantee immediate employment", "To replace the need for a CV", "To rank participants against each other"], "correct": 0}
        ]
    }
]