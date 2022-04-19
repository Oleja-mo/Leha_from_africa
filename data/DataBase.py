#для удобной организации по хранению пользователей,
# будет класс пользователя User и класс собирающий список пользователей

class SqliteUsers:
    def __init__(self, name):
        self.name = name

    def get_by_id(self, id):
        query = '''Select '''