import sys
def shrink(s):
    print(s[:8])
def enlarge(s):
    print(s.ljust(8, 'Z'))
for arg in sys.argv[1:]:
    if len(arg) > 8:
        shrink(arg)
    else:
        enlarge(arg)