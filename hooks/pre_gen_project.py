import re
import sys


MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

module_name = "{{ cookiecutter.pkg_name}}"

if not re.match(MODULE_REGEX, module_name):
    print(
        "ERROR: The pkg name (%s) is not a valid Python module name. Please do not use"
        " a - and use _ instead" % module_name
    )

    # Exit to cancel project
    sys.exit(1)


SLUG_REGEX = r"^[-a-zA-Z][-a-zA-Z0-9]+$"

pkg_slug = "{{ cookiecutter.pkg_slug}}"
repo_slug = "{{ cookiecutter.repo_slug}}"

if not re.match(SLUG_REGEX, pkg_slug) or not re.match(SLUG_REGEX, repo_slug):
    print(
        "ERROR: The pkg_slug or repo_slug are not valid. Please do not use '_' and"
        " spaces, use '-'!"
    )

    # Exit to cancel project
    sys.exit(1)
