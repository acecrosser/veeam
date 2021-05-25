import sys
from hashlib import md5, sha1, sha256


input_items = sys.argv
file = input_items[1]
path = input_items[2]


print(file)
print(path)

def read_file(file):
    with file:
        file.read()


# md5(read_file(open('file_01.bin', 'br'))).hexdigest()

if __name__ == '__main__':
    pass
