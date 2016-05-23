from django.shortcuts import render, redirect
from blog.models import Post
from blog.forms import PostForm
from django.contrib.auth.decorators import login_required

def index(request):
	return render(request, 'blog/index.html')

def post_list(request):
	posts = Post.objects.all()
	return render(request, 'blog/post_list.html', {
		'posts':posts,
		})

def post_detail(request, pk):
	post = Post.objects.get(pk=pk)
	return render(request, 'blog/post_detail.html', {
		'post':post,
		})

@login_required
def post_new(request): 
	if request.method == "POST":
		form=PostForm(request.POST, request.FILES)
		if form.is_valid():
			form = form.save(commit=False)
			form.author = request.user
			form.save()
			return redirect("blog:post_list")
	else:
		post_form = PostForm()
		return render(request, 'blog/post_form.html', {'post_form':post_form})

def about_me(request):
	return render(request, 'blog/about_me.html')
# Create your views here.
