"""{{ cookiecutter.description }}.

Import the package::

   import {{ cookiecutter.package_name }}

This is the complete API reference:

.. autosummary::
   :toctree: .

   example_function
   ExampleClass
"""

__version__ = "0.1a1"  # pre-release for initial release 0.1.0

from ._core import ExampleClass, example_function  # noqa
