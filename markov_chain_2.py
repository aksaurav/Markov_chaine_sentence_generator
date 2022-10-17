from importlib.resources import path
from sys import path_hooks
import numpy as np
import random
import re
from collections import defaultdict

path = 'C:\python_files\markov_chain\pride-and-prejudice.txt'

with open(path) as f:
    text = f.read()
tokenized_text = [
    word
    for word in re.split('\W+', text)
    if word != ''
]

# Create graph.
markov_graph = defaultdict(lambda: defaultdict(int))

last_word = tokenized_text[0].lower()

for word in tokenized_text[1:]:
    word = word.lower()
    markov_graph[last_word][word] += 1
    last_word = word


# Preview graph.
limit = 3
for first_word in ('the', 'by', 'who'):
  next_words = list(markov_graph[first_word].keys())[:limit]
  for next_word in next_words:
    print(first_word, next_word)