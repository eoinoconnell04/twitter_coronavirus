#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()


# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# sort and count the number of instances that fall into each category
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)

# create list with the top 10 categories and then reverse order
top_10 = items[:10]
keys = [x[0] for x in items_10]
values = [x[1] for x in items_10]
keys.reverse()
values.reverse()

#create bar chart
plt.bar(range(len(keys)), values,)
plt.xticks(range(len(keys)), keys)

#add labels, then save
plt.ylabel("Number of Tweets")
plt.xlabel(args.input_path[8:])
plt.title('Number of Tweets with ' + args.input_path[:] + "Divided by Country")
plt.savefig(args.key[1:] + "_" + args.input_path[8:] +'.png')
