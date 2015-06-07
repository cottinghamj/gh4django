from django import forms

class RentForm(forms.Form):
    file_name = forms.CharField(label='File to Rent', max_length=100)
    new_file_holder = forms.CharField(label='File Holder', max_length=100)


class ReturnForm(forms.Form):
    file_name = forms.CharField(label='File to Return', max_length=100)
    file_holder = forms.CharField(label='File Holder', max_length=100)

class AddForm(forms.Form):
    new_file_name = forms.CharField(label='New File', max_length=100)
    file_holder = forms.CharField(label='File Holder', max_length=100)
