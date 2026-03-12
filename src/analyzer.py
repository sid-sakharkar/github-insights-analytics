def calculate_statistics(data):
    """Calculate basic statistics such as mean, median, and mode."""
    from statistics import mean, median, mode
    return {
        'mean': mean(data),
        'median': median(data),
        'mode': mode(data)
    }


def trend_analysis(data):
    """Analyze trends over time in the given data."""
    import matplotlib.pyplot as plt
    plt.plot(data)
    plt.title('Trend Analysis')
    plt.xlabel('Time')
    plt.ylabel('Values')
    plt.show()


def perform_clustering(data):
    """Perform clustering on the data using KMeans."""
    from sklearn.cluster import KMeans
    import numpy as np
    data = np.array(data).reshape(-1, 1)  # Reshape for KMeans
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(data)
    return kmeans.labels_


def make_predictions(data):
    """Make predictions based on historical data using a simple linear regression."""
    from sklearn.linear_model import LinearRegression
    import numpy as np
    X = np.array(range(len(data))).reshape(-1, 1)
    y = np.array(data)
    model = LinearRegression()
    model.fit(X, y)
    return model.predict(X)
