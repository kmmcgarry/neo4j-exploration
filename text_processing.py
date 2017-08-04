'''
Kristen McGarry
Data Analyst Intern
Summer 2017
'''

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import codecs
import string

def onlyAscii(inFile,outFile):
    ip=open(inFile,'r')
    op=open(outFile,'w')
    for line in ip:
        line=line.strip().decode("ascii","ignore").encode("ascii")
        if line=="":continue
        op.write(line)
    ip.close()
    op.close()


def getText(inFile):
    i_file = open(inFile,'r')
    text = i_file.read()
    return text


def removeStopWords(text):
    stop = (stopwords.words('english')) + (list(string.punctuation))

    clean_text = []
    tokens = word_tokenize(text.lower())

    for word in tokens:
        if word not in stop:
            clean_text.append(word)

    return clean_text


def wordFrequency(clean_text):
    freq_dict = {}

    for word in clean_text:
        if word in freq_dict:
            freq_dict[word] = freq_dict[word] + 1
        else:
            freq_dict[word] =1
    return freq_dict


# Sentence Tokenization
def tokenizer(text):
    sent_tokens = nltk.sent_tokenize(text)
    return sent_tokens



# Part of speech tagger
def posTagger(sent_tokens):
    pos_text = []

    for i in range(0,(len(sent_tokens)-1)):
        word_tokens = word_tokenize(sent_tokens[i])
        pos_temp = nltk.pos_tag(word_tokens)
        pos_text.append(pos_temp)
    return pos_text

# Count frequency of all part of speech tags
def countPos(pos_text):
    return "incomplete."

# ****** COMMANDS ******

#onlyAscii("C:/Users/mcgark9/Documents/main-project/data/sec-edgar-txt-files/APPLE DEF 14A.txt","C:/Users/mcgark9/Documents/main-project/data/sec-edgar-txt-files/APPLE DEF 14A ASCII.txt")
text = getText("C:/Users/mcgark9/Documents/main-project/data/sec-edgar-txt-files/APPLE DEF 14A ASCII.txt")
#clean_text = removeStopWords(text)

#out_file = open("C:/Users/mcgark9/Documents/main-project/data/sec-edgar-txt-files/APPLE DEF 14A ASCII WORD FREQ.txt","w")
#out_file.write(str(wordFrequency(clean_text)))
#print "written to out file"

sent_tokens = tokenizer(text)
#print (sent_tokens[100])
#print len(sent_tokens)

out_file = open("C:/Users/mcgark9/Documents/main-project/data/sec-edgar-txt-files/APPLE DEF 14A ASCII POS.txt","w")
out_file.write(str(posTagger(sent_tokens)))
print "written to file"


#print posTagger(tokenizer(text))





# IF NEED TO TAKE IN FROM HTML FILE: INCOMPLETE
def cleanHtml(htmlFile,outFile):

    i_file = codecs.open(htmlFile,'r')
    text = i_file.read()

    # remove all tables, find all lines that start with <TABLE and end with </TABLE>
    counter = 0
    table_occurences = text.count("<TABLE ")
    print table_occurences
    for i in range(0,table_occurences):
        counter += 1
        begin = text.find("<TABLE ")
        end = text.find("</TABLE>")
        #print "BEGIN " + str(begin)
        #print "END " + str(end)

        text = text[:begin] + text[end+8:]
        begin = (-1)
        end = (-1)

        i+=1

    text_v1 = text

    o_file = codecs.open(outFile,'w')
    o_file.write(text_v1)

#cleanHtml("C:\Users\mcgark9\Desktop\practice.html")
#cleanHtml("C:/Users/mcgark9/Desktop/apple.html","C:/Users/mcgark9/Desktop/apple_v1.html")
