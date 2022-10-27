FROM python:3.10.4

WORKDIR /backend

COPY /backend .

RUN cd /backend && pip install -e .

WORKDIR /backend/common

CMD ["alembic", "upgrade", "head"]