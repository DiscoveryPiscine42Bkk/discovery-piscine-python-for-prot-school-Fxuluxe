import sys

def downcase_it():
    if len(sys.argv) != 2:
        print("none")
    else:
        print(sys.argv[1].lower())

if __name__ == "__main__":
    downcase_it()
