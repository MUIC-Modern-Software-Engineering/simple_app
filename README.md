Link: [Sonarqube](https://sonarcloud.io/summary/overall?id=thegangtechnology_simple_app)
## Setup Instruction
```
poetry install
```

## Run Test
```
poetry run pytest
```

## DB
If you need to migrate see
https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/


## What to do next

### Install Pre-commit (Recommended)
```
poetry run pre-commit install
```
If you wish to edit pre-commit behavior see ```.pre-commit-config.yaml```.
Normally it checks only the file you are committing. But if you wish to run it manually for all files do
```
poetry run pre-commit run --all
```

### Install Jupyter Notebook Kernel
```
poetry run python -m ipykernel install --user --name simple_app
```

### Adjusting the Dependencies
edit pyproject.toml or just do
```
poetry add numpy
```
or for dev dependencies
```
poetry add --dev numpy
```
See [python-poetry.org](https://python-poetry.org/)

### Change Pytest, Flake, Coverage Setting
See ```tox.ini```

### Change how sonarqube behaves.
See ```sonar-project.properties```

### Get Pycharm to show the correct coverage
Ironically in pycharm test configuration add `--no-cov` to `Additional Arguments` this turn off pytest-cov coverage and uses Pycharm's own pytest.
