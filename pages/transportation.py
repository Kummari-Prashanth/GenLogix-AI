import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def show_transportation():

    st.title("Live Transportation Intelligence")
    st.caption("Real-Time Transportation Monitoring & AI Optimization")

    st.markdown("---")

    c1,c2,c3,c4=st.columns(4)

    c1.metric("Vehicles","2450","+25")
    c2.metric("Active Routes","186","+6")
    c3.metric("Congestion","14","-2")
    c4.metric("Avg Delay","18 Min","-5")

    st.markdown("---")

    left,right=st.columns([2,1])

    with left:

        st.subheader("Traffic Density")

        df=pd.DataFrame({

            "Time":[
                "6 AM",
                "8 AM",
                "10 AM",
                "12 PM",
                "2 PM",
                "4 PM",
                "6 PM",
                "8 PM"
            ],

            "Traffic":[15,52,84,73,61,95,88,42]

        })

        fig=px.line(
            df,
            x="Time",
            y="Traffic",
            markers=True,
            template="plotly_dark"
        )

        fig.update_layout(height=350)

        st.plotly_chart(fig,use_container_width=True)

        st.subheader("Route Performance")

        routes=pd.DataFrame({

            "Route":[
                "NH44",
                "NH65",
                "ORR",
                "SH12"
            ],

            "Delay":[48,25,15,35]

        })

        fig2=px.bar(

            routes,

            x="Route",

            y="Delay",

            color="Delay",

            template="plotly_dark"

        )

        st.plotly_chart(fig2,use_container_width=True)

    with right:

        st.subheader("Live Alerts")

        st.error("🔴 NH44 Heavy Traffic")

        st.warning("🟡 Weather Warning")

        st.info("🔵 Chennai Port Delay")

        st.success("🟢 Route ORR Recommended")

        st.markdown("---")

        st.subheader("AI Route Recommendation")

        st.success("""
Best Route

ORR Hyderabad

Distance : 38 KM

ETA : 42 Minutes

Fuel Saving : 11%

Cost Saving : ₹7,850
""")

    st.markdown("---")

    st.subheader("Transportation Control Center")

    col1,col2,col3=st.columns(3)

    with col1:

        st.info("""
### Fleet Status

Active : 2450

Idle : 182

Maintenance : 64
""")

    with col2:

        st.warning("""
### Weather

Rain Risk

Medium

Visibility

Good
""")

    with col3:

        st.success("""
### AI Recommendation

Dispatch Before

8:00 AM

Use ORR

Avoid NH44
""")

    st.markdown("---")

    st.subheader("AI Summary")

    st.success("""
AI has detected increasing congestion on NH44.

The ORR route is currently the fastest and most cost-effective.

Estimated savings:

• Fuel: 11%

• Delay Reduction: 27 Minutes

• Logistics Cost Saving: ₹7,850

Overall Transportation Efficiency: 91%
""")