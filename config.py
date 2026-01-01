from pathlib import Path
from json import load
from logging import getLogger, basicConfig, DEBUG

basicConfig(
    level=DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = getLogger(__name__)

logger.debug("starting config load")
try:
    base_config_file = Path("/etc/opt/cell/default_config.json")
    with open(base_config_file, "r") as f:
        base_config = load(f)

    configs_path = Path(base_config["default_configs_path"])
    main_config_file = Path(configs_path, "config.json")
    with open(main_config_file, "r") as f:
        main_config = load(f)
    is_config_loaded = True
except:
    logger.error(f"Could not load config")
    raise


class Config:
    default_config_path = "/etc/opt/cell/default_config.json"
    configs_path = str(configs_path)
    database_path = main_config["database_path"]

