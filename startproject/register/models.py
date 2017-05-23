# Create your models here.

from django.db import models

# Create your models here.
class User(models.Model):
    '''
    用户
    '''

    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    #email = models.EmailField('邮箱')
    #school = models.CharField(max_length=50)
    #phone = models.CharField(max_length=11)  # 字符型，必须有个参数max_length字符最大值

    def __str__(self):
        return self.username