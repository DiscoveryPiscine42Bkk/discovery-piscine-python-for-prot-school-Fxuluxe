import sys

def append_it():
    if len(sys.argv) <= 1:
        print("none")
        return
    for param in sys.argv[1:]:
        if not param.endswith("ism"):
            print(f"{param}ism")

if __name__ == "__main__":
    append_it()
