from django.shortcuts import render
from .forms import PostForm
from django.shortcuts import render , get_object_or_404 , redirect
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
def add_post(request):
    if request.method == "POST":
        # form = PostForm(request.POST)
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid() :
            post_item = form.save(commit=False)
            post_item.save()
            return redirect('/post/')
    else:
        form = PostForm()
    return render (request, '../templates/post_form.html' , {'form' : form})


class PostDetailView(DetailView):
    model = Post
    template_name = '../templates/post_detail.html'

class PostListView(ListView):
    model = Post
    template_name = '../templates/post_list.html'

def edit_post(request , pk=None):
    item = get_object_or_404(Post , pk=pk)
    form = PostForm(request.POST or None , request.FILES or None ,instance=item)
    if form.is_valid():
        form.save()
        return redirect('/post/' + str(pk) + '/')
    #return render (request, 'post/post_form.html' , {'form' : form})
    return render (request, '../templates/post_form.html' , {'form' : form})
