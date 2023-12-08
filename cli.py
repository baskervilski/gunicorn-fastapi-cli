import invoke
import typer
from server import CustomGunicorn

cli = typer.Typer()


@cli.command()
def start(config_file: str, daemon: bool = False):
    invoke.run(f"venv/bin/python cli.py start-server {config_file}", disown=daemon)


@cli.command(hidden=True)
def start_server(config_file):
    server = CustomGunicorn(config_file=config_file)
    server.run()


@cli.command()
def status():
    from utils import find_processes

    find_processes(cmd_patterns=["start-server", "cli.py"])


@cli.command()
def stop():
    from utils import find_processes

    procs = find_processes(cmd_patterns=["start-server", "cli.py"])
    for p in procs:
        if p.children():
            print(f"Terminating: {p}")
            p.terminate()


if __name__ == "__main__":
    cli()
