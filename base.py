from sqlalchemy.orm import declarative_base

Base = declarative_base()
Base.metadata.schema = 'stock_scanner_v1'