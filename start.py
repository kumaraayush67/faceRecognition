# from . import dataCap, detector, train
from detector import detectFace
from dataCap import capture
from train import train
import os

print("Hello User!\nThis is Face Recognition application.")


while True:
    print("\nWhat do You wanna DO?\n 1. Recognize A Face.\n 2. Upload New Face.\n 3. End Program")
    c = input(" Choice: ")

    if c == "1":
        detectFace()
        print("Rec Start!")
    elif c == "2":
        input("Press Enter to Click a Photo (5 photos needed)...")
        capture()
        a = input("Press Enter to start Training on the new Data...")
        train()
    elif c == "3":
        break
    else:
        print("Wrong Input")

    os.system('cls')

print("The End")
