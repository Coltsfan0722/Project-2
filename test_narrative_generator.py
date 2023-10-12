from narrative_generator import install_package
import importlib


import pytest

class TestInstallPackage:

    # Successfully installs a package using pip.
    def test_install_package_success(self):
        package = "numpy"
        install_package(package)
        spec = importlib.util.find_spec(package)
        assert spec is not None

