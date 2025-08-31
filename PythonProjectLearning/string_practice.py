# Coding Program 1: String Manipulation - User Information Formatter
# Objective:
#  Create a program that collects the user's full name and a short bio and
#  performs various string manipulations.
import string

# Problem Statement:
# Collect the user's first name, last name, and a short bio.
# Perform the following string operations:
# Convert the full name to uppercase.
# Extract the first character of the first name and the last character of the last name.
# Count the number of characters in the bio (excluding spaces).
# Replace all occurrences of the word "I" with "You" in the bio.

# Instructions:
# Use string methods like .upper(), .lower(), .replace(), .strip(), and .len().

# Sample Input:
# Enter your first name: Neelam
# Enter your last name: Pal
# Enter a short bio: I am a software testing expert and I love teaching Python.

# Expected Output:
# Name in uppercase: NEELAM PAL
# Initials: N P
# Bio Length (excluding spaces): 51
# Modified Bio: You are a software testing expert and You love teaching Python.

first_name= input("Enter first name:")
last_name= input("Enter last name:")
bio= input("Enter short bio:")

full_name= f"{first_name} {last_name}"
name_upper= full_name.upper()
initials= first_name[0]+" "+last_name[0]
# len_bio= len(bio)
# print(f"Length of bio with spaces including: {len_bio}")
lenght_bio= len(bio.replace(" ", ""))
modified_bio= bio.replace("I", "You")

print(f"Your full name is: {full_name}")
print(f"Name in UPPERCASE: {name_upper}")
print(f"Initials:{initials.upper()}")
print(f"Length of bio with spaces excluding: {lenght_bio}")
print(f"Modified BIO: {modified_bio}")

#***************************************************************************

# Coding Program 2: String Analysis - Sentence Analyzer
# Objective:
#  Create a program that takes a sentence as input and performs various string operations.

# Problem Statement:
# Accept a sentence from the user.
# Perform the following string manipulations:
# Count the number of words in the sentence.
# Convert the sentence to lowercase and uppercase.
# Find the position of the first occurrence of the word "Python".
# Check if the sentence starts with "Hello" and ends with a period (.).

# Instructions:
# Use string methods like .lower(), .upper(), .find(), .startswith(), and .endswith().

# Sample Input:
# Enter a sentence: Hello, I am learning Python and I love Python

# Expected Output:
# Number of words: 10
# Sentence in lowercase: hello, i am learning python and i love python.
# Sentence in uppercase: HELLO, I AM LEARNING PYTHON AND I LOVE PYTHON.
# First occurrence of 'Python': 18
# Starts with 'Hello': True
# Ends with '.': False
#
sentence= input("Enter a sentence:")
word_count= sentence.split(" ")
print("Number of words:",len(word_count))
print("Sentence in lowercase:", sentence.lower())
print("Sentence in uppercase:", sentence.upper())
python_position= sentence.replace(" ", "").lower().find("Python")
print(f"First occurence of 'Python': {python_position}")
print("Starts with 'Hello': ",sentence.startswith("Hello"))
print("Ends with '.': ",sentence.endswith("."))

#************************************************************************************

# Coding Program 3: Word Frequency Counter

# Objective:
#  Create a program that accepts a paragraph of text and calculates the frequency of each word.
#  Display the word frequency in descending order.

# Problem Statement:
# Accept a paragraph of text from the user.
# Remove punctuation and convert the text to lowercase.
# Split the text into words and count the occurrence of each word.
# Display the word frequency in descending order of occurrence.

# Instructions:
# Use .lower(), .replace(), .split(), and .strip() methods.

# Use a dictionary to track word frequencies.
# Use the sorted() function with a lambda function to sort by frequency.

# Sample Input:
# Enter a paragraph of text: Python is great. Python is easy. Python is powerful.

# Expected Output:
# Word Frequency:
# python - 3
# is - 3
# great - 1
# easy - 1
# powerful - 1

paragraph = "Python's great. Python is easy. Python is powerful."

for char in string.punctuation:
    paragraph= paragraph.replace(char, "")

paragraph= paragraph.lower()
words= paragraph.split()
print(words)

words_count={}
for word in words:
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word]= 1

print(words_count)
print("Word Frequency:")
for word in words_count:
    print(f"{word} - {words_count[word]}")

#*********************************************************************
# Coding Program 4: Anagram Checker

# Objective:
#  Create a program that checks if two input strings are anagrams of each other,
#  ignoring spaces, punctuation, and capitalization.

# Problem Statement:
# Accept two strings from the user
# Remove all spaces and punctuation, and convert the strings to lowercase.
# Check if the sorted versions of both strings are identical.
# If they are, print "Anagram"; otherwise, print "Not an Anagram".
# Instructions:
# Use .lower(), .replace(), and sorted() methods.
# Handle punctuation using string.punctuation.

# Sample Input:
# Enter the first string: Listen
# Enter the second string: Silent!
#
# Expected Output:
# Anagram

first_string= input("Enter first string:")
second_string= input("Enter second string:")
first_string= first_string.lower().replace(" ", "")
second_string= second_string.lower().replace(" ", "")

for char in string.punctuation:
    first_string= first_string.replace(char, "")
    second_string = second_string.replace(char, "")

sorted_first_string= sorted(first_string)
sorted_second_string= sorted(second_string)
# print(sorted_first_string)
# print(sorted_second_string)

if sorted_first_string == sorted_second_string:
    print("Anagram")
else:
    print("Not Anagram")

# *************************************************************
# Coding Program 5: Palindrome Detector
# Objective:
#  Create a program that checks if a given string is a palindrome, ignoring spaces, punctuation, and capitalization.

# Problem Statement:
# Accept a string input from the user.

# Instructions:
# Use .lower(), .replace(), and slicing for palindrome check.

# Sample Input:
# Enter a string:
# A man, a plan, a canal, Panama
# amanaplanacanalpanama
# amanaplanacanalpanama

# Expected Output:
# Palindrome

