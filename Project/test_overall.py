"""
Test module to provide testing for components of the
project.

Testing of utils.py will be implicit in the testing
of other tasks.

Note that this testing does not cover expected
functionality when the programs are executed
directly.  You should carefully read the project
document to understand what is expected from
standalone execution, and test that yourselves.

Author: CS @ RIT
File:  test_overall.py
"""

import utils
import ranking
import growth
import drop


def test_ranking(data):
    """
    Function to test ranking functionality.  Also implicitly
    tests filtering functionality from utils.py.
    :param data: data structures returned from reading files.
    :return: None
    """

    print("Filtering for region Middle East & North Africa...", end="")
    fdata = utils.filter_region(data, "Middle East & North Africa")
    print("complete.")
    print("Sorting data for 1977...", end="")
    sorted_data = ranking.sorted_ranking_data(fdata, 1977)
    print("complete.")
    test_strings = list()
    test_strings.append("len(sorted_data) == 20")
    test_strings.append("sorted_data[0].country == 'Israel'")
    test_strings.append("sorted_data[6].value == 66.454")

    for test_str in test_strings:
        print("Testing:", test_str, "->", eval(test_str))

    print("Sorting data for 1965...", end="")
    sorted_data = ranking.sorted_ranking_data(fdata, 1965)
    print("complete.")

    test_strings = list()
    test_strings.append("len(sorted_data) == 19")
    test_strings.append("sorted_data[1].country == 'Qatar'")

    for test_str in test_strings:
        print("Testing:", test_str, "->", eval(test_str))

    print("Additional filtering for Upper middle income...", end="")
    fdata = utils.filter_income(fdata, "Upper middle income")
    print("complete.")
    print("Sorting data for 1999...", end="")
    sorted_data = ranking.sorted_ranking_data(fdata, 1999)
    print("complete.")

    test_strings = list()
    test_strings.append("len(sorted_data) == 5")
    test_strings.append("sorted_data[3].country == 'Algeria'")

    for test_str in test_strings:
        print("Testing:", test_str, "->", eval(test_str))

    print("Filtering for region South Asia...", end="")
    fdata = utils.filter_region(data, "South Asia")
    print("complete.")
    print("Sorting data for 2010...", end="")
    sorted_data = ranking.sorted_ranking_data(fdata, 2010)
    print("complete.")
    test_strings = list()
    test_strings.append("len(sorted_data) == 8")
    test_strings.append("sorted_data[4].country == 'Bhutan'")
    test_strings.append("sorted_data[1].value == 74.3392439")

    for test_str in test_strings:
        print("Testing:", test_str, "->", eval(test_str))

    print("Additional filtering for High income...", end="")
    fdata = utils.filter_income(fdata, "High income")
    print("complete.")

    print("Sorting data for 1984...", end="")
    sorted_data = ranking.sorted_ranking_data(fdata, 1984)
    print("complete.")

    test_strings = list()
    test_strings.append("len(sorted_data) == 0")

    for test_str in test_strings:
        print("Testing:", test_str, "->", eval(test_str))


def test_growth(data):
    """
        Function to test growth functionality.  Also implicitly
        tests filtering functionality from utils.py.
        :param data: data structures returned from reading files.
        :return: None
        """

    print("Filtering for region Latin America & Caribbean...", end="")
    fdata = utils.filter_region(data, "Latin America & Caribbean")
    print("complete.")
    print("Growth data for 1971 to 1991...", end="")
    sorted_data = growth.sorted_growth_data(fdata, 1971, 1991)
    print("complete.")
    test_strings = list()
    test_strings.append("len(sorted_data) == 34")
    test_strings.append("sorted_data[0].country == 'Honduras'")
    test_strings.append("sorted_data[11].value == 7.695")

    for test_str in test_strings:
        print("Testing:", test_str, "->", eval(test_str))

    print("Additional filtering for Low income...", end="")
    fdata = utils.filter_income(fdata, "Low income")
    print("complete.")
    print("Growth data for 1996 to 2012...", end="")
    sorted_data = growth.sorted_growth_data(fdata, 1996, 2012)
    print("complete.")

    test_strings = list()
    test_strings.append("len(sorted_data) == 1")
    test_strings.append("sorted_data[0].country == 'Haiti'")

    for test_str in test_strings:
        print("Testing:", test_str, "->", eval(test_str))

    print("Filtering for region North America...", end="")
    fdata = utils.filter_region(data, "North America")
    print("complete.")
    print("Growth data for 1960 to 1970...", end="")
    sorted_data = growth.sorted_growth_data(fdata, 1966, 1970)
    print("complete.")
    test_strings = list()
    test_strings.append("len(sorted_data) == 2")
    test_strings.append("sorted_data[0].country == 'Canada'")

    for test_str in test_strings:
        print("Testing:", test_str, "->", eval(test_str))

    print("Additional filtering for Lower middle income...", end="")
    fdata = utils.filter_income(fdata, "Lower middle income")
    print("complete.")

    print("Growth data for 1981 to 1982...", end="")
    sorted_data = growth.sorted_growth_data(fdata, 1981, 1982)
    print("complete.")

    test_strings = list()
    test_strings.append("len(sorted_data) == 0")

    for test_str in test_strings:
        print("Testing:", test_str, "->", eval(test_str))


