"""
Create a dictionary and take input from the user and return the meaning of the word from the dictionary
"""

caution = "Enter the word to find the meaning of the below words"
print(caution.upper())
print("string, integer, float, python, function")
dictionary = {"string":"material consisting of threads of cotton, hemp or other material twisted together to form a thin length.", "integer":"a number is not a fraction","float":"move or hover slowly and lightly in a liquid or the air.","python":"a large heavy-boiled non-venomous snake occurring throughout the old world topics, killing the prey by constriction and asphyxiation.","function":"an activity that is natural to or the purpose of person or thing."}
words = input()
print(words+":- "+dictionary.get(words))



