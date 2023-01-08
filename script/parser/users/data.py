from script.parser.captcha import auth_vk

uncollected_data = []

vk = auth_vk()

fields = [
    "status,"  "city," "activities," "photo_max,"
    "interests,"  "games," "country," "about,"
    "sex," "education," "books," "movies," "music,"
    "online," "quotes,"  "tv," "last_seen," "domain,"
    "contacts," "relation," "bdate,"
    "schools," "career," "relatives," "personal"
]


def get(user_ids):
    """ Получать данных пользователя

    :param user_ids: идентификатор пользователя
    """
    data = vk.users.get(user_ids=user_ids, fields=fields)
    for i in data:
        uncollected_data.append(i)

    return uncollected_data
