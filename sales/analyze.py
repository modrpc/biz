import sys
import pandas as pd

import pathlib


def run(file):
    datadir = pathlib.Path('data/')
    path = datadir / (file + '.xlsx')
    df = pd.read_excel(path)
    print(df)

if __name__ == '__main__':
    print(os.getcwd())
    if (len(sys.argv) < 2):
        print('Usage: ' + sys.argv[0] + ' <filename>')
        sys.exit()
    run(sys.argv[1])
