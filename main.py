import typer
from rich import print


def main(name: int):
    print(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
