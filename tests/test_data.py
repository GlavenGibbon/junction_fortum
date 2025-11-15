import pandas as pd
from src.data.ingest import load_local_csv


def test_load_local_csv_raises():
    import pytest
    with pytest.raises(FileNotFoundError):
        load_local_csv('data/raw/this_file_does_not_exist.csv')


def test_basic_dataframe():
    df = pd.DataFrame({'timestamp': ['2020-01-01'], 'value': [1]})
    assert not df.empty
