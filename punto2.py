#punto A 
import numpy as np
import matplotlib.pyplot as plt

def f(y):
    return y * (3 - y) * (y - 2)

# Puntos críticos
puntos = [0, 2, 3]

# Eje vertical
y = np.linspace(-1, 4, 500)

plt.figure(figsize=(8, 5))

# Línea del eje de fase
plt.axhline(0, color="black", linewidth=1)

# Flechas según el signo de y'
intervalos = [(-1, 0), (0, 2), (2, 3), (3, 4)]

for a, b in intervalos:
    medio = (a + b) / 2

    if f(medio) > 0:
        plt.arrow(
            medio, 0, 0, 0.7,
            head_width=0.08,
            head_length=0.15,
            length_includes_head=True
        )
    else:
        plt.arrow(
            medio, 0, 0, -0.7,
            head_width=0.08,
            head_length=0.15,
            length_includes_head=True
        )

# Puntos críticos
for p in puntos:
    plt.scatter(0, p, s=100, zorder=5)
    plt.text(0.08, p, f"y = {p}", va="center")

plt.xlim(-0.5, 0.8)
plt.ylim(-1, 4)
plt.xticks([])
plt.ylabel("y")
plt.title("Diagrama de fase - Ejercicio a")
plt.grid(axis="y", alpha=0.3)

plt.show()


#punto B 
import numpy as np
import matplotlib.pyplot as plt

def f(y):
    return y**2 - y**3

puntos = [0, 1]

plt.figure(figsize=(8, 5))
plt.axhline(0, color="black", linewidth=1)

intervalos = [(-1, 0), (0, 1), (1, 2)]

for a, b in intervalos:
    medio = (a + b) / 2

    if f(medio) > 0:
        plt.arrow(
            medio, 0, 0, 0.7,
            head_width=0.08,
            head_length=0.15,
            length_includes_head=True
        )
    else:
        plt.arrow(
            medio, 0, 0, -0.7,
            head_width=0.08,
            head_length=0.15,
            length_includes_head=True
        )

for p in puntos:
    plt.scatter(0, p, s=100, zorder=5)
    plt.text(0.08, p, f"y = {p}", va="center")

plt.xlim(-0.5, 0.8)
plt.ylim(-1, 2)
plt.xticks([])
plt.ylabel("y")
plt.title("Diagrama de fase - Ejercicio b")
plt.grid(axis="y", alpha=0.3)

plt.show()


#Punto C 

import numpy as np
import matplotlib.pyplot as plt

def f(y):
    return (y + 2) * (10 + 3*y - y**2)

puntos = [-2, 5]

plt.figure(figsize=(8, 5))
plt.axhline(0, color="black", linewidth=1)

intervalos = [(-4, -2), (-2, 5), (5, 7)]

for a, b in intervalos:
    medio = (a + b) / 2

    if f(medio) > 0:
        plt.arrow(
            medio, 0, 0, 0.7,
            head_width=0.08,
            head_length=0.15,
            length_includes_head=True
        )
    else:
        plt.arrow(
            medio, 0, 0, -0.7,
            head_width=0.08,
            head_length=0.15,
            length_includes_head=True
        )

for p in puntos:
    plt.scatter(0, p, s=100, zorder=5)
    plt.text(0.08, p, f"y = {p}", va="center")

plt.xlim(-0.5, 0.8)
plt.ylim(-4, 7)
plt.xticks([])
plt.ylabel("y")
plt.title("Diagrama de fase - Ejercicio c")
plt.grid(axis="y", alpha=0.3)

plt.show()


#punto D 

import numpy as np
import matplotlib.pyplot as plt

def f(y):
    return y**5 - 4*y**3 - 5*y**2

punto_aprox = 2.456

puntos = [0, punto_aprox]

plt.figure(figsize=(8, 5))
plt.axhline(0, color="black", linewidth=1)

intervalos = [(-2, 0), (0, punto_aprox), (punto_aprox, 4)]

for a, b in intervalos:
    medio = (a + b) / 2

    if f(medio) > 0:
        plt.arrow(
            medio, 0, 0, 0.7,
            head_width=0.08,
            head_length=0.15,
            length_includes_head=True
        )
    else:
        plt.arrow(
            medio, 0, 0, -0.7,
            head_width=0.08,
            head_length=0.15,
            length_includes_head=True
        )

for p in puntos:
    plt.scatter(0, p, s=100, zorder=5)
    plt.text(0.08, p, f"y = {p:.3f}", va="center")

plt.xlim(-0.5, 0.8)
plt.ylim(-2, 4)
plt.xticks([])
plt.ylabel("y")
plt.title("Diagrama de fase - Ejercicio d")
plt.grid(axis="y", alpha=0.3)

plt.show()


#Punto E 

import numpy as np
import matplotlib.pyplot as plt

def f(y):
    return (1 - y) * (y - 2)**3

puntos = [1, 2]

plt.figure(figsize=(8, 5))
plt.axhline(0, color="black", linewidth=1)

intervalos = [(0, 1), (1, 2), (2, 3)]

for a, b in intervalos:
    medio = (a + b) / 2

    if f(medio) > 0:
        plt.arrow(
            medio, 0, 0, 0.7,
            head_width=0.08,
            head_length=0.15,
            length_includes_head=True
        )
    else:
        plt.arrow(
            medio, 0, 0, -0.7,
            head_width=0.08,
            head_length=0.15,
            length_includes_head=True
        )

for p in puntos:
    plt.scatter(0, p, s=100, zorder=5)
    plt.text(0.08, p, f"y = {p}", va="center")

plt.xlim(-0.5, 0.8)
plt.ylim(0, 3)
plt.xticks([])
plt.ylabel("y")
plt.title("Diagrama de fase - Ejercicio e")
plt.grid(axis="y", alpha=0.3)

plt.show()


 

