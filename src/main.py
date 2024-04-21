import os
from src.utils import sort_status, format_date, get_from_to, cipher, get_json, sort_dates, revers

FILE_NAME = os.path.join('../data/operations.json')


def main():
    data_json = get_json(FILE_NAME)
    list_sorted_status = sort_status(data_json, state="EXECUTED")
    list_sorted_dates = sort_dates(list_sorted_status)
    last_5_transaction = revers(list_sorted_dates[-5:])

    for i in last_5_transaction:
        print(f"{format_date(i['date'])} {i.get('description')}")
        from_transaction, to_transaction = get_from_to(i, from_='from', to_='to')
        if from_transaction:
            print(f"{cipher(from_transaction)} -> {cipher(to_transaction)}")
        else:
            print(f"{cipher(to_transaction)}")
        print(f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")
        print()


if __name__ == "__main__":
    main()
