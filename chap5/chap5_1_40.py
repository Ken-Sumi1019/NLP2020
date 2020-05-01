import re

class Morph:
    def __init__(self,row = None):
        self.surface = ""
        self.base = ""
        self.pos = ""
        self.pos1 = ""
        if row != None:
            self.cabochaSlice(row)

    def cabochaSlice(self,row):
        ls = re.split("[\t,\n]",row)
        self.surface = ls[0]
        self.base = ls[-4]
        self.pos = ls[1]
        self.pos1 = ls[2]

    def makeDict(self):
        return {'surface':self.surface,'base':self.base,
                'pos':self.pos,'pos1':self.pos1}

def main():
    Sentences = []
    with open("neko.txt.cabocha","r",encoding="utf-8") as f:
        for v in f:
            Sentences.append(v)

    result = [[]]
    for i in range(len(Sentences) - 1):
        sent = Sentences[i]
        if sent == 'EOS\n':
            if Sentences[i+1] != 'EOS\n':result.append([])
            continue
        if sent[0] == "*":continue
        result[-1].append(Morph(row=sent))

    for v in result[2]:
        print(v.makeDict())
        

if __name__ == "__main__":
    main()