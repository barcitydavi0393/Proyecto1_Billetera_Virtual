from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Definimos la ubicación del archivo de la base de datos SQLite
DATABASE_URL = "sqlite:///./billetera.db"

# 2. Creamos el motor de conexión
# 'check_same_thread=False' es exclusivo y necesario para SQLite en FastAPI
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# 3. Creamos una fábrica de sesiones (para hacer consultas e inserciones)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Creamos la clase Base de la cual heredarán todos nuestros modelos de tablas
Base = declarative_base()

# 5. Dependencia para obtener la sesión de la BD en cada petición HTTP
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()