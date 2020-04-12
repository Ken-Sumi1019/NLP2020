import random

def _00(s):
    return s[::-1]

def _01(s):
    return "".join([s[i] for i in range(0,len(s),2)])

def _02(s,t):
    return "".join([s[i] + t[i] for i in range(len(s))])

def _03(s:str):
    ls = s[:len(s)-1].split(" ")
    ans = [None]*len(ls)
    for i in range(len(ls)):
        count = {}
        for v in ls[i]:
            if v in count:count[v] += 1
            else:count[v] = 1
        ans[i] = [[v,count[v]] for v in count.keys()]
        ans[i].sort(reverse=True,key = lambda x: x[1])
    return ans

def _04(s:str):
    ls = s[:len(s)-1].split(" ")
    icheck = set([1, 5, 6, 7, 8, 9, 15, 16, 19])
    ans = {}
    for i in range(len(ls)):
        if (i + 1) in icheck:ans[ls[i][0]] = ls[i]
        else:ans[ls[i][:2]] = ls[i]
    return ans
            
def _05(s:str,n):
    chara = [""]*(len(s) - n + 1)
    for i in range(len(s) - n + 1):
        chara[i] = s[i:i + n]
    ls = s.split(" ")
    word = [None]*(len(ls) - n + 1)
    for i in range(len(ls) - n + 1):
        word[i] = ls[i:i+n]
    return chara,word

def _06(s = "paraparaparadise",t = "paragraph"):
    x = set(_05(s,2)[0]);y = set(_05(t,2)[0])
    print("和集合:",x|y)
    print("差集合:",x-y,y-x)
    print("積集合:",x&y)

def _07(x = 12,y = "気温",z = 22.4):
    return (f"{x}時の{y}は{z}")

def _08_cipher(s):
    ls = [""]*len(s)
    for i in range(len(ls)):
        if 97 <= ord(s[i]) <= 122:ls[i] = chr(219 - ord(s[i]))
        else:ls[i] = s[i]
    return "".join(ls)

def _09(s):
    ls = s.split(" ")
    for i in range(len(ls)):
        if len(ls[i]) <= 4:continue
        ls[i] = ls[i][0] + "".join(random.sample(ls[i][1:len(ls[i]) - 1],len(ls[i]) - 2)) + ls[i][-1]
    return " ".join(ls)


def main():
    s = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print(_09(s))

if __name__ == "__main__":
    main()