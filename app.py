import random
from flask import Flask, render_template, jsonify
from shapely.geometry import Point, Polygon, MultiPolygon
from shapely.ops import unary_union

app = Flask(__name__)

# South Korea mainland + Jeju simplified polygon coordinates
# (longitude, latitude) pairs
SOUTH_KOREA_POLYGONS = [
    # Mainland
    [
        (126.10, 38.61), (126.94, 38.61), (127.78, 38.31), (128.37, 38.61),
        (128.66, 38.37), (129.07, 38.07), (129.41, 37.07), (129.58, 36.05),
        (129.43, 35.50), (129.35, 35.16), (129.08, 35.10), (128.57, 34.88),
        (128.04, 35.05), (127.57, 34.62), (127.30, 34.55), (126.53, 34.34),
        (126.12, 34.54), (126.26, 34.82), (126.43, 35.13), (126.15, 35.10),
        (125.95, 35.33), (126.05, 35.57), (126.34, 35.68), (126.48, 36.02),
        (126.05, 36.07), (125.99, 36.41), (126.05, 36.58), (126.13, 36.69),
        (126.19, 36.79), (126.33, 36.88), (126.05, 37.02), (126.05, 37.25),
        (126.39, 37.39), (126.22, 37.59), (126.55, 37.69), (126.35, 37.77),
        (126.60, 37.94), (126.10, 38.05), (126.10, 38.61),
    ],
    # Jeju Island
    [
        (126.16, 33.19), (126.26, 33.14), (126.57, 33.22),
        (126.88, 33.28), (126.96, 33.42), (126.72, 33.56),
        (126.36, 33.52), (126.16, 33.35), (126.16, 33.19),
    ],
]

# Build shapely MultiPolygon
_polygons = [Polygon(coords) for coords in SOUTH_KOREA_POLYGONS]
KOREA_SHAPE = unary_union(_polygons)
BOUNDS = KOREA_SHAPE.bounds  # (minx, miny, maxx, maxy)


def random_point_in_korea() -> tuple[float, float]:
    """Generate a random point within South Korea's borders."""
    minx, miny, maxx, maxy = BOUNDS
    while True:
        lon = random.uniform(minx, maxx)
        lat = random.uniform(miny, maxy)
        if KOREA_SHAPE.contains(Point(lon, lat)):
            return round(lat, 6), round(lon, 6)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/random")
def api_random():
    lat, lon = random_point_in_korea()
    return jsonify({"lat": lat, "lon": lon})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
