"""
Author: Pedro Breton pab3507@rit.edu
Date: 11/14/2017
This task involves computing the largest drops in life expectancy experienced
across any portion of the entire timeline.
"""
from utils import *


def sorted_drop_data(data):
    """
    Args:
        data:a tuple

    Returns:A sorted list of Range structures. The list is sorted in ascending order based on
    the change in life expectancy from the first value to the second value
    """

    country_values_list = []

    dict_countries = {}
    for key, info in data[1].items():
        if info.region != "":
            dict_countries[key] = info

    data = filter_year(data[0], dict_countries)

    for key, value in data.items():
        filter0 = list(filter(lambda x: x[1] != 0, value.values))
        if len(filter0) < 2:
            continue
        max_drop = (Range(key, 0, 0, 1.0, 100.0))
        for i in range(len(value.values)):
            if value.values[i][1] == 0:
                continue

            filter_zeroes = list(filter(lambda x: x[1] != 0, value.values[i + 1:]))
            if filter_zeroes == []:
                continue
            min_growth = min(filter_zeroes, key=lambda x: x[1])

            drop = min_growth[1] - value.values[i][1]

            if drop < max_drop.value2 - max_drop.value1:
                max_drop = (Range(key, int(value.values[i][0]), int(min_growth[0]), value.values[i][1], min_growth[1]))

        country_values_list.append(max_drop)

    country_values_list = sorted(country_values_list, key=lambda x: x.value2 - x.value1)
    return country_values_list


def main():
    data = read_data("worldbank_life_expectancy")

    sorted_CountryValues = sorted_drop_data(data)

    # print the top 10 life expectancy drops
    print("Worst life expectancy drops: 1960 to 2015")
    for i in range(len(sorted_CountryValues)):
        if i == 10:
            break
        print("%d: %s from %d (%s) to %d (%s): %s" % (
        i + 1, sorted_CountryValues[i].country, sorted_CountryValues[i].year1, sorted_CountryValues[i].value1,
        sorted_CountryValues[i].year2, sorted_CountryValues[i].value2,
        sorted_CountryValues[i].value2 - sorted_CountryValues[i].value1))


if __name__ == '__main__':
    main()
