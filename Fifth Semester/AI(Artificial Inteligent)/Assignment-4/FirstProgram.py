# i. Simple Language Model using NLTK

import random
try:
 import nltk
 from nltk import word_tokenize, bigrams, FreqDist
 # nltk.download('punkt') # commented to avoid network call
 text = "
Artificial intelligence is transforming the world.
AI makes machines intelligent.
Artificial intelligence enables computers to learn from data.
"
 tokens = word_tokenize(text.lower())
 unigram_freq = FreqDist(tokens)
 total_unigrams = len(tokens)
 def unigram_prob(word): return unigram_freq[word] / total_unigrams
 from collections import defaultdict
 bigrams_list = list(bigrams(tokens))
 bigram_freq = FreqDist(bigrams_list)
 conditional_prob = defaultdict(dict)
 for (w1, w2), freq in bigram_freq.items():
 conditional_prob[w1][w2] = freq / unigram_freq[w1]
 def generate_text(start_word, length=10):
 word = start_word; result=[word]
 for _ in range(length-1):
 next_words = list(conditional_prob[word].keys())
 if not next_words: break
 word = random.choice(next_words); result.append(word)
 return " ".join(result)
 print("Unigram Probability of 'intelligence':", round(unigram_prob('intelligence'),3))
 print("Bigram Probability P(world | transforming):", round(conditional_prob['transforming'].get('the',0), print("\nGenerated Text:"); print(generate_text('artificial',8))
except Exception as e:
 print('NLTK example could not run:', e)
