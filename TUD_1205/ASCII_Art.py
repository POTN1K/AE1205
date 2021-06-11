# Assignment 6. Conversion of image files into ASCII art.
# Author. Nikolaus Ricker

# ------------------------------------------------------
# Libraries
import numpy as np
import pygame as pg

# ------------------------------------------------------
# Pre-calculated values:

# Dimensions of a single, fixed-width character:
# (determined for Courier New: cour.ttf)
char_width = 12
char_height = 20
char_hw_ratio = char_height / char_width

# A list of characters that you can use in your ASCII art...
characters = ['M', 'W', 'Q', 'B', 'E', 'R', 'N', '@', 'H', 'q', 'p', 'g', 'K', 'A', '#', 'm', 'b', '8', '0', 'd', 'X',
              'D', 'G', 'F', 'P', 'e', 'h', 'U', '9', '6', 'k', 'Z', '%', 'S', '4', 'O', 'x', 'y', 'T', '5', 'w', 'f',
              'a', 'V', 's', '2', 'L', '$', 'Y', '&', 'n', '3', 'C', 'J', 'u', 'o', 'z', 'I', 'j', 'v', 'c', 'r', 't',
              'l', 'i', '1', '=', '?', '7', '>', '<', ']', '[', '(', ')', '+', '*', ';', '}', '{', ':', '/', '\\', '!',
              '|', '_', ',', '^', '-', '~', '.', ' ']
n_characters = len(characters)

# ... and the corresponding grayscale values
grayscale = np.array([217.56944444, 218.82291667, 219.89236111, 220.19444444,
                      222.14583333, 222.94097222, 223.0625, 223.17361111,
                      223.22222222, 223.23958333, 223.45486111, 223.60416667,
                      224.05208333, 224.09722222, 224.33333333, 225.25,
                      225.59722222, 225.62152778, 225.91666667, 225.96180556,
                      226.10763889, 226.74305556, 226.80208333, 227.04861111,
                      227.42361111, 228.45833333, 228.61458333, 228.73958333,
                      228.76736111, 228.80555556, 228.8125, 228.90625,
                      228.98611111, 229.06597222, 229.28472222, 229.61805556,
                      229.96527778, 230.07291667, 230.17361111, 230.21875,
                      230.60416667, 230.62847222, 230.84375, 231.03472222,
                      231.05555556, 231.46875, 231.55555556, 231.9375,
                      232.04861111, 232.07291667, 232.64583333, 232.68055556,
                      233.16319444, 233.53472222, 233.70138889, 234.20833333,
                      234.40625, 234.76388889, 234.93055556, 235.30208333,
                      235.36805556, 235.44791667, 235.5, 236.53472222,
                      237.32986111, 237.67361111, 237.70138889, 238.61458333,
                      238.61805556, 238.78125, 238.78472222, 238.79166667,
                      238.98611111, 239.07638889, 239.08680556, 239.97569444,
                      240.32291667, 240.78125, 241.50694444, 241.57291667,
                      242.25694444, 243.13194444, 243.18055556, 243.31944444,
                      244.30208333, 244.61805556, 245.03819444, 246.62847222,
                      247.58333333, 247.60763889, 248.62847222, 255.0])


# ------------------------------------------------------
# Functions
def C_linear(color):
    # Less than 0.04045
    c1 = color / 12.92
    c2 = ((color + 0.055) / 1.055) ** 2.4
    color = np.where((color <= 0.04045), c1, c2)
    return color


def C_expand(color):
    # Less than 0.0031308
    c1 = color * 12.92
    c2 = 1.055 * (color ** (1 / 2.4)) - 0.055
    color = np.where((color <= 0.0031308), c1, c2)
    return color


def get_char_for_value(val, min=0, max=255, charlist=characters, char_grey=grayscale):
    idx = 0
    min_grey = np.min(char_grey)
    max_grey = np.max(char_grey)
    x = (max_grey - min_grey) / (max - min) * val + min_grey
    for scale in char_grey:
        if scale >= x:
            idx = np.where(char_grey == scale)
            return charlist[int(idx[0])]
    return charlist[idx]


def print_string(list):
    print(''.join(list))


# ------------------------------------------------------
# Loading an image

file_1 = pg.image.load('./Data/ASCII_Art/ASCII_art.png')
file_2 = pg.image.load('./Data/ASCII_Art/gradient.jpg')
file_3 = pg.image.load('./Data/ASCII_Art/swarm_of_drones.jpg')

# Obtaining color per pixel
red = pg.surfarray.pixels_red(file_3)
blue = pg.surfarray.pixels_blue(file_3)
green = pg.surfarray.pixels_green(file_3)

# Converting to range [0-1]
red = red / 255
blue = blue / 255
green = green / 255

# Linearize values
l_red = C_linear(red)
l_blue = C_linear(blue)
l_green = C_linear(green)

# Linear luminescence
y_linear = 0.2126 * l_red + 0.7152 * l_green + 0.0722 * l_blue

# De-linearize
y = C_expand(y_linear)
y = y * 255

# Create patches
p_width = 12
p_height = int(p_width * char_hw_ratio)

m, n = y.shape
x_patches = int(m / p_width)
y_patches = int(n / p_height)
max = y.max()
min = y.min()

# Create greyscale
for y_ in range(y_patches):
    temp = []
    for x_ in range(x_patches):
        patch = y[x_ * p_width:(x_ + 1) * p_width, y_ * p_height:(y_ + 1) * p_height]
        val = np.average(patch)
        char = get_char_for_value(val, min, max)
        temp.append(char)
    print_string(temp)
