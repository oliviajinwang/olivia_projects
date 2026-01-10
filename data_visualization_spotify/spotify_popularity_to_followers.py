import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
dataframe = pd.read_csv("data_visualization_spotify/spotify_data_clean.csv")

# Alternative file load path.
# datafram = pd.read_csv("D:/Olivia/GitHub/olivia_projects/data_visualization_spotify/spotify_data_clean.csv")

# Quick sanity check
print(dataframe.head())
print(dataframe.info())

followers_filtered = dataframe[dataframe['artist_followers'] < 150000000]

# Applying Log Transformation, turning exponential growth into a linear relationship
followers_filtered['log_followers'] = np.log10(followers_filtered['artist_followers'])

plt.figure()

# Uses Log followers to plot
plt.scatter(followers_filtered['artist_popularity'], followers_filtered['log_followers'])

# Alternative Plot Method
# plt.scatter(followers_filtered['artist_popularity'], followers_filtered['artist_followers'])
plt.title("Artist Popularity to Logarithm of Artist Followers")
plt.xlabel("Artist Popularity")
plt.ylabel("Logarithm of Artist Followers")
plt.show()

