from django import forms 
from courses.models import Course
from django.forms import TextInput, Textarea, SelectMultiple

# class CourseCreateForm(forms.Form):
#      title = forms.CharField(
#          label="Kurs Basligi", 
#          required=True, 
#          error_messages={
#              "required": "Kurs basligi yazilmalidir."}, 
#          widget=forms.TextInput(attrs={"class":"form-control"}))
#      description = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
#      imageUrl = forms.CharField( widget=forms.TextInput(attrs={"class":"form-control"}))
#      slug = forms.CharField( widget=forms.TextInput(attrs={"class":"form-control"}))


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title','description','image','slug')
        labels = {
            "title": "Kurs Basligi",
            "description": "Aciqlama"
         }
        widgets = {
            "title":TextInput(attrs={"class":"form-control"}),
            "description":Textarea(attrs={"class":"form-control"}),
            "slug":TextInput(attrs={"class":"form-control"}),
         }

        error_messages = {
            "title":{
                "required":"Kurs basligi yazmalisiz.",
                "max_length": "Maksimum 50 herf olmalidir."
             },
            "description":{
                "required":"Kurs aciqlamasi girmelisiniz."
             }
         }
        
class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title','description','image','slug','categories', 'isActive',)
        labels = {
            "title": "Kurs Basligi",
            "description": "Aciqlama"
         }
        widgets = {
            "title":TextInput(attrs={"class":"form-control"}),
            "description":Textarea(attrs={"class":"form-control"}),
            "slug":TextInput(attrs={"class":"form-control"}),
            "categories":SelectMultiple(attrs={"class":"form-control"}),
            
         }

        error_messages = {
            "title":{
                "required":"Kurs basligi yazmalisiz.",
                "max_length": "Maksimum 50 herf olmalidir."
             },
            "description":{
                "required":"Kurs aciqlamasi girmelisiniz."
             }
         }
        
class UploadForm(forms.Form):
    image = forms.ImageField()

