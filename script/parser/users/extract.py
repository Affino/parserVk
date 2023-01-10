# from colorama import init, Fore
from datetime import datetime

from ..users import KEY_DICT
from .which import *


def extract_str_data(data, first_dict_key, collected_data):
    """ Извлекать строковых данных """

    if KEY_DICT.DOMAIN is first_dict_key:
        domain = data
        collected_data['profile']['url'] = f'https://vk.com/{domain}'

    if KEY_DICT.PHOTO is first_dict_key:
        collected_data['profile']['photo'] = data
    elif first_dict_key in KEY_DICT.FIRST_KEYS[1:14]:
        if bool(data) is True:
            collected_data['profile'][first_dict_key] = data
        else:
            collected_data['profile'][first_dict_key] = None

    if first_dict_key in KEY_DICT.FIRST_KEYS[14:23]:
        if bool(data) is True:
            collected_data['interests'][first_dict_key] = data
        else:
            collected_data['interests'][first_dict_key] = None

    if first_dict_key in KEY_DICT.FIRST_KEYS[23:28]:
        if bool(data) is True:
            collected_data['university'][first_dict_key] = data
        else:
            collected_data['university'][first_dict_key] = None


def extract_int_data(data, first_dict_key, collected_data):
    """ Извлекать числовые данные """

    index = data
    if KEY_DICT.FOLLOWERS is first_dict_key:
        collected_data['profile']['followers_count'] = data
    if KEY_DICT.GENDER is first_dict_key:
        collected_data['profile']['gender'] = users_gender[index]

    elif KEY_DICT.GRADUATION is first_dict_key:
        collected_data['university'][first_dict_key] = data

    elif KEY_DICT.ONLINE is first_dict_key:
        collected_data['profile']['activity'] = online_status[index]

    elif KEY_DICT.RELATION is first_dict_key:
        gender = collected_data['profile']['gender']
        if gender == 'мужской':
            collected_data['profile'][first_dict_key] = status_relations_man[index]

        elif gender == 'женский':
            collected_data['profile'][first_dict_key] = status_relations_woman[index]


def extract_dict_data(data, first_dict_key, collected_data):
    """ Извлекать данных из словаря """
    second_dict_keys = None

    if KEY_DICT.CITY is first_dict_key:
        title = data['title']
        collected_data['profile']['city'] = title

    if KEY_DICT.COUNTRY is first_dict_key:
        title = data['title']
        collected_data['profile']['country'] = title

    if KEY_DICT.LAST_SEEN is first_dict_key:
        time = data['time']
        dt_object = datetime.fromtimestamp(time)
        collected_data['profile']['last_seen'] = dt_object

    if KEY_DICT.PERSONAL is first_dict_key:
        first_dict_key = 'life_position'
        second_dict_keys = KEY_DICT.personals

    if second_dict_keys is not None:
        for key_dict in second_dict_keys:
            try:
                index = data[key_dict]
                if 'political' == key_dict:
                    data_ = political_views[index]
                    collected_data[first_dict_key][key_dict] = data_
                if 'alcohol' == key_dict:
                    data_ = views_one_alcohol[index]
                    collected_data[first_dict_key][key_dict] = data_
                if 'religion' == key_dict:
                    data_ = index
                    collected_data[first_dict_key][key_dict] = data_.lower()
                if 'life_main' == key_dict:
                    data_ = personals_priority[index]
                    collected_data[first_dict_key][key_dict] = data_
                if 'smoking' == key_dict:
                    data_ = views_one_alcohol[index]
                    collected_data[first_dict_key][key_dict] = data_
                if 'people_main' == key_dict:
                    data_ = important_in_others[index]
                    collected_data[first_dict_key][key_dict] = data_
                if 'inspired_by' == key_dict:
                    data_ = index
                    collected_data[first_dict_key][key_dict] = data_
            except KeyError:
                print(f'KeyError[{key_dict}]')
                collected_data[first_dict_key][key_dict] = None


