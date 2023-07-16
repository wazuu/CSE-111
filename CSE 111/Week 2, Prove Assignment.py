import math
from datetime import datetime

width = float(input("Please enter the width of your vehicles tire in mm (ex 185): "))
ratio = float(input("Please enter the aspect ratio of your vehicles tire (ex 70): "))
diameter = float(input("Please enter the diameter of your vehicles wheel in inches (ex 17): "))

top = math.pi * width **2 * ratio * (width * ratio + 2540 * diameter)
bottom = top / 10000000000

bottom = round(bottom, 1)

print(f"The approximate volume of your vehicles tires are {bottom} liters")

current_date_and_time = datetime.now()

with open("volumne.txt", "at") as volumne_file:
    print(f"{current_date_and_time: %Y-%m-%d}, {width}, {ratio}, {diameter}, {bottom:.2f}", file=volumne_file)