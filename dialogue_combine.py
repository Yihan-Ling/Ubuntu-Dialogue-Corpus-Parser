import os
output_file_path = './data/parsed_data/dialogue.tsv'

def main():
    input_path = './data/dialogs'
    output_file = open(output_file_path, "w")
    output_file.write('')
    for root, dirs, files in os.walk(input_path):
        num = root[15:]
        if(len(num)<1):
            continue
        if(int(num)>100):
            continue
        # print(root)
        for file in files:
            if(file.endswith('.tsv')):
                file_path = root+'/'+file
                print(file_path)
                combine(file_path)


def combine(input_file_path):
    with open(input_file_path) as input_file:
        input_content = input_file.read()

    output_file = open(output_file_path, "a")
    output_file.write(input_content + '\n')



if __name__ == '__main__':
    main()