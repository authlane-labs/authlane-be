import os

DATABASE_URL = os.getenv("DATABASE_URL", "mysql://app:app@localhost:3306/app")
ORM = "SQLAlchemy 2.0 Async Mode"
DATABASE = "MariaDB"
REST_ONLY = True
