from typing import Dict
import requests


def download_file(url, file_name):
    with open(file_name, "wb") as file:
        response = requests.get(url)
        file.write(response.content)


def evaluate_seller_id(manufact: str):
    key_map: Dict[str, int]
    key_map = {}
    key_map["Falcon Embroidery"] = 1752935
    key_map["Download Patterns"] = 1752600
    key_map["KZ Digitizing"] = 1752652
    key_map["Falcon Eli"] = 1752604
    key_map["Bushi Embroidery Pattern"] = 1752581
    key_map["ULeatheR"] = 1752655
    return key_map[manufact]


# Download Patterns
# Falcon Embroidery
# KZ Digitizing
# Falcon Eli
# Bushi Embroidery Pattern
# ULeatheR
