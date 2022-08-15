# Ubuntu Dialogue Corpus Parser
>This repository contains the source code for the models used in the following paper:
>(Fill Research Paper Publication link when available)


## Background 
This Corpus Parser is based on the open-source Ubuntu Dialogue Corpus by Lowe, Ryan, et al. The Corpus consists of almost one million one-to-one chat dialogues from Ubuntu technical support.

This open-source corpus can be found available [_here_](https://github.com/npow/ubottu).



## Introduction 
I used this corpus to find the most frequently occurred person in this corpus, and then parse and extract all the conversations involving that specific person (as sender or recipient).
The format of the parsed conversation would look like this:
```
[me] ...
[others]...
[me] ...
...
<|endoftext|>
```
`[me]` represents the most often occurred person and `[others]` is the other participant in the chat. 

## Method 
I first download the .tgz file containing all the information using this [link](http://cs.mcgill.ca/~jpineau/datasets/ubuntu-corpus-1.0/ubuntu_dialogs.tgz). I then unzipped the file using the command:
```
$ tar -xvzf ubuntu_dialogs.tg
```

The unzipped result would be a folder called `dialogue`, which contains about 350 sub-directories that each include a large number of different .tsv files. So I created `dialogue_combine.py` to combine all the sub-directories whose name is `< 100`, thus shrinking the size of the parsing dataset to one that the computer can handle more comfortably. 

- `dialogue_combine.py` takes in the directory named `dialogue` and outputs a .tsv file named `dialogue.tsv` under path `./data/parsed_data/`

To find the most frequently occurred speaker, I created `dialogue_counter.py` to return the name of the most-frequent occurred speaker and the number of times they appear. The result was:
```
ActionParsnip: 161411
```
- `dialogue_counter.py` takes the `dialogue.tsv` file as input and prints the most-frequent occurred speaker and the number of times they appear in the console.

Knowing the most frequently occurred speaker is `ActionParsnip`, I created `dialogue_restrict.py` to extract all the conversations involving `ActionParsnip`
- `dialogue_restrict.py` takes in the `dialogue.tsv` file as input and creates a .txt file named `ActionParsnip_chat.txt` under path `./data/parsed_data/` as output
- `ActionParsnip_chat.txt` is included in this GitHub repository. Due to the size of the files, other files such as `dialogue.tsv` are not included.

## Setup 
For `dialogue_counter.py` to run correctly, it requires `pandas` package installed.

For installation, please refer to this [document](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html).

## Procedure
To replicate this process described above, follow the instructions below: 

1. Go to this [link](http://cs.mcgill.ca/~jpineau/datasets/ubuntu-corpus-1.0/ubuntu_dialogs.tgz), a .tgz file will be downloaded automatically. 
2. Run this command in terminal to unzip:
```
$ tar -xvzf ubuntu_dialogs.tg
```
3. The unzipped result is a folder named `dialogue`, put it under path `Ubuntu-Dialogue-Corpus-Parser/data/`, replace the empty `dialogue` directory that comes with this project
4. Run `dialogue_combine.py`, to adjust the number of sub-directories it combines, adjust this variable in `line 3`:
```
combine_num = 100
```
It is set to 100 by default.
5. Run `dialogue_counter.py`, the most frequently occurred speaker and the number of times they appear will be printed in the console
6. Run `dialogue_restrict.py`, to set the desired speaker name, adjust the variable in `line 1`:
```
speaker_name = 'ActionParsnip'
```
It is set to `ActionParsnip` by default.

_The extraction result will be under this path: `/data/parsed_data/{speaker_name}_chat.txt`_

## Reference 
- Ubuntu Dialogue Corpus:

Lowe, Ryan, et al. “The Ubuntu Dialogue Corpus: A Large Dataset for Research in Unstructured Multi-Turn Dialogue Systems.” Proceedings of the 16th Annual Meeting of the Special Interest Group on Discourse and Dialogue, 30 June 2015, https://doi.org/10.18653/v1/w15-4640. 





