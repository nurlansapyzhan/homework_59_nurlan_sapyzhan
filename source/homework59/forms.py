from django import forms

from homework59.models import Issue, Type, Project


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


class ProjectForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.widgets.DateInput(
        attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'})
    )
    end_date = forms.DateField(widget=forms.widgets.DateInput(
        attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'})
    )

    class Meta:
        model = Project
        fields = ('name', 'description', 'start_date', 'end_date')
        labels = {
            'start_date': 'Дата начала',
            'end_date': 'Дата окончания',
            'name': 'Название проекта',
            'description': 'Описание проекта'
        }


# class IssueProjectForm(forms.Form):
#     class Meta:
#         model = Issue
#         fields = ('summary', 'description', 'status', 'type', 'project')
#         labels = {
#             'summary': 'Краткое описание',
#             'description': 'Полное описание',
#             'status': 'Статус',
#             'type': 'Тип',
#         }
#         widgets = {
#             'project': forms.TextInput(attrs={'disabled': True})
#         }
class IssueProjectForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('summary', 'description', 'status', 'type')
        labels = {
            'summary': 'Краткое описание',
            'description': 'Полное описание',
            'status': 'Статус',
            'type': 'Тип',
        }
        # widgets = {
        #     'project': forms.TextInput(attrs={'disabled': True})
        # }
