from django.shortcuts import render, redirect
from django.http import HttpResponse
from popeye.forms import SignupForm, ContentRequestForm,EmailForm, WebsiteRequestForm, ProfileInfo,PasswordChange, UserChange, resetForm

# Create your views here.

def home(request):
    return render(request, "home.html", {})

def myprofile(request):
    articles = ContentWriting.objects.filter(user_id=request.user.id, is_done=1)
    pending = ContentWriting.objects.filter(user_id=request.user.id, is_done=0)
    websites = WebsiteBuilding.objects.filter(user_id=request.user.id)
    return render(request, "myprofile.html", { 'articles': articles, 'pending': pending,'websites': websites})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        #country = ProfileInfo(request.POST)
        if form.is_valid():
            #data = form.cleaned_data
            form.save()
            return redirect('/login')
        else:
            return render(request, "signup.html",{'form': form})
    else:
        form = SignupForm()
        #country = ProfileInfo()
        return render(request, "signup.html",{'form': form})

def edit_profile(request):
    return render(request, "edit_profile.html", {})

def mywallet(request):
    return render(request, "mywallet.html", {})

def pricing(request):
    return render(request, "pricing.html", {})

def passwordchange(request):
    return render(request, "passwordchange.html", {})

def articles(request):
    return render(request, "articles.html", {})

def web(request):
    return render(request, "web.html", {})

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
