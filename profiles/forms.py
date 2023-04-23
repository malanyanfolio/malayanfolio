from django import forms

from profiles.models import *


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            "fname",
            "lname",
            "strand",
            "pronouns",
            "pfp",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["fname"].required = True
        self.fields["lname"].required = True
        self.fields["strand"].required = True
        self.fields["pronouns"].required = True
        self.fields["pfp"].required = True

class ExtraCurriForm(forms.ModelForm):
    class Meta:
        model = Clubs
        fields = (
            "user_club",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user_club"].required = True

class InterestForm(forms.ModelForm):
    class Meta:
        model = Interests
        fields = (
            "user_interest",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user_interest"].required = True
        


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Languages
        fields = (
            "lang_proficiency",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["lang_proficiency"].required = True