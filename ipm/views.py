from django.shortcuts import render
from ipm import models
from django.shortcuts import HttpResponse

user_list = models.User.objects.all()


# Create your views here.
def index(request):
    # return HttpResponse("Hello world!")
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        # print(username,password)
        # temp = {"user": username, "pwd": password}
        models.User.objects.create(name=username, password=password)
        # user_list.append(temp)
        global user_list
        user_list = models.User.objects.all()
    return render(request, "index.html", {"data": user_list})


def pj(request):
    pj_list = models.ProjectInfo.objects.all()
    return render(request, "pj.html", {"pj_list": pj_list})
    # return HttpResponse("PROJECT INFO")
