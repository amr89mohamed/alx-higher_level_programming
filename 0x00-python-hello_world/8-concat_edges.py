#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
  language that combines remarkable power with very clear syntax"
str = str.split()
print(" ".join(str[5:7] + [str[12] + " " + str[0]]))
