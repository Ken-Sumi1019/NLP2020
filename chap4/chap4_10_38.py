import chap4_7_35
from matplotlib import pyplot as plt

def drowHist():
    data = chap4_7_35.hindo()
    ls = [v[1] for v in data]
    plt.hist(ls,bins=100)
    plt.show()

if __name__ == "__main__":
    drowHist()