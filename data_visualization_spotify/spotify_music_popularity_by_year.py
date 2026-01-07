import pandas as pd
import matplotlib.pyplot as plt

# Load data
datafile = pd.read_csv("data_visualization_spotify/spotify_data_clean.csv")
df = pd.DataFrame(datafile)

# This step converts the given column, album_release_date, which holds strings, 
# to a datetime Type that carries a variable for the year, month, and day
df['album_release_date'] = pd.to_datetime(df['album_release_date'], errors='coerce')

# This step extracts the year and popularity by assigning them to new columns in the new dataframe
new_df = pd.DataFrame({
    'year': df['album_release_date'].dt.year,
    'popularity': df['track_popularity']
})

# This step will remove rows where the year couldn't be parsed
new_df = new_df.dropna(subset=['year'])

# This step converts the year to an integer
new_df['year'] = new_df['year'].astype(int)

popularity_by_year = new_df.groupby('year')['popularity'].mean()

plt.figure()
plt.plot(popularity_by_year.index, popularity_by_year.values)
plt.title("Average Track Popularity Over Time")
plt.xlabel("Year")
plt.ylabel("Popularity")
plt.show()
