# import asyncio
#
# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.0.2500 Yowser/2.5 Safari/537.36"
# }
#
# async def get_group(id, vk):
#     # сбор данных сообщество
#     vk_group = vk.groups.getById(id=id, fields="members_count")
#     return vk_group[0]
#
# async def get(groups_ids, vk, addingGroupsData):
#
#     tasks = [
#         asyncio.ensure_future(get_group(id, vk))
#         for id in groups_ids
#     ]
#
#     groups_data = await asyncio.gather(*tasks)
#
#     for group_data in users_data:
#         addingUsersData.append(user_data)
