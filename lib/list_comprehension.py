#!/usr/bin/env python3

def return_evens(num_list):
    # Using a list comprehension, write a function return_evens() that returns a list of all of the even elements of a sequence of integers.
    return [num for num in num_list if num % 2 == 0]
numbers = [0, 1, 3, 5, 7, 8, 9]
print(return_evens(numbers))


def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]
sentences = ["Hello", "I'm doing great", "Python is fun"]
print(make_exclamation(sentences))
