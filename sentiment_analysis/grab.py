
def solution(S):
    n = len(S)
    pattern = "H-H"
    start = 0
    count = 0
    my_pos = []
    while start<len(S) - 2:
        pos = S.find(pattern,start)
        if pos!=1:
            pos = S.append(pos)
            start = pos + 3
            count +=1

        else:
            break
    S_tmp = list(S)
    for i in my_pos:
        for j in range(3):
            S_tmp[i+j]='0'
    S = "".join(S_tmp)
    if S.find("H")!=-1:
        for i in range(len(S_tmp)):
            if S_tmp[i] = "H":
                if i ==0:
                    if S_tmp[i+1]=="-":
                        count+=1
                    else:
                        return -1
                elif i==len(S_tmp)-1:
                    if S_tmp[i-1] == "-":
                        count+=1
                    else:
                        if S_tmp[i-1]





def main():
    S = "H-HH-H"
    result = solution(S)
    print(result)


if __name__ == '__main__':
    main()
