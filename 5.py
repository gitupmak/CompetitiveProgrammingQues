def XOR_array(K,A,M):
    '''
    You are given an array of integers A of size N. You perform a certain operation K times on the array A, modifying the array with 
    every operation. The operation is to replace the array A with a new array, which is the XOR of the adjacent elements of A, and of 
    length size(A)-1. You are given an index M, the value of this index in array A after K operations is to be found. 
    Note: Partial points are present

    INPUT :  2 (K) 1 (M) 1 2 3 4 (Array) 
    OUTPUT :  6 
    Explanation Original Array => 1234 Operation 1 => 3 1 7 (1 XOR 2 = 3, 2 XOR 3 =1, 3 XOR 4 = 7) 
    Operation 2 => 2 6 (3 XOR 1 = 2, 1 XOR 7 = 6) M is 1, so after 2 operations, A[1] = 6
    '''
    for i in range(K):
        for j in range(len(A)-1):
            A[j]=A[j]^A[j+1]
        A.pop()
    return(A[M])
K=int(input())
M=int(input())
A=[1,2,3,4]
print(XOR_array(K,A,M))
