from django import forms


class BootstrapForm(forms.Form):
    """
    Add bootstrap class to form visible fields.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
