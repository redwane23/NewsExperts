from django.shortcuts import render,redirect
from home.models import Profile
from .models import TaskList,Task,CountryList
from .forms import AlterProfileInformationForm,RegisterForm,LoginForm
from django.db.models import Case,When
from django.contrib.auth import login,authenticate
from django.views import View
from django.contrib.auth.decorators import login_required


@login_required
def ProfileView(request):
    user=request.user
    profile=Profile.objects.get(User=user)
    task_list=TaskList.objects.get(owner=user)
    countrylist=CountryList.objects.get(owner=user)
    tasks=Task.objects.filter(list=task_list).annotate(
        preiority_order=Case(
            When(Preiorety='H', then=1),
            When(Preiorety='M', then=2),
            When(Preiorety='L', then=3)
        )
    ).order_by("preiority_order")
    city=[profile.City.name,profile.City.latitude,profile.City.longitude]
    context={                
        'user':user,
        'profile':profile,
        'tasks':tasks,
        'task_list':task_list,
        'countrylist':countrylist,
        'city':city,
    }
    return render(request,"Profile/profile.html",context)

@login_required
def AlterInforamtino(request):
    user=request.user
    profile=Profile.objects.get(User=user)
    if request.method == 'POST':
        form=AlterProfileInformationForm(request.POST,instance=profile)
        if form.is_valid():
            print("valid")
            form.save()
            return redirect('profile')
        else: 
            print('not valid')
            return redirect('alter')
    else:
        form=AlterProfileInformationForm(instance=profile)
        return render(request,'Profile/AlterProfile.html',{'from':form})


class registerview(View):
    def get(self,request):
        form=RegisterForm()
        return render(request,'Profile/register.html',{'form':form})
    def post(self,request):
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request,user)
            return redirect("/profile")
        return render(request,'Profile/register.html',{'form':form})
        
class loginview(View):
    def get(self,request):
        form=LoginForm()
        return render(request,'Profile/login.html',{'form':form})
    def post(self,request):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect("/profile")
        return render(request,'Profile/login.html',{'form':form})

