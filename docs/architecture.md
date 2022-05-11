# Architecture

- Sphinx with https://myst-nb.readthedocs.io/ and an adopted https://pydata-sphinx-theme.readthedocs.io.
- Testing with [Pytest](https://pytest.org) (unittest is still supported out of the box)
- Code coverage report and endorsed by [Codecov](https://codecov.io)
- [nox](https://nox.thea.codes/): Test your code against environment matrix, lint and artifact check
- Format with [Black](https://github.com/psf/black) and [Isort](https://github.com/PyCQA/isort)
- Lint code with [Flake8](https://flake8.pycqa.org) and [Flake8-docstrings](https://pypi.org/project/flake8-docstrings/)
- [flit](https://python-poetry.org/): Manage releases
- [Pre-commit hooks](https://pre-commit.com/): Formatting/linting anytime when commit your code

Not yet integrated:

- Check static type with [Mypy](http://mypy-lang.org/) (optional)
- [bump2version](https://github.com/c4urself/bump2version): Pre-configured version bumping with a single command
