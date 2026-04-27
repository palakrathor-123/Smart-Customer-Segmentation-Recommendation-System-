import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(file):
    df = pd.read_csv(file)
    return df

def preprocess_data(df):
    features = df[['Annual Income (k$)', 'Spending Score (1-100)']]

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(features)

    return df, scaled_data