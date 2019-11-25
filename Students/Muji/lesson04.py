# Lesson - 04

# Dictionaries
# What is a dictionary datastructure?

#-------------------------------------------
print("# 4.1")

my_dict={'first_name': 'Munkh', 'Last_name': 'Gankh'}
print(f' {my_dict.keys()} is {my_dict.values()} ')

#-------------------------------------------
print("# 4.2")

river={'nile': 'Egypt', 'Eg': "Mongolia", 'Amazon': 'Brazil' }
for item, value in river.items():
    print(f" The {item.title()} runs through {value.title()}")



"""
Ex-4.1
Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. 
You should have keys such as first_name , last_name , age , and city . 
Print each piece of information stored in your dictionary.

Ex-4.2. 
Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program.
Ex.4.3 
Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous
lesson. Use these words as the keys in your glossary, and store their
meanings as values.
• Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character ( \n ) to insert a blank line between each word-meaning
pair in your output.

Ex.4.4
Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt' .
• Use a loop to print a sentence about each river, such as f"The Nile runs
through Egypt". items() ('nile', 'egypt')
• Use a loop to print the name of each river included in the dictionary.  keys()
• Use a loop to print the name of each country included in the dictionary. values()

Game Programming: 
Count all the words for given input and save the words into dictionary with its 
number of occurences in the sentence.

Input  : "This should be enough to store each word in a list. 
words is already a list of the words from the sentence, 
so there is no need for the loop."

Output : {'This': 2, 'should': 2, 'be': 2, 'enough': 2, 'to': 2, 'store': 2, 'each': 2, '
word': 2, 'in': 2, 'a': 3, 'list.': 2, 'words': 3, 'is': 3, 'already': 2, 'list'
: 2, 'of': 2, 'the': 4, 'from': 2, 'sentence,': 2, 'so': 2, 'there': 2, 'no': 2,
 'need': 2, 'for': 2, 'loop.': 2}
"""
text = "This should be enough to store each word in a list. words is already a list of the words from the sentence, so there is no need for the loop."
splitted_text = text.split()
word_counter = {}
for i in splitted_text:
        if i in word_counter.keys():
            count = word_counter[i]
            count = count + 1
            word_counter[i] = count
        else:
            word_counter[i] = 1
print (word_counter)


def splitter (splitted_text, word_counter_dictionary):
    for i in splitted_text:
        if i in splitted_text.keys():
            count = word_counter_dictionary[i]
            count = count + 1
            word_counter_dictionary[i] = count
        else:
            word_counter_dictionary[i] = 1


