# Junction Fortum — Energy Consumption ML

This repository contains a reproducible scaffold for building predictive machine-learning models of energy consumption. It combines local training data with optional public data sources.

Structure highlights

- `data/` — raw, external and processed datasets
- `src/` — source code (data ingestion, feature engineering, modeling, utilities)
- `notebooks/` — EDA and training notebooks
- `configs/` — yaml config files for experiments
- `models/` — serialized model artifacts
- `scripts/` — helper scripts (fetch public data, infra)
- `tests/` — unit and integration tests
- `.github/workflows/` — CI config

Quickstart

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Edit `configs/default.yaml` for dataset paths and training params
3. Run `make train` to train a model (placeholder target)

For more details, see `docs/architecture.md` and the files under `src/`.
