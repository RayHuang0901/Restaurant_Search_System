from django import forms

class Position(forms.Form):
    Name = forms.CharField(max_length=100 )
    Area = forms.CharField(max_length=100 )
    Road = forms.CharField(max_length=100 )
    Door_num = forms.CharField(max_length=100 )
    Floor = forms.CharField(max_length=100 )

class Prices(forms.Form):
    Name = forms.CharField(max_length=100 )
    Service_charge = forms.CharField(max_length=100 )
    min_charge = forms.CharField(max_length=100 )
    Avg_charge = forms.CharField(max_length=100 )
  
class Food_Type(forms.Form):
    Name = forms.CharField(max_length=100 )
    Type = forms.CharField(max_length=100 )
    Style = forms.CharField(max_length=100 )
    Veg = forms.CharField(max_length=100 )
  
class Infos(forms.Form):
    Name = forms.CharField(max_length=100 )
    START_Time = forms.TimeField()
    Close_Time = forms.TimeField()
    Menu = forms.CharField(max_length=100 )
    FB = forms.CharField(max_length=100 )
    Phone = forms.CharField(max_length=100 )

class Comment(forms.Form):
    Name = forms.CharField(max_length=100 )
    CP = forms.CharField(max_length=100 )
    Service = forms.CharField(max_length=100 )
    Delicious_level = forms.CharField(max_length=100 )
    Clean = forms.CharField(max_length=100 )