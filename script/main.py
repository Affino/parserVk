from itertools import zip_longest

import parser.users.data
import parser.groups.data

from script.mysql.execute import Query
from script.mysql.saving import save


def start_parser_users():
    user_ids = query1.select_value('resource_users', 'vk_id')
    primary_keys = query1.select_value('resource_users', 'id')

    count = range(len(primary_keys))
    # print(user_ids)
    uncollected_data = parser.users.get(user_ids=user_ids)
    index_ = 0
    for uncollected_d, primary_key, index in zip_longest(uncollected_data, primary_keys, count):
        # print(f'{1} - Первичный ключ: {primary_key}')
        index_ += 1
        collected_users_data = {
            'profile': {}, 'interests': {},
            'university': {}, 'career': {},
            'schools': {}, 'relatives': {},
            'life_position': {},
        }
        parser.users.extract(uncollected_d, collected_users_data)
        save(collected_users_data,  query1, tables_names_user, primary_key, index, 'user_id')


def start_parser_groups():
    group_ids = query2.select_value('resource_groups', 'vk_id')
    primary_keys = query2.select_value('resource_groups', 'id')
    count = range(len(primary_keys))
    uncollected_data = parser.groups.get(group_ids)
    for uncollected_d, primary_key,  index in zip_longest(uncollected_data, primary_keys, count):
        collected_data = {'groups_info': {}}
        parser.groups.extract(uncollected_d, collected_data)
        save(collected_data, query2, tables_names_group, primary_key, index, 'group_id')


def main():
    start_parser_users()
    start_parser_groups()


if __name__ == "__main__":
    tables_names_user = [
        'profile',
        'interests',
        'university',
        'career',
        'schools',
        'relatives',
        'life_position'
    ]
    tables_names_group = ['groups_info']

    query1 = Query("users_vk")
    query2 = Query("groups_vk")
    while True:
        main()
