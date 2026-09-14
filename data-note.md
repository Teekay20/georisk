# Data Note — Week 2

**Project:** GeoRisk — Identifying settlements in Akure South near watercourses and low-lying land
**Question:** Which settlements in Akure South Local Government Area sit in low-lying areas near watercourses?

All datasets below were clipped/extracted to the Akure South LGA study area and opened in QGIS.

---

## 1. Watercourses (Streams)

- **Source:** OpenStreetMap, extracted via QuickOSM (`waterway=stream`, Akure South bounding box) — https://www.openstreetmap.org/copyright
- **Feature count:** 54 line segments
- **Geometry type:** LineString
- **Key columns:** `waterway`, `name`, `intermittent`, `alt_name`, `osm_id`
- **Gaps / notes:** the `name` field is empty for a significant number of stream segments, which is typical of OSM hydrology data in this region — segments are still usable for proximity analysis via `waterway` type, but named-stream identification is limited.

## 2. LGA / Administrative Boundary

- **Source:** Nigeria Subnational Administrative Boundaries (COD-AB), OCHA — https://data.humdata.org/dataset/cod-ab-nga
- **Feature count:** 1 (Akure South LGA, isolated from the national admin-2 boundary layer)
- **Geometry type:** Polygon (MultiPolygon)
- **Key columns:** `admin2Name`, `admin2Pcod`, `admin1Name`, `admin0Name`
- **Gaps / notes:** `admin2AltN` (alternate name field) is blank for this feature; not an issue for the analysis since it's only used as a study-area mask.

## 3. Settlement Extents

- **Source:** GRID3 Nigeria Settlement Extents v3.1 — https://data.humdata.org/dataset/grid3-nga-settlement-extents-v3-1
- **Feature count:** 214 polygons (clipped to Akure South)
- **Geometry type:** Polygon (MultiPolygon)
- **Key columns:** `type` (settlement classification), `building_count`, `building_area`, `probability`, `source`
- **Gaps / notes:** a portion of polygons have low `probability` scores, meaning some settlement extents are modeled/estimated rather than confirmed — worth flagging as a data quality caveat for the risk analysis.

## 4. Elevation (DEM)

- **Source:** Copernicus GLO-30 Digital Elevation Model, via OpenTopography — https://portal.opentopography.org
- **Coverage:** Akure South bounding box (5.06–5.39°E, 7.07–7.35°N), ~1,133 km²
- **Resolution:** 30 m (raster, no feature count — pixel-based)
- **Type:** Digital Surface Model (DSM), GeoTiff format
- **Gaps / notes:** no data voids observed within the study area; being a DSM rather than a bare-earth DTM, elevation values include building/vegetation height, which is a known limitation for low-lying land analysis.

---

*All layers loaded and reviewed in QGIS. See project-brief.md for full project background.*
