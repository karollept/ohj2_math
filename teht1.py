from calendar import day_abbr
from difflib import diff_bytes

import numpy as np
import math
pi = math.pi

#1

a = 2.493
b = 0.911

print("")
print("tehtävä 1")
print(np.degrees(a))
print(np.degrees(b))

#2

c = 137.7
d = 62.3

print("")
print("tehtävä 2")
c = c * pi/180
print(c)

d = d * pi/180
print(d)

#3
d_a = 30
r_d_a = d_a * pi/180

d_b = 45
r_d_b = d_b * pi/180

d_c = 60
r_d_c = d_c * pi/180

d_d = 90
r_d_d = d_d * pi/180

d_e = 120
r_d_e = d_e * pi/180

d_f = 135
r_d_f = d_f * pi/180

d_g = 150
r_d_g = d_g * pi/180

d_h = 185
r_d_h = d_h * pi/180

d_i = 270
r_d_i = d_i * pi/180

d_j = 360
r_d_j = d_j * pi/180

def display_menu():
    print ("aste\t\tradiaani")
    print ("---------------------------------------------------------------")
    print (f"{d_a}\t\t{r_d_a}")
    print (f"{d_b}\t\t{r_d_b}")
    print (f"{d_c}\t\t{r_d_c}")
    print (f"{d_d}\t\t{r_d_d}")
    print (f"{d_e}\t\t{r_d_e}")
    print (f"{d_f}\t\t{r_d_f}")
    print (f"{d_g}\t\t{r_d_g}")
    print (f"{d_h}\t\t{r_d_h}")
    print(f"{d_i}\t\t{r_d_i}")
    print(f"{d_j}\t\t{r_d_j}")
    print ("---------------------------------------------------------------")
print("")
print("tehtävä 3")
display_menu()