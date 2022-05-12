import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path[:0] = [str(HERE)]
from lamin_sphinx import *  # noqa

import {{ cookiecutter.pkg_name}}  # noqa

project = "{{ cookiecutter.pkg_slug}}"
html_title = f"{project} | Lamin Labs"
release = cookiecutter_py.__version__
html_context["github_repo"] = "{{ cookiecutter.repo_slug}}"  # noqa

ogp_site_url = f"https://lamin.ai/{project}"
