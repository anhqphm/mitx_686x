import numpy as np
import kmeans
import common
import naive_em
import em

X = np.loadtxt("toy_data.txt")
# TODO: Your code here


def main():
    seed = 4
    for i in range(1, 5):
        K = i
        mix, post = common.init(X, K, seed)
        mixture, post, cost = kmeans.run(X, mix, post)
        print('K = {}; Costs = {} '.format(K, cost))


if __name__ == '__main__':
    main()
