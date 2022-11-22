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


class BuiltInCSVConverter:
    def __init__(self):
        pass
        
    def to_json(self, data):
        json_array = []
        csv_reader = csv.DictReader(data)
        for row in csv_reader: 
            json_array.append(row)
        return json.dumps(json_array, indent=4)


if __name__ == "__main__":
    # python csv_converter.py -i <input.csv> -o <output.json>
    # -i  input file name
    # -o  output file name
    input_file_name, output_file_name = get_args(sys.argv[1:])
    data = read_data(input_file_name)

    conv = BuiltInCSVConverter()
    json_data = conv.to_json(data)
    write_data(output_file_name, json_data)
