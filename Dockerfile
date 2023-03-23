FROM python:3.10-slim

WORKDIR /app

RUN apt-get update \
    && apt-get -y install --no-install-recommends libpq-dev gcc build-essential

# Install Poetry
ENV POETRY_VERSION=1.4.0
RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock

RUN poetry install --no-root

COPY . .

RUN poetry install

CMD [ "poetry", "run" , "runserver"]
