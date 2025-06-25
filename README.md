# 📄 FinScreen PDF Extractor

A lightweight Streamlit app to extract structured business information from PDF documents using OpenAI's GPT-4o-mini. Built for screening crowdinvesting campaign materials quickly and efficiently.

## 🚀 Features

* Upload one or more PDF documents per company
* Automatically extract key business fields such as:

  * Company Name
  * Industry
  * Funding Requested (EUR)
  * Revenue Last Year (EUR)
  * EBIT (EUR)
  * Use of Funds
  * Business Model
  * Target Market
  * Go-To-Market Strategy
  * Team Info
  * Vision
  * Mission
* Compliance checklist showing presence of essential fields
* Download extracted data as CSV

## 🧠 Powered by

* **OpenAI GPT-4o-mini** for zero-shot information extraction
* **PyMuPDF** (`fitz`) for reliable PDF parsing
* **Streamlit** for the interactive user interface
* **pandas** for data manipulation and CSV export

## 🔑 Setup

### 1. Create and activate a virtual environment

Using `venv`:

```bash
python -m venv finscreen-env
source finscreen-env/bin/activate  # macOS/Linux
# OR
finscreen-env\Scripts\activate   # Windows
```

Or using `conda`:

```bash
conda create -n finscreen-env python=3.10
conda activate finscreen-env
```

### 2. Add your OpenAI API key

For testing purposes my API key is added but will be deactivated after the grading of the assignment. 

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

## 🗂️ Output

* Extracted information is displayed as a formatted JSON block
* Compliance checklist shows presence or absence of key fields
* One-click CSV download for storing extracted results

## ⚡ Notes

* Only the first \~3000 characters of each PDF are sent to the LLM due to token limits
* If the returned response contains invalid JSON, the app attempts to clean and parse it

## 🚩 Caution

This is an MVP prototype. It assumes semi-structured business documents and may not generalize well to poorly formatted or overly technical PDFs.

---

**FinScreen MVP – Making early-stage investment screening smarter with AI.**
