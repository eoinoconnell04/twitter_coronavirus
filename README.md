# Coronavirus twitter analysis

In this project, I will work with a data set of all geotagged tweets from 2020, and generate some plots to analyze the data. Initially, the two things that I will analyze will be the number of mentions of "coronavirus" accross different languages, and also the distrubtion accross different countries.

## Mapping

The first step is mapping the data, which consists of running my mapping function on every day of the year. To do this, I create a script that uses glob on `/data/Twitter dataset/'geoTwitter20-*.zip` to get files for every day of the year, and then runs `map.py` on each of them. To run this normally would take a prohibitive amount of time, so the data is partitioned into many sections and mapped individually and concurrently.

## Reducing

After mapping, I need to combine all the data from all of the partitioned mapped files, and create a single file.

## Visualizing

Now that I have my data, I use matplotlib to create bar charts of the number of tweets in each category in order to compare values from different categories, and to see what the top 10 categories were for each graph.

Here we can see the charts that I created.

Here is a chart of the number of tweets with hashtag #coronavirus divided up by country, showing the top 10 countries from fewest to most tweets.
![alt text](https://github.com/eoinoconnell04/twitter_coronavirus/blob/master/coronavirus_country.png)

Here is a chart of the number of tweets with hashtag #coronavirus divided up by language, showing the top 10 languages from fewest to most tweets.
![alt text](https://github.com/eoinoconnell04/twitter_coronavirus/blob/master/coronavirus_lang.png)

Here is a chart of the number of tweets with hashtag #코로나바이러스 divided up by country, showing the top 10 countries from fewest to most tweets.
![alt text](https://github.com/eoinoconnell04/twitter_coronavirus/blob/master/korean_country.png)

Here is a chart of the number of tweets with hashtag #코로나바이러스 divided up by language, showing the top 10 languages from fewest to most tweets.
![alt text](https://github.com/eoinoconnell04/twitter_coronavirus/blob/master/korean_lang.png)
