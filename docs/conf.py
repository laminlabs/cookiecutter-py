import sys
from datetime import datetime
from pathlib import Path
from sphinx.application import Sphinx

HERE = Path(__file__).parent
sys.path[:0] = [str(HERE.parent), str(HERE)]

from lamin_sphinx import *  # noqa
import cookiecutter_py  # noqa
for generated in HERE.glob("cookiecutter_py.*.rst"):
    generated.unlink()

project = "cookiecutter_py"
release = cookiecutter_py.__version__
html_title = "cookiecutter-py | Lamin Labs"

ogp_site_url = "https://lamin.ai/cookiecutter_py"
