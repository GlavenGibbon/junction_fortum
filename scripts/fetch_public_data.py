"""Script to fetch public datasets (placeholder).

Implement connectors to APIs (e.g., weather, pricing) and save them to `data/external/`.
"""
import requests
from pathlib import Path


def fetch_dummy(url: str, outpath: str):
    Path(outpath).parent.mkdir(parents=True, exist_ok=True)
    # Simple request example (user should implement retries/auth)
    r = requests.get(url)
    r.raise_for_status()
    with open(outpath, 'wb') as f:
        f.write(r.content)


if __name__ == '__main__':
    print('This script should be implemented to fetch public datasets.')
