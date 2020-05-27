import sys

sys.path.append('/home/karthik/.local/lib/python3.6/site-packages')

import clean
import pickle
import os 

import indexer
import math


if (not os.path.exists('tfs.pkl') or not os.path.exists('dfs.pkl') or not os.path.exists('posting_list.pkl') or not os.path.exists('word2id.pkl')):
    indexer.run()

tfs = pickle.load(open('tfs.pkl','rb'))
dfs = pickle.load(open('dfs.pkl','rb'))
posting_list = pickle.load(open('posting_list.pkl','rb'))
word2id = pickle.load(open('word2id.pkl','rb'))

N = len(tfs) #total number of docs

if (len(sys.argv) > 1):
    limit = int(sys.argv[1])
else:
    limit = 5

query = ' '.join(sys.argv[2:])
cleaned = clean.clean(query)


query_vec = {}
for word in cleaned:
    if (word in word2id):
        word = word2id[word]
        if (word not in query_vec):
            query_vec[word] = 0
        query_vec[word] += 1

for word in query_vec:
    query_vec[word] *= math.log(N/dfs[word])


#print('cleaned',cleaned)
#print('query_vec',query_vec)
    

results = []


#retrieve documents containing atleast one of the words in the query
union_docs = set()
for word in query_vec:
    if (word in posting_list):
        for doc in posting_list[word]:
            union_docs.add(doc)


#print('union_docs',union_docs)


for file_name in union_docs:

    vec = {}
    norm = 0

    for word in tfs[file_name]:
        vec[word] = tfs[file_name][word] * math.log(N/dfs[word])
        norm += vec[word] ** 2

    norm = math.sqrt(norm)

    score = 0
    for word in query_vec:
        a = query_vec[word]
        b = (0 if word not in tfs[file_name] else tfs[file_name][word]/norm)
        score += a*b

    results.append((file_name,score))

results.sort(key = lambda x : -x[1])
results = results[:limit]
for i in range(len(results)):
    results[i] = results[i][0]
    
for result in results:
    print(result,end=',')
