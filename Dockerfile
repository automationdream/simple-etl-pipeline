FROM python:3.10

RUN apt-get update
RUN pip install -U pip

WORKDIR etl

COPY requirements.txt .
COPY ETL.py .
COPY alembic.ini .
COPY alembic .
COPY dataset .
COPY models .
COPY settings.py .

RUN pip install -r requirements.txt

RUN alembic upgrade head

RUN #python -m ETL
