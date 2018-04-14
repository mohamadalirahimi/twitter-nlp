import codecs
import fnmatch
import os

import pathlib

files_object = open("nlp/step3/word-frequency.txt", "r", encoding='utf-8')
stopwords = {}

for i in range(0, 19):
    s = files_object.readline()
    stopwords[s.split(":")[0]] = s.split(":")[1]


Tweet_Directory = "nlp/step4"
pathlib.Path(Tweet_Directory).mkdir(parents=True, exist_ok=True)

for dirpath, dirs, files in os.walk('nlp/step2'):
    for filename in fnmatch.filter(files, '*.txt'):
        with codecs.open(os.path.join(dirpath, filename), 'r', encoding="utf-8")as f :
            text =f.read()
            edited = text
            for word in text.split():
                if word in stopwords :
                    edited = edited.replace( " " + word  + " " , " ");

            file = codecs.open(os.path.join(Tweet_Directory , filename), 'w', encoding="utf-8")
            file.write(edited)

