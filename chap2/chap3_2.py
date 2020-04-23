import chap2_1
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


def main():
    s = readFile()
    ls = s.split("\n")
    for col in ls:
        if "[[Category:" in col:
            print(col)
            

if __name__ == "__main__":
    main()