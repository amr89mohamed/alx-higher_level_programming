#!/usr/bin/python3
def islower(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    elif ord(c) >= ord('A') and ord(c) <= ord('Z'):
        return False
    else:
        return False
