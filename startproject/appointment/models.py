# Create your models here.

from django.db import models

from register.models import User

class Acm(models.Model):
    '''
    '''

    member = models.CharField('成员', max_length=32)
    gender = models.CharField('性别', max_length=16)
    major = models.CharField('专业', max_length=16)
    phone = models.CharField('电话',max_length=11)  # 字符型，必须有个参数max_length字符最大值
    email = models.EmailField('邮箱')
    awards = models.TextField('获奖')
    introduction = models.TextField('介绍')

    def __str__(self):
        return self.member

class Station(models.Model):
    '''
    '''

    project_name = models.CharField('应用名称', max_length=32)
    introduction = models.TextField('介绍')

    def __str__(self):
        return self.project_name

class Lecture(models.Model):
    '''
    '''

    theme = models.CharField('讲座主题', max_length=140)
    professor = models.CharField('教授', max_length=32)
    time = models.CharField('时间', max_length=32)
    place = models.CharField('地点', max_length=32)
    introduction = models.TextField('介绍')

    def __str__(self):
        return self.theme

class appoint_acm(models.Model):
    '''
    '''

    acm = models.ForeignKey(Acm, verbose_name='竞赛生')

    #x_id = models.CharField('预约对象的id', max_length=9)
    #x_type = models.CharField('预约对象的类型', max_length=9)
    start_time = models.DateField('开始时间')
    people = models.CharField('预约人数', max_length=10)

    #user = models.ForeignKey(User, verbose_name='用户')
    name = models.CharField('用户名称', max_length=20)
    email = models.EmailField('邮箱')

    def __str__(self):
        return self.name

class appoint_lecture(models.Model):
    '''
    '''

    lecture = models.ForeignKey(Lecture, verbose_name='讲座')

    start_time = models.DateField('开始时间')
    people = models.CharField('预约人数', max_length=10)

    #user = models.ForeignKey(User, verbose_name='用户')
    name = models.CharField('用户名称', max_length=20)
    email = models.EmailField('邮箱')

    def __str__(self):
        return self.name

class appoint_station(models.Model):
    '''
    '''

    station = models.ForeignKey(Station, verbose_name='讲座')

    start_time = models.DateField('开始时间')
    people = models.CharField('预约人数', max_length=10)

    #user = models.ForeignKey(User, verbose_name='用户')
    name = models.CharField('用户名称', max_length=20)
    email = models.EmailField('邮箱')

    def __str__(self):
        return self.name

