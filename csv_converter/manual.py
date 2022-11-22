import sys, getopt


def read_data(file_name):
    file = open(file_name)
    content = file.readlines()
    file.close()
    return content

def write_data(file_name, data):
    file = open(file_name, 'w')
    file.write(data)
    file.close()

def get_args(argv):
    inputfile = 'input.csv'
    outputfile = 'output.json'
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


class ManualCSVConverter:
    def __init__(self):
        pass

    def _prepare_data(self, data):
        titles = data[0].strip().split(',')
        content = data[1:]
        return titles, content

    def _convert_row_to_json(self, row):
        title_rows_tuple = [(i,j) for i, j in zip(self.titles, row.strip().split(','))]
        s = ', '.join(map(lambda t: '"{}": "{}"'.format(t[0],t[1]), title_rows_tuple))
        return "{{{}}}".format(s)

    def to_json(self, data):
        self.titles, self.content = self._prepare_data(data)
        return '[' + ','.join([self._convert_row_to_json(row) for row in self.content]) + ']'
    

if __name__ == "__main__":
    # python csv_converter.py -i <input.csv> -o <output.json>
    # -i  input file name
    # -o  output file name
    input_file_name, output_file_name = get_args(sys.argv[1:])
    data = read_data(input_file_name)
    
    conv = ManualCSVConverter()
    json_data = conv.to_json(data)
    write_data(output_file_name, json_data)
