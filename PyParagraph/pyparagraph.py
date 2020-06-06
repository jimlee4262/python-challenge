# importing modules
import re
import os

sentence_split = []
paragraph = ""
word_count = []
letter_count = []

# importing the file
paragraph_data = os.path.join('raw_data','paragraph_1.txt')

with open(paragraph_data, 'r') as text_file:

    lines = text_file.read()
    # paragraph = text_file.read().replace("\n"," ")
    # print(paragraph)

    #count sentences
    sentence_split = re.split("(?<=[.!?]) +", lines)
    sentence_count = len(sentence_split)

    #count words
    word_split = lines.split(" ")
    word_count = len(word_split)

    #count letters
    for word in word_split:
        letter_count.append(len(word))

    #Calculate Average Word Count
    avg_letter_count = round(sum(letter_count)/word_count,2)

    #Average sentence length
    avg_sentence_count = round(word_count/sentence_count, 2)

print("'''output")
print("Paragraph Analysis")
print(f'Approximate Word Count: {word_count}')
print(f'Approximate Senttence Count: {sentence_count}')
print(f'Average Letter Count: {avg_letter_count}')
print(f'Average Sentence Length: {avg_sentence_count}')
print("'''")



