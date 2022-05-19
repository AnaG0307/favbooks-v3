from django import forms
from .models import Book, Category, Sub_Category


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        sub_categories = Sub_Category.objects.all()
        friendly_names_c = [(c.id, c.get_friendly_name()) for c in categories]
        friendly_names_s = [(s.id, s.get_friendly_name()) for s in sub_categories]

        self.fields['book_category'].choices = friendly_names_c
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'

        self.fields['book_sub_category'].choices = friendly_names_s
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'
