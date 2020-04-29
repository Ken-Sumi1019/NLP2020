import chap3_2_30

def hindo():
    data = chap3_2_30.makeData()
    check = {}
    for sent in data:
        for v in sent:
            if v['surface'] in check:check[v['surface']] += 1
            else:check[v['surface']] = 1
    ls = [["",0] for i in range(len(check))]
    i = 0
    for key in check:
        ls[i][0] = key
        ls[i][1] = check[key]
        i += 1
    ls.sort(reverse=True,key=lambda x: x[1])
    return ls

def main():
    print(hindo())

if __name__ == "__main__":
    main()