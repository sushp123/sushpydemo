import urllib3
from collections import Counter
import requests

TARGET_URL = "https://www.gutenberg.org/files/2701/2701-0.txt"
UNION_WORDS = [
    'the', 'of', 'to', 'and', 'a', 'in', 'is', 'it', 'you', 'that', 'he', 'was', 'for', 'on', 'are', 'with', 'as', 'I',
    'his', 'they', 'be', 'at', 'one', 'have', 'this', 'from', 'or', 'had', 'by', 'not', 'word', 'but', 'what', 'some',
    'we', 'can', 'out', 'other', 'were', 'all', 'there', 'when', 'up', 'use', 'your', 'how', 'said', 'an', 'each', 'she'
]


def get_data(url):
    """
        Function to hit the target API and get the data
    :return: data -> list
    """
    try:
        http = urllib3.PoolManager()
        response = http.request('GET', url)
        return response.data.decode('utf-8')
    except requests.exceptions.HTTPError as err:
        print(err)


def fetch_words(data):
    if not data:
        return
    stopwords = set(line.strip() for line in open('stopwords.txt'))
    stopwords = stopwords.union(set(UNION_WORDS))

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
    final_words = []
    for word, count in word_counter.most_common(50):
        final_words.append([word, count])
    return final_words


data = get_data(TARGET_URL)
words = fetch_words(data)
for word in words:
    print(f"Word :{word[0]} , Count : {word[1]}")
