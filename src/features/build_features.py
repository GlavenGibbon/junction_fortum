"""Feature engineering helpers."""
import pandas as pd


def basic_feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """Create basic time features and simple aggregations.

    Expects a column `timestamp` (or index) and numeric `value`/`energy`.
    """
    df = df.copy()
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['hour'] = df['timestamp'].dt.hour
        df['dayofweek'] = df['timestamp'].dt.dayofweek
        df['month'] = df['timestamp'].dt.month
    return df
