from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import silhouette_score

def apply_kmeans(data, n_clusters=5):
    model = KMeans(n_clusters=n_clusters, random_state=42)
    labels = model.fit_predict(data)

    score = silhouette_score(data, labels)

    return labels, score, model

def apply_dbscan(data):
    model = DBSCAN(eps=0.5, min_samples=5)
    labels = model.fit_predict(data)

    return labels, model