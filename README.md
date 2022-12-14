# random-spatial-py

Generate random coordinates with Python!

## How does it work?

1. Get the point of interest in a decimal coordinates, for example here are Helsinki: `60.170833, 24.9375` (Lat / Lon).
2. Run:

```shell
python -m get_coordinates -x 24.9375 -y 60.170833
```

```shell
...
(24.805761542425525, 60.12636229548734)
(24.992194545035403, 59.99617042369173)
(24.85936846675646, 60.352041172278234)
(24.90421708758241, 59.99680822317264)
(25.010361179054506, 60.2346001210305)
(24.694265198206605, 60.2134501651695)
...
```

3. You may store results in a csv file or json file with options:

```shell
python -m get_coordinates -x 24.9375 -y 60.170833 --txt mycsv.csv --json myjson.json
```

4. You may check results on a map with option:

**Global view**:

```shell
python -m get_coordinates -x 24.9375 -y 60.170833 -v
```

![Image with random points located near Helsinki, Finland and world countries borders](https://github.com/SimonMolinsky/random-spatial-py/blob/main/Figure_1.png "Show random points on the world map")

**Local view with country POSTAL code**:

```shell
python -m get_coordinates -x 24.9375 -y 60.170833 -p FIN
```

![Image with random points and Finnish border. Points are located near Helsinki.](https://github.com/SimonMolinsky/random-spatial-py/blob/main/Figure_2.png "Show random points within a finnish borders")

## Limits

- `show()` function works only with EPSG:4326 projection (decimal representation of spherical coordinates used by GPS system)

## Setup

```shell
pip install random-spatial-py
```

## API

### `get_coordinates.lib.points.random_from_point()`

> Generates random set of points from a given coordinates.

**Parameters**:

* `cx`: `float` - Longitude,
* `cy`: `float` - Latitude,
* `no`: `int`, default=`100`, number of generated points.
* `step_size`: `float`, default=`0.1`, step to define the bounding box borders from (cx, cy) to create random points.

**Returns**:

* `List[(lon, lat), ...]` - number of points defined by `no`.

---

### `get_coordinates.utils.export.export_txt()`

Exports given list of points to csv file with the header `Lon/Lat`.

**Parameters**:

* `fname`: `str` - path to the file where points must be exported,
* `points`: `List` - the set of random points.

### `get_coordinates.utils.export.export_json()`

Exports given list of points to json file with headers the **key** named `Lon/Lat`.

**Parameters**:

* `fname`: `str` - path to the file where points must be exported,
* `points`: `List` - the set of random points.

---

### `get_coordinates.utils.show.show_points()`

Shows points on a map.

**Parameters**:

* `points`: `List` - the set of random points.
* `boundaries`: `gpd.GeoDataFrame`, default=None. If given it is a canvas for drawing points. Package can draw world countries boundaries.
* `postal_code`: `str`, default=None. If given then only single country is used as a canvas for drawing.

## Contributors

1. Szymon Moli??ski, TT: [@SimonMolinsky](https://twitter.com/SimonMolinsky), Github: [@SimonMolinsky](https://github.com/SimonMolinsky)