from PIL import Image
from io import StringIO
from django.shortcuts import render, redirect
from django.http import HttpResponse
from popeye.forms import SignupForm, CheckOutForm, AnonContentRequestForm, ContentRequestForm, EmailForm, AnonWebsiteRequestForm, WebsiteRequestForm, ProfileInfo,PasswordChange, UserChange, resetForm
from .models import Profile, User, ContentWriting, WebsiteBuilding
from django.contrib.auth.decorators import login_required
from django.conf import settings
from decimal import Decimal
import re
import braintree


# Create your views here.

def home(request):
    return render(request, "home.html", {})

@login_required(login_url='/login')
def myprofile(request):
    my_articles = ContentWriting.objects.filter(user_id=request.user.id)
    my_web_requests = WebsiteBuilding.objects.filter(user_id=request.user.id)
    return render(request, "myprofile.html", {"my_articles":my_articles, "my_web_requests":my_web_requests})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/login')
        else:
            return render(request, "signup.html",{'form': form})
    else:
        form = SignupForm()
        return render(request, "signup.html",{'form': form})

@login_required(login_url='/login')
def edit_profile(request):
    if request.method == 'POST':
        profile = UserChange(request.POST, instance=request.user)
        extra = ProfileInfo(request.POST, request.FILES, instance=request.user.profile)
        if profile.is_valid() and extra.is_valid():
            imgfile = request.FILES['profile_picture']
            img =  StringIO(imgfile.read())
            profpic = Image.open(img)
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



@login_required(login_url='/login')
def mywallet(request):
    me_articles = ContentWriting.objects.filter(user_id=request.user.id, is_done=0)
    me_web_requests = WebsiteBuilding.objects.filter(user_id=request.user.id, is_done=0)
    sum = 0
    for cost in me_articles:
        cost=(re.sub('[$]', '',cost.article_cost))
        sum += float(cost)
    for web_cost in me_web_requests:
        web_cost=(re.sub('[$]', '',web_cost.website_cost))
        sum += float(web_cost)
    balance = float(Decimal(request.user.profile.Balance) - Decimal(sum))
    braintree.Configuration.configure(
        braintree.Environment.Sandbox,
        merchant_id=settings.BRAINTREE_MERCHANT_ID,
        public_key=settings.BRAINTREE_PUBLIC_KEY,
        private_key=settings.BRAINTREE_PRIVATE_KEY
        )
    if request.method== 'POST' and request.POST.get("payment_method_nonce"):
        add_amount = CheckOutForm(request.POST)
        if add_amount.is_valid():
            nonce_from_the_client =  request.POST.get("payment_method_nonce")
            result = braintree.Transaction.sale({
               "amount": add_amount.cleaned_data['Amount'],
               "payment_method_nonce": nonce_from_the_client,
               "options": {
                   "submit_for_settlement": True
                   }
                })
            if result.is_success:
                return redirect('/mywallet')
            else:
                return render(request, 'checkout_error.html', {})
        else:
            return render(request, 'checkout_error.html', {})
    else:
        client_token = braintree.ClientToken.generate()
        add_amount = CheckOutForm(initial={"Client_Token":client_token})
        return render(request, "mywallet.html", {"client_token":client_token, "me_articles":me_articles, "sum_total":sum,"balance": balance, "add_amount": add_amount})

def pricing(request):
    return render(request, "pricing.html", {})

@login_required(login_url='/login')
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
    if request.user.is_authenticated:
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
    else:
        if request.method == 'POST':
            form = AnonContentRequestForm(request.POST)
            if form.is_valid():
                writing.save()
                return redirect('/articles')
            else:
                return render(request, "articles.html", {'form': form})
        else:
            form = AnonContentRequestForm()
            return render(request, 'articles.html', {"form": form})
        
def web(request):
    if request.user.is_authenticated:
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
    else:
        if request.method == 'POST':
            form = AnonWebsiteRequestForm(request.POST)
            if form.is_valid():
                web.save()
                return redirect('/web')
            else:
                return render(request, "web.html", {'form': form})
        else:
            form = AnonWebsiteRequestForm()
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

@login_required(login_url='/login')
def edit_request(request):
    return render(request, "edit_request.html", {})

def articles_request(request):
    return render(request, "article_request.html", {})
