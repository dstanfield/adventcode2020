import sys
import re

# ([a-z]{3}):(\S+)( |\n) for finding the individual attributes, \n\n

def main():
    
    success = 0
    fail = 0
    chunk = ""
    initList = load_file("input.txt")
    for x in initList:
        if re.match('([a-z]{3}):(\S+)( |\n)',x):
            chunk += x
        elif re.match("\n", x):
            print("yes")
            result = processChunk(chunk)
            if result == True:
                success +=1
            if result == False:
                fail +=1
            chunk = ""
    print(str(success) + " successes and " + str(fail) + " failures")


def load_file(file):
    try:
        input_file = open(file, "r")
        output_list = input_file.readlines()
        input_file.close()
        return output_list
    except IOError:
        sys.exit("ERROR: Cannot load file: %s" % file)

# thanks buso now I can't unsee it
def processChunk(chonk):
    valid_fields = [
        "hgt:",
        "eyr:",
        "byr:",
        "iyr:",
        "hcl:",
        "ecl:",
        "pid:",
        ]

    for x in valid_fields:
        if not re.search(x, chonk):
            return False
    return True


if __name__ == "__main__":
    main()