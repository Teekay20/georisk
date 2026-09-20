# Week 3 Data Preparation Notes

## Project question

Which settlements in Akure South LGA sit in low-lying areas near watercourses?

## 1. CRS check

The working CRS selected for the project is EPSG:32631, WGS 84 / UTM Zone 31N. This CRS was selected because Akure South is in western Nigeria and UTM Zone 31N provides projected coordinates in metres, which are appropriate for distance and area calculations.

The prepared study area boundary, settlement layer, watercourses layer, and DEM use EPSG:32631.

## 2. Study area boundary

The Akure South LGA boundary was prepared as the project study area and saved as:

`data/processed/Akure_South_Study_Area_UTM31.gpkg`

The layer contains the Akure South study area used for subsequent clipping.

## 3. Reprojection and clipping

The settlement data were prepared in the working CRS, EPSG:32631, and then clipped to the Akure South study area. The prepared layer is:

`data/processed/Akure_South_Settlements_UTM31.gpkg`

The watercourses were obtained using the QuickOSM plugin in QGIS. The resulting layer was prepared in the working CRS, EPSG:32631, and then clipped to the Akure South study area. The prepared layer is:

`data/processed/Akure_South_Watercourses_Clipped.gpkg`

The DEM was already in EPSG:32631 and was clipped to the Akure South study area using the study-area boundary as the mask. The prepared raster is:

`data/processed/Akure_South_DEM_Clipped.tif`

All prepared datasets were saved in `data/processed/`.

The filenames containing `Clipped` refer to prepared analysis layers. The watercourses and DEM also use EPSG:32631, as stated above, although `_UTM31` is not included in those two filenames.

## 4. Area sanity check

The area of the prepared Akure South study-area boundary was calculated in EPSG:32631 using:

`$area / 1000000`

The calculated area is:

`308.06 km²`

This was compared with the commonly cited area of approximately 331 km² for Akure South LGA. The difference is approximately 22.94 km², or 6.93%.

The difference was flagged as a boundary/data-source discrepancy rather than ignored. Different administrative boundary datasets and boundary versions can produce different calculated extents. The 308.06 km² boundary was therefore retained as the working study area because it is the boundary dataset used for this project.

## 5. Raw data check

The original/source datasets that were available were placed in:

`data/raw/`

These include the original administrative boundary data, GRID3 settlement data and documentation, and the original DEM.

The watercourses were obtained directly through the QuickOSM plugin in QGIS. A separate original QuickOSM watercourse file was not retained in `data/raw/`; the prepared watercourse layer is stored in `data/processed/`.

The available raw files were not modified during processing.

## 6. Problems and decisions

One data-management issue was identified: the QuickOSM watercourses were generated directly in QGIS, and a separate original watercourse file was not retained in `data/raw/`.

Decision: this was documented rather than creating or claiming a raw watercourse file that does not exist. The prepared watercourse layer was retained in `data/processed/`.

The 308.06 km² study-area result also differed from the commonly cited 331 km² LGA area by approximately 6.93%. This was flagged as a boundary/data-source discrepancy, and the project boundary was retained as the working study area.

No other problems were identified during the reprojection and clipping steps.

## 7. Analysis-ready data location

The prepared datasets are stored in:

`data/processed/`

The main analysis-ready layers are:

* `Akure_South_Study_Area_UTM31.gpkg`
* `Akure_South_Settlements_UTM31.gpkg`
* `Akure_South_Watercourses_Clipped.gpkg`
* `Akure_South_DEM_Clipped.tif`
