from .user_repository import UserRepository
from src.models.settings.db_connectio_handler import db_connection_handler

def test_registry_user():
    db_connection_handler.connect()
    conn = db_connection_handler.get_connection()
    repo = UserRepository(conn)

    username = "Lucas"
    password = "1234"

    repo.registry_user(username, password)