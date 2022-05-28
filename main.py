# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import string;


def read_file_content():
    # [assignment] Add your code here
    with open('story.txt') as f:
        contents = f.read()
        print(contents)
    return "Hello World"


def count_words():
    text = open("story.txt", "r")
    d = dict()
    for line in text:
        line = line.strip()
        line = line.lower()
        line = line.translate(line.maketrans("", "", string.punctuation))
        words = line.split(" ")

        for word in words:
            if word in d:
                d[word] = d[word] + 1
            else:
                d[word] = 1

    for key in list(d.keys()):
        print(key, ":", d[key])

    return {"as": 10, "would": 20}


read_file_content()
count_words()
