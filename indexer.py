import os 
import pickle
import clean

base_dir = 'docs_test'


def run():

    file_names = os.listdir(base_dir)

    if (os.path.exists('tfs.pkl')):
        tfs = pickle.load(open('tfs.pkl','rb'))
    else:
        tfs = {}

    if (os.path.exists('dfs.pkl')):
        dfs = pickle.load(open('dfs.pkl','rb'))
    else:
        dfs = {}

    if (os.path.exists('posting_list.pkl')):
        posting_list = pickle.load(open('posting_list.pkl','rb'))
    else:
        posting_list = {}

    if (os.path.exists('word2id.pkl')):
        word2id = pickle.load(open('word2id.pkl','rb'))
    else:
        word2id = {}

    for file_name in file_names:

        if (file_name not in tfs):

            doc_tfs = {}
            doc_words = set()
            f = open(base_dir + os.path.sep + file_name,'r')

            for line in f:

                cleaned = clean.clean(line)

                for word in cleaned:

                    if (word not in word2id):
                        word2id[word] = len(word2id)
                    word = word2id[word]

                    doc_words.add(word)
                    if (word not in doc_tfs):
                        doc_tfs[word] = 0
                    doc_tfs[word] += 1

                    if (word not in posting_list):
                        posting_list[word] = []
                    posting_list[word].append(file_name)

            for word in doc_words:
                if (word not in dfs):
                    dfs[word] = 0
                dfs[word] += 1

            print(doc_tfs)

            tfs[file_name] = doc_tfs

    #print(dfs)

    print(posting_list)

    pickle.dump(tfs,open('tfs.pkl','wb'))
    pickle.dump(dfs,open('dfs.pkl','wb'))
    pickle.dump(posting_list,open('posting_list.pkl','wb'))
    pickle.dump(word2id,open('word2id.pkl','wb'))
