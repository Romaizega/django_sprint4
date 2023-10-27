from django import forms

from blog.models import Comment, Post, User


class CommentEditForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)


class PostEditForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ('author',)
        widgets = {
            'text': forms.Textarea(),
            'comment': forms.Textarea(),
            'pub_date': forms.DateInput(attrs={'type': 'date'}),
        }


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'
