import chap4_2_30

def connect(i,j,data):
    ref = ""
    for k in range(i,j):
        ref += data[k]['surface']
    return ref

def mostLongmeishi():
    data = chap4_2_30.makeData()
    result = []
    for sent in data:
        index = 0;max_ln = 0;max_words = ""
        while index < len(sent):
            if sent[index]['pos'] == "名詞":
                j = index + 1
                while j < len(sent):
                    if sent[j]['pos'] != '名詞':break
                    j += 1
                w = connect(index,j,sent)
                if max_ln < len(w):
                    max_ln = len(w)
                    max_words = w
                index = j + 1
            else:index += 1
        if max_words != "":
            result.append(max_words)
    return result

def main():
    print(mostLongmeishi())

if __name__ == "__main__":
    main()