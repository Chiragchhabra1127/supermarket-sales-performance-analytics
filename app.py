"""
Supermarket Sales Analysis Dashboard
Author: Chirag | IBM SkillsBuild - Data Analytics with AI Internship

Run with: streamlit run app.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Supermarket Sales Dashboard", page_icon="🛒", layout="wide")

PALETTE = ['#2E5EAA', '#F2A541', '#4CAF91', '#D9534F', '#8E6FCE', '#5BA3D0']
sns.set_palette(PALETTE)
plt.rcParams.update({
    'axes.spines.top': False, 'axes.spines.right': False,
    'axes.grid': True, 'grid.alpha': 0.25, 'figure.dpi': 110,
})


@st.cache_data
def load_data():
    df = pd.read_csv('SuperMarket_Analysis.csv')
    df.columns = [c.strip() for c in df.columns]
    df = df.drop_duplicates()
    df['Date'] = pd.to_datetime(df['Date'])
    df['Time'] = pd.to_datetime(df['Time'], format='%I:%M:%S %p', errors='coerce').dt.time
    df['Hour'] = pd.to_datetime(df['Time'].astype(str)).dt.hour
    df['Weekday'] = df['Date'].dt.day_name()
    weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    df['Weekday'] = pd.Categorical(df['Weekday'], categories=weekday_order, ordered=True)
    return df


df = load_data()

# ---------------- SIDEBAR FILTERS ----------------
st.sidebar.header("Filters")
branches = st.sidebar.multiselect("Branch", options=sorted(df['Branch'].unique()), default=sorted(df['Branch'].unique()))
cust_types = st.sidebar.multiselect("Customer Type", options=sorted(df['Customer type'].unique()), default=sorted(df['Customer type'].unique()))

filtered = df[(df['Branch'].isin(branches)) & (df['Customer type'].isin(cust_types))]

st.sidebar.markdown("---")
st.sidebar.caption(f"Showing {len(filtered):,} of {len(df):,} transactions")

# ---------------- HEADER ----------------
st.title("🛒 Supermarket Sales Analysis Dashboard")
st.caption("IBM SkillsBuild — Data Analytics with AI Internship | Prepared by Chirag")
st.markdown("---")

if filtered.empty:
    st.warning("No data matches the selected filters. Please widen your selection.")
    st.stop()

# ---------------- LEVEL 1: KPIs ----------------
st.subheader("📊 Level 1 — Executive KPIs")
total_revenue = filtered['Sales'].sum()
total_orders = len(filtered)
avg_order = filtered['Sales'].mean()
avg_rating = filtered['Rating'].mean()
gross_income = filtered['gross income'].sum()

k1, k2, k3, k4, k5 = st.columns(5)
k1.metric("Total Revenue", f"${total_revenue:,.0f}")
k2.metric("Total Orders", f"{total_orders:,}")
k3.metric("Avg. Order Value", f"${avg_order:,.2f}")
k4.metric("Gross Income", f"${gross_income:,.0f}")
k5.metric("Avg. Rating", f"{avg_rating:.2f} / 10")

st.markdown("---")

# ---------------- LEVEL 2: TRENDS ----------------
st.subheader("📈 Level 2 — Trends")
c1, c2 = st.columns(2)

with c1:
    st.markdown("**Revenue by Day of Week**")
    weekday_sales = filtered.groupby('Weekday', observed=True)['Sales'].sum()
    fig, ax = plt.subplots(figsize=(6, 4))
    weekday_sales.plot(kind='line', marker='o', ax=ax, color=PALETTE[2], linewidth=2)
    ax.set_ylabel("Revenue ($)")
    ax.set_xlabel("")
    plt.xticks(rotation=30, ha='right')
    st.pyplot(fig)

with c2:
    st.markdown("**Revenue by Hour of Day**")
    hourly_sales = filtered.groupby('Hour')['Sales'].sum()
    fig, ax = plt.subplots(figsize=(6, 4))
    hourly_sales.plot(kind='bar', ax=ax, color=PALETTE[3])
    ax.set_ylabel("Revenue ($)")
    ax.set_xlabel("Hour")
    st.pyplot(fig)

st.markdown("---")

# ---------------- LEVEL 3: DRIVERS ----------------
st.subheader("🔍 Level 3 — Drivers")
c3, c4 = st.columns(2)

with c3:
    st.markdown("**Revenue by Branch**")
    branch_summary = filtered.groupby('Branch').agg(
        Total_Sales=('Sales', 'sum'), Orders=('Invoice ID', 'count'), Avg_Rating=('Rating', 'mean')
    ).round(2).sort_values('Total_Sales', ascending=False)
    fig, ax = plt.subplots(figsize=(6, 4))
    branch_summary['Total_Sales'].plot(kind='bar', ax=ax, color=PALETTE[0])
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))
    plt.xticks(rotation=0)
    st.pyplot(fig)
    st.dataframe(branch_summary, use_container_width=True)

with c4:
    st.markdown("**Revenue by Product Line**")
    product_summary = filtered.groupby('Product line').agg(
        Total_Sales=('Sales', 'sum'), Orders=('Invoice ID', 'count'), Gross_Income=('gross income', 'sum')
    ).round(2).sort_values('Total_Sales', ascending=False)
    fig, ax = plt.subplots(figsize=(6, 4))
    product_summary['Total_Sales'].plot(kind='barh', ax=ax, color=PALETTE[1])
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))
    st.pyplot(fig)
    st.dataframe(product_summary, use_container_width=True)

st.markdown("---")

# ---------------- LEVEL 4: RISK ----------------
st.subheader("⚠️ Level 4 — Risk")
weakest_branch = filtered.groupby('Branch')['Rating'].mean().idxmin()
weakest_product = filtered.groupby('Product line')['Sales'].sum().idxmin()
corr = filtered[['Quantity', 'Sales', 'Rating']].corr()

r1, r2, r3 = st.columns(3)
r1.warning(f"**Lowest-rated branch:** {weakest_branch}\n\nNeeds service quality review.")
r2.warning(f"**Weakest category:** {weakest_product}\n\nUnderperforming vs. peers — revenue risk.")
r3.info(f"**Rating vs. Sales correlation:** {corr.loc['Rating','Sales']:.2f}\n\nSatisfaction doesn't track spend — don't assume one drives the other.")

st.markdown("---")

# ---------------- LEVEL 5: ACTION ----------------
st.subheader("✅ Level 5 — Recommended Actions")
st.markdown("""
1. **Investigate and test Giza's practices at Cairo** — The dataset does not capture staffing, layout, or service-process details, so investigate Giza's actual practices and pilot the most promising ones at Cairo for one quarter, tracking rating and revenue before and after.
2. **Invest marketing budget in the weakest product category** to close the revenue gap with top performers.
3. **Expand the loyalty program** — Member customers already show higher average order value.
4. **Align staffing with peak demand** — concentrate resources around the busiest weekday and hour shown above.
5. **Track customer satisfaction as an independent KPI** — since it does not strongly correlate with revenue.
""")

st.markdown("---")
st.caption("Built with Streamlit · Data source: SuperMarket_Analysis.csv · IBM SkillsBuild Data Analytics with AI Internship")
