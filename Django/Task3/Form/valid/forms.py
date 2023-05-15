from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["username", "gender", "text"]

    def clean(self):
        super(PostForm, self).clean()
        username = self.cleaned_data.get('username')
        text = self.cleaned_data.get('text')
        if len(username) < 5:
            self._errors['username'] = self.error_class(['Minimum 5 Characters Required'])
        if len(text) < 10:
            self._errors['text'] = self.error_class(['Post Should Contain a Minimum of 10 Characters'])
        return self.cleaned_data
