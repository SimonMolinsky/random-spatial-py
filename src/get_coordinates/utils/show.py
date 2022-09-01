from typing import List

import geopandas as gpd
from shapely.geometry import Point

import matplotlib.pyplot as plt


def show_points(points: List, boundaries: gpd.GeoDataFrame = None, country_postal=None):
    """
    Function shows points on a world map.
    :param points: (List) [lon, lat] or [x, y]
    :param boundaries: (str) file with world boundaries
    :param country_postal: (str) postal code of a country if we want to show only it.
    """

    fig, ax = plt.subplots()

    if not isinstance(points[0], Point):
        points = [Point(x) for x in points]

    pseries = gpd.GeoSeries(points)

    if boundaries is not None:
        if country_postal is None:
            base = boundaries.plot(
                ax=ax, edgecolor='black', color='white', figsize=(14, 14)
            )
        else:
            base = boundaries[boundaries['POSTAL'] == country_postal].plot(
                ax=ax, edgecolor='black', color='white', figsize=(14, 14)
            )

        pseries.plot(ax=base, marker='o', color='red', markersize=2)
    else:
        pseries.plot(ax=ax, marker='o', color='red', markersize=2)
    plt.show()


if __name__ == '__main__':
    from src.points import random_from_point

    tpoint = [50.45, 30.523333]  # lat , lon
    rpoints = random_from_point(tpoint[1], tpoint[0])
    show_points(points=rpoints,
                boundaries=gpd.read_file('../boundaries/world_countries.geojson'),
                country_postal='UA')
