import json
import datetime
from .models import *
from django.db.models import Q
from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator


def login(request):
    return render(request, 'login.html', locals())


def register(request):
    return render(request, 'register.html', locals())


def forget(request):
    return render(request, 'forget.html', locals())


def logout(request):
    return render(request, 'login.html', locals())


def index(request):
    return render(request, 'base.html', locals())


def user_add(request):
    role_info = Role.objects.filter().all()
    return render(request, 'user_add.html', locals())


def user_list(request):
    role_info = Role.objects.filter().all()
    if request.method == 'GET':
        username = request.GET.get('username', '')
        phone = request.GET.get('phone', '')
        email = request.GET.get('email', '')
        role = request.GET.get('role', '')
        employee_name = request.GET.get('employee_name', '')
        sex = request.GET.get('sex', '')
        position = request.GET.get('position', '')
        job_status = request.GET.get('job_status', '')
        department = request.GET.get('department', '')
        group = request.GET.get('group', '')
        superior = request.GET.get('superior', '')
        administration = request.GET.get('administration', '')
        profile = request.GET.get('profile', '')

        if username or phone or email or role:
            if SysUser.objects.filter(username=username):
                return HttpResponse(-1)
            else:
                new_add = SysUser.objects.create(username=username,
                                                 password='111111',
                                                 phone=phone,
                                                 email=email,
                                                 role=role,
                                                 sex=sex,
                                                 position=position,
                                                 employee_name=employee_name,
                                                 job_status=job_status,
                                                 department=department,
                                                 group=group,
                                                 superior=superior,
                                                 administration=administration,
                                                 profile=profile)
                new_add.save()
                return HttpResponse(0)
        else:
            return render(request, 'user_list.html', locals())
    return render(request, 'user_list.html', locals())


def user_data(request):
    if request.method == 'GET':
        username = request.GET.get('username', '')
        role = request.GET.get('role', '')
        page = request.GET.get('page')
        limit = request.GET.get('limit')
        if username or role:
            data = SysUser.objects.values('id', 'username', 'sex', 'job_status', 'role', 'join_time').\
                filter(Q(username=username) | Q(role=role)).order_by().all()
        else:
            data = SysUser.objects.all().values()
        data_list = list(data)
        if page and limit:
            limits = Paginator(data_list, limit)
            contacts = limits.page(page)
            res = []
            for contact in contacts:
                contact['join_time'] = str(contact['join_time'])
                res.append(contact)
            data_json = {"code": 0, 'msg': "ok", 'count': data_list.__len__(), 'data': res}

            return HttpResponse(json.dumps(data_json))
        else:
            return render(request, 'role_list.html', locals())
    else:
        return render(request, 'role_list.html', locals())


def user_edit(request, name):
    if name:
        role_info = Role.objects.filter().all()
        user = SysUser.objects.values('id',
                                      'username',
                                      'phone',
                                      'email',
                                      'role',
                                      'sex',
                                      'position',
                                      'employee_name',
                                      'job_status',
                                      'department',
                                      'group',
                                      'superior',
                                      'administration',
                                      'profile').filter(id=name).order_by().all()
        if request.method == 'GET':
            username = request.GET.get('username', '')
            phone = request.GET.get('phone', '')
            email = request.GET.get('email', '')
            role = request.GET.get('role', '')
            employee_name = request.GET.get('employee_name', '')
            sex = request.GET.get('sex', '')
            position = request.GET.get('position', '')
            job_status = request.GET.get('job_status', '')
            department = request.GET.get('department', '')
            group = request.GET.get('group', '')
            superior = request.GET.get('superior', '')
            administration = request.GET.get('administration', '')
            profile = request.GET.get('profile', '')
            
            if username or phone or email or role:
                if SysUser.objects.filter(id=name).update(username=username,
                                                          phone=phone,
                                                          email=email,
                                                          role=role,
                                                          sex=sex,
                                                          position=position,
                                                          employee_name=employee_name,
                                                          job_status=job_status,
                                                          department=department,
                                                          group=group,
                                                          superior=superior,
                                                          administration=administration,
                                                          profile=profile):
                    return HttpResponse(0)
                else:
                    return HttpResponse(-1)
            else:
                return render(request, 'user_edit.html', locals())
        else:
            return render(request, 'user_edit.html', locals())


