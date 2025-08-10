from sqlalchemy import create_engine

engine = None

def init_engine(url):
    global engine
    if engine is not None:
        engine.dispose()
    engine = create_engine(url)

def get_engine():
    global engine
    if engine is None:
        raise ValueError('Must init engine first')
    return engine