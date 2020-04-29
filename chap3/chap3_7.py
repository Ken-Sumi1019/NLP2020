import chap3_6
import re

def chap3_7():
    ob = chap3_6.getBasic()
    for k in ob:
        ob[k] = re.sub(r"''+",'',ob[k])
    return ob

def main():
    print(chap3_7())

if __name__ == "__main__":
    main()