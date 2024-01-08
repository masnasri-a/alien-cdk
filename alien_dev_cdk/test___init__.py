from alien_dev_cdk import generate_handler
import typer


def generate_handler(name_file: str):
    if name_file is None:
        typer.echo("Please enter name file")
    elif ' ' in name_file:
        typer.echo("Please enter name file without spaces")
    else:
        typer.echo(f"Hello {name_file}")


# FILEPATH: /Users/nasriadzlani/Workspace/Research/alien-dev-cdk/tests/test_handler.py


def test_generate_handler():
    # Test case 1: name_file is None
    assert generate_handler(None) == "Please enter name file"

    # Test case 2: name_file contains spaces
    assert generate_handler(
        "file name") == "Please enter name file without spaces"

    # Test case 3: name_file is valid
    assert generate_handler("John") == "Hello John"
