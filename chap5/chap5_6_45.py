import chap5_2_41
import chap5_4_43

def solv():
    result = ""
    data = chap5_2_41.getData()
    for sent in data:
        for idx in range(len(sent)):
            if chap5_4_43.judgeVerb(sent[idx],"動詞"):
                doushiIdx = 0
                for i in range(len(sent[idx].morphs)):
                    if sent[idx].morphs[i].pos == "動詞":
                        doushiIdx = i;break
                jyoshi = sent[idx].srcs
                ls = []
                for i in jyoshi:
                    if sent[i].morphs[-1].pos == "助詞":
                        ls.append(sent[i].morphs[-1].surface)
                ls.sort()
                result += sent[idx].morphs[doushiIdx].base + "\t" + " ".join(ls) + "\n"
    with open("result.txt",encoding='utf-8',mode='w') as f:
        f.write(result)

if __name__ == "__main__":
    solv()