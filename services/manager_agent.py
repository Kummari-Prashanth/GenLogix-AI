from services.traffic_agent import traffic_agent
from services.weather_agent import weather_agent
from services.cost_agent import cost_agent
from services.risk_agent import risk_agent
from services.optimization_agent import optimization_agent
from services.gemini_service import ask_gemini

def manager_agent(question):

    prompt = f"""
You are an AI Logistics Manager.

User Question:
{question}

Traffic Analysis:
{traffic_agent(question)}

Weather Analysis:
{weather_agent(question)}

Cost Analysis:
{cost_agent(question)}

Risk Analysis:
{risk_agent(question)}

Optimization Analysis:
{optimization_agent(question)}

Based on all analyses, generate:

1. Executive Summary
2. Transportation Bottlenecks
3. Cost Optimization
4. Risk Assessment
5. Best Route
6. Final Recommendation

Keep the response professional and well formatted.
"""

    return ask_gemini(prompt)