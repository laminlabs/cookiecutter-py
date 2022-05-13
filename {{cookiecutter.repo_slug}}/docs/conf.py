import sys
from pathlib import Path

import {{ cookiecutter.package_name}}

HERE = Path(__file__).parent
sys.path[:0] = [str(HERE), str(HERE.parent)]
from lamin_sphinx import *  # noqa
from lamin_sphinx import html_context  # noqa

project = "{{ cookiecutter.project_name}}"
html_title = f"{project} | Lamin Labs"
release = {{ cookiecutter.package_name}}.__version__
html_context["github_repo"] = "{{ cookiecutter.repo_slug}}"  # noqa

ogp_site_url = "https://lamin.ai/{{ cookiecutter.project_name}}"
