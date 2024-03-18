import geopandas as gpd
import matplotlib.pyplot as plt
from pathlib import Path

from helper_functions.plot_file_name import create_plot_file_name


def plot_country_occurrences(country_count_dict, title):
    unprinted_countries = []
    # Read the world map shapefile
    world_map = gpd.read_file(r"C:\Users\sweth\Documents\Repos\citations_meta_data_summary\world_map"
                          r"\ne_50m_admin_0_countries\ne_50m_admin_0_countries.shp")

    # print(world_map['NAME'].unique())
    # Plot the world map with all countries
    fig, ax = plt.subplots(figsize=(15, 10))
    world_map.plot(ax=ax, color='#F0F0F0', edgecolor='#CCCCCC', linewidth=0.5)

    # Iterate over the dictionary and plot circles for countries with occurrences
    for country, count in country_count_dict.items():
        try:
            # Get the geometry (polygon) of the country
            country_geometry = world_map[world_map['NAME'] == country].geometry.iloc[0]

            # Get the centroid of the country polygon
            lon, lat = country_geometry.centroid.coords[0]

            # Plot the circle
            ax.plot(lon, lat, 'o', markersize=count * 1.2, color='red', alpha=0.5)
        except (KeyError, IndexError):
            unprinted_countries.append(country)
            # Handle cases where country data might be missing
            pass
    print(f"unprinted_countries: {unprinted_countries}")
    # Add labels and title
    ax.set_title(title)
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')

    plt_name = title + "_.png"
    plt_path = create_plot_file_name(filename=plt_name)
    # plot_folder = Path(r".\citations_meta_data_summary")
    # plt_path = plot_folder / plt_name
    # # plt.savefig(f"{title}_.png")
    plt.savefig(plt_path.as_posix())


def fix_countries_name(country_count_dict):
    keys = country_count_dict.keys()

    if 'United States' in keys:
        country_count_dict['United States of America'] = country_count_dict.pop('United States')
    elif 'Czech Republic' in keys:
        country_count_dict['Czechia'] = country_count_dict.pop('Czech Republic')
    return country_count_dict


def main():
    country_count_dict = {'France': 10, 'United Kingdom': 15, 'Germany': 8, 'United States': 20}
    country_count_dict = fix_countries_name(country_count_dict)
    plot_country_occurrences(country_count_dict, title="test_run")


if __name__ == "__main__":
    main()