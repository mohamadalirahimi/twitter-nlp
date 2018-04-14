import os,fnmatch,codecs
import re


wordcount = {}
for dirpath, dirs, files in os.walk('nlp/step2'):
    for filename in fnmatch.filter(files, '*.txt'):
        with codecs.open(os.path.join(dirpath, filename),'r',encoding="utf-8")as f:

            for word in f.read().split():
                if word not in wordcount:
                    wordcount[word] = 1
                else:
                    wordcount[word] += 1

files_object = open("nlp/step3/word-frequency.txt" , "w" ,encoding='utf-8')

for k,v in sorted(wordcount.items(), key=lambda x: x[1] , reverse=True):
    files_object.write(str(k) + ":" + str(v) + "\n")

files_object.close();



