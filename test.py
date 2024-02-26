import csv

def csv_to_md(input_file, output_file):
    with open(input_file, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        data = list(csvreader)
        print('|'.join(data[0]))
        print("test")

    with open(output_file, 'w') as mdfile:
        mdfile.write('| ' + ' | '.join(data[0]) + ' |\n')
        mdfile.write('|' + '---|' * len(data[0]) + '\n')
        for row in data[1:]:
            mdfile.write('| ' + ' | '.join(row) + ' |\n')
            
if __name__ == "__main__":
    input_file = "./input/input1.csv"
    output_file = "./output/output1.md"
    csv_to_md(input_file, output_file)
    print("Done!")
