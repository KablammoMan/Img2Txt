import numpy as np
import tqdm
import cv2
import os

def average(img: np.ndarray, chnlst: np.ndarray) -> int:
    """
    Calculate the average value of the channels in an image.

    Args:
        img (np.ndarray): Input image.
        chnlst (np.ndarray): Array of channel values.

    Returns:
        int: Average value of the channels.
    """
    avg = 0
    for i in range(img.shape[2]):
        avg += chnlst[i]
    avg = int(avg/3)
    return avg

# Constants
WIDTH = 150

# Determine the home directory based on the operating system
if "nt" in os.name.lower():  # Windows
    home = "C:"
else:  # Unix-based systems
    home = f"\\home"

print("Path to Image:")
# Prompt the user to enter the path to the image
path = input(f"{home}\\Img2Txt\\ImgPath> ")
# Validate the path by checking if it exists
while not os.path.exists(path):
    print()
    print("That path does not exist!\n")
    print("Path to Image:")
    path = input(f"{home}\\Img2Txt\\ImgPath> ")
print()

# Read the image using OpenCV
image = cv2.imread(path)
# Scale the image width to a fixed value while maintaining the aspect ratio
scaleF = WIDTH/image.shape[1]
# Calculate the new height based on the scaling factor
newh = int(scaleF*image.shape[0])
newd = (WIDTH, newh)
# Resize the image
image = cv2.resize(image, newd)

# ASCII characters used for representing the image
ASCII = '!@#$%^&-+=.?:"~ '
# ASCII characters sorted by intensity for mapping pixel values to ASCII characters
SORTED_ASCII = ' ."^-~+=:!?&#$%@'

timg = ""
# Iterate over each row of the image
for row in tqdm.trange(image.shape[0]):
    # Iterate over each column of the image
    for col in range(image.shape[1]):
        # Calculate the average intensity of the pixel channels
        sm = average(image, image[row][col])
        # Add the appropriate escape sequence for setting the text color based on the pixel values
        timg += f"\033[38;2;{image[row][col][2]};{image[row][col][1]};{image[row][col][0]}m"
        # Map the average intensity to an ASCII character and append it to the text image representation
        timg += SORTED_ASCII[int(sm // (256 / len(SORTED_ASCII)))]
    timg += "\n"
print(timg)
