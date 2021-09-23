import sys
import getopt
import pandas as pd


def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o", ["ifile="])
    except getopt.GetoptError:
        print('sumCSV.py -i <inputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print('test.py -i <inputfile>')
            sys.exit()
        elif opt in ("-i", "-ifile"):
            inputfile = arg

    df = pd.DataFrame
    try:
        df = pd.read_csv(inputfile, header=None)
    except:
        print('Error in pd.read_csv')
        sys.exit(2)

    total = df[0].sum(axis=0)
    print(f'Total is: {total}')


if __name__ == "__main__":
    main(sys.argv[1:])
