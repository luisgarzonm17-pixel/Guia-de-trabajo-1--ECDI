import numpy as np
import matplotlib.pyplot as plt

# Campo de pendientes
x = np.linspace(-5, 5, 25)
y = np.linspace(-5, 5, 25)

X, Y = np.meshgrid(x, y)

DY = X + Y
DX = np.ones_like(DY)

M = np.sqrt(DX**2 + DY**2)

DX = DX / M
DY = DY / M

plt.figure(figsize=(10, 7))

plt.quiver(X, Y, DX, DY, color="gray")

# Familia de soluciones
xx = np.linspace(-5, 2, 500)

for C in [-4, -2, -1, 0, 1, 2, 4]:
    yy = C * np.exp(xx) - xx - 1

    # Evitar que las curvas se salgan demasiado de la gráfica
    yy[np.abs(yy) > 5] = np.nan

    plt.plot(xx, yy)

# Solución particular
yp = np.exp(xx + 2) - xx - 1
yp[np.abs(yp) > 5] = np.nan

plt.plot(xx, yp, linewidth=3, label="Solución particular")

plt.scatter([-2], [2], s=50, label="y(-2)=2")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Ejercicio b: y' = x + y")
plt.grid()
plt.legend()
plt.ylim(-5, 5)

plt.show()