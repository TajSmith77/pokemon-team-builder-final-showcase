from django import forms
from .models import *

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name',
            'pokemon1','ability1','move1_1','move1_2','move1_3','move1_4',
            'pokemon2','ability2','move2_1','move2_2','move2_3','move2_4',
            'pokemon3','ability3','move3_1','move3_2','move3_3','move3_4',
            'pokemon4','ability4','move4_1','move4_2','move4_3','move4_4',
            'pokemon5','ability5','move5_1','move5_2','move5_3','move5_4',
            'pokemon6','ability6','move6_1','move6_2','move6_3','move6_4',]

        
            
    
