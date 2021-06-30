# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from .models import request_info
# from .forms import reg_info
# from datetime import date, time
# import datetime as dates
# from .json import python_string
# import json
#
# # Create your views here.
# def home(request):
#     return render(request, 'home.html',{'name':'Rakul'})
#
# def contact(request):
#     return render(request, 'contact.html', {'name':'Rakul'})
#
# def result(request):
#     return render(request, 'result.html')
#
# def add_func(request):
#     context={
#         "form": reg_info
#     }
#     return render(request, 'signup.html', context)
#
# def user(request):
#     if request.method== "POST":
#         valid=False
#         form= reg_info(request.POST)
#         if form.is_valid():
#             firstname=form.cleaned_data['firstname']
#             middlename=form.cleaned_data['middlename']
#             lastname=form.cleaned_data['lastname']
#             dob=age_check(request, form.cleaned_data['dob'])
#             gender=gender_data(request, form.cleaned_data['gender'])
#             nationality=nation(request, form.cleaned_data['nationality'])
#             city=get_city(request, form.cleaned_data['city'])
#             state=get_state(request, form.cleaned_data['state'])
#             pincode=get_pin(request, form.cleaned_data['pincode'])
#             qualification=get_qualification(request, form.cleaned_data['qualification'])
#             salary=get_salary(request, form.cleaned_data['salary'])
#             panid=pan_number(request, form.cleaned_data['panid'])
#             ValidateAge = validate_date(request, dob, gender)
#             ValidatePan = validate_pan(request, panid)
#             count, validate = validate_all_data(dob, ValidateAge, ValidatePan, state, salary, nationality)
#             form.save()
#             if isinstance(count, int):
#                 response = "Success"
#                 reason = validate
#                 valid = True
#             else:
#                 response = count
#                 reason = validate
#             context = {"form": form, "Valid": valid, "Response": reason, "Reason": response}
#             return render(request, 'main/result.html', context)
#     else:
#         form_data = reg_info()
#     context = {"form": form_data}
#     return render(request, 'main/resultget.html', context)
#
# def age_check(request, birthdate):
#     formate = "%Y-%m-%d"
#     try:
#         datetime.strptime(age, formate)
#         born = datetime.strptime(age, formate).date()
#         today = date.today()
#         age_result = today.year \
#                      - born.year - ((today.month, today.day) < (born.month, born.day))
#     except:
#         age_result = "Format should be %Y-%m-%d"
#     return age_result
#
# def validate_age(request, age_1, gender_1):
#     gender_1=gender_1.casefold()
#     if gender_1=="male" and age_1>=21 or gender_1=="female" and age_1>=18:
#         return "Eligible"
#     if gender_1=="male" and age_1<=20 or gender_1=="female" and age_1<=18:
#         return "Not Eligible. Your age is lesser!"
#     return "Not Eligible"
#
# def gender_data(request, gender):
#     gender_list = []
#     if gender == 'Male' or gender == 'Female':
#         gender_list.append(gender)
#     else:
#         if gender_list == []:
#             gender_list.append("Not a Valid")
#         else:
#             gender_list
#     # gender_list = gender_list.append("Not a Valid") if gender_list == [] else gender_list
#     return gender_list[0]
#
# def nation(request, n_1):
#     n_1=n_1.casefold()
#     list1 = ["Indian", "American"]
#     str1 = []
#     if n_1 in list1:
#         str1.append(n_1)
#     else:
#         str1.append("Enter valid nationality")
#     return str1[0]
#
# def get_salary(request, salary):
#     salary_list = []
#     if ((int(salary) > 10000) and (int(salary) < 90000)):
#         salary_list.append(salary)
#     else:
#         salary_list.append("Salary from 11,000 to 89,000")
#     return salary_list[0]
#
# def get_state(request, state_1):
#     states=['andhrapradhesh', 'arunachalpradesh', 'assam','bihar','chhattisgarh','karnataka',
#                 'madhyapradesh','odisha','tamilnadu','telangana','westbengal']
#     state_1=state_1.replace(' ','')
#     state_1=state_1.casefold()
#     state_data = []
#     if state_1 in states:
#         state_data.append(state_1)
#     state_data.append("State not present")
#     return state_data[0]
#
# def fivevalid(request, days):
#     if days > 5:
#         return "Eligible"
#     return "Last request were must be greater than 5 days"
#
# def get_city(request, city):
#     city = city.lower()
#     city = city.capitalize()
#     return city
#
# def get_pin(request, pin):
#     return pin
#
# def get_qualification(request, qualification):
#     return qualification
#
# def pan_number(request, pan_number):
#     return pan_number
#
# def validate_date(request, birth, gender):
#     gender_list = []
#     birth_type = isinstance(birth, int)
#     if birth_type:
#         dob = birth
#         gender_data = gender
#         if ((gender_data == 'Male' and dob > 21) or
#                 (gender_data == 'Female' and dob > 18)):
#             gender_list.append("Success")
#         else:
#             gender_list.append("Invalid Input for DOB")
#     gender_list.append("Format should be %Y-%m-%d")
#     return gender_list[0]
#
# def validate_pan(request, pan_num):
#     dates = []
#     validate_result = []
#     for p in request_info.objects.raw('SELECT id,pan,request_date FROM request_info'):
#         if pan_num == p.pan:
#             str1 = ''.join(str(p.request_date))
#             str1 = str1.split()
#             dates.append(str1)
#     if len(dates) > 0:
#         dates.reverse()
#         date_formate = '%Y-%m-%d'
#         get_date = date.today()
#         d1_data = get_date.strftime(date_formate)
#         print(d1_data)
#         a_data = datetime.strptime(d1_data, date_formate)
#         b_data = datetime.strptime(dates[0][0], date_formate)
#         delta = a_data - b_data
#         delta = abs(delta)
#
#         validate_result.append("Activity in last five days") \
#             if delta.days <= 5 else validate_result.append("Validate Success")
#
#         print(validate_result)
#     else:
#         validate_result.append("New User")
#     return validate_result[0]
#
# def validate_all_data(birth, date_validate, pan_activity, state, salary, nation):
#     count_validate = 0
#     json_data = json.loads(python_string)
#     if birth != "Format should be %Y-%m-%d":
#         count_validate += 1
#     else:
#         return json_data['InvalidResponse'], json_data['DReason']
#
#     if date_validate == "Success" or date_validate == 'Format should be %Y-%m-%d':
#         count_validate += 1
#     else:
#         return json_data['AResponse'], json_data['AReason']
#
#     if pan_activity == "Validate Success" or pan_activity == "New User":
#         count_validate += 1
#     else:
#         return json_data['AResponse'], json_data['PanReason']
#
#     if state != "State not present":
#         count_validate += 1
#     else:
#         return json_data['AResponse'], json_data['StateError']
#
#     if salary != "Salary from 10,001 to 89,999":
#         count_validate += 1
#     else:
#         return json_data['AResponse'], json_data['Salary']
#
#     if nation != "Enter valid nationality":
#         count_validate += 1
#     else:
#         return json_data['AResponse'], json_data['Nation']
#
#     return count_validate, "Success"