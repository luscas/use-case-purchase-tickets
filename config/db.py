import dotenv
import os

dotenv.load_dotenv()

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

from db.models import Base

engine = sa.create_engine(os.environ["DB_CONNECTION_STRING"])

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)
