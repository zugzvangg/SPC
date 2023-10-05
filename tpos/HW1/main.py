import libtmux
import os
from tqdm import tqdm
from loguru import logger

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

def start(num_users: int, base_dir='./'):
    session = get_session()
    for i in tqdm(range(1, num_users + 1)):
        new_window_name = random_session_name()
        session.new_window(attach=True, window_name=new_window_name)
        logger.info(f"Start window {new_window_name}")

        
def stop(session_name, num):
    pass


def stop_all(session_name: str = SESSION_BASE_NAME):
    session = get_session()
    all_windows = session.windows
    print(all_windows)
    for window in tqdm(all_windows):
        print(window)
        window.kill_window()


if __name__ == "__main__":
    start(num_users = 5)
    # stop_all()