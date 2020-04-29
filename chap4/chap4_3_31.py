import chap3_2_30

def dousi_hyoso():
    data = chap3_2_30.makeData()
    result = []
    for sentenc in data:
        for word in sentenc:
            if word["pos"] == "動詞":
                result.append(word["surface"])
    return result

def main():
    print(dousi_hyoso())

if __name__ == "__main__":
    main()