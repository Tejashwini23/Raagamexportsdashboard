import streamlit as st
import pandas as pd
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")

st.set_page_config(page_title="Raagam Export Dashboard", layout="wide")
st.title("📊 Raagam Export Dashboard")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

# Upload all 3 Excel files
fabric_file = st.file_uploader("Upload Fabric Details", type=["xlsx", "xls"], key="fabric")
pending_file = st.file_uploader("Upload Pending Orders", type=["xlsx", "xls"], key="pending")
received_file = st.file_uploader("Upload Received Orders", type=["xlsx", "xls"], key="received")

# Dropdown for selecting which dataset to analyze
view_option = st.selectbox("Select Data View", 
                           ["Select an option", "📦 Fabric Details for Order", "⏳ Pending Orders Details", "✅ Received Orders Details"])

# Load files based on selection
if view_option == "📦 Fabric Details for Order" and fabric_file:
    df = pd.read_excel(fabric_file)
    df['Order Date'] = pd.to_datetime(df['Order Date'])

    st.subheader("📦 Fabric Orders Overview")
    st.dataframe(df)

    col1, col2 = st.columns(2)
    with col1:
        start_date = pd.to_datetime(st.date_input("Start Date", df['Order Date'].min()))
    with col2:
        end_date = pd.to_datetime(st.date_input("End Date", df['Order Date'].max()))

    filtered_df = df[(df['Order Date'] >= start_date) & (df['Order Date'] <= end_date)]
    
    st.bar_chart(filtered_df.groupby("Quality")["Order Quantity"].sum())
    st.subheader("Order Quantity by Colour")
    fig = px.pie(filtered_df, names='Colour', values='Order Quantity', title='Colour Distribution')
    st.plotly_chart(fig)

elif view_option == "⏳ Pending Orders Details" and pending_file:
    df = pd.read_excel(pending_file)
    df['Order Date'] = pd.to_datetime(df['Order Date'])

    st.subheader("⏳ Pending Orders Overview")
    st.dataframe(df)

    col1, col2 = st.columns(2)
    with col1:
        start_date = pd.to_datetime(st.date_input("Start Date", df['Order Date'].min(), key="start_pending"))
    with col2:
        end_date = pd.to_datetime(st.date_input("End Date", df['Order Date'].max(), key="end_pending"))

    filtered_df = df[(df['Order Date'] >= start_date) & (df['Order Date'] <= end_date)]
    
    st.bar_chart(filtered_df.groupby("Quality")["Pending Quantity"].sum())
    st.subheader("Pending Quantity by Color")
    fig = px.pie(filtered_df, names='Color', values='Pending Quantity', title='Color Distribution')
    st.plotly_chart(fig)

elif view_option == "✅ Received Orders Details" and received_file:
    df = pd.read_excel(received_file)
    df['Received Date'] = pd.to_datetime(df['Received Date'])

    st.subheader("✅ Received Orders Overview")
    st.dataframe(df)

    col1, col2 = st.columns(2)
    with col1:
        start_date = pd.to_datetime(st.date_input("Start Date", df['Received Date'].min(), key="start_received"))
    with col2:
        end_date = pd.to_datetime(st.date_input("End Date", df['Received Date'].max(), key="end_received"))

    filtered_df = df[(df['Received Date'] >= start_date) & (df['Received Date'] <= end_date)]

    st.line_chart(filtered_df.groupby("Received Date")["Received Quantity"].sum())
    st.subheader("Received Quantity by Challan No")
    fig = px.bar(filtered_df, x='Challan No', y='Received Quantity', color='Challan No')
    st.plotly_chart(fig)

elif view_option != "Select an option":
    st.warning("⚠️ Please upload the corresponding file for the selected view.")
