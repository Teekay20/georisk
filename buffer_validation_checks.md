### Purpose of the buffer

The 200 m buffer defines a zone extending 200 m around mapped watercourses in Akure South. It is the first step towards identifying settlements located near watercourses. The buffer alone does not assess flood risk or elevation, so elevation and other factors would be needed for a more complete risk assessment.

### Buffer definition and prediction

A 200 m buffer was selected as the operational definition of "near a watercourse" for this exploratory analysis. This is a judgement-based analytical threshold and should not be interpreted as a formal flood-risk or regulatory standard.

Before running the buffer, I expected the output to contain 30 features, based on the 30 watercourse features in the clipped input layer. The buffer was run without dissolving the features, so one buffer feature was retained for each input watercourse feature.

### Validation checks

**Map alignment:** The 200 m buffer follows the mapped watercourses, forming corridors along the stream network within the study area.

**Row count:** The buffered layer contains 30 features, matching the 30 watercourse features in the clipped input layer. The buffer was created without dissolving the features.

**Distance check:** A manual measurement from a watercourse to the buffer edge gave a distance of about 198 m, which is close to the intended 200 m buffer distance.

**Empty geometry:** I used Select by Expression with `$geometry IS NULL` to check for empty/null geometries. No features were selected, indicating that no empty geometries were found.

### Input discrepancy

The reprojected `Akure_South_Watercourses_UTM31.gpkg` contains 54 features, while `Akure_South_Watercourses_Clipped.gpkg` contains 30 features. The 24 features removed during clipping were outside the study area and did not intersect the clipped extent. The clipped layer contains 30 unique `osm_id` values.

### Additional observation

Fifteen of the 30 retained watercourse features are tagged `tunnel = culvert`. These represent piped sections carrying water beneath roads. They are included in the mapped watercourse network and therefore also contribute to the 200 m buffer corridors.
