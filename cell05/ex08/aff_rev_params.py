import sys

def aff_rev_params():
    if len(sys.argv) < 2:
        print("none")
    else:
        reversed_params = sys.argv[1:][::-1]
        for param in reversed_params:
            print(param)

if __name__ == "__main__":
    aff_rev_params()
