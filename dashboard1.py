
# # # st.sidebar.header("Filters & Controls")
# # import streamlit as st
# # import sqlite3
# # import pandas as pd

# # # Use the correct full path to your DB file
# # conn = sqlite3.connect(r"D:\rangam exports\raagamexports1.db")

# # # Load data
# # @st.cache_data
# # def load_data():
# #     query = "SELECT * FROM Received_Orders"
# #     return pd.read_sql_query(query, conn)

# # df = load_data()

# # # Page configuration
# # st.set_page_config(page_title="📦 Received Orders Dashboard", layout="wide")
# # st.title("📈 Raagam Exports - Orders Dashboard")

# # if df.empty:
# #     st.warning("No data found in Received_Orders table.")
# # else:
# #     # Convert date columns
# #     df['Received Dt'] = pd.to_datetime(df['Received Dt'], errors='coerce')
# #     df['Delivery Dt'] = pd.to_datetime(df['Delivery Dt'], errors='coerce')

# #     # ✅ Convert value columns to numeric
# #     df['FGN Value'] = pd.to_numeric(df['FGN Value'], errors='coerce')
# #     df['INR Value'] = (
# #     df['INR Value']
# #     .astype(str)
# #     .str.replace(',', '', regex=False)      # Remove commas
# #     .str.replace('₹', '', regex=False)      # Remove currency symbol
# #     .str.strip()                            # Remove spaces
# # )
# #     df['INR Value'] = pd.to_numeric(df['INR Value'], errors='coerce')
 
# #     # Sidebar filters
# #     with st.sidebar:
# #         st.header("🔍 Filters")

# #         order_filter = st.text_input("Search Order No")
# #         currency_filter = st.selectbox("Select Currency", ["All"] + sorted(df['Currency '].dropna().unique().tolist()))

# #         date_range = st.date_input("Select Received Date Range", [])
# #         if len(date_range) == 2:
# #             df = df[(df['Received Dt'] >= pd.to_datetime(date_range[0])) &
# #                     (df['Received Dt'] <= pd.to_datetime(date_range[1]))]

# #         if order_filter:
# #             df = df[df['Order No'].astype(str).str.contains(order_filter)]

# #         if currency_filter != "All":
# #             df = df[df['Currency '] == currency_filter]

# #     # Summary metrics
# #     st.subheader("📊 Summary")
# #     col1, col2, col3 = st.columns(3)
# #     col1.metric("🧾 Total Orders", len(df))
# #     col2.metric("💸 Total FGN Value", f"{df['FGN Value'].sum():,.2f}")
# #     col3.metric("₹ Total INR Value", f"{df['INR Value'].sum():,.2f}")

# #     # INR Value by Currency
# #     st.subheader("📦 INR Value by Currency")
# #     currency_chart = df.groupby("Currency ")["INR Value"].sum().reset_index()
# #     st.bar_chart(currency_chart.set_index("Currency "))

# #     # 🔝 Top 5 Orders by INR Value
# #     st.subheader("🔝 Top 5 Orders by INR Value")
# #     top5 = df[['Order No', 'INR Value']].sort_values(by='INR Value', ascending=False).head(5)
# #     st.table(top5.reset_index(drop=True))

# #     # 📈 Monthly Trends
# #     st.subheader("📆 Monthly Order Trend (INR Value)")
# #     df['Month'] = df['Received Dt'].dt.to_period('M').astype(str)
# #     monthly_trend = df.groupby('Month')['INR Value'].sum().reset_index()
# #     st.line_chart(monthly_trend.set_index('Month'))

# #     # Filtered Data Table (optional)
# #     with st.expander("📋 View Filtered Data"):
# #         st.dataframe(df, use_container_width=True)

# # # Close database connection
# # conn.close()
# import streamlit as st
# import sqlite3
# import pandas as pd

# # Page config
# st.set_page_config(page_title="📦 Raagam Exports Dashboard", layout="wide")

# # Sidebar navigation
# st.sidebar.title("🔍 Navigation")
# page = st.sidebar.radio("Go to", ["Received Orders", "Pending Orders"])

# # Database connection
# conn = sqlite3.connect(r"D:\rangam exports\raagamexports1.db")

# # 📦 RECEIVED ORDERS DASHBOARD
# if page == "Received Orders":
#     st.title("📈 Raagam Exports - Received Orders Dashboard")

#     @st.cache_data
#     def load_received_data():
#         query = "SELECT * FROM Received_Orders"
#         return pd.read_sql_query(query, conn)

#     df = load_received_data()

