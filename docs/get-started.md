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

The dialogue for setting up the `collab-doloromics` repository, which holds the `doloromics` package, looked like this:

```
$ cookiecutter https://github.com/laminlabs/cookiecutter-py.git
repo_slug [collab-? or something else?]: collab-doloromics
pkg_slug [doloromics]: doloromics
pkg_name [doloromics]: doloromics
description: Code for Doloromics
Select license:
1 - not open source
2 - Apache-2.0
Choose from 1, 2 [1]: 1

Repository successfully created in directory collab-doloromics! 🎉

1. Ask Alex or Sunny to connect https://lamin.ai/doloromics 👋📣
2. Open https://github.com/organizations/laminlabs/repositories/new, and make a
   *private empty* repository with name "collab-doloromics" and
   description "Code for Doloromics"
   Ignore the suggestions from GitHub!
3. Initialize the project by copying the below to the command line.
   When gitmoji asks you to select an emoji, select "🎉 - Begin a project".
   Check out https://gitmoji.dev/ if you don't yet know about it!

cd collab-doloromics
gitmoji -i
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/laminlabs/collab-doloromics
git branch -M main
git push -u origin main

4. Get started with a task in collab-doloromics/docs/tasks/ 🤩💪😎
   Make a PR for every task and squash merge them to the main branch! 🧐😅
```

## Background

To learn about all the components of your Python project, check out [architecture](architecture).
