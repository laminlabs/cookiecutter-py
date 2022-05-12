# Get started

```
pip install -U cookiecutter
```

Generate a Python package project:

```
cookiecutter https://github.com/laminlabs/cookiecutter-py.git
```

For instance, the dialogue for setting up the `collab-maren` repository, which hosts the `maren` package, looked like this:

```
$ cookiecutter https://github.com/laminlabs/cookiecutter-py.git
repo_slug [collab-? or something else?]: collab-maren
pkg_slug [maren]: maren
pkg_name [maren]: maren
description: Flow cytometry for Maren
Select license:
1 - not open source
2 - Apache-2.0
Choose from 1, 2 [1]: 1

Repository successfully created in directory collab-maren 🎉
Please ask Alex or Sunny to launch https://lamin.ai/maren 👋📣
Browse to collab-maren/docs/tasks/ and get started on a first task! 🤩💪😎
```

To learn about all the components of your Python project, check out [architecture](architecture).
