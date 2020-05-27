import os 
import pickle
import clean

file_names = os.listdir('docs/')
allwords = set()


def list_to_dict(words):
    d = {}  
    for word in words:
        if (word not in d):
            d[word] = 1
        else:
            d[word] += 1


if (os.path.exists('tfs.pkl')):
    tfs = pickle.load(open('tfs.pkl','rb'))
else:
    tfs = {}

if (os.path.exists('idfs.pkl')):
    idfs = pickle.load(open('idfs.pkl','rb'))
else:
    idfs = {}
    

for file_name in file_names:

    if (file_name not in tfs):

        tmp = {}
        f = open(file_name,'r')
        words = []

        for line in f:
            words.extend(clean.clean(line))
    