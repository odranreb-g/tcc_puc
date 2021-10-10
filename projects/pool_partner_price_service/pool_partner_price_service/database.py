from prettyconf import config
from sqlalchemy import create_engine

engine = create_engine(
    f"postgresql+psycopg2://{config('POSTGRES_USER')}:{config('POSTGRES_PASSWORD')}"
    f"@{config('POSTGRES_HOST')}:{config('POSTGRES_PORT')}/{config('POSTGRES_DB')}"
)
