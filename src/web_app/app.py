import streamlit as st
import requests
from pathlib import Path

# Streamlit app title and instructions
st.title("News Research Report Generator")
st.write("Enter a topic and country to generate a research report.")

# User inputs
topic = st.text_input("Enter the topic for research:")
country = st.text_input("Enter the country of interest:")

# Button to trigger the report generation
if st.button("Generate Report"):
    if topic and country:
        # Display loading status
        with st.spinner("Generating report..."):
            # Send POST request to the FastAPI endpoint
            response = requests.post(
                "https://surveysearch-production.up.railway.app/generate_report/",
                json={"topic": topic, "country": country}
            )
        
        # Handle the response
        if response.status_code == 200:
            st.success("Report generated successfully!")
            st.json(response.json())

            # Define the expected report file path
            report_filename = f"{country}_report.md"
            report_path = Path(report_filename)

            # Check if the report file exists
            if report_path.exists():
                with open(report_path, "r") as file:
                    report_content = file.read()

                # Display the report content in the app
                st.text_area("Generated Report", report_content, height=300)

                # Provide a download button
                with open(report_filename, "rb") as file:
                    btn = st.download_button(
                        label=f"Download {report_filename}",
                        data=file,
                        file_name=report_filename,
                        mime="text/markdown"
                    )
            else:
                st.error(f"Report file '{report_filename}' not found.")
        else:
            st.error(f"Failed to generate report: {response.text}")
    else:
        st.warning("Please provide both a topic and a country.")
