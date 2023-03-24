FROM python:3.10-slim-bullseye

WORKDIR /app

RUN apt-get update \
    && apt-get -y install --no-install-recommends libpq-dev gcc build-essential

# Install Poetry
ENV POETRY_VERSION=1.4.0
RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock

RUN poetry install --no-root --with gunicorn

RUN apt-get remove -y gcc build-essential
RUN apt-get autoremove -y

COPY . .

RUN poetry install

# actually the default gunicorn runs on port 80 which works with default azure cloud but I wanna show you here you
# and get it to work on any port your like

EXPOSE 5555

CMD [ "poetry", "run", "gunicorn", "-w", "3", "-b", "0.0.0.0:5555", "simple_app.app:app"]

# CMD [ "poetry", "run" , "runserver"]
