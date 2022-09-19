from django import forms
from .models import UserReservation, UserMessage


class UserReservationForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'name': 'name',
            'class': 'form-control',
            'id': 'name',
            'placeholder': 'Your Name',
            'data - rule': 'minlen:4',
            'data - msg': 'Please enter at least 4 chars'

        })
    )
    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control',
            'name': 'phone',
            'id': 'phone',
            'placeholder': 'Phone number in format xxx xxx xxxx',
            'data-rule': 'minlen:10',
            'data-msg': 'Phone number in format xxx xxx xxxx',
            'pattern': '^(\d{3}[- .]?){2}\d{4}$'
        })
    )

    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            'type': 'email',
            'class': 'form-control',
            'name': 'email',
            'id': 'email',
            'placeholder': 'Your Email',
            'data-rule': 'email',
            'data-msg': 'Please enter a valid email'
        })
    )

    persons = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'type': 'number',
            'class': 'form-control',
            'name': 'people',
            'id': 'people',
            'placeholder': '# of people',
            'data-rule': 'minlen:1',
            'data-msg': 'Please enter at least 1 chars'
        })
    )

    req_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'id': 'date',
            'placeholder': 'Date',
            'data - rule': 'minlen:4',
            'data - msg =': 'Please enter required date'
        })
    )

    req_time = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'type': 'time',
            'class': 'form-control',
            'name': 'time',
            'id': 'time',
            'placeholder': 'Time',
            'data - rule': 'minlen:4',
            'data - msg': 'Please enter required time'
        })
    )

    message = forms.CharField(
        max_length=300,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'name': 'message',
            'rows': '5',
            'placeholder': 'Message',
        })
    )

    class Meta:
        model = UserReservation
        fields = ('name', 'phone', 'email', 'persons', 'req_date', 'req_time', 'message')


class UserMessageForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'name': 'name',
            'class': 'form-control',
            'id': 'name',
            'placeholder': 'Your Name'
        })
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            'type': 'email',
            'class': 'form-control',
            'name': 'email',
            'id': 'email',
            'placeholder': 'Your Email'
        })
    )
    subject = forms.CharField(
        max_length=300,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control',
            'name': 'subject',
            'id': 'subject',
            'placeholder': 'subject'
        })
    )
    message = forms.CharField(
        max_length=1500,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'name': 'message',
            'rows': '5',
            'placeholder': 'Message'
        })
    )

    class Meta:
        model = UserMessage
        fields = ('name', 'email', 'subject', 'message')