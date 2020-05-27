import clean
import pickle
import os 
import sys
import indexer
import math


if (not os.path.exists('tfs.pkl') or not os.path.exists('dfs.pkl')):
    indexer.run()

tfs = pickle.load(open('tfs.pkl','rb'))
dfs = pickle.load(open('dfs.pkl','rb'))

N = len(tfs) #total number of docs

if (len(sys.argv) > 1):
    limit = int(sys.argv[1])
else:
    limit = 5

query = ' '.join(sys.argv[2:])
cleaned = clean.clean(query)


query_vec = {}
for word in cleaned:
    if (word not in query_vec):
        query_vec[word] = 0
    query_vec[word] += 1

for word in query_vec:
    query_vec[word] *= math.log(N/dfs[word])


#print('cleaned',cleaned)
#print('query_vec',query_vec)
    

results = []


for file_name in tfs:

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
    
print(results)
