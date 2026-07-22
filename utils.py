import json
from json import JSONDecodeError


def load_words():
    try:
        with open("words.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print("words.json not found!")
        return {}

    except JSONDecodeError:
        print("Invalid JSON!")
        return {}