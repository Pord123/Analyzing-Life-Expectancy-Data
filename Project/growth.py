"""
Author: Pedro Breton pab3507@rit.edu
Date: 11/14/2017
This task has inputs of a starting year and an ending year, and involves
computing and rank ordering the absolute growth in life expectancy over the time
period.
"""
from utils import *


def sorted_growth_data(data, year1, year2):
    """

    Args:
        data: tuple with two dictionaries
        year1: start of the year range
        year2:end of the year range

    Returns: list of CountryValues
    """
    country_values_list = []
    data = filter_year(data[0], data[1])

    for key, value in data.items():
        if (value.values[year1 - 1960][0] == year1 and value.values[year1 - 1960][1] != 0) and (
                value.values[year2 - 1960][0] == year2 and value.values[year2 - 1960][1] != 0):
            country_values_list.append(CountryValue(key, value.values[year2 - 1960][1] - value.values[year1 - 1960][1]))

    country_values_list = sorted(country_values_list, key=lambda x: x.value, reverse=True)
    return country_values_list


def main():
    data = read_data("worldbank_life_expectancy")

    # print top 10 and bottom 10 growth in a certain year range
    while True:
        try:
            target_year1 = int(input("Enter starting year of interest (-1 to quit): "))

            if target_year1 == -1:
                break
            if target_year1 < 1960 or target_year1 > 2015:
                print("Valid years are 1960-2015")
                continue

            target_year2 = int(input("Enter ending year of interest (-1 to quit): "))

            if target_year2 == -1:
                break
            if target_year2 < 1960 or target_year2 > 2015:
                print("Valid years are 1960-2015")
                continue

            filtered_data = data
            target_region = input("Enter region (type ’all’ to consider all): ")
            valid_regions = ["Middle East & North Africa", "Middle East & North Africa", "North America",
                             "Latin America & Caribbean", "South Asia", "East Asia & Pacific", "Sub-Saharan Africa"]
            if target_region not in valid_regions and target_region != "all":
                print("’%s’ is not a valid region" % target_region)
                continue
            if target_region != "all" and target_region != "":
                filtered_data = filter_region(filtered_data, target_region)

            target_income = input("Enter income category (type ’all’ to consider all): ")
            valid_incomes = ["Lower middle income", "Upper middle income", "High income", "Low income"]
            if target_income not in valid_incomes and target_income != "all":
                print("’%s’ is not a valid income" % target_income)
                continue
            if target_income != "all" and target_income != "":
                filtered_data = filter_income(filtered_data, target_income)

            sorted_CountryValues = sorted_growth_data(filtered_data, target_year1, target_year2)

            print("Top 10 Life Expectancy Growth: %d to %d" % (target_year1, target_year2))
            for i in range(len(sorted_CountryValues)):
                if i == 10:
                    break
                print("%d: %s %s" % (i + 1, sorted_CountryValues[i].country, sorted_CountryValues[i].value))

            print("Bottom 10 Life Expectancy  Growth: %d to %d" % (target_year1, target_year2))

            count = 0
            for i in range(len(sorted_CountryValues))[::-1]:
                if count == 10:
                    break
                print("%d: %s %s" % (count + 1, sorted_CountryValues[i].country, sorted_CountryValues[i].value))
                count += 1
        except:
            pass


if __name__ == '__main__':
    main()
