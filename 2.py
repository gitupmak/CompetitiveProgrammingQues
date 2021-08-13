def kth_element(arr, M, K):
    """
    Given an array arr[] of size N and two integers M and K, the task is to find the array element at the Kth index after performing 
    following M operations on the given array.

    In a single operation, a new array is formed whose elements have the Bitwise XOR values of the adjacent elements of the current array.

    If the number of operations M or the value of K after M operations is invalid then print -1.

    Examples:

    Input: arr[] = {1, 4, 5, 6, 7}, M = 1, K = 2 
    Output: 3 
    Explanation: 
    Since M = 1, therefore, the operation has to be performed only once on the array. 
    The array is modified to {1^4, 4^5, 5^6, 6^7} = {5, 1, 3, 1}. 
    The value of the element at index K = 2 in the updated array is 3.
    """
    temp=[]
    if M < 0 or M >= len(arr):
        return -1
    for j in range (M):
        for i in range (len(arr)-1):
            value = arr[i]^arr[i+1]
            temp.append(value)
        if j < (M-1):
            arr = temp
            temp = []
    if K<0 or K>len(temp):
        return -1
            
    return temp[K]
       
#Given array
arr=[1,2,3,4,5,6]
M=2
K=3
#Function call
print(kth_element(arr,M,K))