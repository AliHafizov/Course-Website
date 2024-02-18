from django.shortcuts import  render, get_object_or_404, redirect
from .models import Course, Category, UploadModel
from django.core.paginator import Paginator
from courses.forms import CourseCreateForm, CourseEditForm, UploadForm
from django.contrib.auth.decorators import login_required, user_passes_test

  


def index(request):
  #list_items=""
  #category_list = list(data.keys()) 
  kurslar = Course.objects.filter(isActive=1, isHome=1)
  kategoriler = Category.objects.all()

  #for kurs in db["courses"]:
    #if kurs["isActive"]==True:
      #kurslar.append(kurs)
  return render(request, 'courses/index.html', {
  'categories': kategoriler,
  'courses' : kurslar
})


def isAdmin(user):
    return user.is_superuser


@user_passes_test(isAdmin)
def create_course(request):
    if request.method == "POST":
        form = CourseCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/kurs")
    else:    
        form = CourseCreateForm()
    return render(request, "courses/create-course.html",{"form":form})



@login_required()
def course_list(request):
    kurslar = Course.objects.all()
    return render(request, 'courses/course-list.html', {
        'courses' : kurslar
})




def course_edit(request, id):
    course = get_object_or_404(Course, pk=id)

    if request.method == "POST":
        form = CourseEditForm(request.POST, request.FILES, instance=course)
        form.save()
        return redirect("course_list")
    else:
        form = CourseEditForm(instance=course)

    return render(request, "courses/edit-course.html", { "form":form })





def course_delete(request, id):
    course = get_object_or_404(Course, pk=id)

    if request.method == "POST":
        course.delete()
        return redirect("course_list")
    
    return render(request, "courses/course-delete.html", { "course":course })



def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            model = UploadModel(image=request.FILES["image"])
            model.save()
            return render(request, "courses/success.html")
    else:
        form = UploadForm()
    return render(request, "courses/upload.html", {"form":form})

 
 
 
  #for category in category_list:
   # redirect_url =reverse ('courses_by_category', args=[category])
   # list_items += f"<li><a href='{redirect_url}'>{category}</a></li>"

  #html= f"<h1>Kurs Listesi</h1><br><ul>{list_items}</ul>"


def search(request):
  if "q" in request.GET and request.GET["q"] !="":
      q = request.GET["q"]
      kurslar = Course.objects.filter(isActive=1,title__contains=q).order_by("date")
      kategoriler = Category.objects.all()
  else:
      return redirect("/kurs")
  
  return render (request, 'courses/search.html', {
     'categories': kategoriler,
     'courses': kurslar,
  })



  
  

def details(request, slug):
  # try:
  #   course = Course.objects.get(pk=kurs_id)
  # except:
  #   raise Http404()
  course = get_object_or_404(Course, slug=slug)
  context = {
    'course': course
  }
  return render(request, 'courses/details.html', context)





def getCoursesByCategory(request, slug):
  kurslar = Course.objects.filter(categories__slug=slug, isActive=1).order_by('date')
  kategoriler = Category.objects.all()

  paginator = Paginator(kurslar,2)
  page = request.GET.get('page',1)
  page_obj = paginator.page(page)

  # print(page_obj.paginator.count)
  # print(page_obj.paginator.num_pages)
  
  return render(request, 'courses/list.html', {
    'categories': kategoriler,
    'page_obj' : page_obj,
    'seciliKategori': slug,
  })







  # try:
  #   category_text = data[category_name];
  #   return render(request, 'courses/kurslar.html', {
  #     'category':category_name,
  #     'category_text':category_text
  #   })
  # except:
  #   return HttpResponseNotFound('yanlis kategori bilgisi')

  
  
# def getCoursesByCategoryId(request, category_id):
#   category_list = list(data.keys())
#   if (category_id > len(category_list)):
#     return HttpResponseNotFound('yanlis kategori secimi')
#   category_name = category_list[category_id - 1]
  
#   redirect_url = reverse('courses_by_category', args=[category_name] )
  
#   return redirect(redirect_url)
  
  
  
  
  
  
  #text = ""
  

#if (category_name == "programlama"):
  #  text = "programlama kategorisine ait kurslar"
  #elif(category_name == "web-gelistirme"):
   # text = "web gelistirme kategorisine ait kurslar"
  #else:
   # text = "yanlis bilgi girdiniz"
  #return HttpResponse(text)



    
  
  
  
  
  
