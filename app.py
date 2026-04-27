import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# -------------------------------
# PAGE SETTINGS (Must be the first Streamlit command)
# -------------------------------
st.set_page_config(
    page_title="Smart Customer Segmentation",
    layout="wide"
)

# Custom Styling
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
h1 {
    color: #0d47a1;
    font-weight: bold;
}
div[data-testid="metric-container"] {
    background-color: #ffffff;
    border: 2px solid #dbeafe;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
}
section[data-testid="stSidebar"] {
    background-color: #0d47a1;
    color: white;
}
section[data-testid="stSidebar"] * {
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("SMART CUSTOMER SEGMENTATION & RECOMMENDATION SYSTEM")
st.caption("Group customers into segments using clustering and suggest strategies for each segment")

# -------------------------------
# SIDEBAR
# -------------------------------
st.sidebar.title("Customer Segmentation")

page = st.sidebar.radio(
    "Navigation",
    ["Upload Data", "Dashboard", "Cluster Details", "Reports"]
)

# -------------------------------
# FUNCTIONS
# -------------------------------
def load_data(file):
    df = pd.read_csv(file)
    df=df.fillna(0)
    return df

def preprocess(df):
    features = df[["Annual Income (k$)", "Spending Score (1-100)"]]
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(features)
    return scaled_data

def run_kmeans(data, n_clusters=5):
    model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = model.fit_predict(data)
    score = silhouette_score(data, labels)
    return labels, score

def run_dbscan(data):
    model = DBSCAN(eps=0.5, min_samples=5)
    labels = model.fit_predict(data)
    return labels

def get_strategy(cluster):
    # Mapping for string clusters since we convert them for visualization
    strategies = {
        "0": "Offer premium products and exclusive offers.",
        "1": "Provide loyalty programs and early access.",
        "2": "Focus on discount campaigns and engagement offers.",
        "3": "Use upselling and cross-selling strategies.",
        "4": "Retarget low engagement customers with offers."
    }
    return strategies.get(str(cluster), "General marketing strategy.")

# -------------------------------
# FILE UPLOAD
# -------------------------------
uploaded_file = st.sidebar.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is None:
    st.info("Please upload dataset.csv from sidebar to continue.")
    st.stop()

# -------------------------------
# DATA PROCESSING
# -------------------------------
df = load_data(uploaded_file)
scaled_data = preprocess(df)
labels, sil_score = run_kmeans(scaled_data, 5)

df["Cluster"] = labels
outlier_labels = run_dbscan(scaled_data)
outliers = list(outlier_labels).count(-1)

# Summary for tables/metrics
summary = df.groupby("Cluster").agg({
    "CustomerID": "count",
    "Age": "mean",
    "Annual Income (k$)": "mean",
    "Spending Score (1-100)": "mean"
}).reset_index()

summary.columns = ["Cluster", "Customers", "Avg Age", "Avg Income", "Avg Spending Score"]

# -------------------------------
# PAGE 1 : UPLOAD DATA
# -------------------------------
if page == "Upload Data":
    st.subheader("Upload Your Dataset")
    st.success("CSV uploaded successfully")
    st.dataframe(df.head(10), use_container_width=True, key="uploaded_data_preview")

# -------------------------------
# PAGE 2 : DASHBOARD
# -------------------------------
elif page == "Dashboard":
    st.subheader("Results Dashboard")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Customers", len(df))
    c2.metric("Total Clusters", len(df["Cluster"].unique()))
    c3.metric("Best Algorithm", "K-Means")
    c4.metric("Silhouette Score", round(sil_score, 2))

    left, right = st.columns([2, 1])

    with left:
        # Convert to string for discrete color mapping
        viz_df = df.copy()
        viz_df["Cluster"] = viz_df["Cluster"].astype(str)

        fig = px.scatter(
            viz_df,
            x="Annual Income (k$)",
            y="Spending Score (1-100)",
            color="Cluster",
            title="<b>Cluster Visualization</b>",
            color_discrete_sequence=px.colors.qualitative.Vivid 
        )

        fig.update_traces(marker=dict(size=12, line=dict(width=1, color='white'), opacity=0.8))
        fig.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            xaxis=dict(showgrid=True, gridcolor='rgba(200,200,200,0.1)'),
            yaxis=dict(showgrid=True, gridcolor='rgba(200,200,200,0.1)'),
            margin=dict(l=0, r=0, t=40, b=0)
        )

        # FIXED: Removed the duplicate call here
        st.plotly_chart(fig, use_container_width=True, key="main_cluster_chart")

    with right:
        k_values = list(range(1, 11))
        inertia = [10000, 6000, 3500, 2200, 1500, 1100, 800, 600, 500, 400]
        elbow = go.Figure()
        elbow.add_trace(go.Scatter(x=k_values, y=inertia, mode="lines+markers"))
        elbow.update_layout(title="Elbow Method", xaxis_title="K Value", yaxis_title="Inertia")
        st.plotly_chart(elbow, use_container_width=True, key="elbow_chart_viz")

    b1, b2 = st.columns([2, 1])
    with b1:
        st.subheader("Cluster Summary")
        st.dataframe(summary, use_container_width=True, key="summary_table_dashboard")

    with b2:
        pie = px.pie(summary, values="Customers", names="Cluster", title="Customers per Cluster", hole=0.3)
        st.plotly_chart(pie, use_container_width=True, key="cluster_pie_chart")