#     if df.empty:
#         st.warning("No data found in Received_Orders table.")
#     else:
#         # Convert columns
#         df['Received Dt'] = pd.to_datetime(df['Received Dt'], errors='coerce')
#         df['Delivery Dt'] = pd.to_datetime(df['Delivery Dt'], errors='coerce')
#         df['FGN Value'] = pd.to_numeric(df['FGN Value'], errors='coerce')
#         df['INR Value'] = (
#             df['INR Value'].astype(str)
#             .str.replace(',', '', regex=False)
#             .str.replace('₹', '', regex=False)
#             .str.strip()
#         )
#         df['INR Value'] = pd.to_numeric(df['INR Value'], errors='coerce')

#         # Sidebar filters
#         st.sidebar.header("📦 Received Orders Filters")
#         order_filter = st.sidebar.text_input("Search Order No")
#         currency_filter = st.sidebar.selectbox("Select Currency", ["All"] + sorted(df['Currency '].dropna().unique().tolist()))
#         date_range = st.sidebar.date_input("Select Received Date Range", [])

#         if len(date_range) == 2:
#             df = df[(df['Received Dt'] >= pd.to_datetime(date_range[0])) &
#                     (df['Received Dt'] <= pd.to_datetime(date_range[1]))]

#         if order_filter:
#             df = df[df['Order No'].astype(str).str.contains(order_filter)]

#         if currency_filter != "All":
#             df = df[df['Currency '] == currency_filter]

#         # Metrics
#         st.subheader("📊 Summary")
#         col1, col2, col3 = st.columns(3)
#         col1.metric("🧾 Total Orders", len(df))
#         col2.metric("💸 Total FGN Value", f"{df['FGN Value'].sum():,.2f}")
#         col3.metric("₹ Total INR Value", f"{df['INR Value'].sum():,.2f}")

#         # INR Value by Currency
#         st.subheader("📦 INR Value by Currency")
#         currency_chart = df.groupby("Currency ")["INR Value"].sum().reset_index()
#         st.bar_chart(currency_chart.set_index("Currency "))

#         # Top 5
#         st.subheader("🔝 Top 5 Orders by INR Value")
#         top5 = df[['Order No', 'INR Value']].sort_values(by='INR Value', ascending=False).head(5)
#         st.table(top5.reset_index(drop=True))

#         # Monthly trend
#         st.subheader("📆 Monthly Order Trend (INR Value)")
#         df['Month'] = df['Received Dt'].dt.to_period('M').astype(str)
#         monthly_trend = df.groupby('Month')['INR Value'].sum().reset_index()
#         st.line_chart(monthly_trend.set_index('Month'))

#         # Optional data view
#         with st.expander("📋 View Filtered Data"):
#             st.dataframe(df, use_container_width=True)

# # 🕒 PENDING ORDERS DASHBOARD
# elif page == "Pending Orders":
#     st.title("🕒 Pending Orders Dashboard")

#     @st.cache_data
#     def load_pending_data():
#         query = "SELECT * FROM Pendingorders"
#         return pd.read_sql_query(query, conn)

#     pending_df = load_pending_data()

#     # SC No input
#     scno_input = st.text_input("🔍 Enter SC No to Search Pending Orders")

#     if scno_input:
#         result = pending_df[pending_df['SC No'].astype(str).str.contains(scno_input, case=False)]
        
#         if not result.empty:
#             st.success(f"Found {len(result)} pending order(s) for SC No: {scno_input}")
#             st.dataframe(result, use_container_width=True)
#         else:
#             st.warning("No pending orders found for the given SC No.")
#     else:
#         st.info("Enter an SC No to see pending order details.")

# # Close DB connection
# conn.close()
import streamlit as st
import sqlite3
import pandas as pd
import time

# Page config
st.set_page_config(page_title="📦 Raagam Exports Dashboard", layout="wide")

# Sidebar navigation
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Go to", ["Received Orders", "Pending Orders", "Fabric Orders"])

# Database connection
conn = sqlite3.connect(r"D:\rangam exports\raagamexports1.db")

