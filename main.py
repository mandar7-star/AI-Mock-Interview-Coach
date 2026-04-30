"""
AI Mock Interview Coach - Multi-Agent System
One file, no over-engineering, all requirements met.
"""

import os
import json
from datetime import datetime
from typing import List, Dict
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL = os.getenv("MODEL_NAME", "gpt-3.5-turbo")  # Cheaper for testing

# ============ AGENT 1: INTERVIEWER ============
class InterviewerAgent:
    """Asks questions, adapts based on answers"""
    
    def __init__(self):
        with open("prompts/interviewer.txt", "r") as f:
            self.system_prompt = f.read()
    
    def ask_question(self, context: Dict, history: List[Dict], difficulty: str) -> str:
        """Generate next question based on conversation history"""
        
        # Build history summary for context
        history_text = ""
        for turn in history[-3:]:  # Last 3 exchanges
            history_text += f"\nQ: {turn['question']}\nA: {turn['answer']}\nScore: {turn.get('score', 'N/A')}/10\n"
        
        user_prompt = f"""
Role: {context['role']}
Focus: {context['focus_area']}
Difficulty: {difficulty}
Candidate background: {context.get('background', 'Not provided')}

Previous conversation:
{history_text if history_text else "This is the first question."}

Generate the next interview question. Adapt based on their performance.
Be concise. Return ONLY the question.
"""
        
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7
        )
        
        return response.choices[0].message.content.strip()


# ============ AGENT 2: EVALUATOR ============
class EvaluatorAgent:
    """Scores answers on multiple dimensions"""
    
    def __init__(self):
        with open("prompts/evaluator.txt", "r") as f:
            self.system_prompt = f.read()
    
    def evaluate(self, question: str, answer: str, context: Dict) -> Dict:
        """Return structured evaluation"""
        
        user_prompt = f"""
Question: {question}
Answer: {answer}
Role: {context['role']}
Focus area: {context['focus_area']}

Return JSON with these fields:
{{
    "overall_score": (0-10),
    "relevance": (0-10),
    "clarity": (0-10),
    "depth": (0-10),
    "confidence": (0-10),
    "strengths": ["strength1", "strength2"],
    "weaknesses": ["weakness1", "weakness2"],
    "feedback": "brief comment"
}}
"""
        
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3,
            response_format={"type": "json_object"}
        )
        
        try:
            return json.loads(response.choices[0].message.content)
        except:
            # Fallback if JSON parsing fails
            return {
                "overall_score": 5,
                "relevance": 5,
                "clarity": 5,
                "depth": 5,
                "confidence": 5,
                "strengths": ["Attempted answer"],
                "weaknesses": ["Needs improvement"],
                "feedback": "Keep practicing!"
            }


# ============ AGENT 3: COACH ============
class CoachAgent:
    """Generates final feedback and improvement plan"""
    
    def __init__(self):
        with open("prompts/coach.txt", "r") as f:
            self.system_prompt = f.read()
    
    def generate_feedback(self, transcript: List[Dict], context: Dict) -> Dict:
        """Comprehensive end-of-interview feedback"""
        
        # Format transcript
        transcript_text = ""
        for turn in transcript:
            transcript_text += f"""
Turn {turn['turn']}:
Q: {turn['question']}
A: {turn['answer']}
Score: {turn['score']}/10
Strengths: {', '.join(turn.get('strengths', []))}
Weaknesses: {', '.join(turn.get('weaknesses', []))}
"""
        
        user_prompt = f"""
Context:
- Target role: {context['role']}
- Focus area: {context['focus_area']}
- Difficulty used: {context.get('difficulty', 'intermediate')}

Full transcript:
{transcript_text}

Return JSON:
{{
    "overall_score": (average of all turns),
    "strengths": ["top 3 strengths across all answers"],
    "gaps": ["top 3 areas needing improvement"],
    "specific_advice": "detailed paragraph of actionable advice",
    "practice_plan": "3 specific things to practice",
    "would_hire": "yes/no/maybe with brief reason"
}}
"""
        
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.5,
            response_format={"type": "json_object"}
        )
        
        return json.loads(response.choices[0].message.content)


