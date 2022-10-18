# title MD Converter modified
# description Добавляет solution.py -> readme.md
#---end---

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