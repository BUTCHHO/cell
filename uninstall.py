from pathlib import Path
import shutil
import os
from config import Config
from logging import getLogger

logger = getLogger(__name__)

if os.geteuid() != 0:
    raise Exception("Cell database can be uninstalled only by root.")

should_delete_configs = input("Do you want to delete the configs? (y/n): ")

match should_delete_configs.lower():
    case "y":
        should_delete_configs = True
    case "n":
        should_delete_configs = False

should_delete_databases = input("Do you want to delete the databases? (y/n): ")
confirmation = input("ARE YOU SURE? This will PERMANENTLY delete user data from the databases, including their FILES, RIGHTS, and ROLES. (y/n): : ").lower()
if confirmation == 'n':
    exit()
match should_delete_databases.lower():
    case "y":
        should_delete_databases = True
    case "n":
        should_delete_databases = False

try:
    if should_delete_databases:
        database_path = Config.database_path
        shutil.rmtree(str(database_path))
except FileNotFoundError:
    logger.debug("Database already deleted. Skip")
except:
    logger.error(f"ERROR: Failed to delete database")
    raise


try:
    if should_delete_configs:
        shutil.rmtree(Config.configs_path)
except FileNotFoundError:
    logger.debug("configs already deleted. Skip")
except:
    logger.error(f"ERROR: Failed to delete configs")
    raise

shutil.rmtree(Path(Config.database_path).parent)