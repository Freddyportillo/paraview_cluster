import numpy as np
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt

#Dataset
slide = np.array([20,40,60,80,100])   #aberturas de slide

u = np.array([58.69,78.46,89.28,94.10,95.33])
u_range = np.array([15.30,22.00,23.38,24.99,28.12])
u_range /= 2.0

v = np.array([2.13,3.72,5.66,6.28,5.57])
v_range = np.array([19.95,24.75,28.39,31.48,31.08])
v_range /= 2.0

w = np.array([1.11,1.11,0.91,1.30,1.61])
w_range = np.array([12.35,16.12,17.56,20.77,19.37])
w_range /= 2.0

USpline = make_interp_spline(slide,u)
UmaxSpline = make_interp_spline(slide,u+u_range)
UminSpline = make_interp_spline(slide,u-u_range)

VSpline = make_interp_spline(slide,v)
VmaxSpline = make_interp_spline(slide,v+v_range)
VminSpline = make_interp_spline(slide,v-v_range)

WSpline = make_interp_spline(slide,w)
WmaxSpline = make_interp_spline(slide,w+w_range)
WminSpline = make_interp_spline(slide,w-w_range)

X_ = np.linspace(slide.min(), slide.max(), 500)

U = USpline(X_)
Umax = UmaxSpline(X_)
Umin = UminSpline(X_)

V = VSpline(X_)
Vmax = VmaxSpline(X_)
Vmin = VminSpline(X_)

W = WSpline(X_)
Wmax = WmaxSpline(X_)
Wmin = WminSpline(X_)

# Plotting the Graph
plt.figure(dpi=150)
plt.plot(X_, U, linestyle='--', linewidth=0.8, color='red', label=r'$\overline{u}$')
plt.fill_between(X_,Umin,Umax,color='red',alpha=0.1)

plt.plot(X_, V, linestyle='--', linewidth=0.8, color='blue',label=r'$\overline{v}$')
plt.fill_between(X_,Vmin,Vmax,color='blue',alpha=0.1)

plt.plot(X_, W, linestyle='--', linewidth=0.8, color='gray',label=r'$\overline{w}$')
plt.fill_between(X_,Wmin,Wmax,color='gray',alpha=0.4)

plt.plot(slide,u,'o',color='black')
plt.plot(slide,v,'*',color='black')
plt.plot(slide,w,'+',color='black')
plt.xlabel("Abertura da válvula 'Slide' (%)")
plt.ylabel("Velocidade média à jusante (m/s)")
plt.legend(loc='upper left')
plt.tight_layout()        
plt.grid(linestyle='--', linewidth=0.3)

plt.show()