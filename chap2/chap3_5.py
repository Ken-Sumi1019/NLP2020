import chap2_1
import re

def main():
    s = chap2_1.readFile()
    #a = re.findall("ファイル:(.[^[^|]+)",s)
    b = re.findall(r"[=:\n{]\s?([^=\n/\[\]:.]+\.[a-z]+)[|\]}]",s)
    for v in b:
        print(v)

if __name__ == "__main__":
    main()