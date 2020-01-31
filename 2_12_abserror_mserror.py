import matplotlib.pyplot as plt


points = [
        (2,-2),
        (5,6),
        (-4,-4),
        (-7,1),
        (8,14)
        ]

x = [p[0] for p in points]
y = [p[1] for p in points]


line = lambda x: 1.2*x+2

yhat = [line(_x) for _x in x]

#plt.scatter(x, y)
#plt.scatter(x, yhat)
#plt.show()

def abserror(y, yhat):
    errors = []
    for a,b in zip(y, yhat):
        errors.append(abs(a-b))

    return sum(errors)/len(y)

print(abserror(y, yhat))


def mserror(y, yhat):
    errors = []
    for a,b in zip(y, yhat):
        errors.append((a-b)**2)

    return sum(errors)/(2*len(y))

print(mserror(y, yhat))
