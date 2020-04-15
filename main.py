# -*- coding: utf-8 -*-
import re

INPUT_FILENAME = "input.txt"


def error(msg):
    print(msg)
    exit(-1)


def sanitize(field, pattern, leave_double_count=1):
    doubles = ". @()+-"
    for double_symbol in doubles:
        field = re.sub(f"[{double_symbol}]+", double_symbol*leave_double_count, field)
    res = dict()
    field = field.strip()
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
    mail_re = re.compile(r"[^@ \t\r\n]+[^.]@[^@ \t\r\n]+\.[^@ \t\r\n]+")

    name = sanitize(name, name_re)
    if name["status"] == "OK":
        name_text = name["text"]
        name_text = re.sub("([А-ЯA-Z][^А-ЯA-Z])", r" \1", name_text).split(" ")
        name_text = " ".join([elem.strip().capitalize() for elem in name_text if elem])
        name["text"] = name_text

    age = sanitize(age, age_re)
    tel = sanitize(tel, tel_re, 0)
    if tel["status"] == "OK":
        tel_text = list(tel["text"])
        if tel_text[0] == "8":
            tel_text[0] = "7"
        code = "".join(tel_text[1:4])
        num1 = "".join(tel_text[4:7])
        num2 = "".join(tel_text[7:])
        new_tel = f"+{tel_text[0]} ({code}) {num1}-{num2}"
        tel["text"] = new_tel

    mail = sanitize(mail, mail_re)

    print("|".join(elem["text"] for elem in [name, age, tel, mail]))



