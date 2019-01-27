import os,io

wd='I:\\AU summer school 2017\\text mining the great unread\\day 3\\tmgu17-master\\tmgu17-master\\DATA'
os.chdir(wd)
data_path = 'data\\'

def read_txt(filepath):
    f=io.open(filepath,'r',encoding='utf-8')
    content=f.read()
    f.close()  #open,read,close,3steps
    return content

def read_dir_txt(dirpath):
    filenames=os.listdir(dirpath) #get file names
    result_list=[] #loop over filenames
    for filename in filenames:
       filepath=dirpath+filename
       text=read_txt(filepath) #read files from filenames and store in list
       result_list.append(text)
    return result_list

someones_corpus=read_dir_txt(data_path)
print(len(someones_corpus))

# single text tokenization 
text = read_txt('data/pan.txt')
print(text)

# list of all takens in text
import re

tokenizer = re.compile(r'[^a-zA-Z]*')
tokens = [token.lower() for token in tokenizer.split(text)]
len(tokens)
type(tokens)
print(tokens[2000:2015])

def tokenize(text, lentoken = 0): # let lentoken = 0 for default
    tokenizer = re.compile(r'[^a-zA-Z]+')
    tokens = [token.lower() for token in tokenizer.split(text) if len(token) > lentoken]
    return tokens

test = tokenize(text, 4) # it will not report an error if empty in lentoken because of default 
print(test[2000:2015])
print(len(test))

tokens = tokenize(text,1)
print(tokens[2000:2050])

# stopword filtering
stopword = read_txt('I:\\AU summer school 2017\\text mining the great unread\\day 4\\res\\stopword_us.txt').split()
tokens_nostop = [token for token in tokenize(text, 1) if token not in stopword]
print(len(tokens_nostop))
print(len(tokens_nostop)/float(len(tokens)))
print(tokens_nostop[1000:1050])

# word counting
def tf(term, tokens):
    result = tokens.count(term)
    return result

print(tf('pan', tokens_nostop))

lexicon = set(tokens_nostop)
tf_all = dict([(token,tokens_nostop.count(token)) for token in lexicon])
print(lexicon)
print(tf_all.items()) # list the frequency of every vocaburary
print(type(tf_all))

# word search
print(tf_all['dog'])

#################### plotting the graph #########################

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

def plotdist(x, sv = 0, filename = "dist.png"):
    """ histogram with normal fit """
    mu = np.mean(x)
    sigma =  np.std(x)
    n, bins, patches = plt.hist(x, 50, normed=1, facecolor='k', alpha=0.75)
    y = mlab.normpdf(bins, mu, sigma)# best normal fit
    ax = plt.plot(bins, y, 'r--', linewidth=1)
    plt.ylabel('Probability')
    plt.grid(True)
    if sv == 1:
        plt.savefig(filename, dpi = 300)
    else:
        plt.show()
        plt.close()

def plotvars(x,y = 0, sv = False, filename = 'qd_plot.png', ax1 = '$x$', ax2 = '$f(x)$'):
    """
    quick and dirty x and x-y plotting
    """
    fig, ax = plt.subplots()
    if y:
        ax.plot(x,y, color = 'k')
        ax.set_xlabel(ax1)
        ax.set_ylabel(ax2)
    else:
        ax.plot(x, color = 'k')
        ax.set_xlabel("$time$")
        ax.set_ylabel("$var~1$")
    #plt.rc('text', usetex=True)
    #font = {'family' : 'serif','serif': ['times'], 'weight' : 'bold', 'size': 12}
    #mpl.rc('font', **font)
    #mpl.rcParams['axes.linewidth'] = 2
    if sv:
        plt.savefig(filename, dpi = 300)
    else:
        plt.show()
        plt.close()

def plotbar(y, sv = False, filename = 'qd_bar.png', ax1 = '$x$', ax2 = '$f(x)$'):
    """
    quick and dirty bar plot of one variable
    """
    fig, ax = plt.subplots()
    x = range(1,len(y)+1)
    ax.bar(x,y,color = 'k')
    ax.set_xlabel(ax1)
    ax.set_ylabel(ax2)
    if sv:
        plt.savefig(filename, dpi = 300)
    else:
        plt.show()
        plt.close()
        
c = 'wendy'
x = [int(l==c) for l in tokens]
print(x[0:100])
plotvars(x, 0, sv = True, filename = 'wendy_plot.png') # export the graph and store on the dirpath
plotvars(x)

type(x)
type(x[0])

plt.plot(x)
plt.show()
plt.close() # another way for calling plot

import matplotlib.pyplot as plt
def disp_plot(text,kws):
   """
   dispersion plot for multiple keywords
   """
   kws = [kw.lower() for kw in kws]
   tokens = tokenize(text)
   pts = [(x,y) for x in range(len(tokens)) for y in range(len(kws)) if tokens[x] == kws[y]]
   if pts:
       x,y = zip(*pts)
   else:
       x = y = ()
   plt.plot(x,y,"ko")
   plt.yticks(range(len(kws)),kws,color="k")
   plt.ylim(-1,len(kws))
   plt.title("Lexical Dispersion Plot")
   plt.xlabel("Word Offset")
   plt.show()
   
ws = ['Peter','love','darling'] # you can add more vocabs if you want
disp_plot(text,ws)

multistring = text + text
disp_plot(multistring, ws)








 



















