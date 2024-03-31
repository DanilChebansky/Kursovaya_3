import json


def json_load(json_file):
    with open(json_file) as file:
        return json.load(file)


def date_sorter(list_):
    sorted_list = sorted(list_, key=lambda x: x["date"], reverse=True)
    return sorted_list


def number_formatter(str_):
    if len(str_) == 20:
        new_str = f"**{str_[-4:]}"
        return new_str
    elif len(str_) == 16:
        new_str = f"{str_[:6]}"+6*"*"+f"{str_[-4:]}"
        new_new_str = f"{new_str[:4]}"+f" {new_str[4:8]}"+f" {new_str[8:12]}"+f" {new_str[12:]}"
        return new_new_str
