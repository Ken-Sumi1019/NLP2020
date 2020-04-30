import chap4_2_30
from matplotlib import pyplot as plt

def catCoOccurrence():
    data = chap4_2_30.makeData()
    count = {}
    for sent in data:
        ls = [v["surface"] for v in sent]
        if "猫" in ls:
            for word in ls:
                if word == "猫":continue
                if word in count:count[word] += 1
                else:count[word] = 1
    result = [[key,count[key]] for key in count]
    result.sort(reverse = True,key = lambda x:x[1])
    return result

def graphPlot():
    data = catCoOccurrence()[:10]
    x = [v[0] for v in data]
    y = [v[1] for v in data]
    plt.bar(x,y)
    plt.show()

def main():
    graphPlot()

if __name__ == "__main__":
    main()
