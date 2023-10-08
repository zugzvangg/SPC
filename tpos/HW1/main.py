import libtmux
import os
from tqdm import tqdm
from loguru import logger
import argparse
import time

SESSION_BASE_NAME = "test"


def run(window: libtmux.window.Window) -> None:
    # создаем папку
    new_dir_name = window.name
    notebook_dir = os.getcwd() + "/" + new_dir_name
    os.makedirs(notebook_dir, exist_ok=True)
    pane = window.panes[0]
    # создаем venv
    pane.send_keys(f"cd {new_dir_name}")
    pane.send_keys(f"python3 -m venv venv")
    time.sleep(3)  # необходимо чтобы активировалось окружение
    # активируем venv
    pane.send_keys(f"source {notebook_dir + '/venv/bin/activate' }")
    time.sleep(1)
    # получаем команду для этого окна
    jupyter_command = get_jupyter_command(
        notebook_dir=notebook_dir,
    )
    # создаем ноутбук

    stderr = pane.send_keys(jupyter_command)
    # чтобы лог успел напечататься
    time.sleep(1)
    # читаем stderr
    stderr = "\n".join(pane.cmd("capture-pane", "-p").stdout)

    def parse_jupyter_log(log: str) -> str:
        link = stderr[-100:].split("or")[1]
        token = link.split("token=")[1]
        port = link.split(":")[2].split("/")[0]
        result = f"run on PORT: {port} with TOKEN: {token}"
        return result

    # достаем из лога порт и токен
    jupyter_log = parse_jupyter_log(stderr)
    logger.debug(jupyter_log)


def get_jupyter_command(
    notebook_dir: str,
    ip: str = "localhost",
    port: int = None,
    token: str = None,
) -> str:
    # return f"""
    # jupyter notebook --ip {ip} --port {port} --no-browser --NotebookApp.token='{token}' --NotebookApp.notebook_dir='{notebook_dir}'
    # """
    return f"""
    jupyter notebook --no-browser --NotebookApp.notebook_dir='{notebook_dir + "/"}'
    """


def get_session() -> libtmux.session.Session:
    """Get session"""
    server = libtmux.Server()
    try:
        session = server.new_session(SESSION_BASE_NAME)
        logger.info(f"Created session {SESSION_BASE_NAME}")
    except libtmux.exc.TmuxSessionExists:
        session = server.sessions.get(session_name=SESSION_BASE_NAME)
        # logger.info(f"Connected to session {SESSION_BASE_NAME}")
    return session


def start(args: argparse.Namespace) -> None:
    num_users = args.num_users
    session = get_session()
    for i in tqdm(range(1, num_users + 1)):
        # назовем окна как и директории, где будет запущен ноутбук
        new_window_name = "dir" + str(i)
        window = session.new_window(attach=True, window_name=new_window_name)
        run(window)
        logger.info(f"Start window {new_window_name}")


def stop(args: argparse.Namespace) -> None:
    session = get_session()
    all_windows = session.windows
    session_name = args.session_name
    for window in all_windows:
        if window.id[1:] == str(session_name):
            # если просто хотим убить ноутбук, не убивая окно
            window.panes[0].send_keys("^Z")
            logger.debug(f"Killed venv with id = {session_name}")
            return
    logger.error(f"No session with id = {session_name}")
    return


def stop_all(args: argparse.Namespace = None) -> None:
    session = get_session()
    all_windows = session.windows
    for window in tqdm(all_windows):
        # зато без повторения кода :)
        stop(argparse.Namespace(session_name=window.id[1:]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title="subcommand")

    parser_start = subparsers.add_parser("start")
    parser_start.add_argument("num_users", type=int, default=1)
    parser_start.set_defaults(func=start)

    parser_stop = subparsers.add_parser("stop")
    parser_stop.add_argument("session_name", type=int)
    parser_stop.set_defaults(func=stop)

    parser_stop_all = subparsers.add_parser("stop_all")
    parser_stop_all.set_defaults(func=stop_all)

    args = parser.parse_args()
    args.func(args)
