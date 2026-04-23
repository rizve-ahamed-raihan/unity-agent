from typer import Typer, echo
app = Typer()

@app.command()
def hello(name: str):
    """Greets the user."""
    echo(f"Hello {name}")

if __name__ == "__main__":
    app()
