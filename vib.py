import matplotlib.pylab as pylab
import flask as flk
import scipy.integrate
import cgi
# from pylab import plot,xlabel,ylabel,title,legend,figure,subplots

from pylab import arange, array


def func(state, t):
    x, xd = state  # displacement,x and velocity x'
    # g = 9.8 # metres per second**2
    if ch == 2:
        xdd = -((k * x) / m) - ((c * xd) / m)
    else:  # metres per second**2
        print("Spring")
        xdd = ((-k * x) / m)  # + g
    return [xd, xdd]
form=cgi.FieldStorage()

# START OF PROGRAM
#print("Select System")
#print("1.MASS,SPRING")
#k = ch = c = m = 0
ch =2# float(input("Enter Choice"))
k = form.getvalue(stiff)
m = form.getvalue(mass)
c = form.getvalue(dc)
#k = 19000#float(input("Enter Stiffness:"))
#m = 500#float(input("Enter Mass:"))
#if ch == 2:
   # c =900# float(input("Enter Damp'g Coeff.:"))
x0 =0.0# float(input("Enter Initial Displacement:"))
v0 =20.0# float(input("Enter Initial Velocity:"))
state0 = [x0, v0]  # initial conditions [x0 , v0]  [m, m/sec]
ti = 0.0  # initial time
tf = 4.0  # final time
step = 0.0001  # step
t = arange(ti, tf, step)
state = scipy.integrate.odeint(func, state0, t)
x = array(state[:, [0]])
xd = array(state[:, [1]])
# Plotting displacement and velocity
pylab.ion()
pylab.rcParams['figure.figsize'] = (20, 12)
pylab.rcParams['font.size'] = 18
#b=0.0

fig, ax1 = pylab.subplots()
ax2 = ax1.twinx()
ax2.plot(t, xd, 'g--', label=r'$\dot{x} (m/sec)$', linewidth=2.0)
ax1.plot(t, x * 1e3, 'b', label=r'$x (mm)$', linewidth=2.0)
ax2.plot(t, xd, 'g--', label=r'$\dot{x} (m/sec)$', linewidth=2.0)
ax2.legend(loc='lower right')
ax1.legend()
ax1.set_xlabel('time , sec')
ax1.set_ylabel('disp (mm)', color='b')
ax2.set_ylabel('velocity (m/s)', color='g')
pylab.title('System Response')
pylab.grid()
pylab.show(block=True)

'''
    k=spring constant, Newtons per metre
    m=mass, Kilograms
    c=dampign coefficient, Newton*second / meter

    for a mass,spring
        xdd = ((-k*x)/m) + g
    for a mass, spring, damper
        xdd = -k*x/m -c*xd-g
    for a mass, spring, dmaper with forcing function
        xdd = -k*x/m -c*xd-g + cos(4*t-pi/4)
    '''
