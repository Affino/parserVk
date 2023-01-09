
tables_names = [
    'profile',
    'interests',
    'university',
    'career',
    'schools',
    'relatives',
    'life_position'
]


def save(data, query, primary_key, index):
    """ Сохранить данные

    :param data: данные
    :param query: для выполнение команды MySql
    :param primary_key: первичный ключ
    :param index: индекс списка (для добавление первичного ключа чтобы обновить данные)
    """

    col_foreign_key = 'user_id'

    for table_name in tables_names:
        column = ''
        print(index)
        try:
            foreign_key = query.select_value(table_name, 'user_id')
            foreign_key = foreign_key[index]
        except IndexError:
            foreign_key = None

        for key, value in data[table_name].items():
            column += f' {key}="{value}",'
        column = column.replace('"None"', 'Null')
        column = column.strip(',')
        query.update_data(table_name, primary_key, foreign_key, col_foreign_key, column)
