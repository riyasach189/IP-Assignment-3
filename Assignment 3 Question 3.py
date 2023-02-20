#COMPLETED

"""
As a TA for Communication Skills course, you have been requested to automate evaluating and scoring 
assignments (which are writing assignments for which each student submit a text file). You are to
automatically evaluate each answer file.  

For names of the input files - you can hard code it in a list, and then process them one by one. 
Or you can name the files as FILE1.txt to FILEn.txt, and take an integer input regarding the number 
of files and then read them. You need to write out the output files in this directory itself.

To score an answer file first determine: 

F1 factor = (Unique words/Total words)
F2 factor = (total occurrences of the top 5 most occurring words)/Total words
F3 factor = (number of sentences >35 words or < 5 words/Total sentences)
F4 factor = (Frequency of consecutive [comma+full-stop+colon+semicolon]/Total words)
F5 factor = 1 if (Total word count > 750 words), else 0. 

Net score is: 4 + F1*6 + F2*6 -F3 - F4 - F5.

Slight change in the score formula - but older one is also fine.

Some clarifications:
The total sentence count needs to be computed after discounting repeated full stops. 
For example - I am a student of IIIT Delhi… Here, there are a few consecutive full-stops. 
We will, however, consider this as a single sentence.  And increase the count of consecutive 
full-stops/ commas/ semi-colons/ colons /hyphens by one regardless of how many full-stops there 
are (.. is one and ….. is also one, so is .,.,.,).
Consider words of the same spelling but different cases as the same word.

Output is to be written in the file scores.txt , as follows:
Write the filename on one line.
On the next line, write the student's score with the text “score: ”[without quotes].
On the next line, write out the five most used words in descending order of usage.
On the next line, write out five randomly selected words from the submission. 
(Points 3 and 4 help to see whether the assignment submission is valid, by checking whether 
the words are actual English words or not. Your program does not have to check whether these 
are English words - this explanation is given just to tell you why points 3 and 4 are to be done.)
"""

#Assumption: Cannot handle titles like Mr. Dr. Sr.
#Assumption: All files have at least 5 words
#Assumption: there are no punctuations in the text other than .,:;
#Assumption for sentence_checker(): if two strings are separated by , : ; they are different words, not sentences. Sentences only split at "."

import random

files = ["file00.txt", "file01.txt", "file02.txt"] 

chars = [",", ".", ":", ";"]


def consecutive_char_counter(text):
    count = 0
    
    if text[0] in ",.:;" and text[1] in ",.:;" and text[2] not in ",.:;":
        count += 1

    for i in range(1, len(text)-1):
        if text[i] in ",.:;" and text[i-1] not in ",.:;" and text[i+1] in ".,:;":
            count += 1

    return count


def word_checker(text):
    unique_words = 0
    total_words = 0
    word_freq = dict()

    text = text.replace(".", " ")
    text = text.replace(",", " ")
    text = text.replace(";", " ")
    text = text.replace(":", " ")
    text_as_list = text.split()

    for i in range(len(text_as_list)):
        text_as_list[i] = text_as_list[i].lower()

    for i in text_as_list:
        total_words += 1
        word_freq[i] = word_freq.get(i,0) + 1

    for i in word_freq:
        if word_freq[i]==1:
            unique_words += 1

    return unique_words, total_words, word_freq, text_as_list


def sentence_checker(text):
    text = text.replace(","," ")
    text = text.replace(":", " ")
    text = text.replace(";", " ")

    text = text.split(".")

    sentence_counter = len(text)
    bad_sentence_counter = 0

    for i in text:
        if len(i)<5 or len(i)>35:
            bad_sentence_counter += 1

    return sentence_counter, bad_sentence_counter


with open("scores.txt", "w") as f:
    f.write("")

for file in files:

    with open(file,"r") as f:
        text = f.read()

    text = text.replace("\n"," ")
    
    sentence_counter, bad_sentence_counter = sentence_checker(text)

    unique_words, total_words, word_freq, text_as_list = word_checker(text)

    word_freq = sorted(word_freq.items(), key=lambda x:x[1])

    word_freq.reverse()

    five_most_common_words = [k[0] for k in word_freq[:5]]
    freq_most_common = 0

    for k in word_freq[:5]:
        freq_most_common += k[1]

    f1 = unique_words/total_words
    f2 = freq_most_common/total_words
    f3 = bad_sentence_counter/sentence_counter
    f4 = consecutive_char_counter(text)/total_words
    f5 = 1 if total_words>750 else 0

    score = 4 + f1*6 + f2*6 - f3 - f4 - f5

    rand_nums = random.sample(range(0, total_words), 5)

    rand_words = [text_as_list[num] for num in rand_nums] 

    output = f"{file}\nScore: {score}\nFive Most Used Words: {five_most_common_words}\nFive Random Words: {rand_words}\n\n"#f1:{f1}\nf2:{f2}\nf3:{f3}\nf4:{f4}\nf5:{f5}\n

    with open("scores.txt","a") as f:
        f.write(output)
