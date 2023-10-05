import libtmux
import os
from tqdm import tqdm
from loguru import logger
import argparse
import inspect

import random, string

def random_session_name(length: int = 4):
   """Just to create some randow window name"""
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))


SESSION_BASE_NAME  = "test"

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
        session.new_window(attach=True, window_name=new_window_name)
        logger.info(f"Start window {new_window_name}")

        
def stop(args: argparse.Namespace):
    session_name = args.session_name
    print(session_name)


def stop_all(args: argparse.Namespace):
    session = get_session()
    all_windows = session.windows
    print(all_windows)
    for window in tqdm(all_windows):
        print(window)
        window.kill_window()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title="subcommand")

    parser_start = subparsers.add_parser('start')
    parser_start.add_argument("num_users", type=int, default=1)
    parser_start.set_defaults(func=start)

    parser_stop = subparsers.add_parser('stop')
    parser_stop.add_argument("session_name", type=int)
    parser_stop.set_defaults(func=stop)

    parser_stop_all = subparsers.add_parser('stop_all')
    parser_stop_all.set_defaults(func=stop_all)

    args = parser.parse_args()
    args.func(args)