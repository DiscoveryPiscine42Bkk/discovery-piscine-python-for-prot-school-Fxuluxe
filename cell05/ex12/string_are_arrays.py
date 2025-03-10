import sys

def string_are_arrays():
    if len(sys.argv) != 2:
        print("none")
        return
    input_string = sys.argv[1]
    if 'z' not in input_string:
        print("none")
    else:
        for char in input_string:
            if char == 'z':
                print("z")

if __name__ == "__main__":
    string_are_arrays()