def user_locking(request):
    if request.method == 'GET':
        username = request.GET.get('username', '')
        print(username)
        # if SysUser.objects.filter(username=username).update(password='111111'):
        return HttpResponse(0)
        # else:
        #     return HttpResponse(-1)
    else:
        return render(request, 'user_list.html', locals())


def user_reset_password(request):
    if request.method == 'GET':
        username = request.GET.get('username', '')
        if SysUser.objects.filter(username=username).update(password='111111'):
            return HttpResponse(0)
        else:
            return HttpResponse(-1)
    else:
        return render(request, 'user_list.html', locals())


def user_del(request):
    if request.method == 'GET':
        username = request.GET.get('username', '')
        if SysUser.objects.filter(username=username).delete():
            return HttpResponse(1)
        else:
            return HttpResponse(0)
    return render(request, 'user_list.html', locals())


def user_del_more(request):
    if request.method == 'GET':
        role_id = request.GET.get('id', '')
        del_id = str(role_id).split(',')
        result = []
        for i in del_id:
            if SysUser.objects.filter(id=int(i)).delete():
                result.append(1)
            else:
                result.append(0)
        if 0 in result:
            return HttpResponse(0)
        else:
            return HttpResponse(1)
    return render(request, 'user_list.html', locals())


def role_list(request):
    role = Role.objects.filter().all()
    if request.method == 'GET':
        name = request.GET.get('name', '')
        describe = request.GET.get('describe', '')
        if name or describe:
            if Role.objects.filter(name=name):
                return HttpResponse(-1)
            else:
                new_add = Role.objects.create(name=name, describe=describe)
                new_add.save()
                return HttpResponse(0)
    return render(request, 'role_list.html', locals())


def role_data(request):
    if request.method == 'GET':
        page = request.GET.get('page')
        limit = request.GET.get('limit')
        data = Role.objects.all().values()
        data_list = list(data)
        limits = Paginator(data_list, limit)
        contacts = limits.page(page)
        res = []
        for contact in contacts:
            res.append(contact)
        data_json = {"code": 0, 'msg': "ok", 'count': data_list.__len__(), 'data': res}

        return HttpResponse(json.dumps(data_json))
    else:
        return render(request, 'role_list.html', locals())


def role_edit(request, name):
    if name:
        role = Role.objects.values('id', 'name', 'describe').filter(id=name).order_by().all()
        if request.method == 'GET':
            role_name = request.GET.get('name', '')
            describe = request.GET.get('describe', '')
            if role_name or describe:
                if Role.objects.filter(id=name).update(name=role_name, describe=describe):
                    return HttpResponse(0)
                else:
                    return HttpResponse(-1)
            else:
                return render(request, 'role_edit.html', locals())
        else:
            return render(request, 'role_edit.html', locals())


def role_user(request, name):
    # if name:
    #     role = Role.objects.values('id', 'name', 'describe').filter(id=name).order_by().all()
    #     if request.method == 'GET':
    #         role_name = request.GET.get('name', '')
    #         describe = request.GET.get('describe', '')
    #         if role_name or describe:
    #             if Role.objects.filter(id=name).update(name=role_name, describe=describe):
    #                 return HttpResponse(0)
    #             else:
    #                 return HttpResponse(-1)
    #         else:
    #             return render(request, 'role_edit.html', locals())
    #     else:
    return render(request, 'role_user.html', locals())


def role_del(request):
    if request.method == 'GET':
        name = request.GET.get('name', '')
        if Role.objects.filter(name=name).delete():
            return HttpResponse(1)
        else:
            return HttpResponse(0)
    return render(request, 'role_list.html', locals())


