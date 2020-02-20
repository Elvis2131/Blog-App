from django.shortcuts import render,redirect, get_object_or_404
from .models import Blog
from .forms import BlogForm
import datetime

# Create your views here.

#Creating a new blog post
def blog_create_view(request):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/blogs')
    context = {
        'objform': form
    }
    return render(request,'blogs/blog_create.html',context)


#Viewing all blog posts in the database
def blog_view_list(request):
    queryset = Blog.objects.all()
    time = datetime.datetime.now().strftime('%A - %B %d, %Y --- %X')
    context ={
        'obj': queryset,
        'who': request.user,
        'bgtime': time
    }
    return render(request, 'blogs/blog_list.html', context)

#View the details of a blog post
def blog_detail_view(request,objid):
    obj = Blog.objects.get(id = objid)
    context = {
        'obj':obj
    }
    return render(request, 'blogs/blog_view.html', context)

# updating a record
def blog_update_view(request, myid):
    blog = Blog.objects.get(pk=myid)
    #obj = BlogForm(instance=blog)
    form = BlogForm(request.POST or None,instance=blog)
    if form.is_valid():
        form.save()
        return redirect('../../')

    context = {
        'objform': form
    }
    return render(request,'blogs/blog_update.html',context)

def blog_delete_view(request, myid):
    obj = Blog.objects.get(id = myid)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')

    context = {
        'obj': obj
    }
    return render(request, 'blogs/blog_delete.html', context)