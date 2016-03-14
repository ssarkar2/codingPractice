#https://www.hackerrank.com/contests/projecteuler/challenges/euler125
import math
def isZero(x): 1 if (x > 1e-6 and x < 1e-6) else 0
def cbrt(x): return math.pow(abs(x),float(1)/3) * (1,-1)[x<0]

def findMaxA(N, d):
    #min 2 terms are needed
    # a^2 + (a+d)^2 > N
    #a*2 + ad + (d^2 - N)/2 > 0
    #t1 = 1; t2 = d; t3 = (d*d - N)/2.0
    D = 2*N - d*d #discriminant
    return int(math.floor((math.sqrt(D) + d)/2)) if D>0 else 0


def solveCubic(coeff):
    # normal form: x^3 + Ax^2 + Bx + C = 0
    A = coeff[2]/float(coeff[3])
    B = coeff[1]/float(coeff[3])
    C = coeff[0]/float(coeff[3])

    #substitute x = y - A/3 to eliminate quadric term:
    #x^3 +px + q = 0

    sq_A = A*A
    p = 1.0/3 * (- 1.0/3 * sq_A + B)
    q = 1.0/2 * (2.0/27 * A * sq_A - 1.0/3 * A * B + C);

    #use Cardano's formula
    cb_p = p * p * p
    D = q * q + cb_p

    if isZero(D):
        if isZero(q):  #one triple soln
            soln = [0]
        else: #one single and one double solution
            u = cbrt(-q)
            soln = [2*u, -u]
    elif D<0: #Casus irreducibilis: three real solutions
        phi = 1.0/3 * math.acos(-q / math.sqrt(-cb_p));
        t = 2 * math.sqrt(-p)
        soln = [t*math.cos(phi), - t * math.cos(phi + math.pi / 3), - t * math.cos(phi - math.pi / 3)]
    else: #one real soln
        sqrt_D = math.sqrt(D)
        u = cbrt(sqrt_D - q)
        v = cbrt(sqrt_D + q)
        soln = [u+v]

    sub = 1/3.0 * A
##    for i in range(len(soln)):
##        soln[i] -= sub
##        if soln[i] > 0:
##            return soln[i] #only 1 positive root is expected  (return max(soln[i]) - sub)
##    print soln
##    return soln#if this is returned it will result in error. should not return this
    print max(soln) - sub
    return max(soln) - sub



def getNextBatch(prevBatch, numDigits): #numDigits in current batch
    if prevBatch==[]:
        return [1,2,3,4,5,6,7,8,9]
    elif prevBatch == [1,2,3,4,5,6,7,8,9]:
        return [11,22,33,44,55,66,77,88,99]
    else:
        c = 0;
        if numDigits%2 == 1:
            out = [0]*len(prevBatch)
            for i in prevBatch:
                t1 = (numDigits-1)/2; t2 = 10**t1; t3 = 10*t2
                out[c] = (i/t2)*t3 + (i%t3); c += 1;
        else:
            out = [0]*len(prevBatch)*10;
            for i in prevBatch:
                t1 = numDigits/2; t2 = 10**t1; t3 = 10*t2
                h1 = i/t2; h2 = i%t2; #divide the number into 2
                for j in range(0,10): #insert a new digit in the middle
                    out[c] = h1*t3 + j*t2 + h2; c+= 1
        return out

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = [False, None]

    while first<=last and not found[0]:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = [True, alist[midpoint]]
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found


def sumSq(a,n,d):
    return n*a*a + a*d*n*(n-1) + (d*d*n*(n-1)*(2*n-1))/6

def checkPalindromes(a, N, d):
    numdigits = int(math.ceil(math.log(N+0.1,10)))  #0.1 added for numbers of form 10**n
##    if numdigits == 1:
##        #only 1 case: 1*1 + 2*2 = 5
##        if N >= 5 and d == 1:
##            return [(1,2)] #a=1, n=2
##        else:
##            return []

    out = []
    prevPalins = []
    for i in range(1,numdigits):
        currPalins = getNextBatch(prevPalins, i-1)  #currPalins is sorted by construction
        #print i,currPalins
        n = 2
        while(1):
            t1 = sumSq(a,n,d)
            #print a,n,d, t1
            if t1 > N:
                break
            t = binarySearch(currPalins, t1)
            n+=1
            if t[0] == True:
                out.append([a,n,t[1]])

        prevPalins = currPalins
    return out


##N = int(raw_input())
##inputs = []
##for i in range(N):
##    x = [int(j) for j in raw_input().split()]
##    inputs.append(x)
#inputs = [[1000,1], [1000,2]]
inputs =[  [1, 1], [5, 1], [6, 1], [1000000000, 1000000000]]
inputs =[ [ 10000, 10],[ 1000000000, 4],[ 6443625136, 11],[ 3258325512, 5]]  #3763 38286115288 214716296540 90392249883.

for i in inputs:
    N = i[0]
    d = i[1]
    amax = findMaxA(N,d)
    #print 'xxx', amax
    out = []
    for a in range(1,amax):
        print a, amax
        t = checkPalindromes(a, N, d)
        out = out + [i[2] for i in t]
    print sum(out)
    #print 'xxxxxxxxxxxxxx'

#print inputs
#Now sum of a^2 + (a+d)^2 ... + (a+(n-1)*d)^2 (n terms) = na^2 + adn(n-1) + (1/6)n(n-1)(2n-1)d^2
# which in terms of a cubic poly in n equals: (n^3 * d^2)/3 + n^2(ad - (d^2)/2) + n(a^2 - ad + (d^2)/6)
