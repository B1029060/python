import sys
N, M, T = list(map(int, input().split()))
l1 = [int(i) for i in input().split()]
bonus = [list(map(int, input().split())) for element in range(M)] if M > 0 else [0, 0]
def movingToRoomDis(end, numOfBonus, time, L1, L2):
    start = 1
    idxBonus = 0
    for move in range(end - 1):
        if time > L1[move]:
            time -= L1[move]
            start += 1
            if numOfBonus != 0:
                if start == L2[idxBonus][0]:
                    time += L2[idxBonus][1]
                    idxBonus += 1 if numOfBonus != idxBonus + 1 else 0
        else:
            print('No')
            sys.exit()
    print('Yes')
movingToRoomDis(N, M, T, l1, bonus)