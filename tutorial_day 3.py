import os,io,glob
wd='I:\\AU summer school 2017\\text mining the great unread\\day 3\\tmgu17-master\\tmgu17-master\\DATA'
os.chdir(wd)
data_path = 'data\\' #relative path to data(text),four texts are stored in the path wd\\data\\...
filenames = os.listdir(data_path)
print(filenames)

for s in filenames:
    print(s.upper())
print(type(filenames[0]))

filename = data_path + filenames[0]
filename='data/pan.txt'

f=io.open(filename,'r',encoding='utf-8') #r=read, utf-8=unicode
content=f.read()
f.close()
print(type(content))

with io.open(filename,'r',encoding='utf-8') as f:
    content=f.read()
print(type(content))

print(len(content))
print(content[:1000])

print(sum([2,3,4]))

def read_txt(filepath):
    f=io.open(filepath,'r',encoding='utf-8')
    content=f.read()
    f.close()  #open,read,close,3steps
    return content

text=read_txt(filename)
print(text[:1000])

lit_list=[]
for filename in filenames:
    filepath=data_path+filename
    text=read_txt(filepath)
    textupper=text.upper()
    lit_list.append(textupper)

print(filenames[0])
print('start 50 char in',filenames[0],':',lit_list[0][:50])

################################################

def read_txt(filepath):
    f=io.open(filepath,'r',encoding='utf-8')
    content=f.read()
    f.close()  #open,read,close,3steps
    return content

###############################################

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

###############################################

def read_dir_txt(dirpath):
    filenames=glob.glob(dirpath+'*.txt')
    result_list=[]
    for filename in filenames:
       text=read_txt(filepath)
       result_list.append(text)
    return result_list

result = read_dir_txt(data_path)
print(len(result))
print(glob.glob(data_path+'*.txt'))





