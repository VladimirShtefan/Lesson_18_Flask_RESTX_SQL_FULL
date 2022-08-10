from pathlib import Path

CURRENT_PATH = Path(__file__).parent.parent
DATA_BASE_PATH_FOR_DEV = Path.joinpath(CURRENT_PATH, 'app', 'movies.db')
DATA_BASE_PATH_FOR_PROD = Path.joinpath(CURRENT_PATH, 'app', 'movies.db')
