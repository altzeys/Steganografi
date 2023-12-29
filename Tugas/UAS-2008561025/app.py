import os
import time
from datetime import datetime
from PIL import Image


def encode():
    inputImage = input("Enter image name: ")
    image = Image.open(inputImage + ".png", 'r')

    data = input("Enter data to be encoded: ")
    if (len(data) == 0):
        raise ValueError('Data is empty')

    res = []
    res.append(len(data))
    for index, x in enumerate(data):
        res.append(ord(data[index]))

    new_image = []
    image_d = image.getdata()

    for index, x in enumerate(image_d):
        if (index) <= res[0]:
            temp = (image_d[index][0], res[index], image_d[index][2])
            new_image.append(temp)
        else:
            new_image.append(image_d[index])

    now = datetime.now()
    image.putdata(new_image)
    image.save(now.strftime("%d-%m-%Y-%H-%M-%S" + ".png"))
    print(f'data insert to image {inputImage} success')
    time.sleep(2)


def decode():
    inputImage = input("Enter image name: ")
    image = Image.open(inputImage + ".png", 'r')
    image_d = image.getdata()

    res = str()
    for x in range(image_d[0][1]):
        res += (chr(image_d[x + 1][1]))

    print(f'Decoded Word : {res}')
    time.sleep(2)


while True:
    os.system('cls')
    print("Program Encoded Decoded PNG image")
    print("-------------")
    print("1. Encode")
    print("2. Decoded")
    print("3. Exit")

    pilihan = int(input("Input pilihan: "))

    if (pilihan == 1):
        encode()

    elif (pilihan == 2):
        print(decode())

    elif (pilihan == 3):
        print("Terima Kasih")
        break

    else:
        print("Enter Correct Input")
        time.sleep(1)
