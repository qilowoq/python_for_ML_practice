# title Narkdown parser
# description Yo
#---end---


def get_file(name):
    with open(name, 'r') as f:
        return f.read()

def write_file(name):
    merged = '+ [{}](#{})\n\n## {}\n\n'.format(title, lower_cased_title, title) + \
    '\n'.join(desc) + '\n\n```python\n{}\n```'.format(code.lstrip('\n'))
    with open('out.txt', 'w') as f:
        f.write(merged)


info, code = get_file('solution.py').split('\n#---end---')
desc = []
for line in info.split('\n'):
    if line.startswith('# title'):
        title = line[8:]
        lower_cased_title = '-'.join(title.lower().split())
    elif line.startswith('# description'):
        desc.append(line[14:])
    else:
        desc.append(line[1:])

write_file('out.txt')