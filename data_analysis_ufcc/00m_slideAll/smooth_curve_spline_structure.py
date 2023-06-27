import numpy as np
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt

#Dataset
slide = np.array([20,40,60,80,100])   #aberturas de slide

u = np.array([-0.06,-0.09,-0.13,-0.18,-0.14])
u_range = np.array([1.16,1.60,1.73,1.96,1.79])
u_range /= 2.0

v = np.array([0.07,0.12,0.17,0.22,0.20])
v_range = np.array([1.45,2.02,2.20,2.49,2.28])
v_range /= 2.0

w = np.array([0.00,0.01,0.01,0.01,0.01])
w_range = np.array([0.09,0.1,0.17,0.2,0.24])
w_range /= 2.0

disp_mag=np.array([0.83,1.16,1.26,1.45,1.51])
mag_range = np.array([0.43,0.58,0.68,0.71,0.77])

USpline = make_interp_spline(slide,u)
UmaxSpline = make_interp_spline(slide,u+u_range)
UminSpline = make_interp_spline(slide,u-u_range)

VSpline = make_interp_spline(slide,v)
VmaxSpline = make_interp_spline(slide,v+v_range)
VminSpline = make_interp_spline(slide,v-v_range)

WSpline = make_interp_spline(slide,w)
WmaxSpline = make_interp_spline(slide,w+w_range)
WminSpline = make_interp_spline(slide,w-w_range)

MagSpline = make_interp_spline(slide,disp_mag)
MagmaxSpline = make_interp_spline(slide,disp_mag+mag_range)
MagminSpline = make_interp_spline(slide,disp_mag-mag_range)

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

Mag = MagSpline(X_)
Magmax = MagmaxSpline(X_)
Magmin = MagminSpline(X_)

# Plotting the Graph
plt.figure(dpi=150)
# plt.plot(X_, U, linestyle='--', linewidth=0.8, color='red', label=r'$\overline{x}$')
# plt.fill_between(X_,Umin,Umax,color='red',alpha=0.6)

# plt.plot(X_, V, linestyle='--', linewidth=0.8, color='blue',label=r'$\overline{y}$')
# plt.fill_between(X_,Vmin,Vmax,color='blue',alpha=0.1)

# plt.plot(X_, W, linestyle='--', linewidth=0.8, color='gray',label=r'$\overline{z}$')
# plt.fill_between(X_,Wmin,Wmax,color='black',alpha=0.3)

plt.plot(X_, Mag, linestyle='--', linewidth=0.8, color='black', label=r'$\overline{x}$')
plt.fill_between(X_,Magmin,Magmax,color='red',alpha=0.1)

# plt.plot(slide,u,'o',color='black')
# plt.plot(slide,v,'*',color='black')
# plt.plot(slide,w,'+',color='black')
plt.plot(slide,disp_mag,'o',color='black')
plt.xlabel("Abertura da válvula 'Slide' (%)")
# plt.ylabel("Deslocamento nodal médio (mm)")
plt.ylabel("Média da magnitude do deslocamento nodal (mm)")
# plt.legend(loc='upper left')
plt.tight_layout()        
plt.grid(linestyle='--', linewidth=0.3)

path = '/media/alejandro/Seagate Expansion Drive/Backup_Freddy/UFCC_project/FTP_final/data_analysis/00m_allslides/str'
output = path+'/disp_mag_00m_Allslides.png'
plt.savefig(output)
