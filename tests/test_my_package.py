from importlib.metadata import version

from data_viewer import main


def test_version():
    assert version("data-viewer") == "0.1.0"


def test_main():
    assert main() == "Hello from python-package-template!"
