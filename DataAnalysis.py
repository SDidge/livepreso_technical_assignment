
import enum
import statistics
import DataPrep


"""
DataAnalysis package

Description:
    Simple package for basic / ADHOC data analysis.
    Does not include error handling by default, so type hints are required.
    Requires DataPrep package for data preparation.
Author: 
    Simon Di Giovanni
"""

class Aggregation(enum.Enum):
    """
    Enum for aggregation functions.
    """
    SUM = 0
    COUNT = 1
    AVERAGE = 2


def distinct_count(data: list):
    """
    For code simplicty and readability.
    """
    return len(set(data))


def sum_list(data: list[str], decimal_places: int) -> float:
    """
    Wrapper for round, sum. Improves readability.
    """ 
    return round(sum([float(x) for x in data]), decimal_places)


def calculate_median(data: list[float]) -> float:
    """
    Simple wrapper to ensure we abstract statistics from the rest of the code.
    """
    return statistics.median(data)


def group_by_aggregate(group_by_data: list[str], data_to_aggregate: list[str], aggregation: Aggregation) -> dict[str, float]:
    """
    Groups the data by a column and aggregates the values in another column.
    Assumes the index of the group_by_data matches the index of the data_to_aggregate.
    Assumes the data_to_aggregate is a list of int / floats if using the SUM or AVERAGE function.
    Reduces code duplication, improves readability. Designed for scalability.
    """
    data_dict = DataPrep.convert_lists_to_dict_of_lists(group_by_data, data_to_aggregate)
    match aggregation:
        case Aggregation.SUM:
            return {key: sum([float(x) for x in value]) for key, value in data_dict.items()}
        case Aggregation.COUNT:
            return {key: sum([1 for x in value]) for key, value in data_dict.items()}
        case Aggregation.AVERAGE:
            return {key: statistics.mean([float(x) for x in value]) for key, value in data_dict.items()}


def order_dict_by(data: dict[str, int], descending: bool) -> dict[str, int]:
    """
    Orders a dictionary by the integer value. Assumes ascending order.
    https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    """
    return {key: value for key, value in sorted(data.items(), key=lambda item: item[1], reverse=descending)}


def calculate_percentage_breakdown(data: dict[str, int], total: int) -> dict[str, float]:
    """
    Calculates the percentage breakdown of a dictionary of values based on an input total.
    """
    return {key: value / total for key, value in data.items()}


def perform_std_on_dict(data: dict[dict[str,int]]) -> dict[str, float]:
    """
    Calculates the standard deviation of a dictionary of dictionaries.
    """
    return {key: statistics.stdev([value for value in values.values()]) for key, values in data.items()}