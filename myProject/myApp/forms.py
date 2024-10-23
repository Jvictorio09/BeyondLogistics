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
            ('First Birthday', 'First Birthday'),
            ('Baptism', 'Baptism'),
            ('Christening', 'Christening'),
            ('Corporate', 'Corporate'),
            ('Others', 'Others'),
        ],
        widget=forms.Select(attrs={
            'class': 'form-control select-event'
        }),
        label='Event Type',
        required=True
    )

    celebrant_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control input-text',
            'placeholder': 'Celebrant’s Complete Name'
        }),
        label='Celebrant’s Complete Name',
        required=True,
        max_length=100
    )

    event_address = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control input-text',
            'placeholder': 'Event Address'
        }),
        label='Event Address',
        required=True,
        max_length=255
    )

    invite_time = forms.TimeField(
        widget=forms.TextInput(attrs={
            'type': 'time',
            'class': 'form-control input-text',
            'placeholder': 'Invite Time'
        }),
        label='Invite Time',
        required=True
    )

    client_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control input-text',
            'placeholder': 'Client’s Name'
        }),
        label='Client’s Name',
        required=True,
        max_length=100
    )

    relationship = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control input-text',
            'placeholder': 'Relationship to the Celebrant'
        }),
        label='Relationship to the Celebrant',
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
