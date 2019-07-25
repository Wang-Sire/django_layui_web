from django.test import TestCase
new_id = 0
data_list = [{'id': 40, 'authorityId': 1, 'authorityName': '个人中心', 'menuUrl': '', 'menuIcon': 'layui-icon-set', 'authority': '', 'isMenu': 0, 'parentId': -1}, {'id': 41, 'authorityId': 2, 'authorityName': '首页', 'menuUrl': '', 'menuIcon': 'layui-icon-set', 'authority': '', 'isMenu': 1, 'parentId': 1}, {'id': 43, 'authorityId': 3, 'authorityName': '系统管理', 'menuUrl': '', 'menuIcon': 'layui-icon-set', 'authority': '', 'isMenu': 0, 'parentId': -1}, {'id': 44, 'authorityId': 4, 'authorityName': '运营管理', 'menuUrl': '', 'menuIcon': 'layui-icon-set', 'authority': '', 'isMenu': 1, 'parentId': 3}, {'id': 45, 'authorityId': 5, 'authorityName': '我的消息', 'menuUrl': '', 'menuIcon': 'layui-icon-set', 'authority': '', 'isMenu': 1, 'parentId': 1}, {'id': 46, 'authorityId': 6, 'authorityName': '系统配置', 'menuUrl': '', 'menuIcon': 'layui-icon-set', 'authority': '', 'isMenu': 1, 'parentId': 3}, {'id': 47, 'authorityId': 7, 'authorityName': '我的设置', 'menuUrl': '', 'menuIcon': 'layui-icon-set', 'authority': '', 'isMenu': 1, 'parentId': 3}, {'id': 48, 'authorityId': 8, 'authorityName': '用户管理', 'menuUrl': '', 'menuIcon': 'layui-icon-set', 'authority': '', 'isMenu': 2, 'parentId': 4}, {'id': 49, 'authorityId': 9, 'authorityName': '角色管理', 'menuUrl': '', 'menuIcon': 'layui-icon-set', 'authority': '', 'isMenu': 2, 'parentId': 4}, {'id': 50, 'authorityId': 10, 'authorityName': '组织机构', 'menuUrl': '', 'menuIcon': 'layui-icon-set', 'authority': '', 'isMenu': 2, 'parentId': 4}, {'id': 51, 'authorityId': 11, 'authorityName': '菜单管理', 'menuUrl': '', 'menuIcon': 'layui-icon-set', 'authority': '', 'isMenu': 2, 'parentId': 4}, {'id': 52, 'authorityId': 12, 'authorityName': '网站设置', 'menuUrl': '', 'menuIcon': 'layui-icon-set', 'authority': '', 'isMenu': 2, 'parentId': 6}, {'id': 53, 'authorityId': 13, 'authorityName': '邮箱配置', 'menuUrl': '', 'menuIcon': 'layui-icon-set', 'authority': '', 'isMenu': 2, 'parentId': 6}, {'id': 54, 'authorityId': 14, 'authorityName': '基本资料', 'menuUrl': '', 'menuIcon': 'layui-icon-set', 'authority': '', 'isMenu': 2, 'parentId': 7}, {'id': 55, 'authorityId': 15, 'authorityName': '修改密码', 'menuUrl': '', 'menuIcon': 'layui-icon-set', 'authority': '', 'isMenu': 2, 'parentId': 7}]
menu_1 = []
menu_2 = []
menu_3 = []
for i in range(len(data_list)):
    if data_list[i]['isMenu'] == 0:
        menu_1.append(data_list[i])
    if data_list[i]['isMenu'] == 1:
        menu_2.append(data_list[i])
    if data_list[i]['isMenu'] == 2:
        menu_3.append(data_list[i])

menu_1_new = []
for i in range(len(menu_1)):
    menu = []
    menu.append(menu_1[i])
    for j in range(len(menu_2)):
        if menu_1[i]['authorityId'] == menu_2[j]['parentId']:
            menu.append(menu_2[j])
    menu_1_new.append(menu)

print(menu_1_new)
# print(menu_2)
# print(menu_3)