def extract_list_data(data, first_dict_key, collected_data):
    second_dict_keys = None
    if KEY_DICT.SCHOOLS is first_dict_key:
        second_dict_keys = KEY_DICT.schools
    if KEY_DICT.CAREER is first_dict_key:
        second_dict_keys = KEY_DICT.careers
    if KEY_DICT.PERSONAL is first_dict_key:
        second_dict_keys = KEY_DICT.personals
    if KEY_DICT.RELATIVES is first_dict_key:
        if data == list():
            insert_none(first_dict_key, collected_data)
        for value in data:
            if value['type'] == 'sibling':
                name = value['name']
                collected_data[first_dict_key][value['type']] = name
            if value['type'] == 'parent':
                name = value['name']
                collected_data[first_dict_key][value['type']] = name
            if value['type'] == 'child':
                name = value['name']
                collected_data[first_dict_key][value['type']] = name
            if value['type'] == 'grandparent':
                name = value['name']
                collected_data[first_dict_key][value['type']] = name
            if value['type'] == 'grandchild':
                name = value['name']
                collected_data[first_dict_key][value['type']] = name

    if second_dict_keys is not None:
        for second_dict_key in second_dict_keys:
            data_ = data[0][second_dict_key]
            if 'from' == second_dict_key:
                collected_data[first_dict_key]['from_'] = data_
            elif 'until' == second_dict_key:
                collected_data[first_dict_key]['until_'] = data_
            else:
                collected_data[first_dict_key][second_dict_key] = data_


def insert_none(first_dict_key, collected_data):
    second_dict_keys = None
    if first_dict_key in KEY_DICT.FIRST_KEYS[0:14]:
        if first_dict_key is KEY_DICT.GENDER:
            collected_data['profile']['gender'] = None
        elif first_dict_key is KEY_DICT.PHOTO:
            collected_data['profile']['photo'] = None
        else:
            collected_data['profile'][first_dict_key] = None

    if KEY_DICT.RELATIVES is first_dict_key:
        collected_data[first_dict_key]['parent'] = None
        collected_data[first_dict_key]['sibling'] = None
        collected_data[first_dict_key]['child'] = None
        collected_data[first_dict_key]['grandparent'] = None
        collected_data[first_dict_key]['grandchild'] = None

    if first_dict_key in KEY_DICT.FIRST_KEYS[14:23]:
        collected_data['interests'][first_dict_key] = None
    if first_dict_key in KEY_DICT.FIRST_KEYS[23:27]:
        collected_data['university'][first_dict_key] = None
    if KEY_DICT.SCHOOLS is first_dict_key:
        second_dict_keys = KEY_DICT.schools
    if KEY_DICT.CAREER is first_dict_key:
        second_dict_keys = KEY_DICT.careers
    if KEY_DICT.RELATIVES is first_dict_key:
        second_dict_keys = KEY_DICT.relatives
    if KEY_DICT.PERSONAL is first_dict_key:
        second_dict_keys = KEY_DICT.personals

    if second_dict_keys is not None:
        for second_dict_key in second_dict_keys:
            if 'from' == second_dict_key:
                collected_data[first_dict_key]['from_'] = None
            elif 'until' == second_dict_key:
                collected_data[first_dict_key]['until_'] = None
            elif KEY_DICT.PERSONAL is not first_dict_key:
                collected_data[first_dict_key][second_dict_key] = None
            else:
                collected_data['life_position'][second_dict_key] = None


def extract(uncollected_data, collected_data):
    """ Извлекать нужных данных из словаря

    :param для извлечение данных (нужных)
    :param для хранение данных
    """

    # profile 0:13
    # interests 13:22
    # university 22:26
    # 26:29 словари и списки
    for n, first_dict_key in enumerate(KEY_DICT.FIRST_KEYS, start=1):
        try:
            data = uncollected_data[first_dict_key]

            if isinstance(data, str):
                extract_str_data(data, first_dict_key, collected_data)
                # print(f'{n} This is string: {first_dict_key}')

            if isinstance(data, int):
                extract_int_data(data, first_dict_key, collected_data)
                # print(f'{n} This is int: {first_dict_key} {data}')

            if isinstance(data, dict):
                extract_dict_data(data, first_dict_key, collected_data)
                # print(f'{n} This is dict: {first_dict_key} {data}')

            if isinstance(data, list):
                extract_list_data(data, first_dict_key, collected_data)
                # print(f'{n} This is list: {first_dict_key} {data}')
        except TypeError:
            # print(f'TypeError[{n}]: данный не существует {first_dict_key}')
            insert_none(first_dict_key, collected_data)
        except KeyError:
            # print(f'KeyError[{n}]: в словари не существует такой ключ {first_dict_key}')
            insert_none(first_dict_key, collected_data)
        except IndexError:
            # print(f'IndexError[{n}]: список {first_dict_key} пустой')
            insert_none(first_dict_key, collected_data)
