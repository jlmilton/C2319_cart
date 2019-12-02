from django.views.generic import ListView, DetailView
from .models import Post
from django.shortcuts import render , get_object_or_404 , redirect
from .forms import PostForm
# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = 'home_page/post_list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'home_page/post_detail.html'

def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid() :
            post_item = form.save(commit=False)
            post_item.save()
            # return redirect('/post/' + slug + '/')
    else:
        form = PostForm()
    return render (request, 'post/post_form.html' , {'form' : form})

def edit_post(request , id=None):
    item = get_object_or_404(Post , id=id)
    form = PostForm(request.POST or None , instance=item)
    if form.is_valid():
        form.save()
    return render (request, 'post/post_form.html' , {'form' : form})
