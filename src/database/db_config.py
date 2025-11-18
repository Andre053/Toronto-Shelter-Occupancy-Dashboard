from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
from dotenv import load_dotenv

import os

load_dotenv()

def get_engine():
    db_url = os.getenv('DB_URL')
    
    engine = create_engine(
        db_url,
        poolclass=NullPool,
        connect_args={
            'connect_timeout': 15,
            'sslmode': 'require' # for cloud dbs
        }
    )
    return engine