def role_del_more(request):
    if request.method == 'GET':
        role_id = request.GET.get('id', '')
        del_id = str(role_id).split(',')
        result = []
        for i in del_id:
            if Role.objects.filter(id=int(i)).delete():
                result.append(1)
            else:
                result.append(0)
        if 0 in result:
            return HttpResponse(0)
        else:
            return HttpResponse(1)
    return render(request, 'role_list.html', locals())


def role_add(request):
    return render(request, 'role_add.html', locals())


def menu_list(request):
    if request.method == 'GET':
        authority_id = request.GET.get('authorityId')
        authority_name = request.GET.get('authorityName')
        menu_url = request.GET.get('menuUrl')
        authority = request.GET.get('authority')
        is_menu = request.GET.get('isMenu')
        parent_id = request.GET.get('parentId')

        if authority_name:
            if Menu.objects.filter(authorityName=authority_name):
                return HttpResponse(-1)
            else:
                new_add = Menu.objects.create(
                    authorityId=authority_id,
                    authorityName=authority_name,
                    menuUrl=menu_url,
                    authority=authority,
                    isMenu=is_menu,
                    parentId=parent_id)
                new_add.save()
                return HttpResponse(0)

    return render(request, 'menu_list.html', locals())


def menu_add(request):
    data = Menu.objects.all().values()
    data_list = list(data)
    new_id = 0
    parent_menu = []
    for i in range(len(data_list)):
        new_id = data_list[i]['authorityId']
        if data_list[i]['parentId'] == -1:
            parent_menu.append(data_list[i]['authorityName'])
    new_id += 1

    return render(request, 'menu_add.html', locals())


def menu_data(request):
    data = Menu.objects.values('authorityId', 'authorityName', 'menuUrl', 'menuIcon',
                               'authority', 'isMenu', 'parentId').order_by().all()
    data_list = list(data)
    data_json = {"code": 0, 'msg': "ok", 'count': data_list.__len__(), 'data': data_list}

    return HttpResponse(json.dumps(data_json))


def menu_edit(request, name):
    menu = Menu.objects.values('authorityId', 'authorityName', 'menuUrl', 'menuIcon',
                               'authority', 'isMenu', 'parentId').order_by().all()
    if name:
        menu_info = Menu.objects.values('authorityId',
                                        'authorityName',
                                        'menuUrl',
                                        'authority',
                                        'isMenu',
                                        'parentId').filter(authorityName=name).order_by().all()
        menu_info = list(menu_info)
        menu_info_parent = menu_info[0]['parentId']
        if request.method == 'GET':
            authority_id = request.GET.get('authorityId')
            authority_name = request.GET.get('authorityName')
            menu_url = request.GET.get('menuUrl')
            authority = request.GET.get('authority')
            is_menu = request.GET.get('isMenu')
            parent_id = request.GET.get('parentId')

            if authority_name:
                if name != authority_name:
                    if Menu.objects.filter(authorityName=authority_name):
                        return HttpResponse(-1)
                if authority_name:
                    if Menu.objects.filter(authorityName=name).update(authorityId=authority_id,
                                                                      authorityName=authority_name,
                                                                      menuUrl=menu_url,
                                                                      authority=authority,
                                                                      isMenu=is_menu,
                                                                      parentId=parent_id):
                        return HttpResponse(0)
                    else:
                        return HttpResponse(1)
            else:
                return render(request, 'menu_edit.html', locals())
        else:
            return render(request, 'menu_edit.html', locals())


def menu_del(request):
    data_all = Menu.objects.all().values()
    data_all_list = list(data_all)
    if request.method == 'GET':
        name = request.GET.get('authorityName', '')
        menu_info = Menu.objects.values('authorityId',
                                        'authorityName',
                                        'menuUrl',
                                        'authority',
                                        'isMenu',
                                        'parentId').filter(authorityName=name).order_by().all()
        data_list = list(menu_info)
        authority_id = data_list[0]['authorityId']
        for i in range(len(data_all_list)):
            if data_all_list[i]['parentId'] == authority_id:
                return HttpResponse(-1)
        if Menu.objects.filter(authorityName=name).delete():
            return HttpResponse(1)
        else:
            return HttpResponse(0)

    return render(request, 'menu_list.html', locals())


