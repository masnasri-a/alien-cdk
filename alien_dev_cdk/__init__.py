import os
import typer

app = typer.Typer()


@app.command('generate-handler')
def generate_handler(name_file: str):
    if name_file is None:
        typer.echo("Please enter name file")
    if ' ' in name_file:
        typer.echo("Please enter name file without spaces")
    if name_file is not None and ' ' not in name_file:
        os.system(f"touch {name_file}.py")

        # Read code from handler.py
        with open("alien_dev_cdk/handler.py", "r") as handler_file:
            code = handler_file.read()

        # Write code to the file
        with open(f"{name_file}.py", "w") as output_file:
            output_file.write(code)

    typer.echo(f"File {name_file}.py created successfully 😊 ")


if __name__ == "__main__":
    app()
