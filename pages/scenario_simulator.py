import streamlit as st

def show_scenario():

    st.title("AI Scenario Simulator")
    st.caption("Predict logistics performance under different conditions")

    st.markdown("---")

    traffic = st.slider("Traffic Congestion (%)", 0, 100, 40)

    weather = st.selectbox(
        "🌦 Weather",
        ["Clear","Rain","Heavy Rain","Fog","Storm"]
    )

    fuel = st.slider("Fuel Price Increase (%)",0,50,10)

    demand = st.slider("Delivery Demand (%)",0,100,65)

    if st.button("Run AI Simulation"):

        delay = traffic*0.6 + fuel*0.3

        saving = max(5,100-delay)

        st.success("Simulation Completed")

        col1,col2,col3 = st.columns(3)

        col1.metric("Estimated Delay",f"{int(delay)} Min")

        col2.metric("Predicted Saving",f"₹ {saving*1200:,.0f}")

        col3.metric("Efficiency",f"{saving:.1f}%")

        st.markdown("---")

        st.subheader("AI Recommendation")

        if traffic>70:
            st.error("Use Alternate Route ORR immediately.")

        elif weather!="Clear":
            st.warning("Weather may impact delivery schedule.")

        else:
            st.success("Current logistics network is operating efficiently.")