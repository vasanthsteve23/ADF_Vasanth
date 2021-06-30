"""This is views file"""
import json
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template.defaultfilters import lower
from datetime import date, datetime
from .models import news
from .forms import RegistrationForm
from .models import RegistrationData
from .info import InformationForm
from .models import InfoData
from .models import Response

# Create your views here.

def newss(request):
    obj = news.objects.get(id=1)
    context={
        "list":["Vasanth","steve","nivi","Rakul"],
        "num": 50,
        "data":obj,
    }
    return render(request,'home.html',context)

def newsdate(request,year):
    obj = news.objects.get(id=1)
    art_list = news.objects.filter(fun_date__year=year)
    context = {
        "year": year,
        "art_list": art_list
    }
    return render(request, 'newsdate.html', context)


def register(request):   
    context={
        "form": RegistrationForm
    }
    return render(request,'signup.html',context)

def addUser(request):
    form = RegistrationForm(request.POST)

    if form.is_valid():
        myregister = RegistrationData(name=form.cleaned_data['name'],
                                    password=form.cleaned_data['password'],
                                    email=form.cleaned_data['email'],
                                    phone = form.cleaned_data['phone'])
        myregister.save()
    return redirect('news')


def addInfo(request):
    context = {
        "form": InformationForm
    }
    return render(request, 'info.html', context)

def addDB(request):
    data1=''
    form = InformationForm(request.POST)
    if form.is_valid():
        myinfo = InfoData(fname=form.cleaned_data['fname'],
                          mname=form.cleaned_data['mname'],
                          lname=form.cleaned_data['lname'],
                          dob=form.cleaned_data['dob'],
                          gender=form.cleaned_data['gender'],
                          nationality=form.cleaned_data['nationality'],
                          city=form.cleaned_data['city'],
                          state=form.cleaned_data['state'],
                          pin=form.cleaned_data['pin'],
                          qualification=form.cleaned_data['qualification'],
                          salary=form.cleaned_data['salary'],
                          pan=form.cleaned_data['pan'])
        myinfo.save()
        data1 = validation()
    return HttpResponse(data1)

def validation():
    p = InfoData.objects.raw('SELECT  id,dob from infos_infodata where id='
                             '(select max(id) from infos_infodata)')[0]
    req_id= p.id

    p = InfoData.objects.raw('SELECT  id,dob as agecurr from infos_infodata where id='
                             '(select max(id) from infos_infodata)')[0]
    dob = p.dob

    p = InfoData.objects.raw('SELECT  id,gender from infos_infodata where id='
                             '(select max(id) from infos_infodata)')[0]
    gender = p.gender

    p = InfoData.objects.raw('SELECT  id,nationality from infos_infodata where id='
                             '(select max(id) from infos_infodata)')[0]
    nation = p.nationality

    p = InfoData.objects.raw('SELECT  id,state from infos_infodata where id='
                             '(select max(id) from infos_infodata)')[0]
    state = p.state

    p = InfoData.objects.raw('SELECT  id,salary from infos_infodata where id='
                             '(select max(id) from infos_infodata)')[0]
    salary = p.salary

    p = InfoData.objects.raw('SELECT  id,pan from infos_infodata where id='
                             '(select max(id) from infos_infodata)')[0]
    pan = p.pan

    p = InfoData.objects.raw('SELECT  id,req_date from infos_infodata where id='
                             '(select max(id) from infos_infodata)')[0]
    req_date = p.req_date


    flag=1
    reason=''
    response=''

    age=age_calculate(dob)

    if flag==1:
        age_val = age_validation(gender,age)
        if age_val != 'Eligible':
            flag=0
            reason=age_val

    if flag==1:
        nat_val = nation_validation(nation)
        if nat_val != 'Eligible':
            flag=0
            reason=nat_val

    if flag==1:
        state_val = state_validation(state)
        if state_val != 'Eligible':
            flag=0
            reason=state_val

    if flag==1:
        salary_val = salary_validation(salary)
        if salary_val != 'Eligible':
            flag = 0
            reason = salary_val

    if flag == 1:
        pan_val = pan_validation(pan)
        if pan_val != 'Eligible' or pan_val != 'New User':
            flag = 0
            reason = pan_val

    if reason == '':
        response = 'Success'
        reason = 'Nil'
    else:
        response = 'Failure'

    dictation = {"Reuest_id":req_id,"Response":response,"Reason":reason}
    dictation = json.dumps(dictation)
    adddatadb(req_id,response,dictation)
    return dictation

def nation_validation(nation):
    list = ['indian','american']
    nation = lower(nation)
    nation = nation.replace(' ','')
    if nation in list:
        return "Eligible"
    else:
        return "Nationality not eligible"


def state_validation(state):
    states = ['andhrapradhesh', 'arunachalpradesh', 'assam', 'bihar', 'chhattisgarh', 'karnataka',
              'madhyapradesh', 'odisha', 'tamilnadu', 'telangana', 'westbengal']
    state = lower(state)
    state = state.replace(' ', '')
    if state in states:
        return "Eligible"
    else:
        return "Nationality not eligible"

def salary_validation(salary):
    if 10000 <= salary <= 90000:
        return "Eligible"
    else:
        return "Salary not eligible"

def age_calculate(dob1):
    today=date.today()
    age1=today.year-dob1.year-((today.month,today.day)<(dob1.month,dob1.day))
    return age1

def age_validation(gender,age):
    gender=lower(gender)
    if gender == 'male' and age<21:
        return 'Age invalid'
    elif gender == 'female' and age<18:
        return 'Age invalid'
    else:
        return 'Eligible'

def pan_validation(pan_num):
    dates = []
    validate_result = []
    for p in InfoData.objects.raw('SELECT id,pan,req_date FROM infos_infodata'):
        if pan_num == p.pan:
            str1 = ''.join(str(p.req_date))
            str1 = str1.split()
            dates.append(str1)
    if len(dates) > 0:
        dates.reverse()
        date_formate = '%Y-%m-%d'
        get_date = date.today()
        d1_data = get_date.strftime(date_formate)
        print(d1_data)
        a_data = datetime.strptime(d1_data, date_formate)
        b_data = datetime.strptime(dates[0][0], date_formate)
        delta = a_data - b_data
        delta = abs(delta)

        validate_result.append("Activity in last five days") \
            if delta.days <= 5 else validate_result.append("Eligible")

        print(validate_result)
    else:
        validate_result.append("New User")
    return validate_result[0]

def adddatadb(req_id,response,dictation):

    mydata = Response(req_id = req_id,
                      response = response,
                      reason = dictation)
    mydata.save()
