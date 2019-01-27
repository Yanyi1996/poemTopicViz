"""
TOPIC MODELING
- import paragraphs from text
- preprocess
- merge paragraphs
- train model
- explore model
"""

### preamble
from __future__ import division
import io, os, re
import numpy as np

from nltk.tag import pos_tag
from gensim import corpora, models

root = 'I:\\AU summer school 2017\\text mining the great unread\\day 8'
filepath = os.path.join(root,'data','kjv.txt')
os.chdir(root)

import textminer as tm

def get_para(filepath, encoding = 'utf-8'):
    """
    Import text file on filepath in paragraphs
    - default encoding unicode
    """
    with io.open(filepath, "r", encoding = encoding) as f:
        text = f.read()
        paragraphs = []
        for s in text.split('\n\n'):
            if s:
                paragraph = s #.lower()
                paragraph = re.sub(r'[^A-Za-z]',' ',paragraph)
                paragraph = re.sub(r' +',' ',paragraph)
                paragraphs.append(paragraph.rstrip())
    return paragraphs

paragraphs = get_para(filepath)
print(paragraphs[0])

# parts of speech tagging
pos_tag(tm.tokenize(paragraphs[100]), tagset = 'universal', lang = 'eng')

# monster tokenizer
para_token = []
i = 0
for paragraph in paragraphs:
    print(i)
    tokens = tm.tokenize(paragraph, length = 1, casefold = False)
    tagset = pos_tag(tokens, tagset = 'universal', lang = 'eng')
    tokens = [tag[0] for tag in tagset if tag[1] == 'NOUN']
    tokens = [token.lower() for token in tokens]
    para_token.append(tokens)
    i += 1
print(para_token[-10])

sw = tm.gen_ls_stoplist(para_token, 10)
print(sw)

data_premerge = para_token

data = []
n = 10
idx = range(0, len(data_premerge),n)
for i in idx:
    if i == max(idx):
        for ii in range(i+1, len(data_premerge)):
            merge = data_premerge[ii]
    else:
        merge = data_premerge[i]
        for ii in range(1,n):
            merge = merge + data_premerge[i+ii]
        data.append(merge)

print(data[0])

# let the topic modeling begin
dictionary = corpora.Dictionary(data)
print(dictionary.num_docs)
print(dictionary.items())
print(dictionary.keys())
print(dictionary.values())
print(dictionary.dfs)

# bag-of-words representation of the paragraphs
paragraph_bag = [dictionary.doc2bow(paragraph) for paragraph in data]
i = 1
print(data[i])
paragraph = paragraph_bag[i]
print(paragraph)

# train the nobel
k = 10
mdl = models.LdaModel(paragraph_bag, id2word = dictionary, num_topics = k, random_state = 1234) 

# explore the model
# print topics as word distribution
for i in range(k):
    print('topic', i)
    print([t[0] for t in mdl.show_topic(i,10)])
    print('---------')
        
print(paragraph)
print(mdl[paragraph])
print(data)

# query the document with unseen documents
query = u'Jesus was a jew who loved Israels people'
quary = query.lower().split()
vocab = dictionary.values()
query = [w for w in query if w in vocab]
print(query)
query = dictionary.doc2bow(query)
print(query)
mdl[query]
print(mdl.show_topic(7,10))

# estimate document similarity on topic


































