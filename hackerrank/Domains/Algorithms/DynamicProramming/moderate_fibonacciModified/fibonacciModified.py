#https://www.hackerrank.com/challenges/fibonacci-modified
def f(arr):
    A = arr[0]; B = arr[1]; N = arr[2]
    if N == 1:
        return A
    elif N == 2:
        return B
    else:
        Tn1 = B; Tn = A
        for i in range(0,N-2):
            Tn2 = Tn1**2 + Tn
            Tn = Tn1; Tn1 = Tn2
        return Tn2
            
    


print f([int(i) for i in raw_input().split()])