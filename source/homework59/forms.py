from django import forms

from homework59.models import Issue, Type


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('summary', 'description', 'status', 'type')
        labels = {
            'summary': 'Краткое описание',
            'description': 'Полное описание',
            'status': 'Статус',
            'type': 'Тип'
        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label='Search')