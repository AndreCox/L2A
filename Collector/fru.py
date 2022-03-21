#######################################################
#                 FILE RENAME UTILITY                 #
# THIS SCRIPT IS USED TO RENAME FILES IN A DIRECTORY. #
#      TO MAKE THEM START FROM A CERTAIN NUMBER.      #
#   THIS ALLOWS US TO INCREASE THE NUMBER OF FILES    #
#             FOR THE TRAINING DATA SET.              #
#######################################################

import os

path = "frames/"
extention = ".jpg"


num_files = 0
# loop through all files in the directory
for filename in os.listdir(path):
    #if the file has our extention
    if filename.endswith(extention):
        num_files += 1

print("Do you want to rename", num_files, "files?")

# get user input
user_input = input("Enter y or n: ")
if user_input == "n":
    print("Exiting")
    exit()

# get the starting number
start_num = int(input("Enter the starting number: "))

# if the user wants to rename the files
if user_input == "y":
    for i in range(0, num_files):
        # get the name of the file
        filename = path + str(i) + extention
        print(path + str(i + start_num) + extention)
        # rename the file
        os.rename(filename, path + str(i + start_num) + extention)

