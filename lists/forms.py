from django import forms
from lists.models import Item

EMPTY_ITEM_ERROR = "You can't have an empty list item"
class ItemForm(forms.models.ModelForm):
    # Django provides the ModelForm class which can be used to  autogenerate
    # a form for a model. It's configured using the special attribute 'Meta'
    class Meta:
        model = Item  # model specifies which model the form is for
        # fields specifies which fields in the model we want the form to use. In this case the text field of Item
        fields = ('text', )
        # You can override widgets for ModelForm fields to customize the form's UIs
        widgets = {
            'text': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a to-do item',
                'class': 'form-control input-lg',
            })
        }
        # You can override the error_messages attribute to display custom messages to the user when
        # there's a form validation error
        error_messages = {
            'text': {'required': EMPTY_ITEM_ERROR}
        }
