#  AI Mock Interview Coach (Multi-Agent System)

A smart interview simulator that mimics real interview scenarios using **multiple AI agents** — designed to give **honest evaluation + actionable feedback**.




##  What this project does

This system conducts a full mock interview by:
- Asking adaptive questions  
- Evaluating answers in real-time  
- Providing structured, personalized feedback  

It behaves like a **real interviewer + evaluator + career coach combined**.




##  Core Idea

Instead of a single chatbot, this project uses a **multi-agent architecture** where each agent has a clear responsibility:

###  Interviewer Agent
- Asks one question at a time  
- Adapts based on previous answers  
- Mixes behavioral, technical, and case questions  

###  Evaluator Agent
- Scores answers on:
  - Clarity  
  - Relevance  
  - Depth  
  - Confidence  
- Identifies strengths and weaknesses  

###  Coach Agent
- Gives structured feedback:
  - Key strengths  
  - Improvement areas  
  - Actionable advice  
  - 3-step practice plan  
- Provides a final hiring recommendation  




##  Interview Flow

1. Candidate selects:
   - Role (e.g., Data Scientist)
   - Focus area (Behavioral / Technical / Mixed)
   - Difficulty level  

2. System runs **5–7 interview rounds**
   - Question → Answer → Evaluation  

3. Difficulty adapts dynamically:
   - Good answer → harder questions  
   - Weak answer → simpler questions  

4. Final output includes:
   - Overall score  
   - Strengths & gaps  
   - Personalized coaching feedback  





##  Key Highlights

- Multi-agent design (Interviewer + Evaluator + Coach)  
- Adaptive questioning based on performance  
- Structured scoring system (0–10 scale)  
- Actionable feedback (not generic advice)  
- Real interview-like experience  




##  Technical Design

- Local LLM-based system (no external API dependency)  
- Modular agent architecture  
- JSON-based structured outputs  
- Transcript logging for analysis  




##  What makes it different

**Most mock interview tools:**
- Give generic feedback  
- Don’t adapt to answers  

**This system:**
- Adjusts difficulty dynamically  
- Evaluates like a strict interviewer  
- Coaches like a real mentor  




##  Use Case

- Data Science / AI interview preparation  
- Practicing structured answers  
- Identifying real weaknesses before interviews  




##  Outcome

Helps candidates:

- Think clearly under pressure  
- Improve answer quality  
- Get interview-ready with targeted feedback

  🚀 AI Mock Interview Coach (Multi-Agent System)

A smart interview simulator that mimics real interview scenarios using multiple AI agents — designed to give honest evaluation + actionable feedback.

🎯 What this project does

This system conducts a full mock interview by:

Asking adaptive questions
Evaluating answers in real-time
Providing structured, personalized feedback

It behaves like a real interviewer + evaluator + career coach combined.

🧠 Core Idea

Instead of a single chatbot, this project uses a multi-agent architecture where each agent has a clear responsibility:

🧑‍💼 Interviewer Agent
Asks one question at a time
Adapts based on previous answers
Mixes behavioral, technical, and case questions
📊 Evaluator Agent
Scores answers on:
Clarity
Relevance
Depth
Confidence
Identifies strengths and weaknesses
🧭 Coach Agent
Gives structured feedback:
Key strengths
Improvement areas
Actionable advice
3-step practice plan
Provides a final hiring recommendation
🔄 Interview Flow
Candidate selects:
Role (e.g., Data Scientist)
Focus area (Behavioral / Technical / Mixed)
Difficulty level
System runs 5–7 interview rounds
Question → Answer → Evaluation
Difficulty adapts dynamically:
Good answer → harder questions
Weak answer → simpler questions
Final output includes:
Overall score
Strengths & gaps
Personalized coaching feedback
⭐ Key Highlights
Multi-agent design (Interviewer + Evaluator + Coach)
Adaptive questioning based on performance
Structured scoring system (0–10 scale)
Actionable feedback (not generic advice)
Real interview-like experience
⚙️ Technical Design
Local LLM-based system (no external API dependency)
Modular agent architecture
JSON-based structured outputs
Transcript logging for analysis
🚀 What makes it different
❌ Most mock interview tools:
Give generic feedback
Don’t adapt to answers
✅ This system:
Adjusts difficulty dynamically
Evaluates like a strict interviewer
Coaches like a real mentor
🎯 Use Case
Data Science / AI interview preparation
Practicing structured answers
Identifying real weaknesses before interviews
🏁 Outcome

Helps candidates:

Think clearly under pressure
Improve answer quality
Get interview-ready with targeted feedback
🧪 Sample Interview Output
🟢 Strong Candidate Example

Context: Role - Product Manager, Focus - Behavioral, Difficulty - Intermediate

Turn 1

Q: Tell me about a time you had to convince a team to adopt your idea.
A: At my previous company, I noticed our user onboarding had 40% drop-off. I proposed a redesign but engineering pushed back due to other priorities. I built a quick prototype, showed data from user sessions, and got buy-in from our VP. The redesign increased retention by 25%.

Score: 9/10 - Excellent STAR format, specific metrics, clear impact

Turn 2

Q: How did you handle the engineering team's initial resistance?
A: I scheduled one-on-ones with the lead engineer to understand their concerns. They were worried about timeline. I offered to reduce scope for v1 and handle user testing myself. We shipped in 3 weeks instead of 2 months.

Score: 8/10 - Good collaboration example, shows empathy

Interview Note

[Interview ends early at Turn 5 due to strong performance]

Final Feedback

Overall Score: 8.5/10
Strengths: Clear communication, metrics-driven, collaborative
Gaps: Could share more failure examples
Verdict: Yes - would hire

