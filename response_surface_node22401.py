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

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make data.
y = np.array([0, 10, 20, 30])
x = np.array([20, 40, 60, 80, 100])
x, y = np.meshgrid(x, y)
z = np.array([
    [0.79,1.10,1.21,1.38,1.45],
    [0.88,1.21,1.30,1.44,1.54],
    [0.83,1.28,1.45,1.74,1.64],
    [1.07,1.72,2.31,2.52,2.54]])

z_std = np.array([
    [0.42,0.58,0.65,0.74,0.75],
    [0.47,0.68,0.75,0.87,0.92],
    [0.55,0.91,1.08,1.20,1.25],
    [0.74,0.99,1.08,1.14,1.10]])

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

degree=3 # Grau do polinomio
reg=make_pipeline(PolynomialFeatures(degree),LinearRegression())

# Fit
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)

y_pred, y_test

yy = np.arange(0,31)
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

# Customize the z axis.
ax.set_zlim(0.0, 1.10*np.max(target_predito))
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=10)
ax.scatter(x,y,z,'o',color='black')
ax.set_title(r'node: 22401')
ax.set_ylabel(r'Válvula "Main" $(°)$')
ax.set_xlabel(r'Válvula "Slide" $(\%)$')
ax.set_zlabel(r'Deslocamento máximo $(mm)$')
plt.grid(linestyle='--')
plt.tight_layout()


plt.show()