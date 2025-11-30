# Architecture

- Docs that heavily use [myst-nb](https://myst-nb.readthedocs.io/). The [lndocs](https://github.com/laminlabs/lndocs) theme is based on the [pydata-sphinx-theme](https://pydata-sphinx-theme.readthedocs.io).
- Organize builds with virtual environments using [nox](https://nox.thea.codes/). Test using [pytest](https://pytest.org).
- Format and lint with [ruff](https://docs.astral.sh/ruff/).
- Manage releases with [flit](https://flit.pypa.io/en/latest/).
- Lint anytime when you commit your code with [pre-commit](https://pre-commit.com/).
- Let others quickly grasp the type of PRs and commits you make with [gitmoji](https://gitmoji.dev/).
- Check static type with [mypy](http://mypy-lang.org/).
- Strip notebook outputs with nbstripout.
- Code coverage, and linkage to [Codecov](https://codecov.io).

## Credits

This template is based on the pydata-sphinx-theme, the furo theme, tiangolo's setup and [waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage).
The latter is based on [zillionare/cookiecutter-pypackage](https://github.com/zillionare/cookiecutter-pypackage), which was based on [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage).
