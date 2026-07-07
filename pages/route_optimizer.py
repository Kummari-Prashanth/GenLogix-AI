import streamlit as st
import pandas as pd
import plotly.express as px

def show_route_optimizer():

    st.title("AI Smart Route Optimizer")
    st.caption("Optimize transportation routes using AI")

    st.markdown("---")

    col1,col2,col3=st.columns(3)

    with col1:
        source=st.selectbox(
            "Source",
            ["Hyderabad","Chennai","Bangalore","Mumbai","Delhi"]
        )

    with col2:
        destination=st.selectbox(
            "Destination",
            ["Hyderabad","Chennai","Bangalore","Mumbai","Delhi"]
        )

    with col3:
        vehicle=st.selectbox(
            "Vehicle",
            ["Truck","Mini Truck","Container","Van"]
        )

    st.markdown("---")

    if st.button("Optimize Route"):

        st.success("AI Route Generated")

        a,b,c,d=st.columns(4)

        a.metric("Distance","624 KM")
        b.metric("ETA","8.2 Hrs")
        c.metric("Fuel Saving","13%")
        d.metric("Cost Saving","₹18,600")

        st.markdown("---")

        df=pd.DataFrame({

            "City":[
                source,
                "Kurnool",
                "Anantapur",
                "Bangalore",
                destination
            ],

            "Latitude":[
                17.385,
                15.828,
                14.681,
                12.971,
                13.082
            ],

            "Longitude":[
                78.486,
                78.037,
                77.600,
                77.594,
                80.270
            ]

        })

        fig=px.scatter_map(
            df,
            lat="Latitude",
            lon="Longitude",
            hover_name="City",
            zoom=4,
            height=600
        )

        st.plotly_chart(fig,use_container_width=True)

        st.markdown("---")

        st.subheader("AI Recommendation")

        st.success("""

Best Route Selected

Traffic Level : Low

Weather Risk : Low

Fuel Saving : 13%

Delivery Time Reduced : 48 Minutes

AI Confidence : 98%

""")