def min_fountain(a,N):
    """
    Count minimum number of fountains to be activated to cover the entire garden
    There is a one-dimensional garden of length N. In each position of the N length garden, a fountain has been installed. 
    Given an array a[]such that a[i] describes the coverage limit of ith fountain. A fountain can cover the range from the 
    position max(i – a[i], 1) to min(i + a[i], N). In beginning, all the fountains are switched off. The task is to find the 
    minimum number of fountains needed to be activated such that the whole N-length garden can be covered by water.

    Examples:

    Input: a[] = {1, 2, 1}
    Output: 1
    Explanation:
    For position 1: a[1] = 1, range = 1 to 2
    For position 2: a[2] = 2, range = 1 to 3
    For position 3: a[3] = 1, range = 2 to 3
    Therefore, the fountain at position a[2] covers the whole garden.
    Therefore, the required output is 1.

    Input: a[] = {2, 1, 1, 2, 1} 
    Output: 2 
    """
    
    dp = [0] * N
    for i in range(N):
      dp[i] = -1
  
    for i in range(N):
        idxLeft = max(i - a[i], 0)
        idxRight = min(i + (a[i] + 1), N)
        dp[idxLeft] = max(dp[idxLeft],
                          idxRight)
  
    cntfountain = 1
  
    idxRight = dp[0]
  
    idxNext = 0
  
    # Traverse dp[] array
    for i in range(N):
        idxNext = max(idxNext,
                      dp[i])
  
        # If left most fountain
        # cover all its range
        if (i == idxRight):
            cntfountain += 1
            idxRight = idxNext
  
    return cntfountain
  
  
# Driver code
if __name__ == '__main__':
  
    a = [2, 1, 1, 2, 1]
    N = len(a)
  
    print(min_fountain(a, N))
