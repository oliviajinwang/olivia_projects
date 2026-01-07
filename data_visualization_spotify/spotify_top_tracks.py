import pandas as pd
import matplotlib.pyplot as plt

# Load data
datafile = pd.read_csv("data_visualization_spotify/spotify_data_clean.csv")

sort_column = 'track_popularity'
ascending_order = False
datafile.sort_values(
    by=sort_column,
    ascending=ascending_order,
    inplace=True
)

# Quick sanity check
print(datafile.head())
print(datafile.info())

# Example 1: Bar chart (top 10 categories)
top_tracks = datafile[['track_popularity', 'track_name']].head(10)
print("First 10 Rows:\n", top_tracks)

plt.figure()
top_tracks.plot.bar(
    x='track_name',
    y='track_popularity',
    title='Top 10 Popular Tracks recently'
)
plt.title("Top 10 Popular Tracks between 2009-2025")
plt.xlabel("Track")
plt.ylabel("Popularity")
plt.xticks(rotation=45,ha='right')
plt.tight_layout()
plt.show()
