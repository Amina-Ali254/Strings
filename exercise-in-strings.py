#  Create a python program to reverse a string?

# def reverse_string(input_string):
#     return input_string[::-1]
# # input_string = "hello" 
# print ("Reversed string:", reverse_string("hello"))

# Exercise 2

# Create a python program to check whether a string is pallindrome.
        # A word that reads the same both backwards and forwards
        #  eg. civic, refer, level, madam

# def is_palindrome(input_string):
#     return input_string == input_string [::-1]
# input_string = "madam"
# print("Is Palindrome:", is_palindrome(input_string))

# def is_palindrome(input_string):
#     return input_string == input_string [::-1]
# input_string = "school"
# print("Is Palindrome:", is_palindrome(input_string))

# Exercise 3
# Create a python program to check whether one string is an anagram of the other. 
        # Two strings are said to beanagram if we can form one string by arranging the characters of another string.
        # For example, Race and Care. Here, we can form Race by arranging the characters of Care.
        # More examples are paws/wasp, hare/hear, wolf/flow, clam/calm

# def is_anagram(string1, string2):
#  return sorted(string1) == sorted(string2)
# string1 = "wolf"
# string2 = "flow"
# print("Is Anagram:", is_anagram(string1, string2))


def is_anagram(string1, string2):
 return sorted(string1) == sorted(string2)
string1 = "goat"
string2 = "sheep"
print("Is Anagram:", is_anagram(string1, string2))