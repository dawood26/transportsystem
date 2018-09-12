from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from transport import forms
from transport import models
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request,'Account Created for {}'.format(username))
            form.save()
            return redirect('accounts:list')
        else:
            context = {'form': form}
            return render(request, 'signup.html', context)
    else:
        form = forms.CustomUserCreationForm()
        context = {'form': form}
        return render(request, 'signup.html', context)
def list(request):
    data = models.CustomUser.objects.all()
    context = {"message":"Users List", "userlist":data}
    return render(request, 'registration/userlist.html', context)

def detail(request,id):
    user = get_object_or_404(models.CustomUser, pk=id)
    context={
        'userdata': user,
        'message':'Details for '+user.username +''
    }
    return render(request, 'registration/userdetail.html', context)
def edit(request,id):
    user = get_object_or_404(models.CustomUser, pk=id)
    #https://sixfeetup.com/blog/django-form-data-in-post
    #https://stackoverflow.com/questions/47842491/django-keyerror-password
    #https://stackoverflow.com/questions/3946036/how-do-i-update-an-instance-of-a-django-model-with-request-post-if-post-is-a-nes
    if request.method == 'POST':
        form = forms.CustomUserCreationForm(request.POST, instance=user)
        if form.is_valid():
            messages.success(request, 'User Successfully updated')
            form.save()
            return redirect('accounts:list')
        else:
            form = forms.CustomUserCreationForm(request.POST, instance=user)
            context = {'form': form}
            return render(request, 'registration/useredit.html', context)
    else:
        form = forms.CustomUserCreationForm(instance=user)
        context = {'form': form}
        return render(request, 'registration/useredit.html', context)

def homepage(request):
    #https://djangobook.com/authentication-web-requests/
    #https: // stackoverflow.com / questions / 12615154 / how - to - get - the - currently - logged - in -users - user - id - in -django
    context = { 'userdata' : request.user}
    return render(request, 'home.html',context)




