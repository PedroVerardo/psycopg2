import psycopg2 as db

class Config:
    def __init__(self):
        self.config = {
            "postgres": {
                "database": "well",
                "user": "postgres",
                "password": "yONDA007",
                "host": "127.0.0.1",
                "port": "5432"
            }
        }

class Connection(Config):
    def __init__(self):
        super().__init__()
        try:
            self.conn = db.connect(**self.config["postgres"])
            self.cur = self.conn.cursor()
        except Exception as e:
            print("erro de conexão" + e)
            exit(1)

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self.conn
    
    @property
    def cursor(self):
        return self.cur
    
    def commit(self):
        self.connection.commit()

    def fetchall(self):
        return self.cursor.fetchall()
    
    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()
    

        