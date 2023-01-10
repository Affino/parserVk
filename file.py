#     # извлечение данных о родствиниках
#     elif 'relatives' == first_dict_key:
#
#         extract_list_data(uncollected_data, first_dict_key, collected_data)
#
#     # для тип данных список
#     elif type([]) == type(uncollected_data):
#         try:
#             init(autoreset=True)
#             print(Fore.BLUE + f'This is list: {first_dict_key}')
#
#             uncollected_data = uncollected_data[0]
#             extract_data_list(uncollected_data, first_dict_key, collected_data)
#         except Exception as ex:
#             extract_data_list(uncollected_data, first_dict_key, collected_data)
#
#     # для тип данных словарь
#     elif type({}) == type(uncollected_data):
#
#         init(autoreset=True)
#         print(Fore.RED + f'This is dict: {first_dict_key}')
#         extract_data_dict(uncollected_data, first_dict_key, collected_data)
#
#     # для тип None_type
#     else:
#         insert_none(uncollected_data, first_dict_key, collected_data)
#
# # при ошибке добавляем none_type