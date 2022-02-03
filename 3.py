def count_number(n1,n2):
    '''
    Input two numbers n1 and n2. Output total number of numbers between n1 and n2 that have repeated digits
    INPUT : 90 110
    OUTPUT : 4
    INPUT : 20 30
    OUTPUT : 1
    '''
    count = 0
    for i in range(n1,n2+1,1):
        a=[0]*10
        while (i>0):
            rm = i%10
            a[rm]=a[rm]+1
            i=i//10
        for j in range(10):
            if a[j]>1:
                count = count +1
    return(count)               
n1 = int(input())
n2 = int(input())
print(count_number(n1,n2))