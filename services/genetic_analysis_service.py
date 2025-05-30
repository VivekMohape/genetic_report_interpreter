import streamlit as st
import instructor
from openai import OpenAI
from datetime import date
from models.genetic_report import GeneticReportResponse

# Load your API key from Streamlit secrets
client = instructor.from_openai(
    OpenAI(api_key=st.secrets["GROQ_API_KEY"])
)

def analyze_genetic_report(report_text: str, report_id: str) -> GeneticReportResponse:
    messages = [
        {"role": "system", "content": "You are a medical genomics assistant. Return structured data on variants."},
        {"role": "user", "content": f"Interpret this genetic report:\n\n{report_text}"}
    ]

    result = client.chat.completions.create(
        # Hard-coded model
        model="llama3-70b-8192",
        response_model=GeneticReportResponse,
        messages=messages
    )

    result.interpretation_date = str(date.today())
    result.report_id = report_id
    return result
