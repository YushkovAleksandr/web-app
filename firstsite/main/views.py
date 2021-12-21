from django.shortcuts import render, redirect
from main.forms import AddPost
from .models import Author, Post
from datetime import datetime
from .forms import UserRegistrationForm

def index(request):
    
    return render(request, 'main/index.html')

def about(request):
    posts = Post.objects.all()
    return render(request, 'main/about.html', {'posts': posts})

def my_works(request):
    return render(request,'main/my_works.html')

def shop(request):
    return render(request,'main/shop.html')

def add_post(request):
    if request.method == "POST": # the form was submited
        form = AddPost(request.POST)

        if form.is_valid():
            post_ent = Post()
            post_ent.title = form.cleaned_data['title']
            post_ent.content = form.cleaned_data['content']
            post_ent.issued = datetime.now()
            post_ent.author = Author.objects.get(name = request.user.username)

            post_ent.save()

            return redirect('about')
    else: 
        form = AddPost()
    
    return render(request, 'main/add_post.html', {'form': form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            
            new_user = user_form.save(commit=False)
           
            new_user.set_password(user_form.cleaned_data['password'])
            
            new_user.save()
            return render(request, 'main/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'main/register.html', {'user_form': user_form})