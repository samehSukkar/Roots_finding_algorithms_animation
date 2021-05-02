
#Newton's method explained : https://www.math.ubc.ca/~pwalls/math-python/roots-optimization/newton/

from matplotlib.animation import FuncAnimation
from matplotlib import pyplot as plt
from numpy import cos ,sin, exp ,linspace


# Define f(x)
def f(x): 
    return  3*x + sin(x) - exp(x)

# Define f(x) derivative
def fp(x): 
    return 3 + cos(x)- exp(x)

#Newton method
def newton(x , tol=0.001 , n=10) :
    counter=1
    l = [[0,x,f(x)]]
    while(abs(f(x)) > tol) :
        x = x - f(x)/fp(x)
        l.append([counter,x , f(x)])
        counter+=1
    return l

# -- applying Newton method -- 
#specify starting points X0

x0 =1.5
n_values= newton(x0)

for i in n_values:
    print(*i)
    

# Define x data range for tangent line
def xrange(x1):
  return linspace(x1-0.5, x1+0.5, 100)

# Define tangent line 
# y = m*(x - x1) + y1
def line(x):
    slope = fp(x)
    y1 = f(x)
    return slope*(xrange(x) - x) + y1



# Define x data range f(x)
x = linspace(-5,5,1000)  

# set figure
fig = plt.figure()
plt.xlim(0,3)
plt.ylim(-1,1.5)
plt.grid()

#Lines
f_line = plt.plot(x, f(x) )
x_axis = plt.axhline(0 , color = 'r')
tang , = plt.plot( xrange(x0), line(x0), 'C1--', linewidth = 2)


#Animation
def animate(i) :
 
    new_x = n_values[i][1]
    tang.set_xdata(xrange(new_x))
    tang.set_ydata(line(new_x))
    p = plt.scatter(new_x, f(new_x), color='r', s=25)
    l = plt.legend([p,], ['x ='+str(new_x)] , loc=2)
    
    return tang , p , l 

anime = FuncAnimation(fig , animate ,repeat = True, frames= len(n_values) , interval=500 ,repeat_delay=3000, blit=True)

plt.show()