from itertools import zip_longest

import parser.users

from script.mysql.execute import Query
from script.mysql.users import save


def main():

    user_ids = query.select_value('resource_users', 'VK_ID')
    # group_ids = query.select_value('resource_group', 'id_group')
    primary_keys = query.select_value('resource_users', 'id')
    count = range(len(primary_keys))
    uncollected_data = parser.users.get(user_ids=user_ids)
    index_ = 0
    for uncollected_d, primary_key, index in zip_longest(uncollected_data, primary_keys, count):  #

        print(f'Количество итерации {index_}')
        index_ += 1
        collected_users_data = {
            'profile': {}, 'interests': {},
            'university': {}, 'career': {},
            'schools': {}, 'relatives': {},
            'life_position': {},
        }
        parser.users.extract(uncollected_d, collected_users_data)
        save(collected_users_data, query, primary_key, index)


if __name__ == "__main__":
    query = Query("vk_data")
    while True:
        main()
