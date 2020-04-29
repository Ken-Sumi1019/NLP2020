import chap3_1
import re

def getBasic():
    s = chap3_1.readFile()
    s = re.sub(r"<ref[^<>/]*?/>","",s)
    s = re.sub(r"<ref[\s\S]*?</ref>","",s)
    s = re.sub(r"<br />","",s)
    name = re.findall("\n\|([^\[\]\s\{\}:]+)\s*?=",s)
    value = re.findall("\n\|[^\[\]\s\{\}:]+\s*?=([^\n]+)",s)
    result = {}
    for i in range(len(name)):
        if name[i] == "style" or name[i] == "注記":continue
        result[name[i]] = value[i]
    return result

def main():
    print(getBasic())

if __name__ == "__main__":
    main()