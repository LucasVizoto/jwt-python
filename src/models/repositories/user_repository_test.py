from .user_repository import UserRepository
from src.models.settings.db_connectio_handler import db_connection_handler
from unittest.mock import Mock

class MockCursor:
    def __init__(self) -> None:
        self.execute = Mock()
        self.fetchone = Mock()
    
class MockConnection:
    def __init__(self) -> None:
        self.cursor = Mock(return_value=MockCursor())
        self.commit = Mock()
# ao invés de eu fazer a conexão direta com o banco de dados
# eu estou fazendo o Mock dos dados, inserindo esses caras acima
# na frente como uma camada de validação para enviar algo ao banco    
    
def test_registry_user():
    username = "Beatriz"
    password = "1234"

    mock_conneciton = MockConnection()
    repo =  UserRepository(mock_conneciton)
    
    repo.registry_user(username, password)  
    
    cursor = mock_conneciton.cursor.return_value

    # com todas esses testes com Mock que eu escrevi, basicametne

    # abaixo há o teste de cada linha do insert para analisar ponto a ponto o que 
    # está sendo enviado
    assert 'INSERT INTO users' in cursor.execute.call_args[0][0]
    assert '(username, password, balance)' in cursor.execute.call_args[0][0]
    assert 'VALUES' in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (username, password, 0)
    #será testado a forma como está sendo enviado a instrução SQL escrita no método

    # db_connection_handler.connect()
    # conn = db_connection_handler.get_connection()
    # repo = UserRepository(conn)

    # username = "Pedro"
    # password = "1234"

    # repo.registry_user(username, password)
    # user = repo.get_user_by_username(username)
    # print(f'\n\n {user}') #retornando uma tupla

    # sendo assim eu posso usar o indice pra apenas pegas a informação que eu quero

def test_edit_balance():
    user_id = 2
    balance = 100.11

    mock_conneciton = MockConnection()
    repo =  UserRepository(mock_conneciton)
    
    repo.edit_balance(user_id, balance)  
    
    cursor = mock_conneciton.cursor.return_value

    # com todas esses testes com Mock que eu escrevi, basicametne

    # abaixo há o teste de cada linha do insert para analisar ponto a ponto o que 
    # está sendo enviado
    assert 'UPDATE users' in cursor.execute.call_args[0][0]
    assert 'SET balance = ?' in cursor.execute.call_args[0][0]
    assert 'WHERE id = ?' in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (balance, user_id)

    mock_conneciton.commit.assert_called_once() #verificar se o commit está sendo chamado ao menos uma vez

def test_get_user_by_username():
    username = "Lucas"

    mock_conneciton = MockConnection()
    repo =  UserRepository(mock_conneciton)
    
    repo.get_user_by_username(username)  
    
    cursor = mock_conneciton.cursor.return_value

    # com todas esses testes com Mock que eu escrevi, basicametne

    # abaixo há o teste de cada linha do insert para analisar ponto a ponto o que 
    # está sendo enviado
    assert 'SELECT id, username, password' in cursor.execute.call_args[0][0]
    assert 'FROM users' in cursor.execute.call_args[0][0]
    assert 'WHERE username = ?' in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (username,)

    cursor.fetchone.assert_called_once() #verificar se o commit está sendo chamado ao menos uma vez

