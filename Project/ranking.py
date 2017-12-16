"""
Author: Pedro Breton pab3507@rit.edu
Date: 11/14/2017
This task involves processing the data and rank ordering it for a given year.
"""

from utils import *


def sorted_ranking_data(data, year):
    """
    Returns a list of Countries sorted in descending order
    Args:
        data: tuple containing readed input from the data and metadata files
        year: target year

    Returns: a list of CuntryValues
    """

    country_values_list = []
    data = filter_year(data[0], data[1])

    for key, value in data.items():
        if value.values[year - 1960][0] == year and value.values[year - 1960][1] != 0:
            country_values_list.append(CountryValue(key, value.values[year - 1960][1]))

    country_values_list = sorted(country_values_list, key=lambda x: x.value, reverse=True)
    return country_values_list


def main():
    # read data
    data = read_data("worldbank_life_expectancy")

    # return the top ten and bottom ten life expectancies for a particular year
    while True:
        try:
            target_year = int(input("Enter year of interest (-1 to quit): "))

            if target_year == -1:
                break
            if target_year < 1960 or target_year > 2015:
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

            sorted_CountryValues = sorted_ranking_data(filtered_data, target_year)

            print("Top 10 Life Expectancy for %d" % target_year)
            for i in range(len(sorted_CountryValues)):
                if i == 10:
                    break
                print("%d: %s %s" % (i + 1, sorted_CountryValues[i].country, sorted_CountryValues[i].value))

            print("Bottom 10 Life Expectancy for %d" % target_year)

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
