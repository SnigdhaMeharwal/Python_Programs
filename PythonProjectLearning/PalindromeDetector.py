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
# Expected Output:
# Palindrome
import string

palindrome_string = input("Enter the string to test for palindrome: ")
palindrome_string = palindrome_string.lower().replace(" ", "")
for char in string.punctuation:
    palindrome_string = palindrome_string.replace(char, "")

palindrome_list = list(palindrome_string)
reversed_palindrome_list = list(reversed(palindrome_list))

if palindrome_list == reversed_palindrome_list:
    print("Palindrome")
else:
    print("Not Palindrome")
