#importregion
from math import sqrt, pi, exp
#endregion
def Probability(PDF, args, c, GT=True)
    '''
    Use Simpson Rule to integrate PDF
    Result is the probability x<c or x>c dependent on the GT boolean
    '''