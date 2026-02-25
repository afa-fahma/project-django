from django import forms
from .models import book
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class BookForm(forms.ModelForm):
    class Meta:
        model=book
        fields=['title','author','price','pub_date','description','cover_image']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control title-input'}),
            'author':forms.TextInput(attrs={'class':'form-control author-input'}),
            'price':forms.NumberInput(attrs={'class':'form-control price-input'}),
            'pub_date':forms.DateInput(attrs={'class':'form-control pub_date-input'}),
            'description':forms.Textarea(attrs={'class':'form-control description-input'}),
            
            

        }

class userRegistrationform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
            

    
        
        

    

    



