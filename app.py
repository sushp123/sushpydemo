import urllib3
from collections import Counter
import requests

target_url = "https://www.gutenberg.org/files/2701/2701-0.txt"

#Http request to URL
try:
    http = urllib3.PoolManager()
    response = http.request('GET', target_url)
    data = response.data.decode('utf-8')

except requests.exceptions.HTTPError as err:
    print(err)

stopwords = set(line.strip() for line in open('stopwords.txt'))
stopwords = stopwords.union(set(['the', 'of', 'to', 'and', 'a', 'in', 'is', 'it', 'you', 'that', 'he', 'was', 'for', 'on', 'are', 'with', 'as', 'I', 'his', 'they', 'be', 'at', 'one', 'have', 'this', 'from', 'or', 'had', 'by', 'not', 'word', 'but', 'what', 'some', 'we', 'can', 'out', 'other', 'were', 'all', 'there', 'when', 'up', 'use', 'your', 'how', 'said', 'an', 'each', 'she']))

# Instantiate a dictionary, and for every word in the file,
# Add to the dictionary if it doesn't exist. If it does, increase the count.
wordcount = {}


# To eliminate duplicates, we split by punctuation, delimiters
for word in data.lower().split():
    word = word.replace(".", "")
    word = word.replace(",", "")
    word = word.replace(":", "")
    word = word.replace("\"", "")
    word = word.replace("!", "")
    word = word.replace("*", "")
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

# Print the top 50 words
word_counter = Counter(wordcount)
for word, count in word_counter.most_common(50):
    print(word, ": ", count)
