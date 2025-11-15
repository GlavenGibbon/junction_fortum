Architecture notes

- Ingestion: `src/data/ingest.py` loads local files and merges external public datasets.
- Feature engineering: `src/features/` contains deterministic transforms to enable reproducible pipelines.
- Training: `src/models/train.py` is the main entrypoint for experiments and logs to MLflow.
- Serving: saved artifacts live in `models/` and `src/models/predict.py` exposes a simple loader.

Recommendations:
- Use MLflow for experiment tracking and model registry.
- Keep configs in `configs/*.yaml` and pass them to training scripts for reproducibility.
- Use CI to run linting and tests on pull requests.
