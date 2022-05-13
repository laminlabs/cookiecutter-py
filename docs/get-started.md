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
repo_slug [collab-maren]:
package_name [maren]:
description: Flow cytometry
Select license:
1 - not open source
2 - Apache-2.0
Choose from 1, 2 [1]: 1

Repository successfully created in directory collab-maren! 🎉

1. Ask Alex or Sunny to connect https://lamin.ai/maren 👋📣
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

## Background

To learn about all the components of your Python project, check out [architecture](architecture).
