from pathlib import Path

CURRENT_PATH = Path(__file__).parent.parent
DATA_BASE_PATH = Path.joinpath(CURRENT_PATH, 'app', 'movies.db')

DEBUG_LOG_PATH = Path.joinpath(CURRENT_PATH, 'debug_log.log')
ERROR_LOG_PATH = Path.joinpath(CURRENT_PATH, 'errors_log.log')
