import chap5_2_41

def make():
    text = ""
    data = chap5_2_41.getData()
    for sent in data:
        for chunk in sent:
            if chunk.dst == -1:continue
            for i in [chunk.this,chunk.dst]:
                for v in sent[i].morphs:
                    text += v.surface
                text += '\t' if i == chunk.this else '\n'
    return text

if __name__ == "__main__":
    print(make())