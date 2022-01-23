"""
Hello from LivePreso :) This is the file you should be editing. Good luck!
"""

import DataIo
import DataPrep
import DataAnalysis


PATH = "./titanic.csv"


def collect_data():
    """
    Collects data and prepares it for analysis
    Creates banding for numerical values to improve analysis results
    Used to ensure we do not have global variables.
    """
    raw_data = DataIo.read_csv_to_matrix(PATH)
    cleaned_data = DataPrep.clean_matrix(raw_data)
    cd_as_dict = DataPrep.convert_matrix_to_dict(cleaned_data)
    cd_as_dict["Fare_Banding"] = DataPrep.create_fare_banding(cd_as_dict["Fare"])
    cd_as_dict["Age_Banding"] = DataPrep.create_age_banding(cd_as_dict["Age"])

    return cd_as_dict


def number_of_passengers():
    data = collect_data()
    return DataAnalysis.distinct_count(data=data["PassengerId"])


def total_fare_paid():
    data = collect_data()
    return DataAnalysis.sum_list(data=data["Fare"], decimal_places=4)


def median_fare():
    data = collect_data()
    return DataAnalysis.calculate_median(data=[float(value) for value in data["Fare"]])


def cherbourg_survival_rate():
    data = collect_data()
    survived_per_embarked = DataAnalysis.group_by_aggregate(
        data["Embarked"], data["Survived"], DataAnalysis.Aggregation.SUM
    )
    passengers_per_embarked = DataAnalysis.group_by_aggregate(
        data["Embarked"], data["PassengerId"], DataAnalysis.Aggregation.COUNT
    )

    return survived_per_embarked["C"] / passengers_per_embarked["C"]


def passenger_class_by_survival():
    data = collect_data()
    survived_per_class = DataAnalysis.group_by_aggregate(
        data["Pclass"], data["Survived"], DataAnalysis.Aggregation.SUM
    )
    passengers_per_class = DataAnalysis.group_by_aggregate(
        data["Pclass"], data["PassengerId"], DataAnalysis.Aggregation.COUNT
    )

    survival_per_class = {
        key: survived_per_class[key] / passengers_per_class[key]
        for key in survived_per_class.keys()
    }
    survival_per_class_ordered = DataAnalysis.order_dict_by(
        data=survival_per_class, descending=True
    ).keys()

    return [int(key) for key in survival_per_class_ordered]


def calculate_survival_per_attribute(exclusions: list[str]):
    data = collect_data()
    results = {}
    for key in data.keys():
        # Remove redundant fields
        if key not in (exclusions):
            survived = DataAnalysis.group_by_aggregate(
                data[key], data["Survived"], DataAnalysis.Aggregation.SUM
            )
            passengers = DataAnalysis.group_by_aggregate(
                data[key], data["PassengerId"], DataAnalysis.Aggregation.COUNT
            )

            survival_per_attribute = {
                key: survived[key] / passengers[key] for key in survived.keys()
            }
            results[key] = survival_per_attribute

    ordered_results = {}
    for key in results.keys():
        ordered_results[key] = DataAnalysis.order_dict_by(
            data=results[key], descending=True
        )

    return ordered_results


def print_survival_analysis_summary():
    """
    Outputs full summary of survival analysis with exlusions.
    """
    exclusions = ["PassengerId", "Survived", "Name", "Cabin", "Ticket", "Fare", "Age"]
    DataIo.print_dict_of_dict(calculate_survival_per_attribute(exclusions))


def measure_function_speed():
    """
    Measures the speed of the high level functions.
    """
    import time

    start = time.time()
    number_of_passengers()
    end = time.time()
    print(f"Number of passengers: {end - start} seconds")

    start = time.time()
    total_fare_paid()
    end = time.time()
    print(f"Total fare paid: {end - start} seconds")

    start = time.time()
    median_fare()
    end = time.time()
    print(f"Median fare: {end - start} seconds")

    start = time.time()
    cherbourg_survival_rate()
    end = time.time()
    print(f"Cherbourg survival rate: {end - start} seconds")

    start = time.time()
    passenger_class_by_survival()
    end = time.time()
    print(f"Passenger class by survival: {end - start} seconds")

    start = time.time()
    calculate_survival_per_attribute(
        ["PassengerId", "Survived", "Name", "Cabin", "Ticket", "Fare", "Age"]
    )
    end = time.time()
    print(f"Calculate survival per attribute: {end - start} seconds")


if __name__ == "__main__":
    # measure_function_speed()
    print_survival_analysis_summary()
