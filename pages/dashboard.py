import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def show_dashboard():

    st.title("Executive Logistics Dashboard")
    st.caption("AI Powered Transportation Bottleneck Analysis & Logistics Cost Optimization")

    st.markdown("---")

    # ================= KPI =================

    c1,c2,c3,c4,c5 = st.columns(5)

    c1.metric("Fleet","2,450","+12")
    c2.metric("Deliveries","1,842","+8%")
    c3.metric("Cost Saved","₹3.2 Cr","+18%")
    c4.metric("Bottlenecks","16","-3")
    c5.metric("AI Accuracy","97.8%","+1.5%")

    st.markdown("---")

    left,right=st.columns([2,1])

    # ================= Charts =================

    with left:

        st.subheader("Logistics Cost Trend")

        df=pd.DataFrame({
            "Month":["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug"],
            "Cost":[85,92,88,79,73,68,62,58]
        })

        fig=px.area(
            df,
            x="Month",
            y="Cost",
            markers=True,
            template="plotly_dark"
        )

        fig.update_layout(height=350)

        st.plotly_chart(fig,use_container_width=True)

        st.subheader("Transportation Bottlenecks")

        bottleneck=pd.DataFrame({

            "Reason":[
                "Traffic",
                "Weather",
                "Road Work",
                "Accident",
                "Port Delay"
            ],

            "Count":[42,18,11,7,14]

        })

        fig2=px.bar(
            bottleneck,
            x="Reason",
            y="Count",
            color="Count",
            template="plotly_dark"
        )

        fig2.update_layout(height=350)

        st.plotly_chart(fig2,use_container_width=True)

    # ================= Right =================

    with right:

        st.subheader("Live AI Alerts")

        st.error("NH44 Heavy Traffic")

        st.warning("Heavy Rain Near Hyderabad")

        st.info("Port Congestion Chennai")

        st.success("Alternate Route Available")

        st.markdown("---")

        st.subheader("Today's Status")

        st.progress(0.82)

        st.write("Fleet Utilization : **82%**")

        st.progress(0.71)

        st.write("Route Efficiency : **71%**")

        st.progress(0.93)

        st.write("Delivery Success : **93%**")

    st.markdown("---")

    a,b=st.columns(2)

    with a:

        st.subheader("Logistics Cost Distribution")

        pie=pd.DataFrame({

            "Category":[
                "Fuel",
                "Driver",
                "Maintenance",
                "Delay"
            ],

            "Value":[40,25,20,15]

        })

        fig3=px.pie(

            pie,

            names="Category",

            values="Value",

            hole=.55,

            template="plotly_dark"

        )

        st.plotly_chart(fig3,use_container_width=True)

    with b:

        st.subheader("AI Recommendations")

        st.success("✅ Shift trucks before 7:30 AM.")

        st.success("✅ Use ORR instead of NH44.")

        st.success("✅ Reduce idle time by 18%.")

        st.success("✅ AI predicts ₹42,000 daily savings.")

        st.success("✅ Low weather risk for next 6 hours.")

    st.markdown("---")

    st.subheader("Executive Summary")

    st.info("""
Today's logistics network is operating efficiently.

AI detected moderate congestion on NH44.

Overall transportation efficiency is 82%.

Predicted savings using AI optimization:
₹42,000 per day.

Recommended Action:

• Dispatch before peak hours

• Use Alternate Route B

• Avoid Chennai Port after 2 PM

• Schedule maintenance tomorrow
""")