import time
import numpy as np
import matplotlib.pyplot as plt
import os

Width = 1000   # Horizontal (colunas)
Length = 1000  # Vertical (linhas)
ITER = 50

Color_Map = "magma"

X_MIN, X_MAX = -2.0, 1.0   # Parte real
Y_MIN, Y_MAX = -1.0, 1.0   # Parte imaginária
C_JULIA = complex(-0.8, 0.156)

Mode = "Mandelbrot"

def flee_time(z, c):
    for n in range(ITER):
        if abs(z) > 2:
            return n
        z = z * z + c
    return ITER

def pixel_for_complex(column, line):
    real = X_MIN + (column / Width) * (X_MAX - X_MIN)
    imagi = Y_MAX - (line / Length) * (Y_MAX - Y_MIN)
    return complex(real, imagi)

def calculate_fractal():
    image = np.zeros((Length, Width))          # linhas x colunas

    for line in range(Length):
        for column in range(Width):
            point = pixel_for_complex(column, line)
            if Mode == "Mandelbrot":           # dentro do loop interno
                image[line, column] = flee_time(0, point)
            else:
                image[line, column] = flee_time(point, C_JULIA)

    return image



if __name__ == "__main__":
    print("Calculating...")
    start = time.monotonic()
    image = calculate_fractal()
    end = time.monotonic()
    print("Algorithm Time:", end - start)

    image[image == ITER] = 0
    plt.title("Conjunct " + Mode)
    plt.ylabel("Imaginary Part")
    plt.xlabel("Real Part")
    plt.imshow(image, cmap=Color_Map, extent=(X_MIN, X_MAX, Y_MIN, Y_MAX))
    print(Mode.__le__)
    plt.savefig(os.path.join(os.path.dirname(os.path.abspath("")), f"{Mode}.png"), dpi=150)
    plt.show()
