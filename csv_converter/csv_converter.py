import sys, getopt
import csv
import json


def read_data(file_name):
    file = open(file_name)
    content = file.readlines()
    file.close()
    return content


def write_data(file_name, data):
    file = open(file_name, 'w')
    file.write(data)
    file.close()


class CSVConverter:
    def __init__(self):
        pass

    def _prepare_data(self, data):
        titles = data[0]
        content = data[1:]
        return titles, content

    def convert_row_to_json(self, row):
        s = '{{"name": "{}", "id": "{}", "birth": "{}", "salary": "{}", "department": "{}"}}'.format(*row.strip().split(','))
        return s

    def convert_csv_to_json(self, data):
        titles, content = self._prepare_data(data)
        return '[' + ','.join([self.convert_row_to_json(row) for row in content]) + ']'


#using csv and json libs
class CSVConverter2:
    def __init__(self):
        pass
        
    def convert_csv_to_json(self, data):
        json_array = []
        csv_reader = csv.DictReader(data)
        for row in csv_reader: 
            json_array.append(row)
        return json.dumps(json_array, indent=4)



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


def main():
    # python csv_converter.py -i <input.csv> -o <output.json>
    # -i  input file name
    # -o  output file name
    input_file_name, output_file_name = get_args(sys.argv[1:])
    data = read_data(input_file_name)
    
    #conv1 = CSVConverter()
    #json_data = conv1.convert_csv_to_json(data)

    conv2 = CSVConverter2()
    json_data = conv2.convert_csv_to_json(data)
    write_data(output_file_name, json_data)


if __name__ == "__main__":
    main()