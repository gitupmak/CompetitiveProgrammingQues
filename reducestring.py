def reduce_string(s):
    '''
    Given a string with multiple characters that are repeated consecutively. You’re supposed to reduce the size of this string using mathematical logic 
    given as in the example below :
    Input :     aabbbbeeeeffggg
    Output:     a2b4e4f2g3
    '''
    count = 1
    str1 = ""
    for i in range (len(s)-1):
        if (s[i] == s[i+1]):
            count = count +1
        else:
            if(count==1):
                str1 = str1 + s[i]
            else:
                str1 = str1 + s[i] + str(count)
            count=1 
    if(count==1):
        str1 = str1 + s[i+1]
    else:
        str1 = str1 + s[i+1] + str(count)
    return str1           

s = input()
print(reduce_string(s))