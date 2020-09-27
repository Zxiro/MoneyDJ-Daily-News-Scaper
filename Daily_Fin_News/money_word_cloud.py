import nltk
import time

from wordcloud import WordCloud

text = open('./txt', 'r', encoding='utf-8').read()
text = ' '.join(nltk.word_tokenize(text))
cloud = WordCloud().generate(text)
cloud.to_file('output.png')
