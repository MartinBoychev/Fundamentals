from django import forms

from exam.exam_project.author.models import Author


class CreateProfileForm(forms.ModelForm):

    class Meta:
        model = Author

        exclude = ('info', 'image_url')
        widgets = {
            'passcode': forms.PasswordInput(),
        }

        help_texts = {
            'passcode': "Your passcode must be a combination of 6 digits",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter your first name...'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter your last name...'
        self.fields['pets_number'].widget.attrs['placeholder'] = 'Enter the number of your pets...'
        self.fields['passcode'].widget.attrs['placeholder'] = 'Enter 6 digits...'


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Author
        exclude = ('passcode', )


class DeleteProfileForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ()