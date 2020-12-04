# import as list of lists 
# keep record of: overall position and y position, relative position and y position, number of hashes

import sys

def main():
    
    coordList = load_file("input.txt")
    numTrees1 = move(coordList, 1, 1)
    numTrees2 = move(coordList, 3, 1)
    numTrees3 = move(coordList, 5, 1)
    numTrees4 = move(coordList, 7, 1)
    numTrees5 = move(coordList, 1, 2)
    numMult = numTrees1 * numTrees2 * numTrees3 * numTrees4 * numTrees5
    print(numMult)
    print(numTrees2)


def load_file(file):
    try:
        # buso again with the elegance and also maybe not closing is bad
        return [line.rstrip() for line in open(file)]
    except IOError:
        sys.exit("ERROR: Cannot load file: %s" % file)

def move(coords, right, down):
    position = 0
    trees = 0
    placekeeper = 1
    for points in coords:
        wrap = position%len(points)
        if down == 2:
            placekeeper +=1
            if placekeeper%2 == 1:
                continue
        if points[wrap] == "#":
            trees +=1
        
        position +=right
    return trees


if __name__ == "__main__":
    main()