import os
from typing import List
from typing import Dict


def get_all_paths(base_dir: str) -> List[str]:  # get all file paths
    file_list = []

    for file in os.listdir(base_dir):  # get all files in the directory
        file_path = os.path.join(base_dir, file)
        if file_path != '/Users/chuwen/Desktop/eland/doc/.DS_Store':
            file_list.append(file_path)
    return file_list


def read_file(file: str) -> str:  # read articles
    with open(file) as f:
        return f.read()


def article2bigram(article: str) -> List[str]:  # generate bigram list
    total_grams = [article[i:i + 2] for i in range(0, len(article) - 1)]
    return total_grams


def bigram2freqdict(total_grams: List[str]) -> Dict[str, int]:  # generate frequency dictionary
    freqdict = dict()
    for ele in total_grams:
        freqdict[ele] = freqdict.get(ele, 0) + 1  # provide a default value: 0 if the key does not exist
    return freqdict
