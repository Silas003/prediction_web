from django import forms
from .models import Fixture

class YourForm(forms.Form):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

class FixtureForm(forms.ModelForm):
    class Meta:
        model=Fixture
        fields='__all__'