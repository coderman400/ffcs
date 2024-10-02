from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool

from alembic import context
# Import your models here
from models.database import \
    Base  # Ensure you have the right import for your Base
from models.models import Course, Professor, Slot  # Import your models

# This is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers if you have defined them in your config.
fileConfig(config.config_file_name)

# Add your model's MetaData object here
target_metadata = Base.metadata  # Assuming 'Base' is the declarative base for your models

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

# This conditional is needed to allow `alembic upgrade` to find the right function to call
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
