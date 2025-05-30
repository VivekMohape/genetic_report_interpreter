import streamlit as st
from services.genetic_analysis_service import analyze_genetic_report
from uuid import uuid4

st.set_page_config(page_title="Genetic Report Interpreter", layout="wide")
st.title("🧬 Genetic Report Interpreter")

uploaded_file = st.file_uploader("Upload report (.txt or .csv)", type=["txt", "csv"])

@st.cache_data(show_spinner="Analyzing with Groq...", ttl="1h")
def cached_analysis(report_text: str, report_id: str):
    return analyze_genetic_report(report_text, report_id)

if uploaded_file:
    report_text = uploaded_file.read().decode("utf-8")
    report_id = f"report-{uuid4().hex[:8]}"
    
    with st.spinner("Running genetic analysis..."):
        try:
            response = cached_analysis(report_text, report_id)
            st.success("✅ Analysis complete!")
            
            st.subheader(f"🧾 Report ID: `{response.report_id}`")
            st.caption(f"Date: {response.interpretation_date}")
            
            for idx, variant in enumerate(response.variants, 1):
                with st.expander(f"🔹 Variant {idx}: {variant.variant_name}"):
                    st.write(f"**Risk Level:** {variant.risk_level}")
                    st.write(f"**Conditions:** {', '.join(variant.associated_conditions)}")
                    st.write(f"**Drug Response:** {variant.drug_response or 'N/A'}")
                    st.write(f"**Recommendations:** {variant.recommendations or 'N/A'}")
        except Exception as e:
            st.error(f"❌ Error during analysis: {e}")
