from {{ cookiecutter.package_name }} import example_function


def test_dummy():
        assert example_function("A") == "a"
