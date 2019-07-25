from django.db import models
from mptt.models import MPTTModel


class Role(models.Model):
    name = models.CharField(max_length=100)
    describe = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '角色管理'
        verbose_name_plural = '角色管理'


class SysUser(models.Model):
    join_time = models.DateField(auto_now_add=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    employee_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    job_status = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    superior = models.CharField(max_length=100)
    administration = models.CharField(max_length=100)
    profile = models.CharField(max_length=100)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户管理'
        verbose_name_plural = '用户管理'


class Menu(models.Model):
    authorityId = models.IntegerField()
    authorityName = models.CharField(max_length=100)
    menuUrl = models.CharField(max_length=100, blank=True)
    menuIcon = models.CharField(max_length=100, blank=True, default='layui-icon-set')
    authority = models.CharField(max_length=100, blank=True)
    isMenu = models.IntegerField()
    parentId = models.IntegerField()

    def __str__(self):
        return self.authorityName

    class Meta:
        verbose_name = '菜单管理'
        verbose_name_plural = '菜单管理'

    # class MPTTMeta:
    #     parent_attr = 'parentId'
    #
    # def __unicode__(self):
    #     return self.authorityName


class DepartmentInfo(models.Model):
    authority_id = models.IntegerField()
    department_name = models.CharField(max_length=100)
    department_leader = models.CharField(max_length=100)
    establish_date = models.CharField(max_length=100)
    department_label = models.CharField(max_length=100, blank=True)
    parent_id = models.IntegerField()

    def __str__(self):
        return self.department_name

    class Meta:
        verbose_name = '部门管理'
        verbose_name_plural = '部门管理'

    # class MPTTMeta:
    #     parent_attr = 'parentId'
    #
    # def __unicode__(self):
    #     return self.department_name


# class MenuNew(MPTTModel):
#     authorityId = models.IntegerField()
#     authorityName = models.CharField(max_length=100)
#     menuUrl = models.CharField(max_length=100, blank=True)
#     menuIcon = models.CharField(max_length=100, blank=True, default='layui-icon-set')
#     authority = models.CharField(max_length=100, blank=True)
#     isMenu = models.IntegerField()
#     parentId = models.IntegerField()
#
#     def __str__(self):
#         return self.authorityName
#
#     class Meta:
#         verbose_name = '菜单管理'
#         verbose_name_plural = '菜单管理'
#
#     class MPTTMeta:
#         parent_attr = 'parentId'
#
#     def __unicode__(self):
#         return self.authorityName
