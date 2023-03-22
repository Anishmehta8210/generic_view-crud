from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.views.generic import ListView,CreateView,DeleteView,UpdateView,FormView,View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
class TeacherView(ListView):
    model = Teacher

class TeacherFormView(CreateView):
    template_name="./insert.html"
    model = Teacher
    fields = "__all__"
    success_url = "/"

class TeacherDeleteView(DeleteView):
    template_name="./delete.html"
    model = Teacher
    success_url = "/"

class TeacherEditView(UpdateView):
    model = Teacher
    fields = "__all__"
    success_url = "/"
    template_name = "./insert.html"

class LoginView(FormView):
    template_name = "login.html"
    form_class = AuthenticationForm
    success_url = "/"

    def post(self,r):
        username = r.POST.get("username")
        password = r.POST.get("password")

        user = authenticate(username=username,password=password)

        if user is not None:
            if user.is_active:
                login(r,user)
                return redirect("home")
            else:
                return HttpResponse("Inactive user")

        else:
            return HttpResponse("invalid username or password")

class LogoutView(View):
    def get(self,r):
        logout(r)
        return redirect("home")





