from django.contrib.auth.forms import UserCreationForm, ValidationError
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()

    def clean_username(self):
        """Reject usernames that differ only in case."""
        username = self.cleaned_data.get("username")
        UserModel = get_user_model()
        if username and UserModel.objects.filter(username__iexact=username).exists():
            raise ValidationError(self.error_messages["unique"], code="unique")
        else:
            return username
