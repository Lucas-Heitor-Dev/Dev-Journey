import time
import numpy as np
import matplotlib.pyplot as plt
import math

Width = 300 #Horizontal
Length = 250 #Vertical
ITER = 50 # Max Iteration

Color_Map = "magma"

X_MIN, X_MAX = -2.0, 1.0 # (Real Part)
Y_MIN, Y_MAX = -1.0, 1.0 # (Imaginary Part)
C_JULIA = complex(-0.8, 0.156)



start = time.monotonic()

Mode = "Mandelbrot"

def flee_time(z, c):
    for n in range(ITER):
        if abs(z) > 2:
            return n
        z = z * z + c
    return ITER

def pixel_for_complex(column, line):
    real = X_MIN + (column / Width ) * (X_MAX - X_MIN)
    imagi = Y_MAX - (line / Width) * (Y_MAX - Y_MIN)
    return complex(real, imagi)

def calculate_fractal():

    image = np.zeros((Width, Length))

    for line in range(Width):
        for column in range(Length):
            point = pixel_for_complex(column, line)

        if Mode == "Mandelbrot":
            image[line, column] = flee_time(0, point)
        else:
            image[line, column] = flee_time(point, C_JULIA)


    return image


if __name__ == "__main__":
    print("Calculating...")
    image = calculate_fractal()
    image[image == ITER] = 0
    plt.title("Conjunct" + Mode)
    plt.ylabel("Imaginary Part")
    plt.xlabel("Real Part")
    plt.imshow(image, cmap=Color_Map, extent=(X_MIN, X_MAX, Y_MIN, Y_MAX))
    plt.show()


end = time.monotonic()
print("Algorithm Time: ", start - end)
