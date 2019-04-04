from transitions_inequality import variables as data
import sympy
import numpy as np

def get_value(nparray):
    return [round(x[0]) for x in nparray.tolist()]

# White stabilization
print('White stabilization')
w = data['white_population_distribution']
prev_w = np.array([[0]])

while get_value(w) != get_value(prev_w):
    prev_w = w
    w = data['White_P_Transition'].dot(w)
    print([round(x[0]) for x in w.tolist()])

# Hispanic stabilization
print('Hispanic stabilization')
w = data['hisp_population_distribution']
prev_w = np.array([[0]])

while get_value(w) != get_value(prev_w):
    prev_w = w
    w = data['Hispanic_P_Transition'].dot(w)
    print([round(x[0]) for x in w.tolist()])

# Black stabilization
print('Black stabilization')
w = data['black_population_distribution']
prev_w = np.array([[0]])

while get_value(w) != get_value(prev_w):
    prev_w = w
    w = data['Black_P_Transition'].dot(w)
    print([round(x[0]) for x in w.tolist()])

# Asian stabilization
print('Asian stabilization')
w = data['asian_population_distribution']
prev_w = np.array([[0]])

while get_value(w) != get_value(prev_w):
    prev_w = w
    w = data['Asian_P_Transition'].dot(w)
    print([round(x[0]) for x in w.tolist()])

# AIAN stabilization
print('AIAN stabilization')
w = data['aian_population_distribution']
prev_w = np.array([[0]])

while get_value(w) != get_value(prev_w):
    prev_w = w
    w = data['AIAN_P_Transition'].dot(w)
    print([round(x[0]) for x in w.tolist()])
