import requests
import os
from dotenv import load_dotenv
import logging

SESSION_KEY = "session"
NOT_LOGGED_IN_TEXT = (
    "Puzzle inputs differ by user.  Please log in to get your puzzle input."
)
USER_AGENT_HEADER_BODY = "https://github.com/H-Rusch/AdventOfCode-Python contact @ https://github.com/H-Rusch/AdventOfCode-Python/issues/new"


def is_empty(row: str = '') -> bool:
    if len(row) == 0 or row == '':
        return True
    return False

class AocDownloadException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


def download_input(year: int, day: int) -> str:
    url = build_url(year, day)
    cookies = build_cookies()
    headers = build_headers()

    response = requests.get(url, cookies=cookies, headers=headers)

    if not response.text.startswith(NOT_LOGGED_IN_TEXT):
        print("Download finished successfully.")

        return response.text
    else:
        raise AocDownloadException(
            "Session to the website has expired. Please log in again and update the session value."
        )

def build_url(year: int, day: int) -> str:
    return f"https://adventofcode.com/{year}/day/{day}/input"


def build_cookies() -> dict:
    return {SESSION_KEY: get_session_cookie()}


def build_headers() -> dict:
    return {"User-Agent": USER_AGENT_HEADER_BODY}


def get_session_cookie() -> str:
    load_dotenv()

    return '53616c7465645f5f5ecdcf36c7bfaf0e3c58cdc6406381365bb07f18266d95c6e8269b5de107d2d03bcff0a3e24a01ad42c2187e579588b7fd8276f822a6142b'
    if SESSION_KEY in os.environ:
        return os.environ[SESSION_KEY]
    else:
        raise AocDownloadException(
            f"Key {SESSION_KEY} not present in this environment. Make sure you set it either as an env variable or through a .env file."
        )

# чтение данных
def read_data_from_file(file_name):
    in_data = None
    with open(file_name, 'r') as fin:
        in_data = [row.strip() for row in fin.readlines()]
    return in_data


# чтение данных
def read_data_from_serv(year:int,day: int):
    in_str = download_input(year, day)
    in_data = in_str.split('\n')
    for i in range(len(in_data)):
        in_data[i] = in_data[i].strip()
    return in_data