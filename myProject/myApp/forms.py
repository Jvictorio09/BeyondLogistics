from django import forms

class ReservationForm(forms.Form):
    event_date = forms.DateField(
        widget=forms.TextInput(attrs={
            'type': 'date',
            'class': 'form-control input-text',
            'placeholder': 'Date of Event'
        }),
        label='Event Date',
        required=True
    )
    
    event_type = forms.ChoiceField(
        choices=[
            ('', 'Select Type of Event:'),
            ('Wedding', 'Wedding'),
            ('Debut', 'Debut'),
            ('Birthday', 'Birthday'),
            ('Corporate', 'Corporate'),
            ('Others', 'Others'),
        ],
        widget=forms.Select(attrs={
            'class': 'form-control select-event'
        }),
        label='Event Type',
        required=True
    )
    
    client_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control input-text',
            'placeholder': 'Client’s Name'
        }),
        label='Client Name',
        required=True,
        max_length=100
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control input-text',
            'placeholder': 'Email Address'
        }),
        label='Email Address',
        required=True
    )
    
    contact_number = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control input-text',
            'placeholder': 'Contact Number'
        }),
        label='Contact Number',
        required=True,
        max_length=20
    )
    
    guests = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control input-text',
            'placeholder': 'Number of Guests'
        }),
        label='Number of Guests',
        required=True
    )
    
    venue = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control input-text',
            'placeholder': 'Venue (If no venue yet, let us know if it’s in Metro Manila or Tagaytay)'
        }),
        label='Venue',
        required=True,
        max_length=255
    )
