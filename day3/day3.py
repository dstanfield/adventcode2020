# import as list of lists 
# keep record of: overall x and y position, relative x and y position, number of hashes

import sys

def main():
    
    coordList = load_file("input.txt")
    numTrees = move(coordList)
    print(numTrees)


def load_file(file):
    try:
        # buso again with the elegance and also maybe not closing is bad
        return [line.rstrip() for line in open(file)]
    except IOError:
        sys.exit("ERROR: Cannot load file: %s" % file)

def move(coords):
    x = 0
    trees = 0
    for points in coords:
        wrap = x%len(points)
        if points[wrap] == "#":
            trees +=1
        x +=3
    return trees


if __name__ == "__main__":
    main()