#!/usr/bin/env python3

class MyString:
  def __init__(self, value):
    if isinstance(value,str):
      self.value=value
    else :
      print("The value must be a string.")

  def is_sentence(self):
    if self.value.find("."):
      return True
    else :
      return False
  
  def is_question(self):
    if self.value.find("?"):
      return True
    else :
      return False

  def is_exclamation(self):
    if self.value.find("!"):
      return True
    else :
      return False
    
  def count_sentences(self):
    count = 0
    delimeters=[".","!","?"]
    for delimeter in delimeters:
      self.value.split(delimeter)
      count +=1
    print(count)
string=MyString("This is a string! It has three sentences. Right?")

print(string.is_sentence())
print(string.is_question())
print(string.is_exclamation())
print(string.count_sentences())