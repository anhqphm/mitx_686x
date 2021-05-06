# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    binary = bin(N)[2:]
    pos_one = []
    for i in range(len(binary)):
        if int(binary[i]) == 1:
            pos_one.append(i)

    # print(len(binary))
    # print(binary[0])
    print(pos_one[1:])
    print(pos_one[:len(pos_one) - 1])
    bin_len = [x - y for x, y in zip(pos_one[1:], pos_one[:(len(pos_one) - 1)])]
    print(bin_len)

    # if len(pos_one) <=1:
    #     return 0
    # else:
    #     bin_len = [x-y for x,y in zip(pos_one[1:],pos_one[:(len(pos_one))])]
    #     return max(bin_len)


def main():
    solution(1041)


if __name__ == '__main__':
    main()
