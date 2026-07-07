import streamlit as st

def show_multi_agent():

    st.title("Multi-Agent AI Decision Center")
    st.caption("Autonomous AI Agents Collaborating for Logistics Optimization")

    st.markdown("---")

    c1,c2,c3,c4 = st.columns(4)

    c1.metric("Traffic Agent","Running","🟢")
    c2.metric("Cost Agent","Running","🟢")
    c3.metric("Weather Agent","Running","🟢")
    c4.metric("Risk Agent","Running","🟢")

    st.markdown("---")

    st.subheader("AI Agent Collaboration")

    with st.expander("Traffic Agent"):
        st.success("""
Detected congestion on NH44.

Average delay: 24 minutes.

Suggested alternate route: ORR.
""")

    with st.expander("Weather Agent"):
        st.info("""
Heavy rain expected between 4 PM and 6 PM.

Risk Level: Medium.
""")

    with st.expander("Cost Agent"):
        st.warning("""
Fuel price increased by 5%.

Estimated logistics cost increase:
₹18,500/day.
""")

    with st.expander("Risk Agent"):
        st.error("""
Accident probability on Route A: 18%.

Recommended Risk Level: Medium.
""")

    st.markdown("---")

    st.subheader("Final AI Decision")

    st.success("""
✅ Best Route: ORR

✅ Dispatch Time: Before 8:00 AM

✅ Estimated Savings: ₹42,500

✅ Delay Reduction: 31 Minutes

✅ AI Confidence: 97.8%
""")