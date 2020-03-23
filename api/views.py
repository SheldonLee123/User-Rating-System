from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import user, professor, module, user_rating, relation
import numpy as np

def register(request):
    try:
        if request.method == 'GET' and request.GET:
            username = request.GET.get("username")
            email = request.GET.get("email")
            pwd = request.GET.get("password")
            new_user = user.objects.create(username=username, emailAddress=email, password=pwd)
            return HttpResponse("Register success!")
    except Exception as e:
        return  HttpResponse("Input error, please try it again!")

def login(request):
    try:
        if request.method == 'GET' and request.GET:
            username = request.GET.get("username")
            pwd = request.GET.get("password")
            new_user = user.objects.filter(username=username, password=pwd).first()
            if new_user:
                request.session["is_login"] = "True"
                return HttpResponse("Login success!")
            else:
                return HttpResponse("Username or password is incorrect!")
        else:
            return HttpResponse("please login first!")
    except Exception as e:
        return HttpResponse("Input error, please try it again!")

def logout(request):
    return HttpResponse("Logout success!")

def require_login(func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get("is_login", None):
            return redirect("/login/")
        return func(request, *args, **kwargs)
    return wrapper

@require_login
def list(request):
    try:
        modules = module.objects.all()
        response = {}
        list = []
        for mod in modules:
            item = {}
            item['code'] = mod.code
            item['name'] = mod.name
            item['year'] = mod.year
            item['semester'] = mod.semester
            relations = relation.objects.filter(mod=mod)
            pros = []
            for rela in relations:
                pros.append(rela.pro.pro_id+", "+rela.pro.name)
            item['taught'] = pros
            list.append(item)
        for i in range(len(list)):
            response[i] = list[i]
        return JsonResponse(response)
    except Exception as e:
        return HttpResponse("Input error, please try it again!")

@require_login
def view(request):
    try:
        response = {}
        pros = professor.objects.all()
        for pro in pros:
            rating = []
            relations = relation.objects.filter(pro=pro)
            for rela in relations:
                rates = user_rating.objects.filter(relation=rela)
                for rate in rates:
                    rating.append(rate.rate)
            response[pro.name] = int(np.mean(rating))
        return JsonResponse(response)
    except Exception as e:
        return HttpResponse("Input error, please try it again!")

@require_login
def average(request):
    try:
        if request.method == 'GET' and request.GET:
            pro_id = request.GET.get("professor_id")
            code = request.GET.get("module_code")
            pro = professor.objects.filter(pro_id=pro_id).first()
            mod = module.objects.filter(code=code).first()
            rela = relation.objects.filter(pro=pro, mod=mod).first()
            rates = user_rating.objects.filter(relation=rela)
            rating = []
            for rate in rates:
                rating.append(rate.rate)
            return HttpResponse(int(np.mean(rating)))
    except Exception as e:
        return HttpResponse("Input error, please try it again!")

@require_login
def rate(request):
    try:
        if request.method == 'GET' and request.GET:
            pro_id = request.GET.get("professor_id")
            code = request.GET.get("module_code")
            year = request.GET.get("year")
            semester = request.GET.get("semester")
            rating = request.GET.get("rating")
            mod = module.objects.filter(code=code,year=year,semester=semester).first()
            pro = professor.objects.filter(pro_id=pro_id).first()
            rela = relation.objects.filter(pro=pro,mod=mod).first()
            new_rate = user_rating.objects.create(relation=rela,rate=rating)
            return HttpResponse("rate success!")
    except Exception as e:
        return HttpResponse("Input error, please try it again!")