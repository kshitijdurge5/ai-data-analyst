import pandas as pd
import streamlit as st
from portfolio_visuals import render_visuals
def profile_csv(file) -> dict:
    df = pd.read_csv(file)
    return {"rows": int(len(df)), "columns": int(len(df.columns)), "missing": df.isna().sum().to_dict(),
            "numeric_summary": df.describe().round(2).to_dict(), "column_names": list(df.columns)}

st.set_page_config(page_title="AI Data Analyst", page_icon="ðŸ“Š")
render_visuals('03_ai_data_analyst')
st.title("AI Data Analyst")
st.caption("Deterministic data profiling MVP; no LLM-generated calculations.")
upload = st.file_uploader("Upload a CSV", type=["csv"])
if upload:
    try:
        df = pd.read_csv(upload)
        st.write({"rows": len(df), "columns": len(df.columns)})
        st.dataframe(df.head(100), use_container_width=True)
        st.subheader("Missing values")
        st.dataframe(df.isna().sum().rename("missing_count"))
        numeric = df.select_dtypes(include="number")
        if not numeric.empty:
            st.subheader("Numeric summary")
            st.dataframe(numeric.describe().T)
            col = st.selectbox("Chart column", list(numeric.columns))
            st.bar_chart(df[col].dropna().head(100))
        st.download_button("Download profile CSV", df.describe(include="all").T.to_csv(), "data_profile.csv", "text/csv")
    except Exception as e:
        st.error(f"Could not read CSV: {e}")

