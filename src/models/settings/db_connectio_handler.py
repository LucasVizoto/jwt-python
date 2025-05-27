from sqlite3 import Connection, connect

class __DbConnectionHandler:
    def __init__(self) -> None :
        self.__connection_string = "storage.db"
        self.__conn = None


    def connect(self) -> None:
        self.__conn = connect(self.__connection_string, check_same_thread=False)

    def get_connection(self) -> Connection:
        return self.__conn
    
db_connection_handler = __DbConnectionHandler()