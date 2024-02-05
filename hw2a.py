#importregion
from math import sqrt, pi, exp
#endregion

def Probability(PDF, args, c, GT=True):
    """
    Use Simpson Rule to integrate PDF
    Function to calculate the probability x<c or x>c dependent on the GT boolean
    Step 1: unpack args into mu & stDev
    Step 2: compute lhl & rhl for Simpson
    Step 3: package new tuple args1=(mu, stDev, lhl, rhl) to be passed to Simpson
    Step 4: call Simpson w/ GPDF & args1
    Step 5: return probability
    :param PDF: the probability density function to be integrated (callback function)
    :param args: a tuple contains mean, standard deviation (in this order)
    :param c: value chosen for calculating
    :param GT: boolean for choosing if i want to P(x>c) (GT=True) or P(x<c) (GT=False)
    :return: probability value [P(x<c) or P(x>c)]
    """
    mu,sig = args  #args tuple unpacked
    if GT:
        a = c
        b = mu + 5 * sig
    else:
        a = mu - 5 * sig
        b = c
    args1 = (mu, sig)
    P = Simpson(PDF,args1, a, b,100)  #use Simpson to integrate PDF w/ 100 points (numpoint)
    return P

def GPDF(args):
    """
    This is the Gaussian Normal Probability Density Function.
    Includes the parameters mean (mu), standard deviation (sig)
    Step 1: unpack args tuple into x, mu, sig
    Step 2: compute GPDF @ whatever x
    Step 3: return value
    :param args: contains (x, mu, sig) in this order
    :return: value of GPDF @ whatever x
        """
    #Step 1: unpack args
    x, mu, sig = args
    #Step 2: compute GPDF @ whatever x
    f = (1 / (sig * sqrt(2 * pi))) * exp(-0.5 * ((x - mu) / sig) ** 2) #calc f(x) from given x
    #Step 3: return value
    return f #return f(x) value

def Simpson (fx, args, a, b, numpoint=20):
    """
    This will execute the Simpson 1/3 rule for numerical integration which uses quadratic lagrange polynomials for interpolation
    Ref Kryszig p. 831-832,Table 19.4
    The panel size is: dX = abs(a-b) / (2 * numpoint)
    Integral is determined by: I = dX / 3 * (f(0) + fx(numpoint + 4 * sum (f(j)), 1 to n-1, odd) + 2 * (fx(j), 2 to n-2 even))
    Step 1: divide range from x = a to x = b into an even number of parts
    Step 2: compute fx at each value between a & b
    Step 3: sum the even & odd values of fx
    Step 4: return the area beneath fx
    :param fx: function of f to integrate
    :param args: tuple containing parameters for Gaussian Normal Distribution (mu,sig)
    :param a: left hand limit of integration (lhl)
    :param b: right hand limit of integration (rhl)
    :param numpoint: number of points for integration
    :return: value of integral of fx between a & b
    """
    #Step 1: divide range
    mu, sig = args #unpack args
    area = 0 #initial integral value
    m = numpoint
    n = 2 * m #even number of panels
    #Step 2: compute fx
    #this checks to see if a & b are passed incorrectly & puts them in order
    xL = min(a, b)  #lower limit
    xR = max(a,b)  #upper limit
    if xL == xR:
        return 0  #operation will have nothing to do so return 0
    h = (xR - xL) / n  #calc panel width
    area = (fx((xL, mu, sig)) + fx((xR, mu, sig))) #calc fx @ xL & xR
    #Step 3: sum even & odd values of fx
    for j in range(1, n):
        x = j * h + xL
        if not j % 2 == 0:  #odd
            area += 4 * fx((x, mu, sig))
        else:  #even
            area += 2 * fx((x, mu, sig))
    #Step 4: return the area beneath fx
    return (h / 3) * area  #return integral value

def main():
    """
    I want to integrate the Guassian probability density function between a lhl & a rhl
    Step 1: Decide mu, sig, a, & b
    Step 2: Define args
    Step 3: Display user inputs
    """
    #Step 1: Decide mu, sig, a, & b
    mu = 0
    sig = 1
    a = -5
    b = 0
    #endregion

    #Step 2: Define args
    f = GPDF((0,0,1))
    print("p={:0.5f}".format(f))

    p = Simpson(GPDF, (mu, sig), a, b, 100)
    print("p={:0.5f}".format(p))

    p1 = Probability(GPDF, (0, 1), 0, True)
    print("p1={:0.5f}".format(p1))
    #endregion

    #Step 3: Display user inputs
    mean = input("Population mean? ")
    stDev = input("Standard deviation?")
    c = input("c value?")
    GT = True if input("Probability greater than c?").lower() in ["y","yes","true"] else "False"
    print("P(x"+(">" if GT else "<") + c +"|"+mean+", "+stDev +")")
    pass
    #endregion

if __name__ == "__main__":
    main()
