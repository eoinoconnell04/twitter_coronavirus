#!/usr/bin/env python3

# imports
import os
import json
from collections import Counter,defaultdict
import glob
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import datetime
import argparse


#function for argument parsing
def list_of_strings(arg):
    return arg.split(',')


# command line argument parsing
parser = argparse.ArgumentParser()
parser.add_argument('--hashtags',required=True,nargs='+', type=list_of_strings)
args = parser.parse_args()



#test if argument parsing worked
print(args.hashtags[0])


#find all paths to mapped data
paths = glob.glob('outputs/geoTwitter*.lang')    # gets all outputs
total = {hashtag: [] for hashtag in args.hashtags[0]}
for path in paths:
    date = os.path.splitext(os.path.basename(path))[0][10:18] #gets the word after reduced. (ie. lang or country)
    with open(path) as f:
        temp = json.load(f)
        
        for k in temp:
            if k in args.hashtags[0]:
                count = 0
                for hashtag in temp[k]:
                    count += temp[k][hashtag]
                total[k].append((date, count))







# plot the values
for hashtag, date_count_pairs in total.items():
    dates, counts = zip(*[(datetime.strptime(date, '%y-%m-%d'), count) for date, count in date_count_pairs])

    # Sorting data based on dates
    sorted_indices = sorted(range(len(dates)), key=lambda k: dates[k])
    dates = [dates[i] for i in sorted_indices]
    counts = [counts[i] for i in sorted_indices]

    # Plotting
    plt.plot(dates, counts, label=hashtag)



#adding labels
plt.xlabel('Date') 
plt.ylabel('Number of Tweets')
plt.title("Daily Frequency of Covid Related Hashtags During 2020")
plt.legend()

#create plot name
hashtag_list = [] 
for hashtag in args.hashtags[0]:
    hashtag_list.append(hashtag[1:])
underscore_tags = '_'.join(hashtag_list)

# save plot file
plt.savefig(underscore_tags + '.png')

