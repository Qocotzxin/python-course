import sys

if len(sys.argv) == 3:
    rows = int(sys.argv[1])
    cols = int(sys.argv[2])

    for r in range(0, rows):
        print("")
        for c in range(0, cols):
            print(" * ", end="")

else:
    print("Please enter two integers between 1 and 9 as arguments")
