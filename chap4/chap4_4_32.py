import chap4_2_30

def dousi_kihon():
    data = chap4_2_30.makeData()
    result = []
    for sentenc in data:
        for word in sentenc:
            if word["pos"] == "動詞":
                result.append(word["base"])
    return result

def main():
    print(dousi_kihon())

if __name__ == "__main__":
    main()