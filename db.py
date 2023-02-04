import sqlite3


class Database:
    def __init__(self, db_file: str):
        self.con = sqlite3.connect(db_file)  # Создает подключение
        self.cursor = self.con.cursor()  # Объект курсора

    def create_table(self):
        with self.con:
            self.cursor.execute("CREATE TABLE IF NOT EXISTS users "
                                "(id INTEGER PRIMARY KEY AUTOINCREMENT, "
                                "name TEXT, "
                                "age INTEGER)")

    def add_one_value(self, user: tuple):
        """Добавление одной строки"""
        with self.con:
            self.cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", user)

    def add_many_users(self, users: list):
        """Множественная вставка
        :param user: кортеж с пользователями
        :return:
        """

        with self.con:
            self.cursor.executemany("INSERT INTO users (name, age) VALUES (?,?)", users)

    def _get_formatted_users(self, users: list):
        """ Возвращает отформатированных пользователей

        :return:
        """

    def get_users(self):
        """Получение данных из БД

        :return:
        """
        with self.con:
            all_data = self.cursor.execute("SELECT * FROM users")
            self._get_formatted_users(all_data.fetchall())

    def get_user(self):
        """

        :return:
        """
        with self.con:
            all_data = self.cursor.execute("SELECT * FROM users").fetchone()

            id_ = all_data[0]
            username = all_data[1]
            age = all_data[2]
            print(f'id: {id_}\nusername: {username}\nage: {age}\n')

    def _get_some_users(self, count: int):
        """Получение нескольких пользователей

        :return:
        """
        with self.con:
            all_data = self.cursor.execute("SELECT * FROM users")
            self._get_formatted_users(all_data.fetchmany(count))

    def update_user(self, name: str, new_name: str):
        """бновление значений в БД

        :param name:
        :return:
        """
        with self.con:
            self.cursor.execute("UPDATE users SET name = ? WHERE name = ?", (new_name,name))

    def delete_user(self, id_: int):
        """Удаление пользователя по id

        :return:
        """
        with self.con:
            self.cursor.execute("DELETE FROM users WHERE id = ?", (id_,))

    def clear_table(self):
        """Удаление всех значений из БД

        :return:
        """
        with self.con:
            self.cursor.execute("DELETE FROM users")


if __name__ == '__main__':
    database = Database('test.db')

    # peoples = [('user_1', 20),('user_2', 30),('user_3', 40)]
    # database.add_many_users(users=peoples)

    # database.get_users()
    #database.get_user()
    #database._get_some_users(2)
    #database.update_user(name='user_2', new_name="Vasyua")

    database.clear_table()
    database.get_users()