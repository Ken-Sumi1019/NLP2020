import chap3_8
import re

def chap3_9():
    ob = chap3_8.chap3_8()
    for k in ob:
        s = ob[k]
        kari = re.findall("\{\{(.*?\)}\}",s)
        for i in range(len(kari)):
            muchs = ""
            if '|' in kari[i] or ':' in kari[i]:
                muchs = re.split("[|:]",kari[i])
"""
脳みそ「ミ゛ッ(脳みそが押しつぶれる音)」
無理です。
"""
def main():
    pass

if __name__ == "__main__":
    main()