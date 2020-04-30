import chap4_2_30

def mashiku():
    data = chap4_2_30.makeData()
    result = []
    for sentence in data:
        for i in range(1,len(sentence)-1):
            if sentence[i]['surface'] == 'の':
                if sentence[i-1]['pos'] == '名詞' and sentence[i+1]['pos'] == '名詞':
                    result.append(sentence[i-1]['surface']+sentence[i]['surface']+sentence[i+1]['surface'])
    return result

def main():
    v = mashiku()
    print(v)

if __name__ == "__main__":
    main()