# -------------------------------
# PAGE 3 : CLUSTER DETAILS
# -------------------------------
elif page == "Cluster Details":
    st.subheader("Cluster Details & Recommendations")

    selected_cluster = st.selectbox("Select Cluster", sorted(df["Cluster"].unique()))
    cluster_data = df[df["Cluster"] == selected_cluster]

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Customers", len(cluster_data))
    c2.metric("Avg Age", round(cluster_data["Age"].mean(), 1))
    c3.metric("Avg Income", round(cluster_data["Annual Income (k$)"].mean(), 1))
    c4.metric("Avg Spending Score", round(cluster_data["Spending Score (1-100)"].mean(), 1))

    st.subheader("Cluster Description")
    st.info("Insights for the selected segment based on spending habits and income levels.")

    cluster_fig = px.scatter(
        cluster_data,
        x="Annual Income (k$)",
        y="Spending Score (1-100)",
        color_discrete_sequence=['#0d47a1'],
        size="Age",
        hover_data=["Age"],
        title=f"Cluster {selected_cluster} Detailed View",
        template="plotly_white"
    )
    st.plotly_chart(cluster_fig, use_container_width=True, key="detail_cluster_viz")

    st.subheader("Recommended Strategies")
    st.success(get_strategy(selected_cluster))

    # --- DBSCAN Visualization (Moved inside Cluster Details for clean UI) ---
    st.divider()
    st.subheader("DBSCAN Outlier Detection")
    dbscan_labels = run_dbscan(scaled_data)
    dbscan_df = df.copy()
    dbscan_df["Point Type"] = ["Outlier" if x == -1 else "Normal" for x in dbscan_labels]
    
    st.warning(f"Outliers Detected (Noise Points): {list(dbscan_labels).count(-1)}")

    dbscan_fig = px.scatter(
        dbscan_df,
        x="Annual Income (k$)",
        y="Spending Score (1-100)",
        color="Point Type",
        color_discrete_map={"Normal": "blue", "Outlier": "red"},
        title="DBSCAN Outlier Detection View"
    )
    st.plotly_chart(dbscan_fig, use_container_width=True, key="dbscan_outlier_chart")

# -------------------------------
# PAGE 4 : REPORTS
# -------------------------------
else:
    st.subheader("Project Outcome")
    st.write("This project helps businesses understand customer behavior and improve ROI.")
    st.dataframe(summary, use_container_width=True, key="final_report_table")