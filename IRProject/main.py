import nltk

nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords


# this functions read all txt data from specific folder and assing it to a data list
def reading_files(numberOfFolders):
    data = []
    for i in range(numberOfFolders):
        with open('D:\Python/' + str(i + 1) + '.txt', 'r') as file2:
            data.append(file2.read().split())
    return data


def tokenization(data):
    simple_set = set()
    for lista in data:
        for item in lista:
            simple_set.add(item)
    return simple_set


def remove_stop_words(tokens, stopWordsList):
    tokens = set(tokens)
    stopWordsList = set(stopWordsList)
    tokens = tokens - stopWordsList
    return tokens

# get the stopwords from english language and put it in list then return it
def getStopWords():
    my_stopwords = stopwords.words('english')
    my_lst = ['in', 'to']
    my_stopwords = [el for el in my_stopwords if el not in my_lst]
    return my_stopwords


# specify the numbers of folders
numberOfFolders = 3
# reading data from files
data = reading_files(numberOfFolders)

# tokenize data
tokens = list(tokenization(data))

# get the stop words list after removing 'in' 'to' from it
stopWordsList = getStopWords()
# remove stop words from the text
tokens = remove_stop_words(tokens, stopWordsList)
#  print data after removing stop words
print(sorted(tokens))
