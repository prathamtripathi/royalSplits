from django import forms
from .models import Comment,JobApplication
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget



PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal')
)
 
COLOR_CHOICE = (
    ('RED','RED'),
    ('YELLOW','YELLOW'),
    ('GREEN','GREEN')


)

class CommentForm(forms.Form):
    your_name =forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    comment_text =forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
 
    def __str__(self):
        return f"{self.comment_text} by {self.your_name}"


class JobForm(forms.Form):
    full_name = forms.CharField(max_length=225,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=225,widget=forms.TextInput(attrs={'class':'form-control'}))
    reason = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    resume = forms.FileField(required=False)


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Promo code',
        'aria-label': 'Recipient\'s username',
        'aria-describedby': 'basic-addon2'
    }))


class CheckoutForm(forms.Form):
    name=forms.CharField(max_length=225,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=225,widget=forms.TextInput(attrs={'class':'form-control'}))
    address= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    state=forms.CharField(max_length=225,widget=forms.TextInput(attrs={'class':'form-control'}))
    zip_code = forms.CharField(max_length=225,widget=forms.TextInput(attrs={'class':'form-control'})) 
    payment_option = forms.ChoiceField(widget=forms.RadioSelect(),choices = PAYMENT_CHOICES)

class ColorForm(forms.Form):
    color = forms.ChoiceField(choices=COLOR_CHOICE)
    


class ProfileForm(forms.Form):
    fname = forms.CharField(max_length=225,widget=forms.TextInput(attrs={
        'class':'form-control mb-3',
        'placeholder':'First Name'
        }))
    lname = forms.CharField(max_length=225,widget=forms.TextInput(attrs={
        'class':'form-control mb-3',
        'placeholder':'Last Name'
        }))
    location = forms.CharField(max_length=225,widget=forms.TextInput(attrs={
        'class':'form-control mb-3',
        'placeholder':'location'
        }))
    website = forms.CharField(max_length=225,widget=forms.TextInput(attrs={
        'class':'form-control mb-3',
        'placeholder':'website',
        
        }))
    bio = forms.CharField(max_length=225,widget=forms.TextInput(attrs={
        'class':'form-control mb-3',
        'placeholder':"Bio"
        }))
    def __init__(self):
        super(ProfileForm, self).__init__()