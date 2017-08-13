# -*- coding: utf-8 -*-

""" all modules """
 
# tools for importing files 
import os, io
from os import path
# Chinese tokenization tool
import jieba
# word frequency counting tool
from collections import Counter
# wordcloud tool
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import numpy as np
# visualization tool
import matplotlib.pyplot as plt


""" all defs """

# read single file
def read_txt(filepath):
    f = io.open(filepath,'r', encoding = 'GB18030')
    content=f.read()
    f.close()
    return content

# read stopword (different encoding type with 'read_txt')
def read_stopword(filepath):
    f = io.open(filepath,'r', encoding = 'utf-8')
    content=f.read()
    f.close()
    return content

# read all files
def read_dir_txt(dirpath):
    filenames = os.listdir(dirpath)
    result_list=[]
    for filename in filenames:
        filepath = dirpath + filename
        text = read_txt(filepath)
        result_list.append(text)    
    ## delete blank poems(strings)
    while '' in result_list:
        result_list.remove('')
    return result_list

# tokenization
def poem_cut(text):
    return " ".join(jieba.cut(text, cut_all = False)) ## False means accurate mode


""" 1. preprocess """

# read all Tang poems into a list
wd='C:\\Users\\lenovo\\Desktop\\final project'
os.chdir(wd)
data_path = 'all-TANG-poems from zhengzhou uni\\'
Tang_poem = read_dir_txt(data_path)

# clean txt
stopword = read_stopword('C:\\Users\\lenovo\\Desktop\\final project\\stopwords.txt').split()
clean_tokens = []
for poem in Tang_poem:
    tokens = poem_cut(poem).split()
    tokens_nostop = [token for token in tokens if token not in stopword]
    clean_tokens.append(tokens_nostop)

# transfer clean_tokens list into string for wordcloud
token_all = []
for tokens in clean_tokens:
    for token in tokens:
        token_all.append(''.join(token))  
        
token_str = " ".join(token_all)


""" 2. word frequency counting"""

dictionary = {} ## start to build corpora
for token in clean_tokens: 
    fredist = Counter(token) ## single word frequency    
    for localkey in fredist.keys(): 
        if localkey in dictionary.keys(): 
           dictionary[localkey] += fredist[localkey] ## accumulation of word frequency and update the dict
        else: 
           dictionary[localkey] = fredist[localkey] ## put new word into dict

# print frequency dict
print(sorted(dictionary.items(), key = lambda  x:x[1]))

  
""" 3. wordcloud """

# read the mask 
poem_coloring = np.array(Image.open(path.join(wd,'poet.jpg')))

# create coloring from mask image
image_colors = ImageColorGenerator(poem_coloring)

# generate wordcloud
## attention: Pass in a Chinese font from font_path (if English, maybe ignore this step)
wc = WordCloud(font_path = u"static/fonts/simhei.ttf",
               max_words = 2000,
               width = 1920,
               height = 1080,
               background_color = "white",
               margin = 5,
               mask = poem_coloring)
wordcloud = wc.generate(token_str)

# print wordcloud picture
## color of words doesn't keep same with mask (mask only provides shape)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

## recolor: color of words keep same with mask (mask provides shape and color)
plt.imshow(wc.recolor(color_func = image_colors), interpolation = "bilinear")
plt.axis("off")




























