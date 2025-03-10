import sys

def scan_it():
    if len(sys.argv) != 3:
        print("none")
        return
    
    keyword = sys.argv[1]
    string = sys.argv[2]
 
    count = string.count(keyword)
    
    if count == 0:
        print("none")
    else:
        print(count)

if __name__ == "__main__":
    scan_it()
