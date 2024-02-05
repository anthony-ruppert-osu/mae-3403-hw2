#importregion
import math
from math import cos
#endregion

def Secant(fcn, x0, x1, maxiter=10, xtol=1e-5):
    """
    Secant method will find the root of the callback function (fcn)
    The value of x should make fcn=0 (or very close to)
    :param fcn: function that I want to find the root of
    :param x0: initial guess for the root (or guess 1)
    :param x1: second initial guess for the root (or guess x0+1)
    :param maxiter: maximum number of iterations
    :param xtol:  exit tolerance if the |xnewest - xprevious| < xtol
    :return: tuple with: (the final estimate of the root (most recent value of x), number of iterations)
    """
    delta = (x1-x0)  #seed value of delta w/ initial guesses
    x = x1
    fold = fcn(x0)  #the value of the callback @ x0
    fnew = fold
    Niter = 0  #counting variable for the number of iterations
    while Niter < maxiter and abs(delta) > xtol:
        fNew = fcn(x)
        delta = (-fNew * (x - x0)) / (fNew - fold)
        x0 = x
        x += delta
        fold = fNew
        Niter += 1
    return x, Niter

def main():
    """
        This tests the secant methdd for finding the roots of equations
       fn1:  x-3cos(x)=0; with x0=1, x1= 2, maxiter = 5 and xtol = 1e-4
       fn2:  cos(2x)*x**3; with x0=1, x1= 2, maxiter = 15 and xtol = 1e-8
       fn2:   with x0=1, x1= 2, maxiter = 3 and xtol = 1e-8
    :return: nothing
    """
    #Defining functions
    fn1 = lambda x: x-3*math.cos(x) # lambda represents some anonymous function with interchangeable variable x
    fn2 = lambda x: (math.cos(2 * x) * x ** 3)  # same as above except 2nd function, cos(2x)*(x^3)

    maxiter1 = 5
    maxiter2 = 15
    maxiter3 = 3

    #use lamba & secant function to plug conditions into either of the functions
    r1 = Secant(fn1, 1, 2, 5,1e-4)
    r2 = Secant(fn2, 1,2,15, 1e-8)
    r3 = Secant(fn2,1,2,3,1e-8)

    #Print statements
    print("root of fn1 = {:.4f}, after {:d} iterations".format(r1[0], r1[1]))
    print("root of fn2 = {:.4f}, after {:d} iterations".format(r2[0], r2[1]))
    print("root of fn3 = {:.4f}, after {:d} iterations".format(r3[0], r3[1]))

if __name__=="__main__":
    main()