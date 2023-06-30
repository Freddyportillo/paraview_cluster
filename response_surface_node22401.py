import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make data.
y = np.array([0, 10, 20, 30, 40, 45])
x = np.array([20, 40, 60, 80, 100])
x, y = np.meshgrid(x, y)
z = np.array([
    [0.79,1.10,1.21,1.38,1.45],
    [0.88,1.21,1.30,1.44,1.54],
    [0.83,1.28,1.45,1.74,1.64],
    [1.07,1.72,2.31,2.52,2.54],
    [1.56,2.19,2.82,2.97,2.94],
    [1.65,2.43,2.73,2.97,2.94]])

z_std = np.array([
    [0.42,0.58,0.65,0.74,0.75],
    [0.47,0.68,0.75,0.87,0.92],
    [0.55,0.91,1.08,1.20,1.25],
    [0.74,0.99,1.08,1.14,1.10],
    [0.53,0.74,0.95,0.96,0.95],
    [0.59,0.72,0.87,0.89,0.86]])

z += z_std

zmin = z-z_std
zmax = z+z_std

# Plot the surface.

surf = ax.plot_surface(x, y, zmin, linewidth=0, antialiased=False,alpha=0.1,color='gray')
surf = ax.plot_surface(x, y, zmax, linewidth=0, antialiased=False,alpha=0.1,color='gray')
surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(0.0, 1.1*np.max(zmax))
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

ax.scatter(x,y,z,'o',color='black')

# plt.show()

df = pd.DataFrame()
for i in range(len(z)):
  x1 = x[i]
  x2 = y[i]
  targ = z[i]

  dfi = pd.DataFrame.from_dict({"x1":x1,
                               "x2":x2,
                               "targ":targ})
  df = pd.concat([df,dfi], ignore_index=True)

data_columns = ["x1","x2"]
target_column = ["targ"]

# Selecionando os dados de treino e teste
"""
Observação: caso queira obter um intervalo de confiança retira a seed,
executa o treino e teste n-vezes e calcule a estatistica
"""
X_train, X_test, y_train, y_test = train_test_split(df[data_columns], df[target_column], random_state=0)

degree = 4 # Grau do polinomio
reg=make_pipeline(PolynomialFeatures(degree),LinearRegression())

# Fit
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)

y_pred, y_test

yy = np.arange(0,46)
xx = np.arange(20,101)
xx, yy = np.meshgrid(xx, yy)

df_teste = pd.DataFrame()
for i in range(len(xx)):
  x1 = xx[i]
  x2 = yy[i]
  dfi = pd.DataFrame.from_dict({"x1":x1,
                                "x2":x2})
  df_teste = pd.concat([df_teste,dfi], ignore_index=True)

# Previsão
y_exp_predito = reg.predict(df_teste)

# Transformando em um array 2d para plot
x1 = np.reshape(df_teste.x1.values, xx.shape)
x2 = np.reshape(df_teste.x2.values, xx.shape)
target_predito = np.reshape(y_exp_predito, xx.shape)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})


# Plot the surface.
surf = ax.plot_surface(x1, x2, target_predito, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False,alpha=0.8)

imax, jmax = np.where(target_predito == np.amax(target_predito))
imin, jmin = np.where(target_predito == np.amin(target_predito))

print('max: ',np.max(target_predito), 'Slide :', x1[imax[0],jmax[0]],'Main :', x2[imax[0],jmax[0]] )#, 'x2:',x2[np.argmax(target_predito)])

max_value = np.max(target_predito)
max_slide = x1[imax[0],jmax[0]]
max_main = x2[imax[0],jmax[0]]

min_value = np.min(target_predito)
min_slide = x1[imin[0],jmin[0]]
min_main = x2[imin[0],jmin[0]]

max_info = rf'máx. valor = {max_value:4.2f} mm   Slide: {max_slide} %   Main: {max_main:4.1f} °'
min_info = rf'min. valor = 0.00 mm   Slide: {min_slide} %   Main: {min_main:4.1f} °'

# Calcular o RMSE
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("RMSE:", rmse)
rmse_info = rf'RMSE = {rmse:4.2f} mm'

# Calcular o R²
r2 = r2_score(y_test, y_pred)

print("R²:", r2)

r2_info = rf'R² = {r2:4.2f}'

# Customize the z axis.
ax.set_zlim(0.0, 1.10*np.max(target_predito))
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=10,location='left')
ax.scatter(x,y,z,'o',color='black')
ax.set_title(r'node: 22401')
ax.set_ylabel(r'Válvula "Main" $(°)$')
ax.set_xlabel(r'Válvula "Slide" $(\%)$')
ax.set_zlabel(r'Deslocamento máximo $(mm)$')
plt.plot([],[],' ',label=max_info)
plt.plot([],[],' ',label=min_info)
plt.plot([],[],' ',label=rmse_info+'  '+r2_info)
ax.view_init(elev=23,azim=160,roll=0)
plt.legend(loc='best')
plt.grid(linestyle='--')
plt.tight_layout()

path = '/media/alejandro/Seagate Expansion Drive/Backup_Freddy/UFCC_project/FTP_final/data_analysis/surface_response'
output = path+'/surface_response_node22401_max.png'
plt.savefig(output)

plt.show()