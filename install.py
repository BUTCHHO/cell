from pathlib import Path
from json import dump
from logging import getLogger

logger = getLogger(__name__)

cell_var_dir = Path('/var/opt/cell')
try:
    cell_var_dir.mkdir(parents=True, exist_ok=False)
except FileExistsError:
    logger.log(1, "ERROR: Error while creating Cell directory")
    raise

cell_database_dir = Path(cell_var_dir, "database")
cell_database_dir.mkdir(parents=True, exist_ok=False)

configs = Path("/etc/opt/cell")
configs.mkdir(parents=True, exist_ok=False)

# Базовый конфиг содержит информацию о том, где находится папка с конфигами. Менять местоположение базового конфига запрещено
base_config_file = Path(configs, 'base_config.json')
base_config_file.touch()
try:
    with open(base_config_file, 'w') as f:
        data = {"base_configs_path": str(configs)}
        dump(data, f)
except:
    logger.log(1, "ERROR: Error while writing base config file")
    raise


try:
    main_config_file = Path(configs, "config.json")
    main_config_file.touch()
    with open(main_config_file, 'w') as f:
        data = {"database_path": str(cell_database_dir)}
        dump(data, f)
except:
    logger.log(1, "ERROR: failed to create main config file ")
    raise


