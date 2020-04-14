import chap2_1
import re

def search():
    c = 2
    text = chap2_1.readFile()
    result = {}
    while True:
        s = "\n={" + str(c) + "}([^=]+)={" + str(c) + "}\n"
        ls = re.findall(s, text)
        if len(ls) == 0:break
        result[c-1] = ls
        c += 1

    return result


def main():
    get = search()
    for i in get:
        for v in get[i]:
            print(i,v,end = " ")
        print()

if __name__ == "__main__":
    main()