# title Compress string
# description in:
#s = ["a","b","b","c","c","c","d"]
#out:
# ab2c3d
#---end---

def compress(s):
    counter = 1
    res = []
    if len(s) == 1:
        return s[0]
    if len(s) == 0:
        return ""
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            counter += 1
        else:
            if counter > 1:
                res.append(s[i-1] + str(counter))
            else:
                res.append(s[i-1])
            counter = 1
    if s[-1] == s[-2]:
        res.append(s[-1] + str(counter))
    else:
        res.append(s[-1])
    return "".join(res)