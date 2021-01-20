from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields[
            'username'].help_text = '<div class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></div>'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].help_text = '<div class="form-text text-muted">' \
                                             '<small>' \
                                             '<ul>' \
                                             '<li>Your password can’t be too similar to your other personal information.</li>' \
                                             '<li>Your password must contain at least 8 characters.</li>' \
                                             '<li>Your password can’t be a commonly used password.</li>' \
                                             '<li>Your password can’t be entirely numeric.</li>' \
                                             '</ul>' \
                                             '</small>' \
                                             '</div>'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].help_text = '<div class="form-text text-muted">' \
                                             '<small>Enter the same password as before, for verification.</small>' \
                                             '</div>'
