import chap5_1_40
import sys

class Chunk:
    def __init__(self,txt):
        self.morphs = []
        self.this = -1
        self.dst = -1
        self.srcs = []
        self.makeData(txt)

    def makeData(self,chunkText:str):
        sents = chunkText.split('\n')
        header = sents[0]
        for v in sents[1:]:
            if len(v) == 0:continue
            self.morphs.append(chap5_1_40.Morph(v))
        
        h = header.split(' ')
        self.this = int(h[1])
        self.dst = int(h[2][:-1])

    def display(self):
        return {'morphs':[v.makeDict() for v in self.morphs],'dst':self.dst,'scrs':self.srcs,'this':self.this}


def readData(path):
    result = []
    with open(file=path,encoding='utf-8',mode='r') as f:
        result = f.read().split("\nEOS")
    return result

def splitChunk(sentence:str):
    return sentence.split('\n*')

# こいつ実行すると目的のデータ手に入る
def getData():
    sents = readData('./neko.txt.cabocha')
    result = []
    for v in sents:
        if len(v) == 0:continue
        chunks = splitChunk(v)
        ls = []
        for c in chunks:
            if len(c) == 0 or c == "\n":continue
            data = Chunk(c)
            ls.append(data)
        for i in range(len(ls)):
            if ls[i].dst == -1:continue
            ls[ls[i].dst].srcs.append(ls[i].this)

        result.append(ls)
    return result

if __name__ == "__main__":
    pass