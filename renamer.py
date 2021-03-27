import os
import string
import random


def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def rename_file(file_name, phrase):
    extension = os.path.splitext(file)[1]
    new_name = phrase + extension
    os.rename(file_name, new_name)


# Input directory
dir_name = input("Enter directory here: ")

# Process directory
try:
    directory = os.listdir(dir_name)
except FileNotFoundError:
    print("No such directory as", dir_name)
    exit()

dir_size = len(directory)
os.chdir(dir_name)
nums = random.sample(range(1, dir_size + 1), dir_size)

# To prevent loss of files, rename each file to strings of characters
for file in directory:
    rename_file(file, get_random_string(5))

# Rename each file in numerical order
count = 0
directory = os.listdir('.')
for file in directory:
    rename_file(file, str(nums[count]))
    count = count + 1
