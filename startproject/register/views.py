# Create your views here.

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from .models import User

#表单
class UserForm(forms.Form):
    username = forms.CharField(label='Username',max_length=50, error_messages={
        'required': '请填写您的称呼',
        'max_length': '称呼太长'
    })
    password = forms.CharField(label='Password',widget=forms.PasswordInput(), error_messages={
        'required': '请填写您的密码',
    })

    '''
    email = forms.EmailField(label='Email', error_messages={
        'required': '请填写您的邮箱',
        'invalid': '邮箱格式不正确'
    })
    school = forms.CharField(label='School',max_length=50, error_messages={
        'required': '请填写您的学校',
        'max_length': '学校太长'
    })
    phone = forms.CharField(label='Phone',max_length=11, error_messages={
        'required': '请填写您的电话号码',
        'max_length': '电话号码太长'
    })
    '''


#注册
def regist(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #email = uf.cleaned_data['email']
            #phone = uf.cleaned_data['phone']
            #school = uf.cleaned_data['school']
            #添加到数据库
            User.objects.create(username= username, password=password) #, email=email, phone=phone, school=school
            return render(request, 'register/index.html', {'uf': uf}, )
    else:
        uf = UserForm()
    return render(request, 'register/regist.html', {'uf':uf},)

#登陆
def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #email = uf.cleaned_data['email']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact=username, password__exact=password) # email__exact=email
            if user:
                #比较成功，跳转index
                response = HttpResponseRedirect('/register/index/')
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username', username, 3600)
                request.session['username'] = username
                return response
            else:
                #比较失败，还在login
                return HttpResponseRedirect('/register/login/')
    else:
        uf = UserForm()
    return render(request, 'register/login.html', {'uf':uf},)

#登陆成功
def index(request):
    username = request.COOKIES.get('username', '')
    return render(request, 'register/index.html', {'username':username})

#退出
def logout(request):
    #清理cookie里保存username
    response.delete_cookie('username')
    return render(request, 'register/index.html', {'uf': uf}, )
