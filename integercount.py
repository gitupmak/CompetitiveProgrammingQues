def integer_count(a):
    '''
    You’re given an array of integers, print the number of times each integer has occurred in the array.
    '''
    b = []
    for i in a:
        if i not in b:
            c = a.count(i)
            print(f"{i} occurs {c} times")
        b.append(i)

a = [1, 2, 3, 2, 5, 1]
integer_count(a)