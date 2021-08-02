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
dir_name = input("Enter directory here: ")

# Process directory
dir_node = m.find(dir_name)[0]
directory = list(m.get_files_in_node(dir_node).items())
dir_size = len(directory)
f_count = 0

# To prevent loss of files, rename each file to strings of characters
# f_type ensures the file type is a regular file and not a folder
for file_pack in directory:
    f_name = file_pack[1]['a']['n']
    f_type = file_pack[1]['t']
    if f_name[0:2] != "0_" and f_type == 0:
        rename_file(file_pack, "kq" + get_random_string(10))
        f_count += 1

# Rename each file in numerical order
count = 0
nums = random.sample(range(1, f_count + 1), f_count)

directory = list(m.get_files_in_node(dir_node).items())
for file_pack in directory:
    f_name = file_pack[1]['a']['n']
    f_type = file_pack[1]['t']
    if f_name[0:2] == "kq" and f_type == 0:
        rename_file(file_pack, str(nums[count]))
        count = count + 1
