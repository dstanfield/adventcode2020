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
            chunk += " | " + x + " | "
        elif re.match("\n", x):
            x.replace("\n", " ")
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
    print(chonk)
    valid_fields = [
        "hgt:(1([5-8][0-9]|9[0-3])cm|((59)|(6[0-9])|(7[0-6]))in)( |\n)",

        "eyr:20(30|2[0-9])( |\n)",
        "byr:(19[2-9][0-9]|200[0-2])( |\n)",
        "iyr:20(20|1[0-9])( |\n)",
        "hcl:#[0-9a-f]{6}( |\n)",
        "ecl:(amb|blu|brn|gry|grn|hzl|oth)( |\n)",
        "pid:\\d{9}( |\n)",
        ]

    for x in valid_fields:
        if not re.search(x, chonk):
            return False
    return True


if __name__ == "__main__":
    main()