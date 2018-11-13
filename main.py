import math
from random import *

def _func(x,y):
    return -abs(math.sin(x)*math.cos(y)*math.exp(abs(1-math.sqrt(x**2 + y**2)/math.pi)))

def _prob(dE, T):
    return math.exp(-dE/T)

def _generateState():
    x = uniform(-10, 10)
    y = uniform(-10, 10)
    return _func(x, y)

def akurasi(Fa, Fr):
    return (1 - abs((Fa-Fr)/Fr))*100

T_start = 225
T_end = 0.0001
cr = 0.99998

current_state = _generateState()
best_state = current_state

while T_start >= T_end:
    next_state = _generateState()
    dE = next_state - current_state
    if dE < 0:
        current_state = next_state
        best_state = current_state
    else:
        P = _prob(dE, T_start)
        R = random()
        if P > R:
            current_state = next_state
            best_state = current_state
    T_start = T_start*cr

print("Hasil : ", best_state)
print("Akurasi : ", akurasi(best_state, -19.2085), "%")