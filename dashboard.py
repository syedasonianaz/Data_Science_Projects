import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Churn Prediction App", page_icon=":chart_with_downwards_trend:", layout="wide")
st.title(" :chart_with_downwards_trend: Predict Customer Churn")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

fl = st.file_uploader(":file_folder: Upload a file", type=(["csv", "txt", "xlsx", "xls"]))

if fl is not None:
    df = pd.read_csv(fl, encoding="ISO-8859-1")
    st.write("Uploaded File Preview:")
    st.dataframe(df)

    if 'Churn' in df.columns:
        st.write("Unique values in 'Churn' column:", df['Churn'].unique())
    else:
        st.error("The dataset must contain a 'Churn' column.")
        st.stop()

    df['Churn'] = df['Churn'].replace({'Yes': 1, 'No': 0, True: 1, False: 0})
    df = df.dropna(subset=['Churn'])

    df['Churn'] = pd.to_numeric(df['Churn'], errors='coerce')

    df_churned = df[df['Churn'] == 1]
    df_not_churned = df[df['Churn'] == 0]

    categorical_cols = df.select_dtypes(include='object').columns.tolist()
    if categorical_cols:
        churn_status = st.radio("Select Customer Status", options=["Churned", "Not Churned"], horizontal=True)
        selected_col = st.selectbox("Select a Column for Pie Chart", options=categorical_cols)

        filtered_df = df_churned if churn_status == "Churned" else df_not_churned

        if not filtered_df[selected_col].dropna().value_counts().empty:
            # Add a slider for controlling pie chart size
            chart_size = st.slider(
                "Adjust Pie Chart Size", min_value=300, max_value=800, value=500, step=50
            )

            fig = px.pie(
                filtered_df,
                names=selected_col,
                title=f"{selected_col} Distribution ({churn_status})"
            )
            fig.update_traces(textposition='inside', textinfo='percent+label')
            fig.update_layout(
                width=chart_size,
                height=chart_size
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning(f"No valid data for '{selected_col}' in selected customer status.")
    else:
        st.warning("No categorical columns found in the dataset.")
else:
    st.info("Please upload a file to get started.")
