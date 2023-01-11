def save(data, query, tables_names, primary_key, index, col_foreign_key):
    """ Сохранить данные

    :param data: данные
    :param query: для выполнение команды MySql
    :param primary_key: первичный ключ
    :param index: индекс списка (для добавление первичного ключа чтобы обновить данные)
    """

    for table_name in tables_names:
        column = ''

        try:
            foreign_key = query.select_value(table_name, col_foreign_key)
            foreign_key = foreign_key[index]
        except IndexError:
            foreign_key = None
        if primary_key == foreign_key:
            foreign_key = query.select_value(table_name, col_foreign_key)
            foreign_key = foreign_key[index]
        else:
            foreign_key = None
        for key, value in data[table_name].items():
            column += f' {key}="{value}",'
        column = column.replace('"None"', 'Null')
        column = column.strip(',')
        query.update_data(table_name, primary_key, foreign_key, col_foreign_key, column)
