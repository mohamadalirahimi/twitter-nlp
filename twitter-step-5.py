import codecs
import fnmatch
import os

inverted_index = {}
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

file = codecs.open("nlp/step5/inverted-index.txt", 'w', encoding="utf-8")
for k,v in inverted_index.items():
    file.write(str(k) + "," + str(v))
    for v in list(data[k]) :
        file.write("," + v)
    file.write("\n")

file.close();


