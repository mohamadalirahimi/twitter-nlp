import codecs
import fnmatch
import os

inverted_index ={}
data = {}
for dirpath, dirs, files in os.walk('nlp/step4'):
    for filename in fnmatch.filter(files, '*.txt'):
        with codecs.open(os.path.join(dirpath, filename), 'r', encoding="utf-8")as f:
            for word in f.read().split():
                if word not in inverted_index:
                    inverted_index[word] = 1
                    data[word] = [str(filename).replace(".txt", "")]
                else:
                    inverted_index[word] += 1
                    j = list(data[word])
                    j.append(str(filename).replace(".txt", ""))
                    data[word] = j

X= input(" enter konid word")


blacklist = []
whitelist = []
for z in X.split():
    if (z in inverted_index) :
        if (len(blacklist) > 0):
            blacklist = set(blacklist) & set(list(data[word]))
        else:
            blacklist = list(data[word])
        whitelist = set(whitelist) | set(blacklist)
Tweet_Step2 = 'nlp/step2/'
if (len(blacklist) > 0) :
    for b in blacklist:
        f = codecs.open(os.path.join(Tweet_Step2, b + ".txt"), 'r', encoding="utf-8")
        print(f.read() + "\n" + "*" * 20)
whitelist = set(whitelist) - set(blacklist)
if (len(whitelist) > 0):
    for b in whitelist:
        f = codecs.open(os.path.join(Tweet_Step2, b + ".txt"), 'r', encoding="utf-8")
        print(f.read() + "\n" + "*" * 20)