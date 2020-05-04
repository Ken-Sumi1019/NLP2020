import chap5_2_41
from graphviz import Digraph




def makeTree(index:int):
    g = Digraph('G', filename='sentenceTree.gv',encoding='utf-8',
    node_attr={'fontname': 'MS Gothic'})
    data = chap5_2_41.getData()
    sentence = data[index]
    chunks = [""]*len(sentence)
    toIndex = [-1]*len(sentence)
    for i in range(len(sentence)):
        toIndex[i] = sentence[i].dst
        for w in sentence[i].morphs:
            chunks[i] += w.surface
        g.node(chunks[i])

    for i in range(len(sentence)):
        if toIndex[i] == -1:continue
        g.edge(chunks[i],chunks[toIndex[i]])

    g.view()
    
if __name__ == "__main__":
    makeTree(150)