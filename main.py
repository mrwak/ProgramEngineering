# -*- coding: utf-8 -*-

FILENAME = "input.txt"

def error(msg):
    print(msg)
    exit(-1)

file_content = ""
io_error = False


try:
    with open(FILENAME, "r") as file:
        file_content = file.readlines()
except:
    io_error = True

if io_error:
    error("IO error")

if not file_content:
    error("File is empty")


for line in file_content:
    line = line.strip()
    print(line, end="")

    line = line.split("|")
    if len(line) != 4 or any([len(elem) == 0 for elem in line]):
        print("Invalid line format")
        continue
    
    name, age, tel, mail = line



