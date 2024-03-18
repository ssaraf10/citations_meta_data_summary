import pandas as pd
import numpy as np
from pathlib import Path

from helper_functions.append_unique_country import append_unique_items
from helper_functions.countries_counter import count_country_occurrences
from helper_functions.extract_country import extract_country
from helper_functions.world_map_plot import plot_country_occurrences, fix_countries_name


def main():
    folder_path = Path(r"C:\Users\sweth\OneDrive\Shashank\Shashank EB1B\Shashank citations")
    countries_count_dict = dict()

    for csv_path in folder_path.rglob("*.csv"):
        # if "Electrochemical" in csv_path.name:
        print(csv_path)
        df = pd.read_csv(csv_path)
        arr = df["Correspondence Address"]
        arr = arr.to_list()

        for line_item in arr:
            if isinstance(line_item, str):
                countries_extract = extract_country(line_item)
                countries_count_dict = count_country_occurrences(countries_extract, countries_count_dict)

    countries_count_dict = fix_countries_name(countries_count_dict)
    plot_country_occurrences(countries_count_dict, title="Shashank's Citation Over the World")


if __name__ == "__main__":
    main()
