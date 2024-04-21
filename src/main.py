import os
from src.utils import sort_status
from src.utils import get_json
from src.utils import sort_dates
from src.utils import revers

FILE_NAME = os.path.join('../data/operations.json')


def main():
    data_json = get_json(FILE_NAME)
    list_sorted_status = sort_status(data_json, state="EXECUTED")
    list_sorted_dates = sort_dates(list_sorted_status)
    last_5_transaction = revers(list_sorted_dates[-5:])

if __name__ == "__main__":
    main()
