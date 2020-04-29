import chap3_7
import re

def chap3_8():
    ob = chap3_7.chap3_7()
    for k in ob:
        s = ob[k]
        if "[[" in s and "]]" in s:
            kari = re.findall(r"\[\[(.*?)\]\]",s)
            for i in range(len(kari)):
                if '|' in kari[i]:
                    kari[i] = kari[i].split('|')[1]
            for i in range(len(kari)):
                s = re.sub(f"\[\[.*?{kari[i]}.*?\]\]",kari[i],s)
            ob[k] = s
    return ob

def main():
    print(chap3_8())

if __name__ == "__main__":
    main()