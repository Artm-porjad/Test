import os
DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql+asyncpg://postgres:23456@localhost:54320/test')