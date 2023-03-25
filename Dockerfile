FROM python:3.10

LABEL Maintainer="gounux <contact@guilhemallaman.net>"

WORKDIR /app
COPY . /app

RUN pip install poetry
RUN poetry install

ENTRYPOINT ["poetry", "run", "python", "mastobots.py"]
