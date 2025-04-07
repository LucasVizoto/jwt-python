from .user_repository import UserRepository
from src.models.settings.db_connectio_handler import db_connection_handler

def test_repository():
    db_connection_handler.connect()
    conn = db_connection_handler.get_connection()
    repo = UserRepository(conn)

    username = "Pedro"
    password = "1234"

    repo.registry_user(username, password)
    user = repo.get_user_by_username(username)
    print(f'\n\n {user}') #retornando uma tupla

    # sendo assim eu posso usar o indice pra apenas pegas a informação que eu quero
