
from django import forms
from .models import PollOption

class PollResponseForm(forms.Form):
    option = forms.ModelChoiceField(queryset=PollOption.objects.none(), widget=forms.RadioSelect, empty_label=None)

    def __init__(self, *args, **kwargs):
        poll_id = kwargs.pop('poll_id', None)
        super().__init__(*args, **kwargs)
        if poll_id is not None:
            self.fields['option'].queryset = PollOption.objects.filter(poll_id=poll_id)
