
def main():
    input_path = './data/parsed_data/dialogue.tsv'
    output_path = './data/parsed_data/ActionParsnip_chat.txt'
    message_file = open(output_path, "w")
    message_file.writelines('')
    message_file = open(output_path, "a")
    flag = False

    fl = open(input_path, "r")
    lines = fl.readlines()
    for line in lines:
        if line == '\n':
            if flag:
                message_file.write('<|endoftext|>\n')
            continue
        line = line.split('\t')
        if line[1] == 'ActionParsnip':
            text = line[-1]
            message_line = '[me] ' + text
            message_file.write(message_line)
            flag = True
        elif line[2] == 'ActionParsnip':
            text = line[-1]
            message_line = '[others] ' + text
            message_file.write(message_line)
            flag = True
        else:
            flag = False

if __name__ == '__main__':
    main()