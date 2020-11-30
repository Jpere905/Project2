import json

def read_from_file(file_name):
    with open(file_name, "r") as read_file:
        data = json.load(read_file)
        print("Successfully read from {}".format(file_name))
    return data

def write_to_file(data, file_name):
    with open(file_name, "w") as write_file:
        json.dump(data, write_file, indent=4)
        print("Successfully wrote to {}".format(file_name))
