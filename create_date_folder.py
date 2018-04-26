from os import mkdir
from time import strftime

mkdir(strftime("%Y-%m-%d"))

answer = input("Do you want to organise folders?(y/n): ")
if answer == "y":
    pass