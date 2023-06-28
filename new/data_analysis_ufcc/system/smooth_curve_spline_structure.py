import numpy as np
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt

#Dataset
slide = np.array([20,40,60,80,100])   #aberturas de slide

disp_mag00=np.array([0.83,1.16,1.26,1.45,1.51])
mag_range00 = np.array([0.43,0.58,0.68,0.71,0.77])

MagSpline00 = make_interp_spline(slide,disp_mag00)
MagmaxSpline00 = make_interp_spline(slide,disp_mag00+mag_range00)
MagminSpline00 = make_interp_spline(slide,disp_mag00-mag_range00)

disp_mag10=np.array([0.94,1.27,1.34,1.51,1.59])
mag_range10 = np.array([0.50,0.69,0.76,0.85,0.90])

MagSpline10 = make_interp_spline(slide,disp_mag10)
MagmaxSpline10 = make_interp_spline(slide,disp_mag10+mag_range10)
MagminSpline10 = make_interp_spline(slide,disp_mag10-mag_range10)

disp_mag20=np.array([0.85,1.32,1.51,1.74,1.66])
mag_range20 = np.array([0.55,0.90,1.0,1.18,1.20])

MagSpline20 = make_interp_spline(slide,disp_mag20)
MagmaxSpline20 = make_interp_spline(slide,disp_mag20+mag_range20)
MagminSpline20 = make_interp_spline(slide,disp_mag20-mag_range20)

disp_mag30=np.array([1.08,1.70,2.22,2.43,2.44])
mag_range30 = np.array([0.75,1.02,1.15,1.23,1.19])

MagSpline30 = make_interp_spline(slide,disp_mag30)
MagmaxSpline30 = make_interp_spline(slide,disp_mag30+mag_range30)
MagminSpline30 = make_interp_spline(slide,disp_mag30-mag_range30)

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

plt.plot(X_, Mag00, linestyle='--', linewidth=0.8, color='black')
plt.plot(X_, Mag10, linestyle='--', linewidth=0.8, color='blue')
plt.plot(X_, Mag20, linestyle='--', linewidth=0.8, color='red')
plt.plot(X_, Mag30, linestyle='--', linewidth=0.8, color='green')


plt.plot(slide,disp_mag00,'o',color='black', label=r'$00m$')
plt.plot(slide,disp_mag10,'*',color='blue', label=r'$10m$')
plt.plot(slide,disp_mag20,'o',color='red', label=r'$20m$')
plt.plot(slide,disp_mag30,'o',color='green', label=r'$30m$')



plt.xlabel("Abertura da válvula 'Slide' (%)")
# plt.ylabel("Deslocamento nodal médio (mm)")
plt.ylabel("Média da magnitude do deslocamento nodal (mm)")
plt.legend(loc='upper left')
plt.tight_layout()        
plt.grid(linestyle='--', linewidth=0.3)

path = '/media/alejandro/Seagate Expansion Drive/Backup_Freddy/UFCC_project/FTP_final/data_analysis/system/str'
output = path+'/disp_mag_system.png'
plt.savefig(output)
