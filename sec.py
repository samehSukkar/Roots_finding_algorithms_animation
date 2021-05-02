

#secant method explained: https://www.math.ubc.ca/~pwalls/math-python/roots-optimization/secant/



import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from numpy import sin, exp ,linspace

# Define f(x)
def f(x):
    return 3*x + sin(x) - exp(x)

#secant method
def secant(x0,x1 , tol = 0.0001 , n=100) :
    values = []
    counter = 1
    if abs(x0) < abs(x1) : 
        x0 , x1 = x1 , x0

    x2 =10
    while abs(f(x2)) > tol and counter <= n:

        x2 = x0 - f(x0) * (x0 - x1 ) /( f(x0) - f(x1) )

        values.append([counter,x0,x1,x2])
        x0 = x1
        x1=x2
        counter+=1       
    return values

# -- applying secant method -- 
#specify starting points X0 , X1
sec_values = secant(2,1 , tol=0.0000001)

for i in sec_values :
  print(*i)



#define x and y ranges
x = linspace(-3,3,1000)
y = f(x)

# -- Plot --
fig , ax = plt.subplots()
plt.ylim(-1,1.5)
plt.xlim(0,3)
plt.grid()

# -- lines --

fun = ax.plot(x,y , 'c')
x_axis = plt.axhline(0 , color = 'r')
v0 = plt.axvline(x = 0, color = 'b',linewidth=3, linestyle = '--' , alpha=0.5)
v1 = plt.axvline(x = 0, color = 'y',linewidth=3, linestyle = '--' , alpha=0.5)
sec_line, = plt.plot(0,0, color='black' , linewidth=3)

# -- animation --

def animate(i):
    
    x0 = sec_values[i][1]
    x1 = sec_values[i][2]
    sec_line.set_xdata([x0,x1])
    sec_line.set_ydata([f(x0),f(x1)])
    v0.set_xdata(x0)
    v1.set_xdata(x1)
    l = ax.legend([v0, v1 ] , ['x0 ='+str(x0) , 'x1 = '+str(x1)] , loc=2)
    return v0 , v1 , l , sec_line


anime = FuncAnimation(fig , animate ,repeat = True, frames= len(sec_values) , interval=1000 ,repeat_delay=3000, blit=True)

plt.show()

