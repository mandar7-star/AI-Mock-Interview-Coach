# 🎯 AI Mock Interview Coach

A multi-agent system that conducts realistic mock interviews and gives actionable feedback.

## ✅ Requirements Fulfilled

| Requirement | How It's Done |
|-------------|----------------|
| **3+ distinct agents** | Interviewer, Evaluator, Coach agents with different roles |
| **5-7 turns with follow-ups** | Loop runs 5-7 questions, adapts based on answers |
| **Adaptive probing** | Follow-up questions if answers are shallow |
| **Multi-dimension evaluation** | Scores relevance, clarity, depth, confidence, overall |
| **Structured feedback** | Strengths, gaps, advice, practice plan, verdict |
| **Handles real messiness** | Handles "I don't know", vague answers, off-topic |

## Quick Start

```bash
# Install
pip install openai python-dotenv

# Set up API key
echo "OPENAI_API_KEY=your_key_here" > .env

# Run
python interview_coach.py