def test_drop(data):
    """
        Function to test drop functionality.  Also implicitly
        tests filtering functionality from utils.py.
        :param data: data structures returned from reading files.
        :return: None
        """

    print("Filtering for region Europe & Central Asia...", end="")
    fdata = utils.filter_region(data, "Europe & Central Asia")
    print("complete.")
    print("Computing drop data...", end="")
    sorted_data = drop.sorted_drop_data(fdata)
    print("complete.")
    test_strings = list()

    test_strings.append("len(sorted_data) == 55")
    test_strings.append("sorted_data[0].country == 'Latvia'")
    test_strings.append("sorted_data[1].year2 == 1996")
    test_strings.append("sorted_data[2].year1 == 1988")
    test_strings.append("sorted_data[3].value2 == 66.5")
    test_strings.append("sorted_data[45].value1 == 76.1804878")

    for test_str in test_strings:
        print("Testing:", test_str, "->", eval(test_str))

    print("Filtering for all income...", end="")
    fdata = utils.filter_income(data, "all")
    print("complete.")
    print("Computing drop data...", end="")
    sorted_data = drop.sorted_drop_data(fdata)
    print("complete.")

    test_strings = list()
    test_strings.append("len(sorted_data) == 207")
    test_strings.append("sorted_data[-1].country == 'Isle of Man'")
    test_strings.append("sorted_data[-2].year1 == 1997")

    for test_str in test_strings:
        print("Testing:", test_str, "->", eval(test_str))

    print("Filtering for region East Asia & Pacific...", end="")
    fdata = utils.filter_region(data, "East Asia & Pacific")
    print("complete.")
    print("Computing drop data...", end="")
    sorted_data = drop.sorted_drop_data(fdata)
    print("complete.")
    test_strings = list()

    test_strings.append("len(sorted_data) == 33")
    test_strings.append("sorted_data[2].country == 'Marshall Islands'")
    test_strings.append("sorted_data[4].year1 == 1966")
    test_strings.append("sorted_data[10].year2 == 2011")

    for test_str in test_strings:
        print("Testing:", test_str, "->", eval(test_str))

    print("Filtering for Sub-Saharan Africa...", end="")
    fdata = utils.filter_region(data, "Sub-Saharan Africa")
    print("complete.")

    print("Computing drop data...", end="")
    sorted_data = drop.sorted_drop_data(fdata)
    print("complete.")

    test_strings = list()
    test_strings.append("len(sorted_data) == 48")
    test_strings.append("sorted_data[0].country == 'Rwanda'")

    for test_str in test_strings:
        print("Testing:", test_str, "->", eval(test_str))

    print("Filtering for all regions...", end="")
    fdata = utils.filter_region(data, "all")
    print("complete.")

    print("Computing drop data...", end="")
    sorted_data = drop.sorted_drop_data(fdata)
    print("complete.")

    test_strings = list()
    test_strings.append("len(sorted_data) == 207")

    for test_str in test_strings:
        print("Testing:", test_str, "->", eval(test_str))


def test_main():
    """
    Input files are read here, and passed to
    individual test functions.
    :return: None
    """

    print("Reading data files...", end="")
    data = utils.read_data("worldbank_life_expectancy")
    print("complete.")

    test_ranking(data)
    test_growth(data)
    test_drop(data)


test_main()
