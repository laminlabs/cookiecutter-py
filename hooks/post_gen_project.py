#!/usr/bin/env python
import os
import subprocess
import sys

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    try:
        os.remove(os.path.join(PROJECT_DIRECTORY, filepath))
    except FileNotFoundError:
        pass


def execute(*args, supress_exception=False, cwd=None):
    cur_dir = os.getcwd()

    try:
        if cwd:
            os.chdir(cwd)

        proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        out, err = proc.communicate()
        out = out.decode("utf-8")
        err = err.decode("utf-8")
        if err and not supress_exception:
            raise Exception(err)
        else:
            return out
    finally:
        os.chdir(cur_dir)


def init_git():
    # workaround for issue #1
    if not os.path.exists(os.path.join(PROJECT_DIRECTORY, ".git")):
        execute(
            "git",
            "config",
            "--global",
            "init.defaultBranch",
            "main",
            cwd=PROJECT_DIRECTORY,
        )
        execute("git", "init", cwd=PROJECT_DIRECTORY)


def install_pre_commit_hooks():
    execute(sys.executable, "-m", "pip", "install", "pre-commit==2.12.0")
    execute(sys.executable, "-m", "pre_commit", "install")


MESSAGE = """
Repository successfully created in directory {{ cookiecutter.repo_slug }} 🎉
Please ask Alex or Sunny to launch https://lamin.ai/{{ cookiecutter.pkg_slug }} 👋📣

You can now already initialize the project using the following lines:

cd {{ cookiecutter.repo_slug }}
gitmoji -i
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/laminlabs/{{ cookiecutter.repo_slug }}
git branch -M main
git push -u origin main

Get started with a first task in {{ cookiecutter.repo_slug }}/docs/tasks/ 🤩💪😎
Make a PR for every task and squash merge them to the main branch! 🧐😅
"""

if __name__ == "__main__":

    if "not open source" == "{{ cookiecutter.license }}":
        remove_file("LICENSE")

    try:
        init_git()
    except Exception as e:
        print(e)

    try:
        install_pre_commit_hooks()
    except Exception as e:
        print(str(e))
        print(
            "Failed to install pre-commit hooks. Please run `pre-commit install` by"
            " your self. For more on pre-commit, please refer to"
            " https://pre-commit.com"
        )

    github_workflow = os.path.join(PROJECT_DIRECTORY, ".github/workflows/build.yml")
    with open(github_workflow, "r") as f:
        original = f.read()
    modified = original.replace("cookiecutter.pkg_slug", "{{ cookiecutter.pkg_slug }}")
    with open(github_workflow, "w") as f:
        f.write(modified)

    # The following doesn't yet work automatically!
    # execute(
    #     "gitmoji", "-i", cwd=PROJECT_DIRECTORY, supress_exception=True
    # )

    print(MESSAGE)
