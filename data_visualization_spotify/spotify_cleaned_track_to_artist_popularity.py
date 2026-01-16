import pandas as pd
import matplotlib.pyplot as plt

# Load data
dataframe = pd.read_csv("data_visualization_spotify/spotify_data_clean.csv")

# This step will make a new dataframe that can aggregate songs by artist
new_df = pd.DataFrame({
    'track_popularity': dataframe['track_popularity'],
    'artist_popularity': dataframe['artist_popularity'],
    'artist_name': dataframe['artist_name'],
    'track_id': dataframe['track_id']
})

# This aggregates by artist, combining track popularities and artist 
# popularities into a harmonic mean 
artist_stats = new_df.groupby('artist_name').agg({
    'track_popularity': 'max',
    'artist_popularity': 'mean',
    'track_id': 'count'
})

# Filter out noise
# Take songs more popular than 0 and artists with more than 3 songs
cleaned_stats = artist_stats[
    (artist_stats['track_popularity'] > 0) & 
    (artist_stats['track_id'] > 1)
]

# Rename the column so they are easier to comprehend
# artist_stats = artist_stats.rename(columns={
#     'track_popularity': 'avg_track_pop',
#     'artist_popularity': 'avg_artist_pop'
# })

plt.figure()
plt.scatter(cleaned_stats['artist_popularity'], cleaned_stats['track_popularity'])
plt.title("Artist Popularity to Track Popularity (Using Cleaned Data)")
plt.xlabel("Artist Popularity")
plt.ylabel("Track Popularity")
plt.show()

