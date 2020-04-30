import chap4_7_35
from matplotlib import pyplot as plt

def graph():
    data = chap4_7_35.hindo()[:10]
    x = [v[0] for v in data]
    y = [v[1] for v in data]
    plt.bar(x,y)
    plt.show()

if __name__ == "__main__":
    graph()