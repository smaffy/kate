import csv
import datetime


def read_csv_file(filename: str, chosen_delimiter=';') -> list:
    """
    Read CSV file into list of rows.

    Each row is also a list of "columns" or fields.

    CSV (Comma-separated values) example:
    name,age
    john,12
    mary,14

    Should become:
    [
      ["name", "age"],
      ["john", "12"],
      ["mary", "14"]
    ]

    Use csv module.

    :param filename: File to read.
    :return: List of lists.
    """
    with open(filename) as f:
        csv_reader = csv.reader(f, delimiter=chosen_delimiter)
        data_list = list(csv_reader)
    return data_list


# a = read_csv_file('username.csv')
# print(a)


def read_csv_file_into_list_of_dicts(filename: str) -> list:
    """
    Read csv file into list of dictionaries.
    Header line will be used for dict keys.

    Each line after header line will result in a dict inside the result list.
    Every line contains the same number of fields.

    Example:

    name,age,sex
    John,12,M
    Mary,13,F

    Header line will be used as keys for each content line.
    The result:
    [
      {"name": "John", "age": "12", "sex": "M"},
      {"name": "Mary", "age": "13", "sex": "F"},
    ]

    [
      ["name", "age"],
      ["john", "12"],
      ["mary", "14"]
    ]

    If there are only header or no rows in the CSV-file,
    the result is an empty list.

    :param filename: CSV-file to read.
    :return: List of dictionaries where keys are taken from the header.
    """

    data_list = read_csv_file(filename)
    keys = data_list[0]
    values = data_list[6:]
    dict_list = []
    for row in values:
        if row:
            row_dict = dict(zip(keys, row))
            dict_list.append(row_dict)

    return dict_list


a = read_csv_file_into_list_of_dicts('username.csv')
print(a)


def read_csv_file_into_list_of_dicts_using_datatypes(filename: str) -> list:
    """
    Read data from file and cast values into different datatypes.

    If a field contains only numbers, turn this into int.
    If a field contains only dates (in format dd.mm.yyyy), turn this into date.
    Otherwise the datatype is string (default by csv reader).

    Example:
    name,age
    john,11
    mary,14

    Becomes ('age' is int):
    [
      {'name': 'john', 'age': 11},
      {'name': 'mary', 'age': 14}
    ]

    But if all the fields cannot be cast to int, the field is left to string.
    Example:
    name,age
    john,11
    mary,14
    ago,unknown

    Becomes ('age' cannot be cast to int because of "ago"):
    [
      {'name': 'john', 'age': '11'},
      {'name': 'mary', 'age': '14'},
      {'name': 'ago', 'age': 'unknown'}
    ]

    Example:
    name,date
    john,01.01.2020
    mary,07.09.2021

    Becomes:
    [
      {'name': 'john', 'date': datetime.date(2020, 1, 1)},
      {'name': 'mary', 'date': datetime.date(2021, 9, 7)},
    ]

    Example:
    name,date
    john,01.01.2020
    mary,late 2021

    Becomes:
    [
      {'name': 'john', 'date': "01.01.2020"},
      {'name': 'mary', 'date': "late 2021"},
    ]

    Value "-" indicates missing value and should be None in the result
    Example:
    name,date
    john,-
    mary,07.09.2021

    Becomes:
    [
      {'name': 'john', 'date': None},
      {'name': 'mary', 'date': datetime.date(2021, 9, 7)},
    ]

    None value also doesn't affect the data type
    (the column will have the type based on the existing values).

    The order of the elements in the list should be the same
    as the lines in the file.

    For date, strptime can be used:
    https://docs.python.org/3/library/datetime.html#examples-of-usage-date
    """
