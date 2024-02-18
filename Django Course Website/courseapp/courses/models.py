from django.db import models
from django.utils.text import slugify

class Category(models.Model):
   name = models.CharField(max_length=40)
   slug = models.SlugField(default="", db_index=True, null=False, unique=True, max_length=50)
   
   def __str__(self):
      return f"{self.name}"
  

class Course(models.Model):
  title = models.CharField(max_length=50)
  description = models.TextField()
  image = models.ImageField(upload_to="images", default="")
  date = models.DateField(auto_now=True)
  isActive = models.BooleanField(default=False)
  isHome = models.BooleanField(default=False)
  slug = models.SlugField(default="", blank=True, null=False, unique=True, db_index=True)
  categories = models.ManyToManyField(Category)
  #category = models.ForeignKey(Category,default=1, on_delete=models.CASCADE)

  
  # def save(self, *args, **kwargs):
  #      self.slug = slugify(self.title) 
  #      super().save(args,kwargs)

  def __str__(self):
      return f"{self.title} {self.date}"
  
  
  
class UploadModel(models.Model):
  image = models.ImageField(upload_to="images") 



  