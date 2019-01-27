import os, re
import textminer as tm
wd = 'I:\\AU summer school 2017\\text mining the great unread\\day 6'
os.chdir(wd)
text = tm.read_txt('pan.txt')

# use regex to identify START and END of Gutenberg text
pat1 = r'\*{3} STAR(.*?)\*{3}'
pat2 = r'\*{3} END(.*?)\*{3}'
start_idx = [(m.start(0), m.end(0)) for m in re.finditer(pat1, text)]
end_idx = [(m.start(0), m.end(0)) for m in re.finditer(pat2, text)]

# print start string of Gutenberg text
print(text[start_idx[0][0]:start_idx[0][1]])
idx1 = start_idx[0][1]+1 # beginning of content
idx2 = end_idx[0][0] # end of content

# extract text content and assign to variable
content = text[idx1:idx2]
print(content[:100])

tokens = tm.tokenize(content, lentoken = 1)
print(tokens[:100])

def slice_tokens(tokens, n = 100, cut_off = True):
    # result: list of slices
    slices = []
    # slice tokens
    for i in range(0, len(tokens), n):
        slices.append(tokens[i:(i+n)])
    #cut_off function
    if cut_off:
        del slices[-1]
    return slices

slices = slice_tokens(tokens, 250, True)

# sentiment analysis with LabMT
import pandas as pd
labmt = pd.read_csv('labmt_dict.csv', sep = '\t', encoding = 'utf-8', index_col = 0)

avg = labmt.happiness_average.mean()
sent_dict = (labmt.happiness_average - avg).to_dict()
print(sent_dict)

sent_vects = []
for s in slices:
    sent_vects.append(sum([sent_dict.get(token, 0.0) for token in s]))
    
print(len(sent_vects)) == len(slices)
print(slices[5])
print(sent_vects[-1])

import quickndirty as qd
qd.plotdist(sent_vects, sv = True)
qd.plotvars(sent_vects, sv = True)

print(sent_dict['pirate'])
print(sent_dict['pirates'])



    
    
    
    
    
    
    

