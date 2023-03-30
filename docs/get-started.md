# Get started

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

1. Make two changes to the codebase by setting the version string (`X.X.X`) in `mypackage/__init__.py` and `docs/changelog.md`. Use [semantic versioning](https://semver.org) with [Python versioning](https://peps.python.org/pep-0440/).
2. Commit these two changes in a commit "Release version X.X.X" with a :bookmark: emoji and push them to GitHub.
3. Publish to PyPI: `flit publish`
4. Tag and push tag: `git tag X.X.X` and `git push origin X.X.X`
5. Make a release on Github. Using the "generate release notes" button is fine.

## Background

To learn about all the components of your Python project, check out [architecture](architecture).

## Migrate schema modules

For instance, in the root of `lnschema-core`:

1. `alembic --config lnschema_core/alembic.ini --name yvzi revision --autogenerate -m "vX.X.X"`
2. `alembic --config lnschema_core/alembic.ini --name yvzi upgrade head`

Replace "yvzi" with the module ID of your schema module.
