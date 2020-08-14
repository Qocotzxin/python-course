import sys


def set_counter():
    file = open("counter.txt", "a+")
    file.seek(0)
    line = file.readline()
    counter = ""

    try:
        counter = int(line)
    except:
        counter = 0

    file.close()

    if len(sys.argv) > 1:
        if sys.argv[1] == "inc":
            counter += 1
        elif sys.argv[1] == "dec":
            counter -= 1

    file = open("counter.txt", "w+")
    file.write(str(counter))
    file.close()
    print(counter)


set_counter()
