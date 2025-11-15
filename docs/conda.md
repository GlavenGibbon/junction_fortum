Conda environment

Create the environment from `environment.yml`:

```bash
# Create env (conda)
conda env create -f environment.yml

# OR, if you have mamba (faster):
mamba env create -f environment.yml

# Activate
conda activate junction_fortum

# Verify installed packages
conda list -n junction_fortum | head -n 40
```

Notes
- The `environment.yml` uses `conda-forge` as a channel to ensure modern package availability.
- If `conda` is not installed, install Miniconda: https://docs.conda.io/en/latest/miniconda.html
- The environment includes a small set of common ML packages; add or pin versions as needed.
