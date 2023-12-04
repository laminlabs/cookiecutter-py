# cookiecutter-py: Python project template

## Get started

Install `cookiecutter`:

```
pip install cookiecutter
```

Generate a Python package project:

```
cookiecutter https://github.com/laminlabs/cookiecutter-py.git
```

## Example

Set up the `collab-maren` repository for the Maren project, which holds the `maren` package:

```
$ cookiecutter https://github.com/laminlabs/cookiecutter-py.git
project_name: Maren
project_slug [maren]:
repository_name [collab-maren]:
package_name [maren]:
description: Flow cytometry
Select license:
1 - not open source
2 - Apache-2.0
Choose from 1, 2 [1]: 1

Repository successfully created in directory `collab-maren`! 🎉

1. Ask Alex or Sunny to connect https://lamin.ai/docs/maren 👋📣
2. Open https://github.com/organizations/laminlabs/repositories/new, and make a
   *private empty* repository with name "collab-maren" and
   description "Flow cytometry."
   Ignore the suggestions from GitHub!
3. Initialize the project by copying the below to the command line.

cd collab-maren
git add .
git commit -m "🎉 Initial commit"
git remote add origin https://github.com/laminlabs/collab-maren
git branch -M main
git push -u origin main
gitmoji -i

4. Get started with a task in collab-maren/docs/tasks/ 🤩💪😎
   Make a PR for every task and squash merge them to the main branch! 🧐😅
```

## Release process

If you don't have `laminci`: `pip install laminci`.

Please ensure that you have either the [Github CLI](https://cli.github.com/) installed or a valid Github token in the `GITHUB_TOKEN` environment variable with at least `read:org` scope.

1. Set the version string (`X.X.X`) in `mypackage/__init__.py` and `docs/changelog.md`. Use [semantic versioning](https://semver.org) with [Python versioning](https://peps.python.org/pep-0440/).
2. Run `laminci release` on the command line. If it's a public package for PyPI, add the `--pypi` flag.

## Architecture & changelog

To learn about all the components of your Python project, check out

- [architecture](docs/architecture.md)
- [changelog](docs/changelog.md)
