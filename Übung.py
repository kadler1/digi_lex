#import importiert Methoden einer anderen Klasse
import re


def write_dict(filename, beolingus_dict):
    with open(filename, mode='w', encoding='utf-8') as f:
        for k, v in beolingus_dict.items():
            f.write(str(k) + '\t' + str(v) + '\n')


def beolingus_as_list(file):
    list_of_lines = []
    with open(file, mode='r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()
            if not line.startswith('#'):
                list_of_lines.append(line)
    return list_of_lines


def split_beolingus(lines):
    beo_dict = {}
    for i, line in enumerate(lines):
        i += 1
        line_dict = {}
        line = line.split('::')
        german = line[0]
        english = line[1]
        german = german.split('|')
        english = english.split('|')
        # if len(german) != len(english):
        #    print(line)
        for e, l in enumerate(german):
            line_dict[german[e]] = english[e]
        beo_dict[i] = line_dict
    return beo_dict


beo_list = beolingus_as_list("de-en.txt")
beo_dic = split_beolingus(beo_list)
write_dict("printed_beo.txt" , beo_dic)
