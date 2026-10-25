import pandas as pd

df = pd.read_csv("wards.csv")

print("Dataset summary:")

ward_summary = {
    "count": int(df["ward"].count()),
    "unique": int(df["ward"].nunique()),
    "values": df["ward"].tolist(),
}
print("ward:", ward_summary)

area_summary = {
    "count": int(df["area_km2"].count()),
    "mean": float(df["area_km2"].mean()),
    "min": float(df["area_km2"].min()),
    "max": float(df["area_km2"].max()),
}
print("area_km2:", area_summary)
