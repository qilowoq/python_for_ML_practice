# title Consecutive subsequence
# description Вход: nums = [0,1,2,4,5,7] # [0, 1, 2], [4, 5], [7]
#Выход: ["0->2","4->5","7"]
#
#Вход: nums = [0,1,2,3,4,5,6,7,8] #
#Выход: ["0->8"]
#
#Вход: nums = [0]
#Выход: ["0"]
#
#Вход: nums = [0, 2, 4, 6, 8]
#Выход: ["0", "2", "4", "6", "8"]
#---end---

def prob(l):
    seq = []
    if len(l) == 0:
        return seq
    left = l[0]
    right = l[0]
    for i in range(1, len(l)):
        if l[i] - 1 != l[i-1]:
            if left == right:
                seq.append(str(left))
            else:
                seq.append(str(left) + '->' + str(right))
            left = right = l[i]
        right = l[i]
    if left == right:
        seq.append([str(left)])
    else:
        seq.append(str(left) + '->' + str(right))
    return seq