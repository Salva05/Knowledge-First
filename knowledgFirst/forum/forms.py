from django import forms

class CategoryChoices(forms.Form):
    CATEGORY_CHOICES = [
    ('Sport', 'Sport'),
    ('Nature', 'Nature'),
    ('Food', 'Food'),
    ('Fashion', 'Fashion'),
    ('Animals', 'Animals'),
    ('Technology', 'Technology'),
    ('Science', 'Science'),
    ('Culture', 'Culture'),
    ('Music', 'Music'),
    ('Entertainment', 'Entertainment'),
    ('History', 'History'),
    ('Fiction', 'Fiction'),
    ('Art', 'Art'),
    ('Other', 'Other')
]
    my_field = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.RadioSelect)