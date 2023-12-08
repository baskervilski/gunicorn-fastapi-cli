from typing import List, Optional
import psutil
from rich import print


def find_processes(
    name_patterns: Optional[List[str]] = None, cmd_patterns: Optional[List[str]] = None
) -> List[psutil.Process]:
    msg_color = "[red]"
    cmd_patterns = cmd_patterns or []
    name_patterns = name_patterns or []

    procs = []

    for p in psutil.process_iter():
        cmd = p.cmdline()
        if all(cp in cmd for cp in cmd_patterns) and all(
            np in cmd for np in name_patterns
        ):
            children_str = ", ".join([f"{c.pid} ({c.name()})" for c in p.children()])
            children = f"children={children_str}; " if p.children() else ""
            print(
                f"pid={p.pid}; "
                f"name={p.name()}; "
                f"cmd={cmd}; "
                f"parent={p.parent().pid} ({p.parent().name()}); "
                f"{children}"
            )
            procs.append(p)
            msg_color = "[green]"
    print(f"[bold]{msg_color}{len(procs)} running processes found")
    return procs
