import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Gerar dados aleatórios de entrada
# np.random.seed(0)
n_samples = 100
x = np.random.uniform(-10, 10, size=(n_samples, 2))
y = np.sin(np.sqrt(x[:, 0]**2 + x[:, 1]**2)) + np.random.normal(0, 0.1, size=n_samples)

# Criar os termos polinomiais
poly = PolynomialFeatures(degree=3)
x_poly = poly.fit_transform(x)

# Realizar a regressão polinomial
model = LinearRegression()
model.fit(x_poly, y)

# Gerar uma malha de pontos para criar a superfície
n_points = 100
x_mesh = np.linspace(-10, 10, n_points)
y_mesh = np.linspace(-10, 10, n_points)
x_mesh, y_mesh = np.meshgrid(x_mesh, y_mesh)
xy_mesh = np.column_stack((x_mesh.ravel(), y_mesh.ravel()))
xy_mesh_poly = poly.transform(xy_mesh)
z_mesh = model.predict(xy_mesh_poly)
z_mesh = z_mesh.reshape(x_mesh.shape)

# Plotar a superfície de resposta
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x_mesh, y_mesh, z_mesh, cmap='viridis')

# Configurar os rótulos dos eixos
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Mostrar o gráfico
plt.show()