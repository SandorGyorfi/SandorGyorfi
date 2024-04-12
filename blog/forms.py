from django import forms

class BlogPostVoteForm(forms.Form):
    VOTE_CHOICES = (
        ('needs_work', 'Needs Work'),
        ('meh', 'Meh'),
        ('interesting', 'Interesting'),
        ('game_changer', 'Game Changer'),
    )
    vote = forms.ChoiceField(choices=VOTE_CHOICES, widget=forms.RadioSelect)

