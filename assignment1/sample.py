import csv
import json

scores = {}  # empty dictionary to store scores for each word

with open('AFINN-111.txt') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        scores[row[0].strip()] = int(row[1].strip()) 
   


with open('ass1_tweet.txt') as f:
    for line in f:
       # print line
        tweet = json.loads(line)
        # print tweet
        text = tweet.get('text','').encode('utf-8')
        # print text
        if text:
            total_sentiment = sum(scores.get(word,0) for word in text.split())
            print("{}: {}".format(text,scores))