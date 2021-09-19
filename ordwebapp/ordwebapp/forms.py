"""forms to choose class of words"""
from django import forms

class WordForm(forms.Form):
    """Select type word form"""
    ALL = 'all'
    ADJECTIVES = 'adjective'
    NOUNS = 'noun'
    VERBS = 'verb'
    TYPE_OF_WORD = [
        (ALL, 'All'),
        (ADJECTIVES, 'Adjectives'),
        (NOUNS, 'Nouns'),
        (VERBS, 'Verbs'),
    ]

    ALL = "all"
    EASY = "low"
    MEDIUM = "medium"
    DIFFICULT = "high"
    DIFFICULTY = [
        (EASY, 'Easy'),
        (MEDIUM, 'Medium'),
        (DIFFICULT, 'Difficult'),
        (ALL, 'All')
    ]
    word_class = forms.ChoiceField(
        choices=TYPE_OF_WORD,
        widget=forms.Select(attrs={'class':'lv-select'})
        )
    level = forms.ChoiceField(
        choices=DIFFICULTY,
        widget=forms.Select(attrs={'class':'lv-select'})
        )
