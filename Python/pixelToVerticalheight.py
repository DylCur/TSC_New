
import os

while True:

    pixel = input("Enter the number of pixels: ")
    
    if(pixel.isnumeric == False):
        break

    print(f"{float(pixel) / 10.8}")

    input("Press enter to exit.")
    os.system("cls")
    
    
    
# In this script, you input an amount of pixels to be converted. The pixels
# will be converted to css vh on a 1080p monitor. The maths involved is:
# pixels / (monitor height / 100)

# For example, if i enter 100 pixels to be converted:
# 100 / ((1800 / 100) ≡ 10.8) = 9.25925925925926

# The result will be rounded to the most appropriate amount of s.f.

# In this case, the most appropriate answer would be 9.259 (4 s.f.)
    
    