# 📦 RECEIVED ORDERS DASHBOARD
if page == "Received Orders":
    st.title("📈 Raagam Exports - Received Orders Dashboard")

    @st.cache_data(ttl=10)
    def load_received_data():
        query = "SELECT * FROM Received_Orders"
        return pd.read_sql_query(query, conn)
    
    if st.button("🔄 Refresh Dashboard"):
        st.cache_data.clear()
        st.success("✅ Dashboard successfully refreshed!")
        time.sleep(1.5)
        st.rerun()

    df = load_received_data()

    if df.empty:
        st.warning("No data found in Received_Orders table.")
    else:
        # Convert columns
        df['Received Dt'] = pd.to_datetime(df['Received Dt'], errors='coerce')
        df['Delivery Dt'] = pd.to_datetime(df['Delivery Dt'], errors='coerce')
        df['FGN Value'] = pd.to_numeric(df['FGN Value'], errors='coerce')
        df['INR Value'] = (
            df['INR Value'].astype(str)
            .str.replace(',', '', regex=False)
            .str.replace('₹', '', regex=False)
            .str.strip()
        )
        df['INR Value'] = pd.to_numeric(df['INR Value'], errors='coerce')

        # Sidebar filters
        st.sidebar.header("📦 Received Orders Filters")
        order_filter = st.sidebar.text_input("Search Order No")
        currency_filter = st.sidebar.selectbox("Select Currency", ["All"] + sorted(df['Currency '].dropna().unique().tolist()))
        date_range = st.sidebar.date_input("Select Received Date Range", [])

        if len(date_range) == 2:
            df = df[(df['Received Dt'] >= pd.to_datetime(date_range[0])) &
                    (df['Received Dt'] <= pd.to_datetime(date_range[1]))]

        if order_filter:
            df = df[df['Order No'].astype(str).str.contains(order_filter)]

        if currency_filter != "All":
            df = df[df['Currency '] == currency_filter]

        # Metrics
        st.subheader("📊 Summary")
        col1, col2, col3 = st.columns(3)
        col1.metric("🧾 Total Orders", len(df))
        col2.metric("💸 Total FGN Value", f"{df['FGN Value'].sum():,.2f}")
        col3.metric("₹ Total INR Value", f"{df['INR Value'].sum():,.2f}")

        # INR Value by Currency
        st.subheader("📦 INR Value by Currency")
        currency_chart = df.groupby("Currency ")["INR Value"].sum().reset_index()
        st.bar_chart(currency_chart.set_index("Currency "))

        # Top 5
        st.subheader("🔝 Top 5 Orders by INR Value")
        top5 = df[['Order No', 'INR Value']].sort_values(by='INR Value', ascending=False).head(5)
        st.table(top5.reset_index(drop=True))

        # Monthly trend
        st.subheader("📆 Monthly Order Trend (INR Value)")
        df['Month'] = df['Received Dt'].dt.to_period('M').astype(str)
        monthly_trend = df.groupby('Month')['INR Value'].sum().reset_index()
        st.line_chart(monthly_trend.set_index('Month'))

        # Optional data view
        with st.expander("📋 View Filtered Data"):
            st.dataframe(df, use_container_width=True)

# 🕒 PENDING ORDERS DASHBOARD
elif page == "Pending Orders":
    st.title("🕒 Raagam Exports - Pending Orders Dashboard")

    @st.cache_data(ttl=10)
    def load_pending_data():
        query = "SELECT * FROM Pendingorders"
        return pd.read_sql_query(query, conn)

    if st.button("🔄 Refresh Dashboard"):
        st.cache_data.clear()
        st.success("✅ Dashboard successfully refreshed!")
        time.sleep(1.5)
        st.rerun()
       

    pending_df = load_pending_data()
    pending_df.columns = pending_df.columns.str.strip()

    # SC No input
    scno_input = st.text_input("🔍 Enter SC No to Search Pending Orders")

    if scno_input:
        result = pending_df[pending_df['SCNo'].astype(str).str.contains(scno_input, case=False)]
        result.columns = result.columns.str.strip()


        if result.empty:
            st.warning("No pending orders found for the given SC No.")
        else:
            # Clean & Convert data
            numeric_cols = ['OrderQty', 'ShippedQty', 'BALQTY', 'INRValue', 'Price', 'FGNValue', 'ExRate']
            for col in numeric_cols:
                result[col] = pd.to_numeric(result[col], errors='coerce').fillna(0)

            # Quantity metrics
            total_order = result['OrderQty'].sum()
            shipped = result['ShippedQty'].sum()
            pending = result['BALQTY'].sum()
            shipped_pct = (shipped / total_order) * 100 if total_order > 0 else 0

            st.subheader("📦 Quantity Summary")
            c1, c2, c3 = st.columns(3)
            c1.metric("Total Order Qty", int(total_order))
            c2.metric("Shipped Qty", int(shipped), f"{shipped_pct:.1f}%")
            c3.metric("Pending Qty", int(pending))
            # Quantity Chart
            st.subheader("📊 Quantity Breakdown")
            q_chart = pd.DataFrame({
                "Type": ["Total Order", "Shipped", "Pending"],
                "Quantity": [total_order, shipped, pending]
            })
            st.bar_chart(q_chart.set_index("Type"))

            # Value Summary
            inr_total = result['INRValue'].sum()
            fgn_total = result['FGNValue'].sum()
            currency = result['Currency'].iloc[0] if 'Currency' in result.columns else 'Unknown'

            st.subheader("💰 Value Summary")
            v1, v2 = st.columns(2)
            v1.metric("🌍 Total FGN Value", f"{currency} {fgn_total:,.2f}")
            v2.metric("₹ Total INR Value", f"₹ {inr_total:,.2f}")

            # Profitability
            result['Converted INR'] = result['FGNValue'] * result['ExRate']
            converted_inr_total = result['Converted INR'].sum()
            estimated_cost = inr_total * 0.8
            profit = inr_total - estimated_cost
            profit_margin = (profit / inr_total) * 100 if inr_total > 0 else 0

            st.subheader("💹 Profitability Summary")
            p1, p2, p3 = st.columns(3)
            p1.metric("Converted INR", f"₹ {converted_inr_total:,.2f}")
            p2.metric("Estimated Cost (80%)", f"₹ {estimated_cost:,.2f}")
            p3.metric("Profit", f"₹ {profit:,.2f} ({profit_margin:.1f}%)")

            # Per-Unit Profit
            result['Unit INR'] = result['INRValue'] / result['ShippedQty'].replace(0, 1)
            result['Unit FGN'] = result['Price']
            result['Unit Profit (INR)'] = result['Unit INR'] - (result['Unit FGN'] * result['ExRate'])

            st.subheader("📌 Per-Unit Profit Analysis")
            st.dataframe(result[['SCNo', 'Unit INR', 'Unit FGN', 'ExRate', 'Unit Profit (INR)']], use_container_width=True)

            # Show filtered table
            st.subheader(f"📋 Filtered Pending Orders for SC No: {scno_input}")
            st.dataframe(result, use_container_width=True)

    # 🧵 FABRIC ORDERS DASHBOARD
