import streamlit as st
import requests

st.title("News Research Report Generator")

topic = st.text_input("Enter a topic for research:")
country = st.text_input("Enter the country for research:")

if st.button("Generate Report"):
    if topic and country:
        st.write(f"Generating report for topic: {topic} in {country}...")
        
        # Send request to FastAPI backend
        response = requests.post(
            "http://127.0.0.1:8000/generate_report/",
            json={"topic": topic, "country": country}
        )
        
        if response.status_code == 200:
            st.success("Report generated successfully!")
        else:
            st.error("Failed to generate the report.")
