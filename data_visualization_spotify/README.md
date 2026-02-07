# Data Visualization for Spotify Global Music Data

This project explores the visualization of popular tracks and artists on Spotify between 2009-2025.

Our data source is from Kaggle.
https://www.kaggle.com/datasets/wardabilal/spotify-global-music-dataset-20092025

We used Python libraries, including pandas and matplotlib, to visualize trends in the data.

## Data

The raw data contains music tracks spanning 16 years from 2009 to 2025. 

There are 8582 unique track ids recorded, each accompanied with information over a wide range. For example, this includes:
* Track name
* Track popularity
* Whether the song is explicit or not
* The name of the song's artist
* That artist's popularity
* That artist's follower count (On Spotify)
* Artist genres


## Visualization

### Distribution of Track Genres

![Distribution of Track Genres](./graphs/spotify_distribution_genres.png)

I wanted to create a pie chart to try out another graph in matplotlib, but I found that there weren't many options for visualizing distribution of a whole. I could have done explicit songs to non explicit songs as percentages, but that seemed a little easy. So, I decided to challenge myself and try visualizing the distribution of genres instead.

There were many roadblocks I faced. 
* First, I studied the data, and noticed that the selection of genres was very diverse, ranging from broad categories such as pop to extremely niche ones such as southern gothic. It wouldn't make sense to create a pie chart with every single genre, as it would be illegible.
* Second, many songs had multiple genres each. Adding them all would result in a cumulative total percentage greater than 100, so I had to figure out how to evenly distribute the weight.
* Third, the format for the artist_genre's column seemed to list genres as a string, meaning that I had to parse the genres into a list
* Finally, there were likely to be many unknown categories, such as ones that can't be classified into large chunks, or tracks that were originally listed as N/A in the genre column

So, I had to approach these problems individually
* For the issue of diverse genres, I decided it was best to create a genre category map that could list out the broad categories with keywords within them that could identify which song belonged where.
* For the songs with multiple genres, it firstly didn't make sense to only choose one of the listed genres. Then, I found all the matching genres to the ones listed under the song, and split the weight evenly among all the matches
* I chose to parse the string into a list by using the .split() function, which separates the string by commas
* The last one was tricky. I made all of the unknowns into a separate category, and removed them at the end. During the troubleshooting process, there were many genre keywords that couldn't be categorized, so I extracted them and used AI to do a classification on the major categories, which is what created the genre map. 

After I successfully produced the pie chart, I found that there were some categories that were very small, and wasn't very readable. So, I collapsed them into the "Other" category, making the visualization more presentable.

Looking at the visualization, it seems that Pop is the most popular category by far, followed by Rock, Hip-hop, and country. Pop is an extremely broad category, which includes many sub-genres such as Indie pop or Synth pop, making it look larger in comparison to the others. However, this data can also be attributed to the fact that Major record labels invest the most into Pop and Hip-hop production as it does well in media and with the younger audience. 

### Artist Popularity to Followers

![Artist Popularity to Followers](./graphs/spotify_artist_popularity_to_followers.png)

This was another scatter plot I did, which visualizes the relationship between an artists poularity to their follower count. 

I visualized raw data multiple times, using different ceiling numbers to control the range of follower counts. This was because there were likely 5-10 artists that had extremely high follower counts compared to the rest, which skewed the data. However, no matter which ceiling number I used, there was always an exponential relationship between the two values, which indicates that as an artist grows more popular, their follower count grows exponentially. 

In order to confirm this relationship of exponential growth, I decided to apply a Log Transformation for the follower count, and produced a second graph. 

![Artist Popularity to Logarithm of Followers](./graphs/spotify_artist_popularity_to_logarithm_followers.png)

This is the graph that shows the Log Transformation on the follower count. The relationship has turned from exponential to linear, confirming the exponential relationship between the two metrics.  

### Music Popularity Trend

![Music Popularity By Year](./graphs/spotify_music_popularity_by_year.png)

This was the second visualization. This visualization was more difficult than the last; I wanted to choose a line graph, as well as a more complex prompt that could showcase trends instead of plain statistics. 

Initially, I wanted to model the popularity of different genres over time, but my approach found that the genres listed in the datafile were so diverse that the visualization could not showcase any trends. For example, one song was labeled under the genre 'neo-psychedelic', while I was looking for general categories such as pop or 90's rap. 

Thus, I decided to switch the prompt, and then chose average track popularity over time, in which I could change the label to something quantifiable. I found that choosing the mean instead of the sum of track popularities would better fit because the number of tracks per year varied. 

The next challenge I encountered was that the data needed to be cleaned. The release date was put in terms of year-month-day, but I only needed the year for my data. I learned that I could use a function to convert the string to a datatime type that could extract the year. 

The graph shows an increase in average track popularity from the 1950s to the 1980s, peaking around 1983 at a popularity of about 80. Then, it dropped in the early 1990s, and later stabilized at around 50-55 in the later years. This means that 80's music was generally more popular and there were very popular artists at the time. For example, popular 80s artists include Michael Jackson, Whitney Houston, and Madonna, who are all incredibly influential in the music industry.

### Track to Artist Popularity

![Track to Artist Popularity](./graphs/spotify_track_to_artist_popularity.png)

This was the next visualization I did, which was a scatter plot. I chose to visualize the relationship between Track Popularity to Artist popularity, in order to see if the popularity of an artist always affects the popularity of their work. 

The Graph shows that there is mostly a positive correlation between the two, indicating that artist popularity does indeed affect track popularity. However, there is also a string of points along the bottom, which shows that even for popular artists, not all of their tracks become popular. 

However, this graph is difficult to interpret in a couple of ways. 
* The graph is unappealing in that roughly half of the white space is covered in dots. Thus, it is hard to tell what the actual distribution of data looks like. This is likely because many artists have multiple songs each, resulting in an abundance of values.
* There is a long string of values where the track popularity is equal to zero. This must mean that the track popularity data is missing data or has unreliable data, such as missing track values or artists that post songs that barely receive any traction.
* This results in a graph that cannot show strong correlation

Thus, I needed to find a way to clean the data, which would include reducing the amount of values as well as unnecessary noise. Looking closer into the data, I eventually produced another graph. 

![Track to Artist Popularity with Cleaned Data](./graphs/spotify_cleaned_track_to_artist_popularity.png)

This graph solves the problem in the first graph in a few ways. 
* Firstly, I created a new dataframe that aggregated track popularity by its maximum value, grouping the resulting values by artist.
* Next, in the new dataframe, I counted the number of track ids, also grouped by artists.
* Finally, I cleaned out extraneous data by only taking tracks with a popularity greater than zero and artists who had two or more songs. This significantly reduced the number of data values as well as noise.

Finally, the graph is interepretable. The scatter plot shows that artist popularity and track popularity have a strong positive correlation, meaning that as an artist becomes more popular, the songs they produce naturally will as well. 

From this experience, I learned a couple things. The first was how to aggregate multiple columns using the groupby() method, which will take values in groups and not the entire column as I did previously. The second thing was the general process of data cleaning by taking constraints that limit unnecessary or unhelpful data. 

### Top 10 Popular Tracks

![Track Popularity](./graphs/spotify_top_tracks.png)

This was the first visualization that I did. 
For starters, I was unfamiliar with the python libraries--pandas and matplotlib. I started with a simple bar graph that has straightforward metrics. These metrics included the track popularity and track name. 

While doing this project, I learned about the basics of data visualization. For example, I firstmost learned what a datafile was, as well as how to sort the data file. I learned simply how to graph using matplotlib, along with using .head() to taken on the first ten values. 