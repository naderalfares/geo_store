import sys
import constants.opt_consts as CONSTS

def choose(elements, length):
    """Return the list of all possible combinations
    """
    def __choose(elements, length):
        """ This method is to calculate nCr. i.e., for the given element list and required length,
            calculate all possible combinations of that length.
        """
        for i in range(len(elements)):
            if length == 1:
                yield (elements[i],)
            else:
                for next in __choose(elements[i+1:len(elements)], length-1):
                    yield (elements[i],) + next
    
    return list(__choose(elements, length))

def gen_abd_params(N, f):
    """ Generate possible values of n, q1, q2
    """
    quorum_params = []
    quorum_params_append = quorum_params.append
    for n in range(f+1, N+1):
        for q1 in range(f+1, n-f+1):
            for q2 in range(f+1, n-f+1):
                if q1+q2 > n:
                    quorum_params_append([n, q1, q2])
    return quorum_params

def gen_cas_params(N, f):
    """ Generates all the possible values of n, k, q1, q2, q3, q4 
        for a given value of N = No. od DCs and f = availability target
    """
    quorum_params = []
    quorum_params_append = quorum_params.append
    for n in range(f+1, N+1):
        for k in range(1, n):
            for q1 in range(f+1, n-f+1):
                for q2 in range(f+1, n-f+1):
                    for q3 in range(f+1, n-f+1):
                        for q4 in range(f+1, n-f+1):
                            if q1 + q3 > n and q1 + q4 > n and  q2 + q4 >= n + k and q4 > k:
                                quorum_params_append([n, k, q1, q2, q3, q4])
    return quorum_params

def generate_placements(N, f, protocol):
    """ Generate quorum params based on protocol
    """
    return CONSTS.GEN_PARAM_FUNC[protocol](N, f)
