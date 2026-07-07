import streamlit as st
import pandas as pd
import plotly.express as px

def show_risk_prediction():

    st.title("AI Risk Prediction Engine")
    st.caption("Predict logistics risks using AI")

    st.markdown("---")

    c1,c2,c3,c4=st.columns(4)

    c1.metric("Traffic Risk","Medium")
    c2.metric("Weather Risk","Low")
    c3.metric("Accident Risk","18%")
    c4.metric("Delivery Success","96%")

    st.markdown("---")

    left,right=st.columns(2)

    with left:

        st.subheader("Risk Analysis")

        risk=pd.DataFrame({

            "Risk":[
                "Traffic",
                "Weather",
                "Road Closure",
                "Vehicle",
                "Fuel"
            ],

            "Probability":[65,25,18,30,40]

        })

        fig=px.bar(
            risk,
            x="Risk",
            y="Probability",
            color="Probability",
            template="plotly_dark"
        )

        st.plotly_chart(fig,use_container_width=True)

    with right:

        st.subheader("Risk Summary")

        st.error("High congestion detected on NH44.")

        st.warning("Moderate rain expected.")

        st.info("Vehicle maintenance due in 2 days.")

        st.success("Alternative route available.")

    st.markdown("---")

    st.subheader("AI Recommendation")

    st.success("""
✔ Dispatch vehicles before 7:30 AM

✔ Use ORR instead of NH44

✔ Schedule preventive maintenance

✔ Monitor weather every 2 hours

✔ Estimated Risk Reduction : 34%
""")