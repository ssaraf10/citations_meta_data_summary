def count_country_occurrences(countries_lst, country_counts):

    for country in countries_lst:
        if country in country_counts:
            country_counts[country] += 1
        else:
            country_counts[country] = 1
    return country_counts
