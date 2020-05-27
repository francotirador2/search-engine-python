import os 
import pickle
import clean

base_dir = 'docs_test'

def run():

    file_names = os.listdir(base_dir)
    allwords = set()

    def list_to_dict(words):
        d = {}  
        for word in words:
            if (word not in d):
                d[word] = 0
            d[word] += 1

    if (os.path.exists('tfs.pkl')):
        tfs = pickle.load(open('tfs.pkl','rb'))
    else:
        tfs = {}

    if (os.path.exists('dfs.pkl')):
        dfs = pickle.load(open('dfs.pkl','rb'))
    else:
        dfs = {}


    for file_name in file_names:

        if (file_name not in tfs):

            doc_tfs = {}
            doc_words = set()
            f = open(base_dir + os.path.sep + file_name,'r')

            for line in f:

                cleaned = clean.clean(line)
                for word in cleaned:
                    doc_words.add(word)
                    if (word not in doc_tfs):
                        doc_tfs[word] = 0
                    doc_tfs[word] += 1

            for word in doc_words:
                if (word not in dfs):
                    dfs[word] = 0
                dfs[word] += 1

            print(doc_tfs)

            tfs[file_name] = doc_tfs

    #print(dfs)

    pickle.dump(tfs,open('tfs.pkl','wb'))
    pickle.dump(dfs,open('dfs.pkl','wb'))
