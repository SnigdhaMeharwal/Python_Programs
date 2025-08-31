import string

first_string = input("Enter the first string: ")
second_string = input("Enter the second string: ")

for char in string.punctuation:
    first_string = first_string.replace(char, "").lower()
    second_string = second_string.replace(char, "").lower()

sorted_first_string = sorted(first_string)
sorted_second_string = sorted(second_string)
if sorted_first_string == sorted_second_string:
    print("Anagram")
else:
    print("Not Anagram")
