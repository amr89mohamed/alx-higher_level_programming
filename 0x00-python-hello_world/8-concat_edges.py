#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
list = str.split( )
words =  " ".join(list[5:7] + [list[12] + " " + list[0]])
print(words)
