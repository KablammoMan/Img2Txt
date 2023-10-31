import numpy as np
import tqdm
import cv2
import os


def average(img: np.ndarray, chnlst: np.ndarray) -> int:
    avg = 0
    for i in range(img.shape[2]):
        avg += chnlst[i]
    avg = int(avg/3)
    return avg


H = "#" * 20
WIDTH = 200

if "nt" in os.name.lower():
    home = "C:"
else:
    home = f"\\home"

print("Path to Image:")
path = input(f"{home}\\Img2Txt\\ImgPath> ")
while not os.path.exists(path):
    print()
    print("That path does not exist!\n")
    print("Path to Image:")
    path = input(f"{home}\\Img2Txt\\ImgPath> ")
print()
image = cv2.imread(path)
scaleF = WIDTH/image.shape[1]
newh = int(scaleF*image.shape[0])
newd = (WIDTH, newh)
image = cv2.resize(image, newd)

timg = ""
for row in tqdm.trange(image.shape[0]):
    for col in range(image.shape[1]):
        sm = average(image, image[row][col])
        timg += f"\033[38;2;{image[row][col][2]};{image[row][col][1]};{image[row][col][0]}m"
        if sm <= 31:
            timg += " "
        elif sm <= 63:
            timg += "."
        elif sm <= 95:
            timg += "^"
        elif sm <= 127:
            timg += "!"
        elif sm <= 159:
            timg += "$"
        elif sm <= 191:
            timg += "@"
        elif sm <= 223:
            timg += "#"
        else:
            timg += "%"
    timg += "\n"
print(timg)
