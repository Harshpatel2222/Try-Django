from django import forms


from .models import Product


class ProductForm(forms.ModelForm):
    title       = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Your description",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 20,
                                    'cols': 120
                                }
                            )
                        )
    price       = forms.DecimalField(initial=199.99)
    email = forms.EmailField()
    
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self,*args,**kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("This is not valid title")
        return title

    def clean_email(self,*args,**kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("Error")
        return email

#pure Django Form
class RawProductForm(forms.Form):
    title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Your description",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 20,
                                    'cols': 120
                                }
                            )
                        )
    price       = forms.DecimalField(initial=199.99)