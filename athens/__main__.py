import tomllib
from fs.osfs import OSFS
import random

from paradigm import *

def main():
    with open("settings.toml", "rb") as file:
        try:
            data: dict[str, any] = tomllib.load(file)
            parse_paradigms(data)
        except tomllib.TOMLDecodeError as e:
            print("Invalid settings.toml")
            print(e)
            exit(1)

if __name__ == "__main__":
    main()