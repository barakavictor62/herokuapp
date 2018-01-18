from PIL import Image
import StringIO
from django import forms
from django.core.files import File
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm, PasswordResetForm, PasswordChangeForm
from django.contrib.auth.models import User
from popeye.models import Profile, ContentWriting, WebsiteBuilding, AnonContentWriting, AnonWebsiteBuilding


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder':'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder': 'Password'

    }))

class EmailForm(forms.Form):
    email_address = forms.CharField(widget=forms.EmailInput(attrs={
    'class': 'form-control',
    'placeholder': 'your email address'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
    'rows': 10,
    'class': 'form-control'
    }))


class SignupForm(UserCreationForm):
    first_name = forms.CharField(label='First name',widget=forms.TextInput(attrs={
        'class': 'form-control',
        'autofocus': ''
    }))
    last_name = forms.CharField(label='Last name',widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
    }))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

class ProfileInfo (forms.ModelForm):
    country = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': '4'
    }))
    
    class Meta:
        model = Profile
        fields = ('country','bio','profile_picture')

    def save(self):
        photo = super(ProfileInfo, self).save()

        country = self.cleaned_data.get('country')
        bio = self.cleaned_data.get('bio')
        image_field = self.cleaned_data.get('profile_picture')
        image_file = StringIO.StringIO(image_field.read())
        image = Image.open(image_file)
       
        resized_image = image.thumbnail((200, 200), Image.ANTIALIAS)
        image_file = StringIO.StringIO()
        resized_image.save(image_file)

        return photo


class resetForm(PasswordResetForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'you@domain.com'
    }))


class PasswordChange(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    new_password1 = forms.CharField(label='New password', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    new_password2 = forms.CharField(label='Confirm new password', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))


class UserChange(forms.ModelForm):
    first_name = forms.CharField(label='First name', widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    last_name = forms.CharField(label='Last name', widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


Topic_choices = (
    ('Arts and Entertainment', 'Arts and Entertainment'),
    ('Technology and Science', 'Technology and Science'),
    ('Education', 'Education'),
    ('Politics', 'Politics'),
    ('Health and Fitness', 'Health and Fitness')
)
word_count = (
    ('150', '150'),
    ('300', '300'),
    ('500', '500'),
    ('700', '700'),
    ('1000','1000'),
    ('1500', '1500'),
    ('2000', '2000')
              )


class ContentRequestForm(forms.ModelForm):
    topic = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'form-control'
    }), choices=Topic_choices)
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    keywords = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 2,

    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 4
    }))
    word_count = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'form-control'
    }), choices=word_count)
    article_cost = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = ContentWriting
        fields = ('topic','title','keywords','description','word_count','article_cost',)

class AnonContentRequestForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder':'Your email address' 
    }))
    topic = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'form-control'
    }), choices=Topic_choices)
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    keywords = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 2,

    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 4
    }))
    word_count = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'form-control'
    }), choices=word_count)
    article_cost = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = AnonContentWriting
        fields = ('email','topic','title','keywords','description','word_count','article_cost',)


class WebsiteRequestForm(forms.ModelForm):
    company = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    category = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    navigation_contents = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': '4'

    }))
    website_cost = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    additional_instructions = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': '4'

    }))

    class Meta:
        model = WebsiteBuilding
        fields = ('company','category','title','navigation_contents','website_cost','additional_instructions')

class AnonWebsiteRequestForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder':'Your email address' 
    }))
    company = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    category = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    navigation_contents = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': '4'

    }))
    website_cost = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    additional_instructions = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': '4'

    }))

    class Meta:
        model = AnonWebsiteBuilding
        fields = ('email','company','category','title','navigation_contents','website_cost','additional_instructions')

class CheckOutForm(forms.Form):
    #Client_Token = forms.CharField(label='', widget=forms.TextInput(attrs={
    #    'type':'hidden'
    #}))
    Amount = forms.IntegerField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    """Payment_Method_Nonce = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))"""