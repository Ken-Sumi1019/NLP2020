import MeCab
import re

def main():
    text = ""
    with open("./neko.txt",encoding='utf-8') as f:
        for tmp in f:
            text += re.sub("\n","",tmp)

    t = MeCab.Tagger()
    result = t.parse(text)
    #print(result)

    with open("./neko.txt.mecab",encoding='utf-8',mode="w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()