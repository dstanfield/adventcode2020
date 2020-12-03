import sys

def main():
    
    pwPass = 0
    pwPass2 = 0
    workpls = load_file("input.txt")

    for item in workpls:
        item,garbage = item.split("\n")
        if pwCheck(item):
            pwPass +=1
        if pwCheck2(item):
            pwPass2 +=1
    print(pwPass)
    print(pwPass2)


def load_file(file):
    try:
        input_file = open(file, "r")
        output_list = input_file.readlines()
        input_file.close()
        return output_list
    except IOError:
        sys.exit("ERROR: Cannot load file: %s" % file)

def pwCheck(thingy):
    reqNums,reqLetter,pw = thingy.split(" ")
    reqLetter,garbage2electricboogaloo = reqLetter.split(":")
    minNum,maxNum = reqNums.split("-")
    # was going to do a drawn out OR statement but buso showed me a very elegant way to do the same thing
    if int(minNum) <= pw.count(reqLetter) <= int(maxNum):
        return True

def pwCheck2(thingy):
    reqNums,reqLetter,pw = thingy.split(" ")
    reqLetter,garbage2electricboogaloo = reqLetter.split(":")
    pos1,pos2 = reqNums.split("-")
    # ^ is XOR, thanks again buso
    if (pw[int(pos1)-1] == reqLetter) ^ (pw[int(pos2)-1] == reqLetter) :
        return True

if __name__ == "__main__":
    main()