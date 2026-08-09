# punto a 
import numpy as np
import matplotlib.pyplot as plt

# Campo de pendientes
x = np.linspace(-5, 5, 25)
y = np.linspace(-5, 5, 25)

X, Y = np.meshgrid(x, y)

DY = -Y - np.sin(X)

# Normalizar los vectores
DX = np.ones_like(DY)
M = np.sqrt(DX**2 + DY**2)

DX = DX / M
DY = DY / M

plt.figure(figsize=(10, 7))

plt.quiver(X, Y, DX, DY, color="gray")

# Familia de soluciones
xx = np.linspace(-5, 5, 500)

for C in [-4, -2, -1, 0, 1, 2, 4]:
    yy = C * np.exp(-xx) + (np.cos(xx) - np.sin(xx)) / 2
    plt.plot(xx, yy)

# Solución particular y(0)=1
yp = 0.5 * np.exp(-xx) + (np.cos(xx) - np.sin(xx)) / 2
plt.plot(xx, yp, linewidth=3, label="Solución particular")

plt.scatter([0], [1], s=50, label="y(0)=1")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Ejercicio a: y' = -y - sin(x)")
plt.grid()
plt.legend()
plt.ylim(-5, 5)

plt.show()





#punto b 
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



#punto c 
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Ecuación diferencial
def ecuacion(x, y):
    return -x**2 + np.sin(y[0])

# Campo de pendientes
x = np.linspace(-3, 3, 25)
y = np.linspace(-5, 5, 25)

X, Y = np.meshgrid(x, y)

DY = -X**2 + np.sin(Y)
DX = np.ones_like(DY)

M = np.sqrt(DX**2 + DY**2)

DX = DX / M
DY = DY / M

plt.figure(figsize=(10, 7))

plt.quiver(X, Y, DX, DY, color="gray")

# Diferentes condiciones iniciales
condiciones = [-4, -2, 0, 2, 4]

for y0 in condiciones:

    solucion = solve_ivp(
        ecuacion,
        [-3, 3],
        [y0],
        dense_output=True,
        max_step=0.02
    )

    xx = np.linspace(-3, 3, 500)
    yy = solucion.sol(xx)[0]

    plt.plot(xx, yy, label=f"y(0)={y0}")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Ejercicio c: y' = -x² + sin(y)")
plt.grid()
plt.legend()
plt.ylim(-5, 5)

plt.show()


#punto d 

import numpy as np
import matplotlib.pyplot as plt

# Campo de pendientes
x = np.linspace(-5, 5, 25)
y = np.linspace(-5, 5, 25)

X, Y = np.meshgrid(x, y)

# Despejamos y'
# (x²+1)y' + 3xy = 6x
# y' = (6x - 3xy)/(x²+1)

DY = (6 * X - 3 * X * Y) / (X**2 + 1)

DX = np.ones_like(DY)

M = np.sqrt(DX**2 + DY**2)

DX = DX / M
DY = DY / M

plt.figure(figsize=(10, 7))

plt.quiver(X, Y, DX, DY, color="gray")

# Familia de soluciones
xx = np.linspace(-5, 5, 500)

for C in [-10, -5, -2, -1, 0, 1, 2, 5, 10]:

    yy = 2 + C / (xx**2 + 1)**(3/2)

    plt.plot(xx, yy)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Ejercicio d: (x²+1)y' + 3xy = 6x")
plt.grid()
plt.ylim(-5, 5)

plt.show()


#punto e 

import numpy as np
import matplotlib.pyplot as plt

# Campo de pendientes
x = np.linspace(-4, 4, 25)
y = np.linspace(-5, 3, 25)

X, Y = np.meshgrid(x, y)

DY = X * np.exp(Y)

DX = np.ones_like(DY)

M = np.sqrt(DX**2 + DY**2)

DX = DX / M
DY = DY / M

plt.figure(figsize=(10, 7))

plt.quiver(X, Y, DX, DY, color="gray")

# Familia de soluciones
xx = np.linspace(-3, 3, 1000)

# Diferentes valores de C
for C in [1, 2, 3, 4, 6, 10]:

    argumento = C - xx**2 / 2

    # La función solo existe cuando el argumento es positivo
    yy = np.full_like(xx, np.nan)

    valido = argumento > 0

    yy[valido] = -np.log(argumento[valido])

    plt.plot(xx, yy, label=f"C={C}")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Ejercicio e: y' = xe^y")
plt.grid()
plt.legend()
plt.ylim(-5, 3)

plt.show()


# punto f 

import numpy as np
import matplotlib.pyplot as plt

# Campo de pendientes
x = np.linspace(-5, 5, 25)
y = np.linspace(-5, 5, 25)

X, Y = np.meshgrid(x, y)

DY = X - Y
DX = np.ones_like(DY)

M = np.sqrt(DX**2 + DY**2)

DX = DX / M
DY = DY / M

plt.figure(figsize=(10, 7))

plt.quiver(X, Y, DX, DY, color="gray")

# Familia de soluciones
xx = np.linspace(-5, 5, 500)

for C in [-4, -2, -1, 0, 1, 2, 4]:

    yy = xx - 1 + C * np.exp(-xx)

    yy[np.abs(yy) > 5] = np.nan

    plt.plot(xx, yy)

# Solución particular
yp = xx - 1 + np.exp(1 - xx)

yp[np.abs(yp) > 5] = np.nan

plt.plot(
    xx,
    yp,
    linewidth=3,
    label="Solución particular"
)

plt.scatter(
    [1],
    [1],
    s=50,
    label="y(1)=1"
)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Ejercicio f: y' = x - y")
plt.grid()
plt.legend()
plt.ylim(-5, 5)

plt.show()