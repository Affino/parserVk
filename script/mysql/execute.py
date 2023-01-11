import pymysql


class Query:
    def __init__(self, db):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            db=db
        )
        self.cursor = self.connection.cursor()

        print(f"||Connected: {db}||")

    def select_value(self, table, column):
        """ Забрать значение из таблицы

        :param table: таблица из база данных
        :param column: столбец
        """
        values = []
        self.cursor.execute("SELECT %s FROM %s" % (column, table))

        values_in_tuple = self.cursor.fetchall()
        for value_in_tuple in values_in_tuple:
            value = value_in_tuple[0]
            values.append(value)
        return values

    def insert_id(self, table, col_foreign_key, primary_key):
        """ Вставить индификатор

        :param table: таблица
        :param col_foreign_key: столбец с индификатором (внешний ключ)
        :param primary_key: первичный ключ
        """
        try:
            # print(f'{4} - Первичный ключ в insert_id() {primary_key}')
            print(id)
            query_insert = "INSERT INTO {0} ({1}) VALUE ({2!r})".format(table, col_foreign_key, primary_key)
            print(query_insert)

            self.cursor.execute(query_insert)
            self.connection.commit()

        except Exception as ex:
            print(ex)

    def update(self, table, column, foreign_key, col_foreign_key):
        """ Обновить старое значение

        :param table: таблица
        :param column: столбец
        :param foreign_key: внешний ключ
        :param col_foreign_key: столбец внешного ключа
        """
        try:
            query_update = f"UPDATE {table} SET {column} WHERE {col_foreign_key} = {foreign_key}"
            print(query_update)
            self.cursor.execute(query_update)
            self.connection.commit()

        except Exception as ex:
            print(ex)

    def update_data(self, table, primary_key, foreign_key, col_foreign_key, column):
        # print(f'{2} - Первичный ключ в update_data() {primary_key}')
        print(f'Внешний ключ {foreign_key}')
        if foreign_key is None:
            # print(f'{3} - Первичный ключ после if {primary_key}')
            self.insert_id(table, col_foreign_key, primary_key)
        else:
            self.update(table, column, foreign_key, col_foreign_key)
