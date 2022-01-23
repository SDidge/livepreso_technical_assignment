"""
DataPrep package

Description:
    Simple package for basic / ADHOC data preperation.
    Does not include error handling by default, so type hints are required.
    Includes 2 bespoke functions specific to the titantic project.
Author: 
    Simon Di Giovanni
"""


def clean_matrix(data: list[list[str]]) -> list[list[str]]:
    """
    Cleans a matrix by removing whitespace and newline characters
    Ensures we have clean data.
    """
    return [[item.strip().replace("\n", "") for item in row] for row in data]


def convert_matrix_to_dict(data: list[list[str]]) -> dict[str, list[str]]:
    """
    Converts a matrix to a dictionary, assuming first row is the keys.
    Reduces code duplication,
    """
    keys = data[0]
    return {keys[i]: [row[i] for row in data[1:]] for i in range(len(keys))}


def convert_lists_to_dict_of_lists(
    keys: list[str], values: list[str]
) -> dict[str, str]:
    """
    Converts two lists to a dictionary of lists
    Reduces code duplication.
    """
    results = {keys: list() for keys in keys}
    for i, j in zip(keys, values):
        results[i].append(j)

    return results


def create_fare_banding(data: list[float]):
    """
    Creates a banding of floats.
    """
    banding = []
    for value in data:
        temp = float(value)
        if temp >= 0 and temp <= 100:
            banding.append("a. 0 - 100")
        elif temp > 100 and temp <= 200:
            banding.append("b. 101 - 200")
        elif temp > 200 and temp <= 300:
            banding.append("c. 201 - 300")
        elif temp > 300 and temp <= 400:
            banding.append("d. 301 - 400")
        elif temp > 400 and temp <= 500:
            banding.append("e. 401 - 500")
        elif temp > 500:
            banding.append("f. 500+")
        else:
            banding.append("g. Error")
    return banding


def create_age_banding(data: list[float]):
    """
    Creates a banding of floats.
    """
    banding = []
    for value in data:
        temp = float(value) if value != "" else 0
        if temp >= 0 and temp <= 10:
            banding.append("a. 0 - 10")
        elif temp > 10 and temp <= 20:
            banding.append("b. 11 - 20")
        elif temp > 20 and temp <= 30:
            banding.append("c. 21 - 30")
        elif temp > 30 and temp <= 40:
            banding.append("d. 31 - 40")
        elif temp > 40 and temp <= 50:
            banding.append("e. 41 - 50")
        elif temp > 50:
            banding.append("f. 50+")
        else:
            banding.append("g. Error")
    return banding
