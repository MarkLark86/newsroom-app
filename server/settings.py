import pathlib

SERVER_PATH = pathlib.Path(__file__).resolve().parent
CLIENT_PATH = SERVER_PATH.parent.joinpath("client")

AGENDA_EXPIRY_DAYS = 1
CONTENT_API_EXPIRY_DAYS = 1
