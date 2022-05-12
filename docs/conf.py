import sys
from pathlib import Path

import cookiecutter_py

HERE = Path(__file__).parent
sys.path[:0] = [str(HERE)]
from lamin_sphinx import *  # noqa
from lamin_sphinx import html_context  # noqa

project = "cookiecutter-py"
html_title = f"{project} | Lamin Labs"
release = cookiecutter_py.__version__
html_context["github_repo"] = "cookiecutter-py"  # noqa

ogp_site_url = f"https://lamin.ai/{project}"
