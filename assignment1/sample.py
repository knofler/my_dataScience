import csv
import json

scores = {}  # empty dictionary to store scores for each word

with open('AFINN-111.txt') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        scores[row[0].strip()] = int(row[1].strip()) 


with open('ass1_tweet.txt') as f:
    for line in f:
        tweet = json.loads(line)
        text = tweet.get('text','').encode('utf-8')
        if text:
            total_sentiment = sum(scores.get(word,0) for word in text.split())
            print("{}: {}".format(text,scores))