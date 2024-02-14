#!/usr/bin/env python3

class MyString:
    
    def __init__(self, value=''):
        self.value = value

    @property
    def value(self):
        "Retrieving value of self"
        return self._value

    @value.setter
    def value(self, value):
        if not isinstance(value, str):
          print("The value must be a string.")
        else:
          self._value = value      
          
    def is_sentence(self):
        return True if self.value.endswith(".") else False

    def is_question(self):
        return True if self.value.endswith("?") else False

    def is_exclamation(self):
        return True if self.value.endswith("!") else False

    def count_sentences(self):
        sentenceCount = 0
        updated = self.value.split()
        # return self.value
        breakpoint()
        for words in updated:
            if words.endswith(".") or words.endswith("?") or words.endswith("!"):
                sentenceCount += 1
        return sentenceCount
        
          


# print 'The value must be a string.' if determined value is not a string.
# to determine if its a string I want to use type(value) == str
# returns True if value ends with a period and False otherwise.
# returns True if value ends with a question mark and False otherwise.
# returns True if value ends with an exclamation mark and False otherwise.
# returns the number of sentences in the value.
  # does a word end with ., !, or ?? then it indicates the end of a sentence.
  # count the words that end with any of these punctuations

# Start by defining a variable to store the count of sentences. Let's call it sentenceCount and initialize it to 0.
# 2 Split the string into an array of words. You can use the split() method in JavaScript to split the string into an array of words based on spaces.

# Iterate over each word in the array and check if it ends with a punctuation mark like ".", "!", or "?". You can use the endsWith() method in JavaScript to check if a word ends with a specific character or string.

# If a word ends with a punctuation mark, increment the sentenceCount variable by 1.

# After iterating through all the words, the sentenceCount variable will hold the count of sentences in the string.

# Finally, return the value of the sentenceCount variable.

# Remember, this is just one approach to estimate the number of sentences. It may not be perfect, as punctuation marks can also be used within sentences. However, it can provide a reasonable estimate in many cases.

# Let me know if you have any questions or need further clarification on any of the steps!

   
