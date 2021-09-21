def hash_string(str):
    '''A function that accepts, a string which length is “len”, the string has some “#”, in it you have to move all the hashes to the front of the string and 
    return the whole string back and print it.'''
    x = str.count("#")
    s = str.replace("#", "")
    return ("#"*x+s)

s = input()
print(hash_string(s))