# Decision log

## 2026-11-18: Use pandas, not polars
- Considered: polars (faster, lower memory)
- Why: heavy transformations happen in PostgreSQL; Python handles
  small result sets. pandas integrates with to_sql, matplotlib and Jupyter.

## 2026-11-18: Java 25 (Temurin) to run Synthea
- Considered: Java 21 LTS; running Synthea inside Docker
- Why: Synthea needs Java 17+; installed locally for simplicity.

## 2026-11-18: Synthea release v4.0.0, downloaded 2026-11-18
- Seed 42, clinician seed 42, reference date 2026-01-01

## 2026-11-18: PostgreSQL 17 + pgvector via Docker Compose
- Considered: installing PostgreSQL directly on Windows
- Why: identical setup for anyone cloning the repo; pgvector preinstalled.

## 2026-11-21: Synthea data generation
- the seed 42 data generation provided single state data
- three states data genereated to support state-based entitlements, total about 5,000 patients to match the Project Definition.
- States: [Massachusetts, Texas, Florida] Seeds: [42, 43, 44] total patients: 5,744