import libtmux
import os
from tqdm import tqdm
from loguru import logger
import argparse
import inspect

import random, string

SESSION_BASE_NAME = "test"


def random_session_name(length: int = 4):
    """Just to create some randow window name"""
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def make_venv(window: libtmux.window.Window):
    # создаем папку
    new_dir_name = window.name
    notebook_dir = os.getcwd() + "/" + new_dir_name
    os.mkdir(notebook_dir)

    jupyter_command = get_jupyter_command(
        port=3000,
        token="smth",
        notebook_dir=notebook_dir,
    )
    window.panes[0].send_keys(jupyter_command)


def get_jupyter_command(
    port: int, token: str, notebook_dir: str, ip: str = "localhost"
):
    return f"""
    jupyter notebook --ip {ip} --port {port} --no-browser --NotebookApp.token='{token}' --NotebookApp.notebook_dir='{notebook_dir}'
    """
    # return f"""
    # jupyter notebook
    # """


def get_session():
    """Get session"""
    server = libtmux.Server()
    try:
        session = server.new_session(SESSION_BASE_NAME)
        logger.info(f"Created session {SESSION_BASE_NAME}")
    except libtmux.exc.TmuxSessionExists:
        session = server.sessions.get(session_name=SESSION_BASE_NAME)
        logger.info(f"Connected to session {SESSION_BASE_NAME}")
    return session


def start(args: argparse.Namespace):
    num_users = args.num_users
    session = get_session()
    for _ in tqdm(range(1, num_users + 1)):
        new_window_name = random_session_name()
        window = session.new_window(attach=True, window_name=new_window_name)
        make_venv(window)
        logger.info(f"Start window {new_window_name}")


def stop(args: argparse.Namespace):
    session_name = args.session_name


def stop_all(args: argparse.Namespace):
    session = get_session()
    all_windows = session.windows
    for window in tqdm(all_windows):
        window.kill_window()


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
