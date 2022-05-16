import re
import sys

n_errors = 0

package_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
slug_REGEX = r"^[-a-zA-Z][-a-zA-Z0-9]+$"
package_name = "{{ cookiecutter.package_name }}"
project_slug = "{{ cookiecutter.project_slug }}"
repository_name = "{{ cookiecutter.repository_name }}"

if not re.match(package_REGEX, package_name):
    print(
        "\nERROR: The package_name is invalid. Do not use '-' and"
        " spaces, use '_' instead!"
    )
    n_errors += 1

if not re.match(slug_REGEX, project_slug) or not re.match(slug_REGEX, repository_name):
    print(
        "\nERROR: `project_slug` or `repository_name` are not valid. Do not use '_' and"
        " spaces, use '-'!"
    )
    n_errors += 1

if "{{ cookiecutter.description }}".endswith("."):
    print("\nERROR: Enter `description` without ending period.")
    n_errors += 1

if len("{{ cookiecutter.description }}") > 50:
    print("\nERROR: `description` needs to be <=50 characters.")
    n_errors += 1

if n_errors > 0:
    print("\n")
    sys.exit(1)
