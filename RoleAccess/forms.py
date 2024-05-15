from django import forms
from django.contrib.auth.models import Group, User


class AssignGroupForm(forms.Form):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), label='Roles',
                                   widget=forms.Select(attrs={'class': 'form-select'}))
    users = forms.ModelMultipleChoiceField(queryset=User.objects.all(),
                                           widget=forms.SelectMultiple(attrs={'class': 'form-select'}))

    def save(self):
        # breakpoint()
        group = self.cleaned_data['group']
        users = self.cleaned_data['users']
        for user in users:
            user.groups.add(group)
        return users
