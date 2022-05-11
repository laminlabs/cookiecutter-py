import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path[:0] = [str(HERE)]
from lamin_sphinx import *  # noqa
import cookiecutter_py  # noqa

project = "cookiecutter-py"
html_title = f"{project} | Lamin Labs"
release = cookiecutter_py.__version__
html_context["github_repo"] = "cookiecutter-py"  # noqa

ogp_site_url = "https://lamin.ai/project"
