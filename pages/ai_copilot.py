import streamlit as st
from services.manager_agent import manager_agent

def show_ai_copilot():

    st.title("AI Logistics Command Center")
    st.caption("Autonomous Multi-Agent Generative AI System")

    question = st.text_area(
        "Enter your logistics problem",
        height=180,
        placeholder="Example: Analyze transportation bottlenecks between Hyderabad and Chennai."
    )

    if st.button("Analyze with AI"):

        if question.strip() == "":
            st.warning("Please enter a question.")
            return

        with st.spinner("AI Agents are analyzing..."):

            answer = manager_agent(question)

        st.success("Analysis Completed")

        st.markdown("## Executive Recommendation")

        st.write(answer)

    st.markdown("---")

    st.subheader("AI Workflow")

    st.info("""
User
⬇
Manager Agent
⬇
Traffic Agent
Weather Agent
Cost Agent
Risk Agent
Optimization Agent
⬇
Gemini AI
⬇
Executive Recommendation
""")