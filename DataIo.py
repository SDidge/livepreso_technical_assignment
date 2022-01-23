import csv

"""
DataIo package

Description:
    Simple package for basic / ADHOC data io.
    Does not include error handling by default, so type hints are required.
    Used to ensure we ingest data in expected formats.
Author: 
    Simon Di Giovanni
"""


def read_csv_to_matrix(path: str) -> list[list[str]]:
    """
    Reads a CSV file and returns a list of lists.
    Assumes no error handling is required.
    Ensures we have data in the correct format for prep and analysis
    """
    with open(path, "r") as file:
        data = csv.reader(file)
        return [row for row in data]


def print_dict_of_dict(data: dict[dict]):
    """
    Prints a dictionary of dictionaries nicely.
    """
    for key, value in data.items():
        print(f"{key}:")
        for key2, value2 in value.items():
            print(f"\t{key2}: {value2}")
