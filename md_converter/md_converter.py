# title MD Converter
# description Конвертирует solution.py -> out.txt
#---end---

import sys

def get_file(name):
    with open(name, 'r') as f:
        return f.read()


def write_file(name, merged):
    with open(name, 'w') as f:
        f.write(merged)


def converter(solution='solution.py', out='out.txt'):
    info, code = get_file(solution).split('\n#---end---')
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