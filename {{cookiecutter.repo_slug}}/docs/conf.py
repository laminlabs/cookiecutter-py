import sys
from pathlib import Path

import {{ cookiecutter.pkg_name}}

HERE = Path(__file__).parent
sys.path[:0] = [str(HERE)]
from lamin_sphinx import *  # noqa
from lamin_sphinx import html_context  # noqa

project = "{{ cookiecutter.pkg_slug}}"
html_title = f"{project} | Lamin Labs"
release = {{ cookiecutter.pkg_name}}.__version__
html_context["github_repo"] = "{{ cookiecutter.repo_slug}}"  # noqa

ogp_site_url = f"https://lamin.ai/{project}"
