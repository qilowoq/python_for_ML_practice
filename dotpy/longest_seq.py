# title Longest subsequence
# description list, состоящий из 0 и 1. Найти длину максимальной непрерывной подпоследовательности, состоящей из 1
#Вход: [1,1,0,1,1,1] 
#Выход: 3    
#---end---   

def prob(l):
    max_val = 0
    cur_val = 0
    for item in l:
        if item == 1:
            cur_val += 1
        else:
            max_val = max(cur_val, max_val)
            cur_val = 0
    return max(cur_val, max_val)