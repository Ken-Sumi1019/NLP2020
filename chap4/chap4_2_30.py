import re

def mecabResult():
    result = []
    with open("./neko.txt.mecab",encoding='utf-8') as f:
        for v in f:
            result.append(v)
    return result

def makeData():
    ls = mecabResult()
    result = [[]]
    for row in ls:
        d = re.split("[,\t\n]",row)
        if d[0] == '。' or d[0] == '」' or d[0] == '「' or d[0] == "EOS":
            if len(result[-1]) == 0:continue
            else:
                result.append([])
                continue
        c = {"surface":d[0],"base":d[-4],"pos":d[1],"pos1":d[2]}
        result[-1].append(c)
    result = result[:len(result) - 1]
    return result
        

def main():
    r = makeData()
    print(r[-1])
    

if __name__ == "__main__":
    main()