import numpy as np

def OR(x1, x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.2
    output = np.sum(w*x) + b

    if output <= 0:
        return 0
    elif output > 0:
        return 1

def AND(x1, x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.7
    output = np.sum(w*x) + b

    if output <= 0:
        return 0
    elif output > 0:
        return 1


print(OR(0,0))
print(OR(0,1))
print(OR(1,0))
print(OR(1,1))

print(AND(0,0))
print(AND(0,1))
print(AND(1,0))
print(AND(1,1))
