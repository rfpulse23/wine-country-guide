# Database Schema

## wineries
| Column | Type | Description |
|---|---|---|
| id | serial PK | |
| name | text | Winery name |
| tier | int | 1–4 quality tier |
| ava | text | American Viticultural Area (e.g. Dry Creek Valley) |
| region | text | Broader region grouping |
| restrained_style_match | int | 1–3 stars |
| like_favorites | text | Ridge / Testarossa / Eleven Eleven |
| public_tasting | text | Yes-appointment / Members / No |
| price_pp | text | Per-person tasting cost |
| days_hours | text | Operating hours |
| known_for | text | Signature wines / style |
| area | text | Specific location / neighborhood |
| book_via | text | URL or booking method |
| drive_from_healdsburg_min | int | Approx drive minutes |
| drive_from_napa_min | int | Approx drive minutes |
| info_status | text | Verified / Partly verified / Last known |
| notes | text | Operational notes |
| created_at | timestamp | |
| updated_at | timestamp | |

## visits
| Column | Type | Description |
|---|---|---|
| id | serial PK | |
| winery_id | int FK → wineries.id | |
| visit_date | date | |
| personal_rating | int | 1–5 |
| personal_notes | text | |
| created_at | timestamp | |

## avas
| Column | Type | Description |
|---|---|---|
| id | serial PK | |
| name | text | AVA name |
| parent_region | text | Napa / Sonoma / Healdsburg |
| lat | float | Centroid latitude |
| lng | float | Centroid longitude |
