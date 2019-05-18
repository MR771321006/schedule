from django import forms 

class ScheduleForm(forms.Form):
    text = forms.CharField(max_length=40, 
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : '输入你想做的：', 'aria-label' : 'Schedule', 'aria-describedby' : 'add-btn'}))