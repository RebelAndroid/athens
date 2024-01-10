import tomllib
from fs.osfs import OSFS
import random

def main():
    with open("settings.toml", "rb") as file:
        try:
            data = tomllib.load(file)
            run(data)
        except tomllib.TOMLDecodeError as e:
            print("Invalid settings.toml")
            print(e)
            exit(1)

def run(data):
    target = OSFS(data["target-folder"], create=True)
    if len(target.listdir("/")) > 0:
        print("target-folder is not empty! Refusing to use it to avoid accidental damage.")
        exit(1)
    
    construct_paradigm(target, "root", data)
    

def construct_paradigm(file_system, paradigm, data):
    if paradigm not in data:
        print("Expected paradigm ", paradigm, " was not found.")
        exit(1)
    
    paradigm_data = data[paradigm]
    print(paradigm_data)
    if 'type' not in paradigm_data:
        print("Paradigm ", paradigm, ' should have a value "type".')
        exit(1)
    
    if 'contents' not in paradigm_data:
        print("Paradigm ", paradigm, ' should have a value "contents".')
        exit(1)

    paradigm_type = paradigm_data["type"]
    paradigm_contents = paradigm_data["contents"]

    if paradigm_type == "folder" or paradigm_type == "directory":
        if type(paradigm_contents) is not list:
            print('Contents of a folder paradigm should be a list') # TODO: Improve error message
            exit(1)

        name = paradigm + " " + str(random.randint(0, 10 ** 6))
        file_system.makedir(name)  

        for item in paradigm_contents:
            construct_paradigm(file_system.opendir(name), item, data)

    elif paradigm_type == "file":
        if paradigm_contents != "empty":
            print("TODO! Non-empty files")
            exit(1)
        file_system.create(paradigm + " " + str(random.randint(0, 10 ** 6)))
    else:
        print("Type of paradigm ", paradigm, 'is not valid. Expected "directory\", "folder", or "file". Found ', paradigm_type, ".")

if __name__ == "__main__":
    main()