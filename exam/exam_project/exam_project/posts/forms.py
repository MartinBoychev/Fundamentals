from django import forms

from exam.exam_project.posts import Post


class BaseClassPostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ('author', )


class CreatePostForm(BaseClassPostForm):
    class Meta:
        model = Post
        exclude = ('author', )

        error_messages = {
            'title': {
                'unique': "Oops! That title is already taken. How about something fresh and fun?",
            }
        }
        help_texts = {
            'image_url': "Share your funniest furry photo URL!"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['placeholder'] = 'Put an attractive and unique title...'
        self.fields['content'].widget.attrs['placeholder'] = 'Share some interesting facts about your adorable pets...'


class EditPostForm(BaseClassPostForm):
    pass


class DeletePostForm(BaseClassPostForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'