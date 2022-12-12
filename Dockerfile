FROM python:3.10

RUN apt-get update
RUN pip install -U pip

WORKDIR etl

COPY requirements.txt .
COPY ETL.py .
COPY alembic.ini .
COPY alembic ./alembic
COPY dataset ./dataset
COPY models ./models
COPY settings.py .

RUN pip install -r requirements.txt

ENTRYPOINT alembic upgrade head && python -m ETL
