import pandas as pd
import matplotlib.pyplot as plt

# Load data
dataframe = pd.read_csv("data_visualization_spotify/spotify_data_clean.csv")

# Quick sanity check
print(dataframe.head())
print(dataframe.info())

plt.figure()
plt.scatter(dataframe['artist_popularity'], dataframe['track_popularity'])
plt.title("Artist Popularity to Track Popularity")
plt.xlabel("Artist Popularity")
plt.ylabel("Track Popularity")
plt.show()

