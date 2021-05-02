
#bisection method explained: https://www.math.ubc.ca/~pwalls/math-python/roots-optimization/bisection/

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from numpy import sin, exp ,linspace

# Define f(x)
def f(x):
    return 3*x + sin(x) - exp(x)

#bisection method
def bisec(x0,x1 , tol = 0.001 , n=100) :

    if f(x0)*f(x1)> 0 : return 0  , ['no roots between x0 x1 ',]

    values = []
    counter=1
    while abs(x0-x1)/2 > tol and counter <= n:
        x2 = (x0+x1)/2
        values.append([counter,x0,x1,x2])

        if f(x2) == 0 :
           return values
        elif f(x0)*f(x2) <0 :
            x1 = x2
        else :
            x0 = x2
        counter+=1

    return 1 , values


is_bracket , bis_values = bisec(1,2 , tol=0.001)
for i in bis_values : print(i)




x = linspace(-3,3,1000)
y = f(x)

#set figure
fig , ax = plt.subplots()
plt.ylim(-1,1.5)
plt.xlim(0,3)
plt.grid()

#Lines
fun = ax.plot(x,y , 'c')
x_axis = plt.axhline(0 , color = 'r')
v0 = plt.axvline(x = 0, color = 'blue',linewidth=3, linestyle = '--' )
v1 = plt.axvline(x = 0, color = 'gold',linewidth=3, linestyle = '--' )


#Animation
def animate(i):
    
    x0 = bis_values[i][1]
    x1 = bis_values[i][2]
    
    v0.set_xdata(x0)
    v1.set_xdata(x1)
    l = ax.legend([v0, v1 ] , ['x0 ='+str(x0) , 'x1 = '+str(x1)] , loc=2)
    return v0 , v1 , l

if (is_bracket) :
    anime = FuncAnimation(fig , animate ,repeat = True, frames= len(bis_values) , interval=1000 ,repeat_delay=3000, blit=True)

plt.show()
