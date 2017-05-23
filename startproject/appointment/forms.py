from django import forms
from django.http import Http404

class AppointAcmForm(forms.Form):
    """
    预约表单
    """

    '''
    school = forms.CharField(label='学校', max_length=20, error_messages={
        'required': '请填写您的学校',
        'max_length': '学校太长'
    })

    phone = forms.CharField(label='电话', max_length=11, error_messages={
        'required': '请填写您的电话',
        'max_length': '电话太长'
    })
    
    user_id = forms.CharField(label='用户ID', error_messages={
        'required': '请填写您的用户id',
        'invalid': 'id格式不正确'
    })
    '''

    name = forms.CharField(label='您的称呼', max_length=20, error_messages={
        'required': '请填写您的称呼',
        'max_length': '称呼太长'
    })

    email = forms.EmailField(label='联系邮箱', error_messages={
        'required': '请填写您的邮箱',
        'invalid': '邮箱格式不正确'
    })

    start_time = forms.DateField(label='开始时间', widget=forms.SelectDateWidget, error_messages={
        'required': '请填写您的预约开始时间',
        'invalid': '时间格式不正确'
    })

    people = forms.CharField(label='预约人数', error_messages={
        'required': '请填写您的预约人数',
    })


class AppointLectureForm(forms.Form):
    """
    预约表单
    """

    name = forms.CharField(label='您的称呼', max_length=20, error_messages={
        'required': '请填写您的称呼',
        'max_length': '称呼太长'
    })

    email = forms.EmailField(label='联系邮箱', error_messages={
        'required': '请填写您的邮箱',
        'invalid': '邮箱格式不正确'
    })

    start_time = forms.DateField(label='开始时间', widget=forms.SelectDateWidget, error_messages={
        'required': '请填写您的预约开始时间',
        'invalid': '时间格式不正确'
    })

    people = forms.CharField(label='预约人数', error_messages={
        'required': '请填写您的预约人数',
    })

class AppointStationForm(forms.Form):
    """
    预约表单
    """

    name = forms.CharField(label='您的称呼', max_length=20, error_messages={
        'required': '请填写您的称呼',
        'max_length': '称呼太长'
    })

    email = forms.EmailField(label='联系邮箱', error_messages={
        'required': '请填写您的邮箱',
        'invalid': '邮箱格式不正确'
    })

    start_time = forms.DateField(label='开始时间', widget=forms.SelectDateWidget, error_messages={
        'required': '请填写您的预约开始时间',
        'invalid': '时间格式不正确'
    })

    people = forms.CharField(label='预约人数', error_messages={
        'required': '请填写您的预约人数',
    })