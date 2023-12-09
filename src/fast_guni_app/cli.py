# Developed by: Nemanja Radojkovic, www.linkedin.com/in/radojkovic

import time
import typer


cli = typer.Typer()

START_CMD_PATTERNS = ["start-server", "fg-app"]


@cli.command()
def start(config_file: str, daemon: bool = False):
    import invoke  # importing when needed -> CLI more responsive

    invoke.run(f"fg-app start-server {config_file}", disown=daemon, echo=True)


@cli.command(hidden=True)
def start_server(config_file):
    import os
    import yaml
    from fast_guni_app.api import app
    from fast_guni_app.server import CustomGunicorn

    with open(config_file) as cfg_file:
        config_dict = yaml.safe_load(cfg_file)

    os.environ["HELLO_MESSAGE"] = config_dict["app"]["hello_message"]
    print(f"Server options: {config_dict['server']}")
    server = CustomGunicorn(app, **config_dict["server"])
    server.run()


@cli.command()
def status():
    from fast_guni_app.utils import find_processes

    procs = find_processes(cmd_patterns=START_CMD_PATTERNS)

    return len(procs)


@cli.command()
def stop():
    from fast_guni_app.utils import find_processes

    procs = find_processes(cmd_patterns=START_CMD_PATTERNS)
    if procs:
        for p in procs:
            if p.children():
                print(f"Terminating master process: {p}")
                p.terminate()
        print("Waiting 2 seconds...")
        time.sleep(2)
        status()


if __name__ == "__main__":
    cli()
