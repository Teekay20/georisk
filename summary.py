
import geopandas as gpd


def read_rows(filename):
    """Read a GeoPackage and return its records."""
    gdf = gpd.read_file(filename)
    return gdf.drop(columns="geometry").to_dict("records")


def clean_values(rows, column):
    """Extract valid numerical values from a column."""
    values = []

    for row in rows:
        try:
            value = float(row[column])

            if value == value and value not in (float("inf"), float("-inf")):
                values.append(value)

        except (ValueError, TypeError, KeyError):
            continue

    return values


def summarise(values):
    """Calculate and return summary statistics."""
    if not values:
        return {
            "count": 0,
            "smallest": None,
            "largest": None,
            "average": None
        }

    return {
        "count": len(values),
        "smallest": min(values),
        "largest": max(values),
        "average": sum(values) / len(values)
    }


def summarise_all(rows, columns):
    """Summarise all selected numerical columns."""
    results = {}

    for column in columns:
        values = clean_values(rows, column)
        results[column] = summarise(values)

    return results


# Run the summary on GeoRisk settlement data
rows = read_rows("data/processed/Akure_South_Settlements_UTM31.gpkg")

report = summarise_all(rows, ["building_count", "building_area"])

for column, value in report.items():
    print(
        f"{column}: "
        f"count={value['count']}, "
        f"smallest={value['smallest']}, "
        f"largest={value['largest']}, "
        f"average={value['average']:.2f}"
    )
