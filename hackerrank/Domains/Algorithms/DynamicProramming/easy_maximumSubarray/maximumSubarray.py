
def f(inp):
    sumNonContag = 0; flag = 0
    for i in inp:
        if i >= 0:
            sumNonContag += i
            flag = 1
    if (flag == 0):  #in case there are only negative numbers
        sumNonContag = max(inp)

    N = len(inp)
    maxSum = None
    allarr = []
    for i in range(N): #initialize and set sums of subarray length = 1
        arr = [None]*(N-i) #if subarray starts at i location, it can go upto atmost N-1-i (exclusive)..so it has length N-i
        #print i, arr[0], inp[i]
        arr[0] = inp[i] #sum(inp[i:i+1] = inp[i])
        allarr.append(arr)
        maxSum = [maxSum,arr[0]][maxSum < arr[0]]

    for ln in range(2,N+1): #subarrays of length 2 to N
        for start in range(0, N-ln+1):  #possible starting locations. the +1 is added as range is exclusive on the 2nd argument
            #print start, ln, allarr[start][ln-2], allarr[start+1][ln-1]
            t = inp[start] + allarr[start+1][ln-2]
            maxSum = [maxSum,t][maxSum < t]
            allarr[start][ln-1] = t
    #print allarr
    print maxSum, sumNonContag



#inp = [2, -1, 2, 3, 4, -5]
#f(inp)

inp = [1,2,3,-4,6, 0, -5, -100, 55]
f(inp)

##num = int(raw_input())
##for i in range(num):
##    arrlen = int(raw_input())
##    inp = [int(i) for i in raw_input().split()]
##    f(inp)
