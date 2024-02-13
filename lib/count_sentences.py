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
        breakpoint()
        for words in self.value:
          print(len(words.endswith(".")))
        
          


# print 'The value must be a string.' if determined value is not a string.
# to determine if its a string I want to use type(value) == str
# returns True if value ends with a period and False otherwise.
# returns True if value ends with a question mark and False otherwise.
# returns True if value ends with an exclamation mark and False otherwise.
# returns the number of sentences in the value.
  # does a word end with ., !, or ?? then it indicates the end of a sentence.
  # count the words that end with any of these punctuations

        
