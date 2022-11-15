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
            links, contents = readme.split('<!--DIVIDER-->')
            links = "{}\n{}".format(links.strip('\n'), link)
            contents = "{}\n\n{}".format(contents.strip('\n'), content)
            merged = "{}\n\n{}\n\n{}".format(links, '<!--DIVIDER-->', contents)
            f.write(merged)
    except FileNotFoundError:
        with open(name, 'w') as f:
            merged = "{}\n\n{}\n\n{}".format(link, '<!--DIVIDER-->', content)
            f.write(merged)


def get_content(title, lower_cased_title, desc, code):
    link = "+ [{}](#{})".format(title, lower_cased_title)
    content = "## {}\n\n{}\n\n```python\n{}\n``` ".format(title, desc, code)
    return link, content


def get_titles(data):
    info = data.split('#---end---')[0]
    title = ''
    lower_cased_title = ''
    for line in info.split('\n'):
        if line.startswith('# title'):
            title = line[8:]
            lower_cased_title = '-'.join(title.lower().split())
            break
    return title, lower_cased_title


def get_desc_code(data):
    try:
        info, code = data.split('#---end---')
    except ValueError:
        return '', ''
    desc = []
    for line in info.split('\n'):
        if line.startswith('# title'):
            pass
        elif line.startswith('# description'):
            desc.append(line[14:])
        else:
            desc.append(line[1:])
    return '\n'.join(desc).strip('\n'), code.strip('\n')


def converter(solution='solution.py', out='readme.md'):
    data = get_file(solution)
    title, lower_cased_title = get_titles(data)
    desc, code = get_desc_code(data)
    link, content = get_content(title, lower_cased_title, desc, code)
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
    # python md_converter_but_better.py -i <solution.py> -o <readme.md>
    # -i  input file name
    # -o output file name
    inputfile, outputfile = get_args(sys.argv[1:])
    data = get_file(inputfile)
    title, lower_cased_title = get_titles(data)
    desc, code = get_desc_code(data)
    print(title, lower_cased_title)
    converter(solution=inputfile, out=outputfile)