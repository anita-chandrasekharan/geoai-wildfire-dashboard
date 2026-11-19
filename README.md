# 🔥 UK Wildfire Infrastructure Exposure Dashboard

An interactive geospatial dashboard that shows which UK roads and industrial assets sit downwind of satellite-detected wildfire hotspots, and how that exposure changes with wind speed and direction.

<!-- TODO: add a screenshot or GIF of the dashboard here, e.g. ![Dashboard](docs/dashboard.png) -->

## Why it matters

Wildfire smoke and spread follow the wind, so a simple circular buffer around a fire under- or over-states which assets are at risk. This project uses wind-aware exposure zones to give insurers, utilities and emergency planners a quicker first look at which infrastructure is in the path of an active fire.

## What it does

1. **Satellite fire detection:** pulls active fire hotspots for the UK from the NASA FIRMS API (VIIRS S-NPP, near-real-time), including fire radiative power (FRP).
2. **Infrastructure context:** downloads roads and commercial, industrial and warehouse buildings from OpenStreetMap (Overpass API) around the most intense fires.
3. **Spatial database:** stores everything in PostgreSQL + PostGIS with GiST spatial indexes.
4. **Wind-driven exposure zones:** for each fire, builds an elliptical exposure zone that is stretched, shifted and rotated downwind based on wind speed and bearing. Distances are computed in British National Grid (EPSG:27700) so buffers are in true metres.
5. **Interactive dashboard:** a Streamlit + Folium app where you move the wind sliders and see which roads and assets fall inside the exposure zones.

## Tech stack

Python · NASA FIRMS · OpenStreetMap / Overpass · PostgreSQL + PostGIS · GeoPandas · Shapely · PyProj · Streamlit · Folium

## Project structure

| File | Purpose |
| --- | --- |
| `app.py` | Streamlit dashboard (reads the snapshot files in `data/`) |
| `data_from_NASA.py` | Fetches FIRMS hotspots into PostGIS |
| `fetch_all_infrastructure.py`, `download_uk_infrastructure.py` | Fetch OSM roads and buildings into PostGIS |
| `generate_risk_map.py` | Builds a static HTML risk map (`wildfire_risk_map.html`) |
| `read_data.py` | Exports PostGIS tables to the snapshot files in `data/` |
| `config.py` | Reads API keys and database settings from `.env` |

## Run the dashboard

The dashboard runs from the snapshot files in `data/`, so no database or API key is needed.

```bash
git clone https://github.com/anita-chandrasekharan/geoai-wildfire-dashboard.git
cd geoai-wildfire-dashboard
pip install -r requirements.txt
streamlit run app.py
```

## Rebuild the data (optional)

This needs a local PostGIS database and a free [NASA FIRMS MAP_KEY](https://firms.modaps.eosdis.nasa.gov/api/map_key/).

```bash
pip install -r requirements-pipeline.txt
cp .env.example .env        # then add your FIRMS key and database password
python data_from_NASA.py
python fetch_all_infrastructure.py
python read_data.py         # refresh the snapshots used by the dashboard
```

## Limitations and next steps

- Exposure zones are a simple geometric wind model, not a physical fire-spread or smoke-dispersion model.
- Wind is set by the user; a next step is to pull live wind from a weather API (for example Open-Meteo).
- Planned: an asset vulnerability score combining distance, asset type and FRP, and a machine-learning model of fire likelihood from vegetation (NDVI), weather and terrain.

## Author

**Dr. Anita Chandrasekharan**, Remote Sensing & GIS (PhD, IIT Bombay) · [LinkedIn](https://www.linkedin.com/in/anita-chandrasekharan/)
