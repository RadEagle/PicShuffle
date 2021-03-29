import os
import string
import random
from mega import Mega
from mega import errors


def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def rename_file(file, phrase):
    file_name = file[1]['a']['n']
    extension = os.path.splitext(file_name)[1]
    new_name = phrase + extension
    m.rename(file, new_name)


# Process MEGA login
mega = Mega()
email = input("Enter your email: ")
password = input("Enter your password: ")

try:
    m = mega.login(email, password)
except errors.RequestError:
    print("Incorrect email or password")
    exit()

# Input directory
# dir_name = input("Enter directory here: ")
dir_name = "The Deep Sea/Tarnished"

# Process directory
dir_node = m.find('The Deep Sea/Tarnished')[0]
directory = list(m.get_files_in_node(dir_node).items())
dir_size = len(directory)
nums = random.sample(range(1, dir_size + 1), dir_size)

# To prevent loss of files, rename each file to strings of characters
for file_pack in directory:
    rename_file(file_pack, get_random_string(10))

# Rename each file in numerical order
count = 0
directory = list(m.get_files_in_node(dir_node).items())
for file_pack in directory:
    rename_file(file_pack, str(nums[count]))
    count = count + 1
