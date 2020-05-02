import chap5_2_41

# 文節内に任意の品詞があるか判定
def judgeVerb(chunk,hinshi) -> bool:
    for w in chunk.morphs:
        if w.pos == hinshi:
            return True
    return False

def make():
    text = ""
    data = chap5_2_41.getData()
    for sent in data:
        for chunk in sent:
            if chunk.dst == -1:continue
            if not (judgeVerb(sent[chunk.this],"名詞") and judgeVerb(sent[chunk.dst],"動詞")):
                continue
            for i in [chunk.this,chunk.dst]:
                for v in sent[i].morphs:
                    text += v.surface
                text += '\t' if i == chunk.this else '\n'
    return text

if __name__ == "__main__":
    print(make())