# GeoRisk

Identifying settlements in Akure South near watercourses and low-lying land.

This project investigates:

Which settlements in Akure South Local Government Area sit in low-lying areas near watercourses?

Built over twelve months with GeoDev Lab Africa, Cohort One.

## Project Progress

### Week 1: Project Definition

The project question was defined around identifying settlements in Akure South LGA that are located in low-lying areas near watercourses. The study area, project objective, and initial approach were established.

See [project-brief.md](project-brief.md) for the full project brief.

### Week 2: Data Collection

The datasets required for the analysis were identified and sourced, including the Akure South administrative boundary, settlement data, watercourses, and elevation data.

See [data-notes.md](data-notes.md) for the Week 2 data sources and notes.

### Week 3: Data Preparation

The datasets were checked, reprojected to EPSG:32631, clipped to the Akure South study area, and saved as analysis-ready data in `data/processed/`.

See [data-notes.md](data-notes.md) for the Week 3 data preparation notes.

## Month 2: Development Environment and Early Python

### Week 5
Set up Python, VS Code and the terminal. [hello.py](hello.py) runs.

[Week 5 screenshot](screenshots/week5.png)

### Week 6
Set up the project with uv and added pandas.

Files: [pyproject.toml](pyproject.toml), [uv.lock](uv.lock), [check.py](check.py).

[Week 6 screenshot](screenshots/week6.png)

### Week 7
[analyse.py](analyse.py) reads [wards.csv](wards.csv), converts each area and classifies each ward.

[Week 7 screenshot](screenshots/week7.png)

### Week 8
[inspect_data.py](inspect_data.py) summarises ward and area_km2 in [wards.csv](wards.csv).

[Week 8 screenshot](screenshots/week8.png)

### Week 9
[summary.py](summary.py) uses reusable functions to analyse building_count and building_area across 214 Akure South settlement records.

[Week 9 screenshot](screenshots/week9.png)

### Month 2 Reflection

Month 2 helped me understand how Python can be used alongside GIS to examine and analyse data. I learned to organise a Python project, work with libraries such as pandas and GeoPandas, and write scripts that inspect and summarise datasets. 

One important part of this month was applying these skills to my GeoRisk project. Instead of working only with GIS software, I used Python to examine settlement attributes such as building count and building area across 214 records. This gave me an introduction to using Python for data analysis within a GIS project.

I still need to improve my Python programming skills, particularly in data cleaning and analysis, but I now have a better foundation to build on in future projects.
