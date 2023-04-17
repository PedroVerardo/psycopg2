from  ..db import Connection

class Well(Connection):
    def __init__(self):
        super().__init__()

    def insert(self, *args):
        try:
            sql = "INSERT INTO test (name) VALUES (%s)"
            self.execute(sql, args)
        except Exception as e:
            print("Erro ao inserir ", e)

