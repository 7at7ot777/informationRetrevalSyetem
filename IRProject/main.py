# import nltk
#
# nltk.download('stopwords')
# nltk.download('punkt')
from nltk.corpus import stopwords

positional_index = dict()

# fileID used for detecting which file we work on
fileID = 1
numberOfFiles = 10

# this functions read all txt data from specific folder and assing it to a data list
def reading_files():
    # for i in range(numberOfFolders):
    with open('D:\Python\ir-workingProject\\files/' + str(fileID) + '.txt', 'r') as file2:
        # read file then convert it to lower case then split the string to list
        data = file2.read().lower().split()
    return data


# function that remove stop words except in and to ### work properly ###
def remove_stop_words(data):
    my_stopwords = stopwords.words('english')
    my_lst = ['in', 'to','where']
    new_data = list()
    my_stopwords = [el for el in my_stopwords if el not in my_lst]
    for term in data:
        if term not in my_stopwords and term != ' ':
            new_data.append(term)
    return new_data


# trying to make a postion index
def PositionalIndexing(token):
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




def PhraseQuery(word):
    # make empty list of lists in the size of number of files
    semiFinalList = [[] for i in range(numberOfFiles + 1)]
    # for every term in the query
    for w in word:
        # if the term in the keys of positional index do the following
        if w in list(positional_index.keys()):
            # loop in every document id
            for key in list(positional_index[w][1].keys()):  # keys is the fileID'ss
                # if final list in the position of document id is not empty do the following
                if semiFinalList[key] != []:
                    # if the postion last element in final list in a certain file == the position of currnt word in the same file  - 1 then it will match
                    if semiFinalList[key][-1] == positional_index[w][1][key][0] - 1:
                        semiFinalList[key].append(positional_index[w][1][key][0])  # appent the position to the final list

                else:  # if the final list is empty then append the position of the keyword in the file
                    semiFinalList[key].append(positional_index[w][1][key][0])
        else:
            continue
    FinalList = dict()
    for document, positions in enumerate(semiFinalList):
        if len(positions) == len(word):
            FinalList[document] = positions[0]
    return FinalList
def termFrequency():
    tf = dict()
    for term in positional_index:
        tf[term] = [0 for i in range(numberOfFiles)]
        for documentId in positional_index[term][1].keys():
            tf[term][documentId-1] += 1

    for term in tf:
        print(term ,"           " , tf[term])

for i in range(numberOfFiles):
    data = reading_files()
    data = remove_stop_words(data)
    PositionalIndexing(data)
    fileID += 1
print(positional_index)
print(termFrequency())
searchWord = input('please enter a searching word : ')
searchWord = remove_stop_words(searchWord.lower().split())
print(PhraseQuery(searchWord))


