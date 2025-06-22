# FinScreen MVP

This is the MVP for **FinScreen**, a SaaS platform that automates the onboarding and screening of crowdfunding campaigns using AI-powered document analysis.

It is implemented as a Jupyter Notebook using Python and OpenAI's GPT models to extract structured campaign information from uploaded PDF files.

---

## 🧠 Features

- Upload **multiple PDFs** per company
- Automatically **extract**:
  - Company name
  - Funding requested
  - Revenue & EBIT
  - Business model, GTM strategy
  - Use of funds, mission, team info
- Generate a **compliance checklist**
- Fully supports **GPT-3.5** or **GPT-4o** extraction

---

## 🚀 How to Use

### 1. Activate your environment
```bash
conda activate finscreen-env
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set your OpenAI API key
**Option A (recommended):** Use an environment variable
```bash
export OPENAI_API_KEY="your-key-here"
```

**Option B:** Set directly in code
```python
from openai import OpenAI
client = OpenAI(api_key="your-key-here")
```

---

## 📂 Running the Notebook

1. Start Jupyter Notebook:
```bash
jupyter notebook
```

2. Open `FinScreen_MVP.ipynb`

3. Set company name and PDF list:
```python
company_name = "GreenFlow Solutions"
pdf_files = ["sample_campaign.pdf"]
```

4. Run the pipeline:
```python
results = process_company_pdfs_llm(company_name, pdf_files)
```

---

## 📊 Output

### Extracted Info
```python
results["extracted_info"]
```

### Compliance Checklist
```python
results["checklist"]
```

---

## 🧾 Requirements

```txt
openai>=1.3.0
pdfplumber>=0.10.0  # or pymupdf>=1.22.0 if working
pandas>=1.5.0
matplotlib>=3.7.0
ipykernel>=6.29.0
notebook>=7.0.0
```

---

## 📌 Notes

- This version uses **GPT** for extraction and skips benchmarking for simplicity.
- You can add benchmarks, visualizations, or validation as future features.

---

## 🔒 Security

- Never upload confidential PDFs without checking OpenAI data usage terms.
- Always keep your `OPENAI_API_KEY` secret.