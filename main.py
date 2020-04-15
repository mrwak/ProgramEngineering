# -*- coding: utf-8 -*-
import re

INPUT_FILENAME = "input.txt"


def error(msg):
    print(msg)
    exit(-1)


def sanitize(field, pattern, leave_double_count=1):
    doubles = ". @()+"
    for double_symbol in doubles:
        field = re.sub(f"[{double_symbol}]+", double_symbol*leave_double_count, field)
    res = dict()
    res["text"] = field
    res["status"] = "ERR"
    if re.fullmatch(pattern, field):
        res["status"] = "OK"
    else:
        res["text"] += " неверное поле"
    return res


file_content = ""

try:
    with open(INPUT_FILENAME, "r", encoding="utf-8") as file:
        file_content = file.readlines()
except Exception as e:
    error(f"File reading error: {e}")

if not file_content:
    error("File is empty")

for line in file_content:
    line = line.strip()
    print()
    print(line)

    line = line.split("|")
    # check if there are exactly 4 fields of non-zero length
    if len(line) != 4 or any([len(elem) == 0 for elem in line]):
        print("Invalid line format")
        continue

    name, age, tel, mail = line

    name_re = re.compile(r"([^|\s]+ *[^|]+)")
    age_re = re.compile(r"[0-9]+")
    tel_re = re.compile(r"([\+]?[(]?([0-9]\W*){3}[)]?[-\s\.]?([0-9]\W*){3}[-\s\.]?([0-9]\W*){4,6})")
    mail_re = re.compile(r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+")

    name = sanitize(name, name_re)
    if name["status"] == "OK":
        name_text = name["text"]
        name_text = re.split("[[а-яa-z][А-ЯA-Z]| +]", name_text)
        name_text = " ".join([elem.capitalize() for elem in name_text])
        name["text"] = name_text

    age = sanitize(age, age_re)
    tel = sanitize(tel, tel_re, 0)
    mail = sanitize(mail, tel_re)

    print("|".join(elem["text"] for elem in [name, age, tel, mail]))



