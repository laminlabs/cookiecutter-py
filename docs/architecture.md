# Architecture

- Docs that heavily use [myst-nb](https://myst-nb.readthedocs.io/). Our theme is based on [pydata-sphinx](https://pydata-sphinx-theme.readthedocs.io).
- [nox](https://nox.thea.codes/): Organize builds with virtual environment. Within, test using [pytest](https://pytest.org).
- Format with [black](https://github.com/psf/black) and lint code with [flake8](https://flake8.pycqa.org).
- [flit](https://python-poetry.org/): Manage releases.
- [pre-commit](https://pre-commit.com/): Formatting/linting anytime when commit your code.
- [gitmoji](https://gitmoji.dev/): Let others quickly grasp the type of PRs and commits you make!
- Sort imports [isort](https://github.com/PyCQA/isort).
- Check static type with [mypy](http://mypy-lang.org/).
- Strip notebooks with nbstripout. [TODO: need to exclude tasks directory!]
- GitHub Actions auto-builds.

We'll soon also integrate:

- Code coverage report and endorsed by [Codecov](https://codecov.io)
- [bump2version](https://github.com/c4urself/bump2version): Pre-configured version bumping with a single command

## Credits

This template is based on the pydata-sphinx-theme, the furo theme, tiangolo's setup and [waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage).
The latter is based on [zillionare/cookiecutter-pypackage](https://github.com/zillionare/cookiecutter-pypackage), which was based on [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage).
