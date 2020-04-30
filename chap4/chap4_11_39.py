import chap4_7_35
from matplotlib import pyplot as plt

def zipf():
    data = chap4_7_35.hindo()
    rank = [i + 1 for i in range(len(data))]
    y = [v[1] for v in data]
    plt.plot(rank,y)
    plt.yscale('log')
    plt.xscale('log')
    plt.show()

if __name__ == "__main__":
    zipf()