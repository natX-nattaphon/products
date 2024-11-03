# env.py
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os

# Import the metadata from your models
from models.models import Base  # Replace this with your actual import

config = context.config
fileConfig(config.config_file_name)

target_metadata = Base.metadata
