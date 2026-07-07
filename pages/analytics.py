import streamlit as st
import pandas as pd
import plotly.express as px

def show_analytics():

    st.title("Cost Intelligence & AI Analytics")
    st.caption("Enterprise Logistics Analytics Dashboard")

    st.markdown("---")

    c1,c2,c3,c4=st.columns(4)

    c1.metric("Total Cost","₹12.8 Cr","+5%")
    c2.metric("Fuel Cost","₹4.5 Cr","-2%")
    c3.metric("Fleet Utilization","91%","+3%")
    c4.metric("AI Savings","₹1.82 Cr","+14%")

    st.markdown("---")

    left,right=st.columns(2)

    with left:

        st.subheader("Monthly Logistics Cost")

        df=pd.DataFrame({
            "Month":["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug"],
            "Cost":[12,13,14,15,14,13,12,11]
        })

        fig=px.line(
            df,
            x="Month",
            y="Cost",
            markers=True,
            template="plotly_dark"
        )

        st.plotly_chart(fig,use_container_width=True)

    with right:

        st.subheader("Cost Distribution")

        pie=pd.DataFrame({
            "Category":[
                "Fuel",
                "Maintenance",
                "Driver",
                "Toll",
                "Delay"
            ],
            "Value":[40,20,18,10,12]
        })

        fig2=px.pie(
            pie,
            names="Category",
            values="Value",
            hole=.6,
            template="plotly_dark"
        )

        st.plotly_chart(fig2,use_container_width=True)

    st.markdown("---")

    a,b=st.columns(2)

    with a:

        st.subheader("Fleet Performance")

        fleet=pd.DataFrame({
            "Vehicle":[
                "Truck A",
                "Truck B",
                "Truck C",
                "Truck D",
                "Truck E"
            ],
            "Efficiency":[91,87,95,82,90]
        })

        fig3=px.bar(
            fleet,
            x="Vehicle",
            y="Efficiency",
            color="Efficiency",
            template="plotly_dark"
        )

        st.plotly_chart(fig3,use_container_width=True)

    with b:

        st.subheader("AI Forecast")

        st.success("""
### AI Prediction

• Logistics Cost will reduce by **11%**

• Fuel consumption expected to drop **8%**

• Route optimization may save **₹52,000/day**

• Fleet utilization expected to reach **95%**

• AI Confidence: **97.6%**
""")

    st.markdown("---")

    st.subheader("Executive Insights")

    st.info("""
### Business Summary

✔ AI has identified unnecessary fuel consumption on NH44.

✔ ORR remains the best alternative.

✔ Delay penalties reduced by 14%.

✔ Fleet utilization increased by 3%.

✔ AI predicts annual savings of ₹4.8 Crore.
""")