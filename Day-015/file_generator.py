# Read a file line by line using a generator

def read_file(filename):

    with open(filename, "r") as file:

        for line in file:
            yield line.strip()


for line in read_file("sample.txt"):
    print(line)
