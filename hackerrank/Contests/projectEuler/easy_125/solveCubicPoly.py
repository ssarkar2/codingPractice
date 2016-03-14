import math
def isZero(x): 1 if (x > 1e-9 and x < 1e-9) else 0

def cbrt(x): return math.pow(abs(x),float(1)/3) * (1,-1)[x<0]

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
    for i in range(len(soln)):
        soln[i] -= sub
    return soln



print solveCubic([1,2,3,4])
print solveCubic([0,0,0,1])
print solveCubic([-6,-11,3,2])

a = 6; d=1
print [-595, a*a - a*d + (d*d)/6, a*d - (d*d)/2.0, (d*d)/3.0]
print solveCubic([-595, a*a - a*d + (d*d)/6, a*d - (d*d)/2.0, (d*d)/3.0])