def form_list(request):

    return render(request, 'form_list.html', locals())


def department_list(request):
    data = DepartmentInfo.objects.all().values()
    if request.method == 'GET':
        authority_id = request.GET.get('authority_id')
        department_name = request.GET.get('department_name')
        department_leader = request.GET.get('department_leader')
        establish_date = request.GET.get('establish_date')
        department_label = request.GET.get('department_label')
        parent_id = request.GET.get('parent_id')
        if department_name:
            if DepartmentInfo.objects.filter(department_name=department_name):
                return HttpResponse(-1)
            else:
                new_add = DepartmentInfo.objects.create(
                    authority_id=authority_id,
                    department_name=department_name,
                    department_leader=department_leader,
                    establish_date=establish_date,
                    department_label=department_label,
                    parent_id=parent_id)
                new_add.save()

                return HttpResponse(0)

    return render(request, 'form_list.html', locals())


def department_add(request):
    data = DepartmentInfo.objects.all().values()
    data_list = list(data)
    new_id = 0
    parent_info = []
    for i in range(len(data_list)):
        new_id = data_list[i]['authority_id']
        if data_list[i]['parent_id'] == -1:
            parent_info.append(data_list[i]['department_name'])
    new_id += 1

    return render(request, 'department_add.html', locals())


def department_data(request):
    data = DepartmentInfo.objects.values('authority_id', 'department_name', 'department_leader', 'establish_date',
                                         'department_label', 'parent_id').order_by().all()
    data_list = list(data)
    data_json = {"code": 0, 'msg': "ok", 'count': data_list.__len__(), 'data': data_list}

    return HttpResponse(json.dumps(data_json))


def department_edit(request, name):
    data = DepartmentInfo.objects.values('authority_id', 'department_name', 'department_leader', 'establish_date',
                                         'department_label', 'parent_id').order_by().all()
    if name:
        department_info = DepartmentInfo.objects.values(
            'authority_id',
            'department_name',
            'department_leader',
            'establish_date',
            'department_label',
            'parent_id').filter(department_name=name).order_by().all()
        department_info = list(department_info)
        parent_id = department_info[0]['parent_id']
        if request.method == 'GET':
            authority_id = request.GET.get('authority_id')
            department_name = request.GET.get('department_name')
            department_leader = request.GET.get('department_leader')
            establish_date = request.GET.get('establish_date')
            department_label = request.GET.get('department_label')
            parent_id = request.GET.get('parent_id')

            if department_name:
                if name != department_name:
                    if DepartmentInfo.objects.filter(department_name=department_name):
                        return HttpResponse(-1)
                if DepartmentInfo.objects.filter(department_name=name).update(
                        authority_id=authority_id,
                        department_name=department_name,
                        department_leader=department_leader,
                        establish_date=establish_date,
                        department_label=department_label,
                        parent_id=parent_id):
                    return HttpResponse(0)
                else:
                    return HttpResponse(1)
            else:
                return render(request, 'department_edit.html', locals())
        else:
            return render(request, 'department_edit.html', locals())


def department_del(request):
    data_all = DepartmentInfo.objects.all().values()
    data_all_list = list(data_all)
    if request.method == 'GET':
        department_name = request.GET.get('department_name', '')
        data_key = DepartmentInfo.objects.values(
            'authority_id',
            'department_name',
            'department_leader',
            'establish_date',
            'department_label',
            'parent_id').filter(department_name=department_name).order_by().all()
        data_list = list(data_key)
        authority_id = data_list[0]['authority_id']
        for i in range(len(data_all_list)):
            if data_all_list[i]['parent_id'] == authority_id:
                return HttpResponse(-1)
        if DepartmentInfo.objects.filter(department_name=department_name).delete():
            return HttpResponse(1)
        else:
            return HttpResponse(0)

    return render(request, 'menu_list.html', locals())


