import streamlit as st
import pandas as pd
from datetime import datetime

def show_reports():

    st.title("AI Report Studio")
    st.caption("Enterprise Logistics Executive Report")

    st.markdown("---")

    company = st.text_input("Company Name", "ABC Logistics Pvt Ltd")

    period = st.selectbox(
        "Report Period",
        [
            "Today",
            "This Week",
            "This Month",
            "Quarterly"
        ]
    )

    report_type = st.selectbox(
        "Report Type",
        [
            "Executive Summary",
            "Transportation Analysis",
            "Cost Optimization",
            "Risk Assessment",
            "Complete Enterprise Report"
        ]
    )

    st.markdown("---")

    if st.button("Generate AI Report"):

        st.success("Report Generated Successfully")

        st.markdown("##Executive Summary")

        st.info(f"""

**Company**

{company}

**Date**

{datetime.now().strftime("%d-%m-%Y")}

**Report**

{report_type}

**Period**

{period}

""")

        st.markdown("---")

        st.subheader("Transportation Analysis")

        st.success("""

• Average Delay : 18 Minutes

• Congestion Level : Medium

• Best Route : ORR Hyderabad

• AI Confidence : 97%

""")

        st.subheader("Cost Intelligence")

        st.success("""

Fuel Saving : 12%

Driver Cost Reduced : 8%

Maintenance Saving : ₹1.4 Lakh

Estimated Monthly Saving : ₹42 Lakh

""")

        st.subheader("Risk Analysis")

        st.warning("""

Traffic Risk : Medium

Weather Risk : Low

Road Closure : None

Delivery Delay Probability : 11%

""")

        st.subheader("AI Recommendations")

        st.success("""

✔ Dispatch Before 8 AM

✔ Avoid NH44 During Peak Hours

✔ Use ORR

✔ Schedule Preventive Maintenance

✔ Enable Dynamic Route Optimization

""")

        st.markdown("---")

        report = f"""
GENLOGIX AI

Enterprise Logistics Report

Company : {company}

Report : {report_type}

Period : {period}

==================================

Transportation

Delay : 18 Minutes

Best Route : ORR

==================================

Cost Saving

₹42 Lakh

==================================

Risk

Medium

==================================

AI Recommendation

Dispatch Early

Avoid NH44

Use ORR

==================================
"""

        st.download_button(
            "Download Report",
            report,
            "GenLogix_AI_Report.txt"
        )