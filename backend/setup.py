from setuptools import setup, find_packages

setup(
    name='test',
    version='0.1.0',
    packages=find_packages(include=['website.*']),
    install_requires=[
        'starlette',
        'uvicorn',
        'sqlalchemy',
        'alembic',
        'asyncpg',
        'psycopg2-binary',
        'python-multipart'
    ]
)