def department_set(request, name):
    data = DepartmentInfo.objects.values('authority_id', 'department_name', 'department_leader', 'establish_date',
                                         'department_label', 'parent_id').order_by().all()
    if name:
        department_info = DepartmentInfo.objects.values(
            'authority_id',
            'department_name',
            'department_leader',
            'establish_date',
            'department_label',
            'parent_id').filter(department_name=name).order_by().all()
        department_info = list(department_info)
        parent_id = department_info[0]['parent_id']
        if request.method == 'GET':
            authority_id = request.GET.get('authority_id')
            department_name = request.GET.get('department_name')
            department_leader = request.GET.get('department_leader')
            establish_date = request.GET.get('establish_date')
            department_label = request.GET.get('department_label')
            parent_id = request.GET.get('parent_id')

            if department_name:
                if name != department_name:
                    if DepartmentInfo.objects.filter(department_name=department_name):
                        return HttpResponse(-1)
                if DepartmentInfo.objects.filter(department_name=name).update(
                        authority_id=authority_id,
                        department_name=department_name,
                        department_leader=department_leader,
                        establish_date=establish_date,
                        department_label=department_label,
                        parent_id=parent_id):
                    return HttpResponse(0)
                else:
                    return HttpResponse(1)
            else:
                return render(request, 'department_set.html', locals())
        else:
            return render(request, 'department_set.html', locals())


def group_list(request):
    group = Group.objects.filter().all()
    if request.method == 'GET':
        name = request.GET.get('name', '')
        describe = request.GET.get('describe', '')
        if name or describe:
            if Group.objects.filter(name=name):
                return HttpResponse(1)
            else:
                new_add = Group.objects.create(name=name, describe=describe)
                new_add.save()
                return HttpResponse(0)
    return render(request, 'group_list.html', locals())


def group_data(request):
    if request.method == 'GET':
        page = request.GET.get('page')
        limit = request.GET.get('limit')
        data = Group.objects.all().values()
        data_list = list(data)
        limits = Paginator(data_list, limit)
        contacts = limits.page(page)
        res = []
        for contact in contacts:
            res.append(contact)
        data_json = {"code": 0, 'msg': "ok", 'count': data_list.__len__(), 'data': res}

        return HttpResponse(json.dumps(data_json))
    else:
        return render(request, 'group_list.html', locals())


def group_edit(request, name):
    if name:
        group = Group.objects.values('id', 'name', 'describe').filter(id=name).order_by().all()
        if request.method == 'GET':
            group_name = request.GET.get('name', '')
            describe = request.GET.get('describe', '')
            if group_name or describe:
                if Group.objects.filter(id=name).update(name=group_name, describe=describe):
                    return HttpResponse(0)
                else:
                    return HttpResponse(-1)
            else:
                return render(request, 'group_edit.html', locals())
        else:
            return render(request, 'group_edit.html', locals())


def group_del(request):
    if request.method == 'GET':
        name = request.GET.get('name', '')
        if Group.objects.filter(name=name).delete():
            return HttpResponse(1)
        else:
            return HttpResponse(0)
    return render(request, 'group_list.html', locals())


def group_del_more(request):
    if request.method == 'GET':
        role_id = request.GET.get('id', '')
        del_id = str(role_id).split(',')
        result = []
        for i in del_id:
            if Group.objects.filter(id=int(i)).delete():
                result.append(1)
            else:
                result.append(0)
        if 0 in result:
            return HttpResponse(0)
        else:
            return HttpResponse(1)
    return render(request, 'group_list.html', locals())


def group_add(request):
    return render(request, 'group_add.html', locals())


def station_list(request, name):
    if name:
        username = str(name).split(',')
        # print(set_id)

    return render(request, 'station_set.html', locals())


def station_set(request):

    return render(request, 'group_add.html', locals())


def user_info(request):
    return render(request, 'user_info.html', locals())


def user_form(request):
    return render(request, 'userform.html', locals())


def password(request):
    return render(request, 'password.html', locals())


def set_web(request):
    return render(request, 'website.html', locals())


def set_email(request):
    return render(request, 'email.html', locals())
