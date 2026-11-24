# Wine Country Guide

A personal winery database and trip planning tool for Napa, Sonoma, and Healdsburg wine country.

## Project Structure

```
wine-country-guide/
├── data/
│   ├── raw/          # Source data exports from Google Sheets
│   └── processed/    # Cleaned, normalized data ready for analysis
├── scripts/
│   ├── etl/          # Data ingestion and transformation scripts
│   └── analysis/     # Data science, trip optimization, clustering
├── frontend/         # Web app (map, filters, trip planner)
└── docs/             # Notes, schema definitions, decisions
```

## Roadmap

- [x] Curated winery spreadsheet (Napa, Sonoma, Healdsburg)
- [ ] AVA / sub-region taxonomy
- [ ] Database schema (PostgreSQL)
- [ ] ETL pipeline from Google Sheets → database
- [ ] Trip optimizer (routing by base location + day count)
- [ ] Style clustering (taste profile similarity)
- [ ] Interactive map frontend (Mapbox)
- [ ] Personal visit log and ratings

## Data

The source data lives in Google Sheets and is periodically exported to `data/raw/`.
Processed/normalized versions live in `data/processed/`.

## Stack

- **Data**: Python, pandas, PostgreSQL
- **ETL**: Python scripts in `scripts/etl/`
- **Analysis**: Jupyter notebooks in `scripts/analysis/`
- **Frontend**: TBD (Next.js or Streamlit)
