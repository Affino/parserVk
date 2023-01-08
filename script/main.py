from itertools import zip_longest

import parser.users

from script.mysql.execute import Query
from script.mysql.users import save


def main():
    query = Query("vk_data")

    user_ids = query.select_value('resource_users', 'id_user')
    # group_ids = query.select_value('resource_group', 'id_group')
    primary_keys = query.select_value('resource_users', 'id')
    uncollected_data = parser.users.get(user_ids=user_ids)
    index = 0
    for uncollected_data, primary_key in zip_longest(uncollected_data, primary_keys):
        # print(uncollected_data)
        parser.users.extract(uncollected_data, collected_users_data)
        print(collected_users_data)
        # save(collected_users_data, query, primary_key, index)
        index += 1


if __name__ == "__main__":

    collected_users_data = {
        'profile': {}, 'interests': {},
        'university': {}, 'career': {},
        'schools': {}, 'relatives': {},
        'life_position': {},
    }

    main()
