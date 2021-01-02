import random
import numpy as np
import timeit

def f(x):
    return np.sin(x)

random.seed(45)
def MonteCarloIntegration(n):
    random.seed(45)
    m=0
    for i in range(n):
        # 0<= random.random() <=1
        x_random=a+(b-a)*random.random()
        y_random=fmin+(fmax-fmin)*random.random()
        if y_random<=f(x_random):
            m+=1
    return m

a=0
b=np.pi # b>a
N=1000
x=np.linspace(a,b,N)
y=f(x)
fmin=min(y)
fmax=max(y)
Area_rectangle=abs(b-a)*abs(fmax-fmin)

start = timeit.default_timer()
M=MonteCarloIntegration(N)
end = timeit.default_timer()

integral=(M/N)*Area_rectangle
print("Integral of sin(x) between {a} and {b} = {L}".format(a=a,b=b,L=integral))
print('\n')
print("Run time:",end-start) 
