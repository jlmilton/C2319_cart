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
            # a = post_item.save()
            n = form.cleaned_data["title"]
            m = form.cleaned_data["cover"]
            a = form.cleaned_data["category"]
            b = form.cleaned_data["condition"]
            c = form.cleaned_data["price"]
            d = form.cleaned_data["body"]
            e = form.cleaned_data["publish"]
            t = Post(title=n, body=d , price=c, condition=b , category=a, cover=m, publish=e)
            t.save()
            request.user.post.add(t)
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

class ForSaleListView(ListView):
    model = Post
    template_name = '../templates/forsale.html'


def edit_post(request , pk=None):
    item = get_object_or_404(Post , pk=pk)
    form = PostForm(request.POST or None , request.FILES or None ,instance=item)
    if form.is_valid():
        form.save()
        return redirect('/post/' + str(pk) + '/')
    #return render (request, 'post/post_form.html' , {'form' : form})
    return render (request, '../templates/post_form.html' , {'form' : form})

def delete_post(request, pk=None):
    item = get_object_or_404(Post , pk=pk)
    form = PostForm(request.POST or None , instance=item)
    item.delete()
    return redirect('/post/')
    # return render (request, '../templates/post_list.html' , {'form' : form})
