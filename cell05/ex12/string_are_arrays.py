import sys
sys.argv = ["scan_it.py", "apple"]
if len(sys.argv) != 2:
    print("none")
      
input_string = sys.argv[1]
if 'z' not in input_string:
    print("none")
else:
    for char in input_string:
        if char == 'z':
                print("z")
