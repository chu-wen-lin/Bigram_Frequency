from typing import List
from typing import Dict
from utils.tools import get_all_paths, read_file, article2bigram, bigram2freqdict
from objects.document import Document

if __name__ == "__main__":
    base_dir = '/Users/chuwen/Desktop/eland/doc'
    result = []
    file_list: List[str] = get_all_paths(base_dir)
    for file in file_list:
        article: str = read_file(file)
        bigram_list: List[str] = article2bigram(article)
        term_freq: Dict[str, int] = bigram2freqdict(bigram_list)
        # create list of object by appending class instances
        result.append(Document(article, bigram_list, term_freq))

    for i, obj in enumerate(result):
        print(f'Doc {i}: ')
        print(obj.article, '\n', obj.bigram_list, '\n', obj.term_freq)
        if i != len(result) - 1:
            print('-' * 20)

