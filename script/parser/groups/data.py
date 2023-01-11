from script.parser.captcha import auth_vk

vk = auth_vk()

fields = [
    'members_count', 'status', 'description'
]


def get(group_ids):
    """ Получать данных сообщества

    :param group_ids: идентификатор сообщества
    """
    uncollected_data = []

    data = vk.groups.getById(group_ids=group_ids, fields=fields)

    for i in data:
        uncollected_data.append(i)

    return uncollected_data