# ============ ORCHESTRATOR ============
class InterviewOrchestrator:
    """Runs the multi-agent system"""
    
    def __init__(self):
        self.interviewer = InterviewerAgent()
        self.evaluator = EvaluatorAgent()
        self.coach = CoachAgent()
        self.transcript = []
    
    def run(self):
        print("\n" + "="*60)
        print("🎯 AI MOCK INTERVIEW COACH".center(60))
        print("="*60)
        
        # Get candidate info
        print("\n📋 Let's set up your interview\n")
        role = input("Target role (e.g., Product Manager, Data Analyst): ").strip()
        background = input("Brief background (2-3 lines, optional): ").strip()
        
        print("\nFocus area:")
        print("  1. Behavioral")
        print("  2. Technical")
        print("  3. Case")
        print("  4. Mixed")
        focus_map = {"1": "behavioral", "2": "technical", "3": "case", "4": "mixed"}
        focus_choice = input("Choose (1-4): ").strip()
        focus_area = focus_map.get(focus_choice, "mixed")
        
        print("\nDifficulty:")
        print("  1. Beginner")
        print("  2. Intermediate")
        print("  3. Advanced")
        diff_choice = input("Choose (1-3): ").strip()
        difficulty_map = {"1": "beginner", "2": "intermediate", "3": "advanced"}
        difficulty = difficulty_map.get(diff_choice, "intermediate")
        
        context = {
            "role": role,
            "background": background,
            "focus_area": focus_area,
            "difficulty": difficulty
        }
        
        print("\n" + "="*60)
        print("🎤 INTERVIEW STARTING".center(60))
        print("="*60)
        print("\n(Answer each question. Type 'exit' to end early)\n")
        
        # Run interview loop (5-7 turns)
        history = []
        for turn_num in range(1, 8):  # Max 7 turns
            print(f"\n--- Turn {turn_num} ---")
            
            # Generate question
            question = self.interviewer.ask_question(context, history, difficulty)
            print(f"\n🎤 Interviewer: {question}")
            
            # Get answer
            answer = input("\n👤 You: ").strip()
            if answer.lower() == 'exit':
                print("\n⚠️ Interview ended early.")
                break
            
            # Evaluate
            evaluation = self.evaluator.evaluate(question, answer, context)
            
            # Store
            turn_data = {
                "turn": turn_num,
                "question": question,
                "answer": answer,
                "score": evaluation["overall_score"],
                "strengths": evaluation.get("strengths", []),
                "weaknesses": evaluation.get("weaknesses", [])
            }
            history.append(turn_data)
            self.transcript.append(turn_data)
            
            # Show immediate feedback (light touch)
            print(f"\n📊 Score: {evaluation['overall_score']}/10 - {evaluation.get('feedback', '')}")
            
            # Adapt difficulty based on performance
            if evaluation["overall_score"] >= 8:
                difficulty = "advanced"
            elif evaluation["overall_score"] <= 4:
                difficulty = "beginner"
            else:
                difficulty = context["difficulty"]  # Keep original
            
            # Early exit if strong performance at turn 5
            if turn_num >= 5 and evaluation["overall_score"] >= 8.5:
                print("\n✨ You're doing great! I think we've seen enough.")
                break
            
            # Early exit if struggling badly at turn 6
            if turn_num >= 6 and evaluation["overall_score"] <= 3:
                print("\n📚 Let's stop here and review where you can improve.")
                break
        
        # Generate final coaching
        print("\n" + "="*60)
        print("📊 GENERATING FEEDBACK".center(60))
        print("="*60)
        
        feedback = self.coach.generate_feedback(self.transcript, context)
        
        # Display results
        print(f"\n🎯 OVERALL SCORE: {feedback['overall_score']}/10")
        print(f"\n✅ STRENGTHS:")
        for s in feedback['strengths']:
            print(f"   • {s}")
        
        print(f"\n⚠️ AREAS TO IMPROVE:")
        for g in feedback['gaps']:
            print(f"   • {g}")
        
        print(f"\n💡 COACH'S ADVICE:")
        print(f"   {feedback['specific_advice']}")
        
        print(f"\n📚 PRACTICE PLAN:")
        print(f"   {feedback['practice_plan']}")
        
        print(f"\n🏆 VERDICT: {feedback['would_hire']}")
        
        # Save transcript
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        with open(f"transcript_{timestamp}.json", "w") as f:
            json.dump({"context": context, "transcript": self.transcript, "feedback": feedback}, f, indent=2)
        print(f"\n💾 Full transcript saved to transcript_{timestamp}.json")


# ============ RUN ============
if __name__ == "__main__":
    coach = InterviewOrchestrator()
    coach.run()