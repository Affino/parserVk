dict_keys = ['name', 'screen_name',
                  'photo_200', 'is_closed',
                  'type', 'members_count',
                  'status', 'description']


def extract_str_data(data, collected_data, dict_key):
    if 'screen_name' == dict_key:
        collected_data['groups_info']['url'] = f'https://vk.com/{data}'
    elif 'is_closed' == dict_key:
        value = ['открытое', 'закрытое', 'частное']
        collected_data['groups_info'][dict_key] = value[data]
    else:
        collected_data['groups_info'][dict_key] = data


def extract(uncollected_data, collected_data):
    """ Извлекать данные сообщества """

    for dict_key in dict_keys:
        try:
            data = uncollected_data[dict_key]
            if bool(data) is True or data == 0:
                extract_str_data(data, collected_data, dict_key)
            else:
                collected_data['groups_info'][dict_key] = None
        except KeyError:
            collected_data['groups_info'][dict_key] = None
        except TypeError:
            collected_data['groups_info'][dict_key] = None