elif page == "Fabric Orders":
    st.title("🧵 Raagam Exports - Fabric Orders Dashboard")

    @st.cache_data(ttl=10)
    def load_fabric_data():
        query = "SELECT * FROM Fabricorder"  # Make sure this matches your table name
        return pd.read_sql_query(query, conn)

    if st.button("🔄 Refresh Fabric Data"):
        st.cache_data.clear()
        st.success("✅ Fabric data refreshed!")
        time.sleep(1.5)
        st.rerun()

   

    fabric_df = load_fabric_data()
    fabric_df.columns = fabric_df.columns.str.strip()

    if fabric_df.empty:
        st.warning("No data found in FabricOrders table.")
    else:
        # Sidebar Filters
        st.sidebar.header("🎛️ Fabric Filters")
        scnos = st.sidebar.multiselect("Select SC No", fabric_df['SCNo'].dropna().unique())
        fabric_types = st.sidebar.multiselect("Select Fabric Type", fabric_df['FabricType'].dropna().unique())
        colors = st.sidebar.multiselect("Select Fabric Color", fabric_df['FabricColor'].dropna().unique())
        components = st.sidebar.multiselect("Select Component", fabric_df['Component'].dropna().unique())

        filtered = fabric_df.copy()
        if scnos:
            filtered = filtered[filtered['SCNo'].isin(scnos)]
        if fabric_types:
            filtered = filtered[filtered['FabricType'].isin(fabric_types)]
        if colors:
            filtered = filtered[filtered['FabricColor'].isin(colors)]
        if components:
            filtered = filtered[filtered['Component'].isin(components)]

        # 📊 Summary Metrics
        st.subheader("📊 Summary Metrics")
        col1, col2, col3 = st.columns(3)
        col1.metric("🔢 Unique SC Nos", filtered['SCNo'].nunique())
        col2.metric("🧵 Fabric Types", filtered['FabricType'].nunique())
        col3.metric("🎨 Fabric Colors", filtered['FabricColor'].nunique())

        # 🧶 Charts
        st.subheader("📦 Fabric Type Distribution")
        fabric_type_chart = filtered['FabricType'].value_counts().reset_index()
        fabric_type_chart.columns = ['FabricType', 'Count']
        st.bar_chart(fabric_type_chart.set_index('FabricType'))

        st.subheader("🎨 Top Fabric Colors")
        color_chart = filtered['FabricColor'].value_counts().head(10).reset_index()
        color_chart.columns = ['FabricColor', 'Count']
        st.bar_chart(color_chart.set_index('FabricColor'))

        st.subheader("🔧 Component Distribution")
        comp_chart = filtered['Component'].value_counts().reset_index()
        comp_chart.columns = ['Component', 'Count']
        st.bar_chart(comp_chart.set_index('Component'))

        # 🔍 Data Table
        with st.expander("📋 View Filtered Fabric Orders"):
            st.dataframe(filtered, use_container_width=True)

        # ⬇️ Download
        fabric_csv = filtered.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download CSV", fabric_csv, "filtered_fabric_orders.csv", "text/csv")

else:
        st.info("Enter an SC No to see pending order details.")

# Close connection
conn.close()
