import vk_api

vk_session = vk_api.VkApi('87476878303', 'Xb-160-7505@')
vk_session.auth()

vk = vk_session.get_api()

data = vk.users.get(user_id='707238197', fields='sex')
print(data[0]['sex'])
