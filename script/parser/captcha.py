import vk_api

login, password = '87476878303', 'YO-Ox-7007#-($)'


def captcha_handler(captcha):
    """ При возникновении капчи вызывается эта функция и ей передается объект
        капчи. Через метод get_url можно получить ссылку на изображение.
        Через метод try_again можно попытаться отправить запрос с кодом капчи
    """

    key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()

    # Пробуем снова отправить запрос с капчей
    return captcha.try_again(key)


def auth_vk():
    """ Пример обработки капчи """

    vk_session = vk_api.VkApi(
        login, password,
        captcha_handler=captcha_handler  # функция для обработки капчи
    )
    try:

        vk_session.auth()
        vk = vk_session.get_api()
        return vk

    except Exception as ex:
        print(ex)


