from geotext import GeoText


def extract_country(text):
    # Extract country names from the text
    countries = GeoText(text).countries
    # print(countries)
    return countries
