from core.cell_life_cycle.cell_maker import CellMaker
from core.cell_life_cycle.cell_deleter import CellDeleter
from config import Config


class App:
    def __init__(self):
        cell_maker = CellMaker(Config.database_path)
        cell_deleter = CellDeleter(Config.database_path)

