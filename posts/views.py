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
        # form = PostForm(request.POST)
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid() :
            post_item = form.save(commit=False)
            post_item.save()
            return redirect('/post/' + str(post_item).lower() + '/')
    else:
        form = PostForm()
    # return render (request, 'post/post_form.html' , {'form' : form})
    return render (request, 'home_page/post_form.html' , {'form' : form})

def edit_post(request , slug=None):
    item = get_object_or_404(Post , slug=slug)
    form = PostForm(request.POST or None , request.FILES or None ,instance=item)
    if form.is_valid():
        form.save()
        return redirect('/post/' + str(slug) + '/')
    #return render (request, 'post/post_form.html' , {'form' : form})
    return render (request, 'home_page/post_form.html' , {'form' : form})
