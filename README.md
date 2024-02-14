# Coronavirus twitter analysis

In this project, I will work with a data set of all geotagged tweets from 2020, and generate some plots to analyze the data. Initially, the two things that I will analyze will be the number of mentions of "coronavirus" accross different languages, and also the distrubtion accross different countries. Then, I will create the framework to create charts with a wider range of hashtags to see their frequency over time.

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

We see that the majority of tweets with #coronavirus were written in english, with the second most in spanish, and the majority of these tweets originated within the United States, with the second most coming from India.


Here is a chart of the number of tweets with hashtag #코로나바이러스 divided up by country, showing the top 10 countries from fewest to most tweets.

![alt text](https://github.com/eoinoconnell04/twitter_coronavirus/blob/master/korean_country.png)



Here is a chart of the number of tweets with hashtag #코로나바이러스 divided up by language, showing the top 10 languages from fewest to most tweets.
![alt text](https://github.com/eoinoconnell04/twitter_coronavirus/blob/master/korean_lang.png)

As expected, we see that the vast majority of tweets with the coronavirus hashtag in korean came from within Korea, and we written in the Korean language.

# Alternative Reduce
Now, I will create a new file `alternative_reduce.py`, which combines elements from my previous reduce file, and my previous visualize file. This new file combines these two steps, taking a list of hashtags as arguments, reduces the mapped files, and then creates a bar chart which tracks the daily usage of each of the inputed hashtags over time.

First, I will plot the frequency of the #covid19 and #coronavirus hashtags over the course of the year, using my new file with the `./src/alternative_reduce.py --hashtags=#coronavirus,#covid19` command. Here, you can see that I can pass in a number of hashtags at once to plot them on the same chart. 

![alt text](https://github.com/eoinoconnell04/twitter_coronavirus/blob/master/coronavirus_covid19.png)

From this plot, we can see that the frequency of these two hashtags was very closely related, which makes sense as they represent the same thing so would be popular at the same time.

We can generate another plot to look at some other related hashtags:

![alt text](https://github.com/eoinoconnell04/twitter_coronavirus/blob/master/virus_doctor_covid-19_covid19.png)

From this, we see that nothing comes close to the frequency of the #covid19 hashtag, but there was a spike for #virus which coincided with the spike of #covid19. The other hashtags had relatively little usage throughout the year, excpet for a little spike of #doctor in July.
