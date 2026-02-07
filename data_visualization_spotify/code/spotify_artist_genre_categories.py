import pandas as pandas
import ast 
import matplotlib.pyplot as plt
from collections import Counter

# Load the dataset
df = pandas.read_csv('data_visualization_spotify/data/spotify_data_clean.csv')

# Parse the artist_genres column
def parse_genres(row):
    # Access specific columns from that row
    genre_str = row['artist_genres']
    track_name = row['track_name'] # Example of a second column

    if pandas.isna(genre_str) or genre_str == 'N/A' or str(genre_str).strip() == '':
        print(f"Unknown: {genre_str}, Track: {track_name}")
        return []

    try:
        cleaned_str = str(genre_str).strip()
        genre_list = cleaned_str.split(',')
        # Final Cleanup
        # Trim whitespace from each genre and remove empty results
        return [g.strip() for g in genre_list if g.strip()]
    except Exception as e:
        print(f"Exception: {e} | Value: {genre_str}")
        return []

# dataframe.apply() allows apply a function to each row of the dataframe.
# To apply a function to a column, use df['column'].apply().
df['parsed_genres'] = df.apply(parse_genres, axis=1)

# Define a genre_map to map a genra to a category.
# After producing the graph, some categories are very small, comment them
# out from the pie chart.
genre_map = {
    'Pop': ['pop', 'disco', 'boy band', 'indie', 'anime'],
    'Hip-Hop/Rap': ['hip hop', 'rap', 'trap', 'drill', 'hop', 'phonk'],
    'Rock': ['rock', 'metal', 'punk', 'grunge', 'riot grrrl', 'southern gothic'],
    'Electronic/Dance': ['edm', 'house', 'techno', 'electro', 'dance', 'moombahton', 'synthwave', 'future bass', 'nightcore', 'jersey club', 'electronic'],
    'R&B/Soul': ['r&b', 'soul', 'funk'],
    'Country/Folk': ['country', 'folk', 'bluegrass', 'sea shanties', 'medieval', 'gnawa'],
    'Soundtrack': ['soundtrack', 'musicals'],
    # 'Latin': ['latin', 'reggaeton', 'bachata'],
    # 'Jazz/Classical': ['jazz', 'classical', 'orchestra'],
    # 'Holiday': ['christmas', 'holiday'],
}

no_match_count = 0

# This function takes the genres of a song, then returns a map with
# each matching category and its corresponding weight
def get_genre_weights(genres):
    global no_match_count

    if not genres:
        return {"Unknown": 1.0}
    
    genre_str = " ".join(genres).lower()
    matches = []
 
    # Check for matches
    for category, keywords in genre_map.items():
        for keyword in keywords:
            if (keyword in genre_str):
                matches.append(category)
    
    if not matches:
        print(f"[{str(no_match_count)}] No match: {genres}")
        no_match_count += 1
        return {'Other': 1.0}
    
    # Split weight
    weight_per_match = 1.0 / len(matches)
    return {cat: weight_per_match for cat in matches}

# Apply function to create a weight dictionary
weights_list = df['parsed_genres'].apply(get_genre_weights)

# Aggregate weights into a total
# The total_distribution is a map of category to count, each weight_dict
# is also a map of category to count. By updating weight_dict to
# total_distribution, it aggregates the count for each category.
total_distribution = Counter()
for weight_dict in weights_list:
    total_distribution.update(weight_dict)

# Removes the "N/A" genras (parsed as "Unknown")
total_distribution.pop('Unknown', None)

# Covert to a Series
genre_counts = pandas.Series(total_distribution).sort_values(ascending=False)

# Plot the Pie chart
genre_counts.plot(
    kind='pie', 
    autopct='%1.1f%%', 
    startangle=90, 
    figsize=(10, 10),
    colors=plt.cm.Paired.colors # Gives it a nice variety of colors
)

# Add a title
plt.title('Consolidated Artist Genre Distribution (Weighted)')

# Clean up the look
plt.ylabel('') # Hides the 'None' label on the side
plt.show()