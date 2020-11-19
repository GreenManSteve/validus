import sqlite3


class DataBase:
    def __init__(self):
        self.dbase = "CapitalCall.db"

    def create_connection(self):

        conn = None
        try:
            conn = sqlite3.connect(self.dbase)
        except TypeError as e:
            print(e)
        return conn

    def create_project(self, fn):
        """
        Create a new project into the projects table
        :param conn:
        :param project:
        :return: project id
        """

        sql = 'INSERT INTO DataFund(fund_name) VALUES(?)'
        print(sql)
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute(sql, [fn])
        conn.commit()
        print(cur.lastrowid)
        return cur.lastrowid
