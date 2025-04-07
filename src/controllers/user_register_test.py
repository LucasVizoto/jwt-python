from .user_register import UserRegister

class MockUserRepository:
    def __init__(self) -> None:
        self.registry_user_attributes = {}

    def registry_user(self, username: str, password: str) -> None:
        self.registry_user_attributes["username"] = username
        self.registry_user_attributes["password"] = password
#fazendo o Mock para não poluir o banco e quebrar o ideia de testes unitários


#testando se a senha está indo encriptada
def test_registry():
    repository = MockUserRepository()
    controller = UserRegister(repository)

    username = "Lucas"
    password = "mypassword"

    response = controller.registry(username, password)

    assert response["type"] == "User"
    assert response["username"] == username

    assert repository.registry_user_attributes["username"] == username
    assert repository.registry_user_attributes["password"] is not None
    assert repository.registry_user_attributes["password"] != password

    #testando os valores retornados na response