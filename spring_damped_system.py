import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation as FA
from scipy.integrate import odeint
m=1#kg
k=30#N/m
C=3#N*s/m
def dSdt(t,S):
    x,v_x=S
    return v_x,-k*x/m-C*v_x/m
x_0=0.3
v_x_0=0
S_0=(x_0,v_x_0)
t=np.linspace(0,3.7,300)
sol=odeint(dSdt,y0=S_0,t=t,tfirst=True)
v_x_sol=sol.T[1]
x_sol=sol.T[0]
fig,ax=plt.subplots()
ax.set_ylim(-1.2,1.2)
ax.set_xlim(0,3.7)
ax.set_ylabel('displacement [m],velocity [m/s]')
ax.set_xlabel('time [s]')
ax.set_title('x(t),v_x(t)')
plt.axhline(0,color='blue',linestyle='--')
t_val=[]
x_val=[]
v_val=[]
line_x,=ax.plot([],[],color='red',label='x(t)')
line_v,=ax.plot([],[],color='orange',label='v_x(t)')
def update(frame):
    t_val.append(t[frame])
    x_val.append(x_sol[frame])
    v_val.append(v_x_sol[frame])
    line_x.set_data(t_val,x_val)
    line_v.set_data(t_val,v_val)
    return line_x,line_v
ani=FA(fig,update,frames=len(t),interval=100,blit=True,repeat=False)
plt.grid()
plt.legend()
plt.show()
