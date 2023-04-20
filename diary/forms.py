from django import forms


class InquiryForms(forms.Form):
    name = forms.CharField(label="お名前", max_length=30)
    email = forms.EmailField(label="メールアドレス")
    title = forms.CharField(label="タイトル", max_length=30)
    message = forms.CharField(label="メッセージ", widget=forms.Textarea)

    def __int__(self, *args, **kwargs):
        super().__int__(*args, **kwargs)


