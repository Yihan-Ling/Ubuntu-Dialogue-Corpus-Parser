import pandas as pd

input_path = './data/parsed_data/dialogue.tsv'


def main():
    max_VALUE = 0;
    max_NAME = ''
    df = pd.read_csv(input_path, sep='\t')
    group = df.groupby('Sender')
    for name, value in group.size().items():
        if value > max_VALUE:
            max_NAME = name
            max_VALUE = value

    print(max_NAME+': ' + str(max_VALUE))


if __name__ == '__main__':
    main()