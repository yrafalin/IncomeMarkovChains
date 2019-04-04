from transitions_inequality import variables as data
import sympy
import numpy as np
from random import random

a = data['All_P_Transition']

# Adjusts for some quintiles not equaling 1
a[0][0] = 0.2877
a[0][1] = 0.2193
a[0][2] = 0.1761
a[0][4] = 0.1192

def simGrow(q1, q2, n, tran=a):
    q1 -= 1
    q2 -= 1
    gens = []
    for i in range(n):
        gen = 0
        _q1 = q1
        while(_q1 != q2):
            _tran = list(map(lambda x: x[_q1], tran))  # meaning lowest quintile is 1, highest is 5
            rand = random()
            _q1 = np.random.choice(list(range(5)), 1, p=_tran)[0] # Chooses random quintile given a list of their probabilities
            gen += 1
        gens.append(gen)
    return sum(gens)/len(gens)

print(simGrow(1, 5, 10000))
