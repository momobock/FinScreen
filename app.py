import os
import fitz  # PyMuPDF
import streamlit as st
import pandas as pd
import json
from openai import OpenAI
from typing import List, Dict
import re

# --- Load API key ---
openai_client = OpenAI(api_key="INSERT_HERE")

# --- PDF Parsing ---
def extract_text_from_pdfs(pdf_paths: List[str]) -> Dict[str, str]:
    texts = {}
    for path in pdf_paths:
        doc = fitz.open(path)
        full_text = ""
        for page in doc:
            full_text += page.get_text()
        texts[os.path.basename(path)] = full_text
    return texts

# --- LLM Extraction ---
def llm_extract_info(text: str, client: OpenAI) -> Dict[str, str]:
    prompt = f"""
You are an AI assistant for a crowdfunding platform. Extract the following structured fields from this business document text:

- Company Name
- Industry
- Funding Requested (EUR)
- Revenue Last Year (EUR)
- EBIT (EUR)
- Use of Funds
- Business Model
- Target Market
- Go-To-Market Strategy
- Team Info (summarize founders or key members)
- Vision
- Mission

If a field is not found, return "N/A".

Business Document:
{text}

Return the result as a JSON dictionary.
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    reply = response.choices[0].message.content
    
    if reply.startswith("```json") or reply.startswith("```"):
        reply = reply.strip("` \n")       # Remove ```
        reply = re.sub(r'^json', '', reply, count=1).strip()  # Remove 'json' if present

    try:
        data = json.loads(reply)
    except json.JSONDecodeError as e:
        st.warning(f"⚠️ JSON decode error: {e}")
        data = {}

    return data

# --- Compliance Checklist ---
def compliance_check(info: Dict[str, str]) -> pd.DataFrame:
    fields = [
        "Company Name", "Funding Requested (EUR)", "Revenue Last Year (EUR)",
        "EBIT (EUR)", "Use of Funds", "Team Info", "Business Model", "Target Market"
    ]
    checklist = [{"Field": field, "Status": "✅" if field in info else "⚠️ Missing"} for field in fields]
    return pd.DataFrame(checklist)

# --- Main Processing Function ---
def process_company_pdfs_llm(company_name: str, pdf_paths: List[str]) -> Dict:
    extracted_texts = extract_text_from_pdfs(pdf_paths)
    merged_info = {}
    for name, text in extracted_texts.items():
        info = llm_extract_info(text[:3000], openai_client)
        merged_info.update(info)
    checklist_df = compliance_check(merged_info)
    return {
        "company": company_name,
        "extracted_info": merged_info,
        "checklist": checklist_df
    }

# --- Streamlit UI ---
st.title("📄 PDF to Structured Business Info")
st.write("Upload a business campaign PDF and get structured data extracted via OpenAI.")

uploaded_files = st.file_uploader("Upload one or more PDF files", type="pdf", accept_multiple_files=True)
company_name = st.text_input("Company Name")

if uploaded_files and company_name:
    with st.spinner("Processing..."):
        temp_paths = []
        for file in uploaded_files:
            temp_path = os.path.join("temp_" + file.name)
            with open(temp_path, "wb") as f:
                f.write(file.getbuffer())
            temp_paths.append(temp_path)

        results = process_company_pdfs_llm(company_name, temp_paths)

        st.subheader("Extracted Info")
        st.json(results["extracted_info"])

        st.subheader("Compliance Checklist")
        st.dataframe(results["checklist"])

        # --- CSV Export Button ---
        csv = pd.DataFrame([results["extracted_info"]]).to_csv(index=False).encode('utf-8')
        st.download_button(
            label="⬇️ Download Extracted Info as CSV",
            data=csv,
            file_name=f"{company_name.replace(' ', '_')}_extracted_info.csv",
            mime="text/csv"
        )

        for path in temp_paths:
            os.remove(path)
else:
    st.info("Please upload at least one PDF and enter a company name.")