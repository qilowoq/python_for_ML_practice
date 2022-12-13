## Python for ML

+ [Squared sorted](#squared-sorted)
+ [Compress string](#compress-string)
+ [Consecutive subsequence](#consecutive-subsequence)
+ [Sum of diagonal elements](#sum-of-diagonal-elements)
+ [Longest subsequence](#longest-subsequence)
+ [Merge two lists](#merge-two-lists)
+ [Squared sorted](#squared-sorted)
+ [MD Converter](#md-converter)
+ [MD Converter modified](#md-converter-modified)

<!--DIVIDER-->

## Squared sorted

Дан отсортированный список в неубавющем порядке. Вернуть элементы этого списка возведенные в квадрат в неубывающем порядке
Элементы списка это целые числа
O(n)

```python
def merge(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    return c

def squares(l):
    ind = len(l) - 1
    for i in range(len(l)):
        if l[i] >= 0:
            ind = i
            break
    a = []
    b = []
    for i in range(ind, len(l)):
        a.append(l[i]**2)
    for j in range(ind-1, -1, -1):
        b.append(l[j]**2)
    return merge(a, b)
```

## Compress string

in:
s = ["a","b","b","c","c","c","d"]
out:
 ab2c3d

```python
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
```

## Consecutive subsequence

Вход: nums = [0,1,2,4,5,7] # [0, 1, 2], [4, 5], [7]
Выход: ["0->2","4->5","7"]

Вход: nums = [0,1,2,3,4,5,6,7,8] #
Выход: ["0->8"]

Вход: nums = [0]
Выход: ["0"]

Вход: nums = [0, 2, 4, 6, 8]
Выход: ["0", "2", "4", "6", "8"]

```python
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
```

## Sum of diagonal elements

Найти сумму элементов на главной и побочной диагоналях
in:
mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
  
out: 
25  

```python
def diagonalSum(mat):
    sum = 0
    n = len(mat)
    for i in range(n):
        if i != n - 1 - i:
            sum += mat[i][i] + mat[i][n-1-i]
        else:
            sum += mat[i][i] 
    return sum
```

## Longest subsequence

list, состоящий из 0 и 1. Найти длину максимальной непрерывной подпоследовательности, состоящей из 1
Вход: [1,1,0,1,1,1] 
Выход: 3    

```python
   

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
```

## Merge two lists

на входе два отсортированных массива (списка), на выходе получить 1 отсортированный массив
Элементы списка это целые числа
O(n)

```python
def merge(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    return c
```

## Squared sorted

Дан отсортированный список в неубавющем порядке. Вернуть элементы этого списка возведенные в квадрат в неубывающем порядке
 Элементы списка это целые числа
 O(n)

```python
def merge(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    return c

def squares(l):
    ind = len(l) - 1
    for i in range(len(l)):
        if l[i] >= 0:
            ind = i
            break
    a = []
    b = []
    for i in range(ind, len(l)):
        a.append(l[i]**2)
    for j in range(ind-1, -1, -1):
        b.append(l[j]**2)
    return merge(a, b)
```

## MD Converter

Конвертирует solution.py -> out.txt

```python
import sys

CODE_DELIMETER = '#---end---'

def get_file(name):
    with open(name, 'r') as f:
        return f.read()


def write_file(name, merged):
    with open(name, 'w') as f:
        f.write(merged)


def converter(solution='solution.py', out='out.txt'):
    info, code = get_file(solution).split('\n' + CODE_DELIMETER)
    desc = []
    for line in info.split('\n'):
        if line.startswith('# title'):
            title = line[8:]
            lower_cased_title = '-'.join(title.lower().split())
        elif line.startswith('# description'):
            desc.append(line[14:])
        else:
            desc.append(line[1:])
    merged = '+ [{}](#{})\n\n## {}\n\n'.format(title, lower_cased_title, title) + \
        '\n'.join(desc) + '\n\n```python\n{}\n```'.format(code.lstrip('\n').rstrip('\n'))
    write_file(out, merged)


if __name__ == "__main__":
    if len(sys.argv) > 3:
        sys.exit('Need at maximum 2 arguments name of solution file and name of out file')
    elif len(sys.argv) == 3:
        _, solution, out = sys.argv
        converter(solution, out)
    elif len(sys.argv) == 2:
        solution = sys.argv[1]
        converter(solution)
    else:
        converter()
```

## MD Converter modified

Добавляет solution.py -> readme.md

```python
import sys, getopt

CODE_DELIMETER = '#---end---'
MD_DELIMETER = '<!--DIVIDER-->'

def get_file(name):
    with open(name, 'r') as f:
        return f.read()


def write_file(name, link, content):
    try:
        readme = get_file(name)
        with open(name, 'w') as f:
            links, contents = readme.split(MD_DELIMETER)
            links = "{}\n{}".format(links.strip('\n'), link)
            contents = "{}\n\n{}".format(contents.strip('\n'), content)
            merged = "{}\n\n{}\n\n{}".format(links, MD_DELIMETER, contents)
            f.write(merged)
    except FileNotFoundError:
        with open(name, 'w') as f:
            merged = "{}\n\n{}\n\n{}".format(link, MD_DELIMETER, content)
            f.write(merged)


def get_content(title, lower_cased_title, desc, code):
    link = "+ [{}](#{})".format(title, lower_cased_title)
    content = "## {}\n\n{}\n\n```python\n{}\n``` ".format(title, desc, code)
    return link, content


def converter(solution='solution.py', out='readme.md'):
    info, code = get_file(solution).split(CODE_DELIMETER)
    desc = []
    for line in info.split('\n'):
        if line.startswith('# title'):
            title = line[8:]
            lower_cased_title = '-'.join(title.lower().split())
        elif line.startswith('# description'):
            desc.append(line[14:])
        else:
            desc.append(line[1:])
    link, content = get_content(title, lower_cased_title, '\n'.join(desc).strip('\n'), code.strip('\n'))
    write_file(out, link, content)

def get_args(argv):
    inputfile = 'solution.py'
    outputfile = 'readme.md'
    try:
        opts, _ = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('-i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('-i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    return inputfile, outputfile

if __name__ == "__main__":
    inputfile, outputfile = get_args(sys.argv[1:])
    converter(solution=inputfile, out=outputfile)
```