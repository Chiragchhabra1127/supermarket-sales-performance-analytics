# 🛒 Supermarket Sales Analytics — Data Analytics with AI Internship

**Author:** Chirag · Maharaja Ganga Singh University (MGSU), Bikaner
**Program:** AICTE | IBM SkillsBuild — Data Analytics with AI Academic Internship (in collaboration with BharatCares)

---

## 📌 Project Overview

This project analyzes 1,000 point-of-sale transactions across three supermarket branches (Alex, Cairo, Giza) to answer a core business question: **which branches, product lines, and customer segments drive revenue — and what should the business do next?**

The project follows the full Business Intelligence workflow taught in the internship:

`Raw Data → Clean Data → EDA → Insights → Dashboard → Decision`

It moves beyond descriptive charts to produce **testable hypotheses** and **prioritized, decision-ready recommendations**, backed by a live interactive dashboard.

## 📊 Dataset

- **Source:** [Supermarket Sales dataset, Kaggle](https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales)
- **File:** `SuperMarket_Analysis.csv`
- **Size:** 1,000 rows × 17 columns
- **Fields:** Invoice ID, Branch, City, Customer type, Gender, Product line, Unit price, Quantity, Tax, Sales, Date, Time, Payment method, COGS, Gross margin %, Gross income, Rating
- **Data quality:** Verified — 0 missing values, 0 duplicate records

## 🧰 Technologies Used

| Layer | Technology |
|---|---|
| Data Processing | Python, pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Dashboard | Streamlit |
| Report | Word (.docx) — auto-generated with embedded charts |
| Environment | Google Colab / Jupyter Notebook |

## 🗂️ Project Structure

```
supermarket_project/
├── SuperMarket_Analysis.csv              # Raw dataset
├── Chirag_SupermarketAnalysis.ipynb      # Full analysis notebook (code file)
├── app.py                                # Streamlit dashboard
├── Chirag_SupermarketAnalysis_Report.docx # Full project report
├── requirements.txt                      # Python dependencies
└── README.md                             # This file
```

## ▶️ How to Run

**1. Install dependencies**
```bash
pip install -r requirements.txt
```

**2. Run the analysis notebook**
Open `Chirag_SupermarketAnalysis.ipynb` in Jupyter or Google Colab and run all cells. It performs data loading, cleaning, aggregation, visualization, and generates the business insights.

**3. Launch the interactive dashboard**
```bash
streamlit run app.py
```
This opens a browser dashboard structured around a five-level information hierarchy:
1. **KPIs** — What is happening?
2. **Trends** — How is it changing?
3. **Drivers** — Why?
4. **Risk** — What could go wrong?
5. **Action** — What should we do?

## 🔑 Key Findings

- **Total revenue:** $322,967 across 1,000 orders (avg. order value $322.97)
- **Top branch:** Giza ($110,569 revenue, highest average rating of 7.07)
- **Top product line:** Food and beverages; **weakest:** Health and beauty (~12% behind)
- **Loyalty impact:** Member customers drive 58.7% of total revenue with a $29 higher average order value than Normal customers
- **Demand pattern:** Revenue peaks on Saturdays and around 7 PM daily
- **Revenue driver:** Quantity purchased correlates strongly with sales (r = 0.71); customer rating does not (r ≈ 0.04)

## 💡 Recommendations

1. Investigate and test Giza's practices at Cairo — the dataset does not capture staffing, layout, or service-process details, so investigate Giza's actual practices and pilot the most promising ones at Cairo for one quarter, tracking rating and revenue before and after
2. Invest targeted marketing in the underperforming Health and beauty category
3. Expand the loyalty program with a higher tier for high-spending Members
4. Align staff schedules with observed demand peaks (Saturdays, 6–9 PM)
5. Track customer satisfaction as an independent KPI, separate from revenue

Full methodology, all visualizations, and detailed reasoning are documented in `Chirag_SupermarketAnalysis_Report.docx`.

## 📝 Note on AI-Assisted Analysis

This project used Google Gemini within Google Colab as an analysis assistant for code generation and drafting insights. In line with the internship's guidance on responsible AI use, all AI-generated conclusions were cross-checked against the underlying dashboard and summary tables before being included in the final report — model output informed, but did not replace, the business judgment behind each recommendation.
