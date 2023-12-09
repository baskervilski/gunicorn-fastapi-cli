import time
import typer


cli = typer.Typer()

START_CMD_PATTERNS = ["start-server"]


@cli.command()
def start(config_file: str, daemon: bool = False):
    import invoke

    invoke.run(f"fgapp start-server {config_file}", disown=daemon, echo=True)


@cli.command(hidden=True)
def start_server(config_file):
    import os
    from fast_guni_app.server import CustomGunicorn
    from fast_guni_app.server import load_config

    config_dict = load_config(config_file)
    os.environ["HELLO_MESSAGE"] = config_dict["app"]["hello_message"]
    server = CustomGunicorn(config_file=config_file)
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
