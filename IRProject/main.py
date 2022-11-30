# import nltk
#
# nltk.download('stopwords')
# nltk.download('punkt')
from nltk.corpus import stopwords

# the positional index
# positional index structure pos[term][numOfDocuments][doc_id] = list of postions
positional_index = dict()

# fileID used for detecting which file we work on
fileID = 1


# this functions read all txt data from specific folder and assing it to a data list
def reading_files():
    # for i in range(numberOfFolders):
    with open('D:\Python\ir/' + str(fileID) + '.txt', 'r') as file2:
        # read file then convert it to lower case then split the string to list
        data = file2.read().lower().split()
    return data


# function that remove stop words except in and to ### work properly ###
def remove_stop_words(data):
    # Getting stop words and put it in a list
    my_stopwords = stopwords.words('english')
    my_lst = ['in', 'to']
    new_data = []
    my_stopwords = [el for el in my_stopwords if el not in my_lst]
    for term in data:
        if term not in my_stopwords:
            new_data.append(term)

    return new_data


# trying to make a postion index
def dictionaryTest(token):
    for pos, term in enumerate(token):
        # if term isn't exist in  pos_list
        if term not in positional_index:
            # initializing a list
            positional_index[term] = []
            # the frequency of document is one because we have just created it once we find it
            positional_index[term].append(1)
            # initializing the doc_id-positions dictionary
            positional_index[term].append({})
            # make the key = to the file id and the value equal position of the keyword in file
            positional_index[term][1][fileID] = [pos]
        # if the term exist in the index
        else:
            # if the file id exist
            if fileID in positional_index[term][1]:
                positional_index[term][1][fileID].append(pos)
            # if the file id doesn't exist
            else:
                positional_index[term][0] = positional_index[term][0] + 1
                positional_index[term][1][fileID] = [pos]


# def searchDocument(searchPhrase):
#     splitted = searchPhrase.split(' ')
#     cleaned_data = remove_stop_words(splitted)
#     getDocuments = dict()
#     # getting that contains the kewords form the pos index
#     for term in cleaned_data:
#         if term in positional_index:
#             getDocuments[term]= positional_index[term]
#     # pos[term][numOfDocuments][doc_id]
#     for term in range(len(getDocuments)):
#         for num in range(len(term)):
#
# ###############################################3
def phraseQuery(query):
    # splitting and removing stop words
    query = query.lower().split(' ')
    cleaned_data = remove_stop_words(query)
    # dictionary contains found document id's
    resultDec = {}
    # add found cleaned document id's  to a result list
    for term in cleaned_data:
        if term not in resultDec:
            if term in positional_index:
                resultDec[term] = []
                resultDec[term].append(list(positional_index[term][1]))

    # initialize variable to get matched documents
    matchedDocuments = []
    # if there's at least term after cleaning data enter the condition
    if len(resultDec) >= 1:
        # append the first item to the list
        for term in resultDec:
            matchedDocuments.append(resultDec[term][0])
            break
        # after appending len will be >= 2
        if len(resultDec) >= 2:
            # change doc to set to remove duplications and get the intersection of doc_id's then return the result
            for doc in matchedDocuments:
                for element in doc:
                    for term in resultDec:
                        doc = set(doc).intersection(resultDec[term][0])
                        matchedDocuments = list(doc)

    else:
        return 0

    return matchedDocuments


for i in range(3):
    data = reading_files()
    dictionaryTest(data)
    fileID += 1
print(positional_index)
searchWord = input('please enter a searching word : ')
matched_docs = phraseQuery(searchWord)
print('docs are found in ',matched_docs)
