
def macabResult():
    result = ""
    with open("./neko.txt.mecab",encoding='utf-8') as f:
        for v in f:
            result += v
    return result

def main():
    pass
    

if __name__ == "__main__":
    main()