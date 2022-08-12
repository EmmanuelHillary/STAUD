from django import forms
from .models import Comments
from mptt.forms import TreeNodeChoiceField


class CommentForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=Comments.objects.all())
    content = forms.CharField(label="", max_length=1000, widget=forms.Textarea(attrs={'placeholder': 'Any Comments?', 'style': 'width: 100%'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['parent'].required = False
        self.fields['name'].required = True

        self.fields['name'].widget.attrs['style'] = "margin-bottom: 5px; width: 200px;"

    class Meta:
        model = Comments
        fields = ['name', 'parent', 'content']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
        }