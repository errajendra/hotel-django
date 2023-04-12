from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ('rating', 'review')
        
        widgets = {
            'rating': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Enter Nomber out of 5', 'min':1, 'max':5}),
            'review' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Write your message here'})
        }
    

    
