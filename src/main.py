import os
from src.utils import sort_status
from src.utils import get_json


FILE_NAME = os.path.join('../data/operations.json')


def main():
    data_json = get_json(FILE_NAME)


    list_sorted_status = sort_status(data_json, state="EXECUTED")

if __name__ == "__main__":
    main()
