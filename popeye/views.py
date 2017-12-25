from django.shortcuts import render, redirect
from django.http import HttpResponse
from popeye.forms import SignupForm, ContentRequestForm,EmailForm, WebsiteRequestForm, ProfileInfo,PasswordChange, UserChange, resetForm
from .models import Profile, User, ContentWriting, WebsiteBuilding
import re


# Create your views here.

def home(request):
    return render(request, "home.html", {})

def myprofile(request):
    my_articles = ContentWriting.objects.filter(user_id=request.user.id)
    my_web_requests = WebsiteBuilding.objects.filter(user_id=request.user.id)
    return render(request, "myprofile.html", {"my_articles":my_articles, "my_web_requests":my_web_requests})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            return render(request, "signup.html",{'form': form})
    else:
        form = SignupForm()
        return render(request, "signup.html",{'form': form})

def edit_profile(request):
    if request.method == 'POST':
        profile = UserChange(request.POST, instance=request.user)
        extra = ProfileInfo(request.POST, request.FILES, instance=request.user.profile)
        if profile.is_valid() and extra.is_valid():
            profile.save()
            extra.save()
            return redirect('/edit_profile')
        else:
            return render(request, "edit_profile.html", {'form': profile, 'form2': extra})
    else:
        profile = UserChange(instance=request.user)
        extra = ProfileInfo(instance=request.user.profile)
        return render(request, "edit_profile.html",
                      {'form': profile,
                       'form2': extra})

def mywallet(request):
    me_articles = ContentWriting.objects.filter(user_id=request.user.id)
    sum = 0
    for cost in me_articles:
        cost=(re.sub('[$]', '',cost.article_cost))
        """sum += cost"""
    return render(request, "mywallet.html", {"me_articles":me_articles})

def pricing(request):
    return render(request, "pricing.html", {})

def passwordchange(request):
    if request.method == 'POST':
        password_change = PasswordChange(request.POST)
        if password_change.is_valid():
            password_change.save()
            return redirect('/myprofile')
        else:
            return render(request, "passwordchange.html",{'form': password_change })
    else:
        password_change = PasswordChange()
        return render(request, 'passwordchange.html',{'form': password_change })

def articles(request):
    if request.method == 'POST':
        form = ContentRequestForm(request.POST)
        if form.is_valid():
            writing = form.save(commit=False)
            writing.user_id = request.user.id
            writing.save()
            return redirect('/articles')
        else:
            return render(request, "articles.html", {'form': form})
    else:
        form = ContentRequestForm()
        return render(request, 'articles.html', {"form": form})

def web(request):
    if request.method == 'POST':
        form = WebsiteRequestForm(request.POST)
        if form.is_valid():
            web = form.save(commit=False)
            web.user_id = request.user.id
            web.save()
            return redirect('/web')
        else:
            return render(request, "web.html", {'form': form})
    else:
        form = WebsiteRequestForm()
        return render(request, "web.html", {"form": form})

def contact(request):
    if request.method == 'POST':
        email_form = EmailForm(request.POST)
        if email_form.is_valid():
            send_mail(
            'Subject',
            email_form.cleaned_data['message'],
            email_form.cleaned_data['email_address'],
            ['oyugavictor44@gmail.com'],
            fail_silently=False,
            )
            return redirect('/contact')
        else:
            return render(request, "contact.html", {'email_form': email_form})
    else:
        email_form = EmailForm()
        return render(request, 'contact.html', {"email_form": email_form})


def edit_request(request):
    return render(request, "edit_request.html", {})

def articles_request(request):
    return render(request, "article_request.html", {})
