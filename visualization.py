import plotly.express as px
import pandas as pd

def cluster_scatter_plot(df):
    fig = px.scatter(
        df,
        x='Annual Income (k$)',
        y='Spending Score (1-100)',
        color='Cluster',
        title="Customer Segmentation"
    )
    return fig

def cluster_summary(df):
    summary = df.groupby("Cluster").agg({
        "CustomerID": "count",
        "Age": "mean",
        "Annual Income (k$)": "mean",
        "Spending Score (1-100)": "mean"
    }).reset_index()

    summary.columns = [
        "Cluster",
        "Customers",
        "Avg Age",
        "Avg Income",
        "Avg Spending Score"
    ]

    return summary