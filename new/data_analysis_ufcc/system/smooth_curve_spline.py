import numpy as np
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt

#Dataset
slide = np.array([20,40,60,80,100])   #aberturas de slide


vel_mag00=np.array([59.88,79.89,90.92,96.12,97.14])
mag_range = np.array([7.88,11.39,12.18,12.88,14.62])

MagSpline00 = make_interp_spline(slide,vel_mag00)
MagmaxSpline00 = make_interp_spline(slide,vel_mag00+mag_range)
MagminSpline00 = make_interp_spline(slide,vel_mag00-mag_range)

vel_mag10=np.array([72.27,95.58,106.14,114.14,118.56])
mag_range = np.array([11.15,16.13,18.55,19.55,17.95])

MagSpline10 = make_interp_spline(slide,vel_mag10)
MagmaxSpline10 = make_interp_spline(slide,vel_mag10+mag_range)
MagminSpline10 = make_interp_spline(slide,vel_mag10-mag_range)

vel_mag20=np.array([64.11,85.87,97.47,105.42,108.68])
mag_range = np.array([17.83,25.56,27.39,31.27,31.97])

MagSpline20 = make_interp_spline(slide,vel_mag20)
MagmaxSpline20 = make_interp_spline(slide,vel_mag20+mag_range)
MagminSpline20 = make_interp_spline(slide,vel_mag20-mag_range)

vel_mag30=np.array([62.71,75.89,88.07,95.25,101.31])
mag_range = np.array([22.78,28.89,31.76,35.89,36.99])

MagSpline30 = make_interp_spline(slide,vel_mag30)
MagmaxSpline30 = make_interp_spline(slide,vel_mag30+mag_range)
MagminSpline30 = make_interp_spline(slide,vel_mag30-mag_range)

X_ = np.linspace(slide.min(), slide.max(), 500)

Mag00 = MagSpline00(X_)
Magmax00 = MagmaxSpline00(X_)
Magmin00 = MagminSpline00(X_)

Mag10 = MagSpline10(X_)
Magmax10 = MagmaxSpline10(X_)
Magmin10 = MagminSpline10(X_)

Mag20 = MagSpline20(X_)
Magmax20 = MagmaxSpline20(X_)
Magmin20 = MagminSpline20(X_)

Mag30 = MagSpline30(X_)
Magmax30 = MagmaxSpline30(X_)
Magmin30 = MagminSpline30(X_)

# Plotting the Graph
plt.figure(dpi=150)
# plt.plot(X_, U, linestyle='--', linewidth=0.8, color='red', label=r'$\overline{u}$')
# plt.fill_between(X_,Umin,Umax,color='red',alpha=0.1)

# plt.plot(X_, V, linestyle='--', linewidth=0.8, color='blue',label=r'$\overline{v}$')
# plt.fill_between(X_,Vmin,Vmax,color='blue',alpha=0.1)

# plt.plot(X_, W, linestyle='--', linewidth=0.8, color='gray',label=r'$\overline{w}$')
# plt.fill_between(X_,Wmin,Wmax,color='gray',alpha=0.4)

plt.plot(X_, Mag00, linestyle='--', linewidth=0.8, color='black')
# plt.fill_between(X_,Magmin00,Magmax00,color='red',alpha=0.1)

plt.plot(X_, Mag10, linestyle='--', linewidth=0.8, color='blue')
# plt.fill_between(X_,Magmin10,Magmax10,color='blue',alpha=0.1)

plt.plot(X_, Mag20, linestyle='--', linewidth=0.8, color='red')
# plt.fill_between(X_,Magmin20,Magmax20,color='black',alpha=0.1)

plt.plot(X_, Mag30, linestyle='--', linewidth=0.8, color='green')
# plt.fill_between(X_,Magmin30,Magmax30,color='orange',alpha=0.1)

# plt.plot(slide,u,'o',color='black')
# plt.plot(slide,v,'*',color='black')
# plt.plot(slide,w,'+',color='black')
plt.plot(slide,vel_mag00,'o',color='black', label=r'$00m$')
plt.plot(slide,vel_mag10,'*',color='blue', label=r'$10m$')
plt.plot(slide,vel_mag20,'+',color='red', label=r'$20m$')
plt.plot(slide,vel_mag30,'v',color='green', label=r'$30m$')


plt.xlabel("Abertura da válvula 'Slide' (%)")
# plt.ylabel("Velocidade média à jusante (m/s)")
plt.ylabel("Média da velocidade à jusante (m/s)")
plt.legend(loc='upper left')
plt.tight_layout()        
plt.grid(linestyle='--', linewidth=0.3)

path = '/media/alejandro/Seagate Expansion Drive/Backup_Freddy/UFCC_project/FTP_final/data_analysis/system/fluid'
output = path+'/velmag_mag_system.png'
plt.savefig(output)