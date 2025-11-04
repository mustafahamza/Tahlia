
import streamlit as st
import pandas as pd
import altair as alt

# Load data
df = pd.read_csv("tahlia_data.csv")

# Page config
st.set_page_config(page_title="Feasibility Dashboard – Tahlia Road", layout="wide")

# Language selector
language = st.radio("Language / اللغة", ["English", "العربية"], horizontal=True)

if language == "English":
    st.title("Feasibility Dashboard – Tahlia Road Project")
    st.markdown("Comparative analysis of investment alternatives.")

    # KPIs
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    col1.metric("Total Investment", "SAR 40.9M")
    col2.metric("NOI", "SAR 3.23M")
    col3.metric("ROI", "7.9%")
    col4.metric("IRR", "11.5%")
    col5.metric("Payback", "8–9 Years")
    col6.metric("Risk", "Medium")

    st.markdown("---")

    # Chart
    chart = (
        alt.Chart(df)
        .mark_bar(cornerRadiusTopLeft=5, cornerRadiusTopRight=5)
        .encode(
            x=alt.X("ROI (%)", title="ROI (%)"),
            y=alt.Y("Type", sort="-x"),
            color=alt.Color("Type", legend=None),
            tooltip=["Type", "ROI (%)", "IRR (%)", "Payback (Years)"],
        )
        .properties(height=300)
    )
    st.altair_chart(chart, use_container_width=True)

    # Table
    st.markdown("### Detailed Comparison")
    st.dataframe(df, use_container_width=True)
    st.caption("Feasibility indicators based on 2025 study of Tahlia Road, Jeddah.")

else:
    st.markdown("<div dir='rtl'>", unsafe_allow_html=True)
    st.title("لوحة الجدوى – طريق التحلية")
    st.markdown("تحليل مقارن لبدائل الاستثمار.")

    # KPIs in Arabic
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    col1.metric("إجمالي الاستثمار", "SAR 40.9M")
    col2.metric("صافي الدخل", "SAR 3.23M")
    col3.metric("العائد على الاستثمار", "7.9%")
    col4.metric("معدل العائد الداخلي", "11.5%")
    col5.metric("فترة الاسترداد", "8–9 سنوات")
    col6.metric("المخاطر", "متوسطة")

    st.markdown("---")

    # Chart RTL
    chart = (
        alt.Chart(df)
        .mark_bar(cornerRadiusTopLeft=5, cornerRadiusTopRight=5)
        .encode(
            x=alt.X("ROI (%)", title="العائد على الاستثمار (%)"),
            y=alt.Y("Type", sort="-x"),
            color=alt.Color("Type", legend=None),
            tooltip=["Type", "ROI (%)", "IRR (%)", "Payback (Years)"],
        )
        .properties(height=300)
    )
    st.altair_chart(chart, use_container_width=True)

    # Table
    st.markdown("### مقارنة تفصيلية")
    st.dataframe(df, use_container_width=True)
    st.caption("مؤشرات الجدوى بناءً على دراسة عام 2025 لطريق التحلية بجدة.")
    st.markdown("</div>", unsafe_allow_html=True)
