import json
import re

def readFile():
    jsons = []
    with open("jawiki-country.json",'r',encoding='utf-8') as f:
        for row in f:
            jsons.append(json.loads(row))


    for i in range(len(jsons)):
        if jsons[i]["title"] == "イギリス":
            return jsons[i]["text"]

def categoryCol():
    s = readFile()
    ls = s.split("\n")
    ans = []
    for col in ls:
        if "[[Category:" in col:
            ans.append(col)
    return ans

def main():
    ls = categoryCol()
    for v in ls:
        print(v[11:len(v) - 2])

if __name__ == "__main__":
    main()