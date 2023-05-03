from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .models import Post, Comments
from .forms import CommentForm, PostForm
from django.views import View, generic
from django.http import JsonResponse
from django.core.mail import send_mail

class Home(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'posts'
    model = Post

class Posts(View):
    
    def get(self, request, post_id):
        article = Post.objects.get(id=post_id)
        split_article = article.content.split("\n")
        # send_mail('Django mail', 
        # 'This is an email sent using smtp with python as the backend.', 
        # 'kingsleyobiefuna01@gmail.com',
        # ['obiefunakingsley01@gmail.com'],
        # fail_silently=False)
        data = {
            'article' : article,
            'contents' : split_article,
            'posts' : Post.objects.all(),
            'comments' : Comments.objects.filter(post = article),
            'form' : CommentForm(),
        }
        return render(request, 'post.html', data)

class Register(View):

    def get(self, request):
        return render(request, 'registration/register.html')
        
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if len(password) < 8:
                messages = 'password must be greater than 8 characters'
                return render(request, 'registration/register.html', {'error':messages})

            if User.objects.filter(username=username).exists():
                messages = 'username already taken'
                return render(request, 'registration/register.html', {'error':messages})

            if User.objects.filter(email = email).exists():
                messages = 'email already used'
                return render(request, 'registration/register.html', {'error':messages})
                
            user = User.objects.create_user(first_name = firstName, last_name = lastName, username=username, email=email, password=password)
            user.save()
            return redirect('login?next=/')
                
        else:
            messages = 'Password mismatch'
            return render(request, 'registration/register.html', {'error':messages})

class Comment(View):    

    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        comments = Comments.objects.filter(post=post)
        return JsonResponse({'comments':list(comments.values())})

    def post(self, request, post_id):
        if not request.user.is_authenticated:
            loginurl = reverse('login')
            return redirect(loginurl+"?next=/post/"+str(post_id))
        form = CommentForm(request.POST)
        if not form.is_valid():
            return redirect('post/'+str(post_id))
        filled_form = form.save(commit=False)
        filled_form.comment_author = request.user.get_username()
        filled_form.post = Post.objects.get(id=post_id)
        filled_form.save()
        return redirect(f'post/{post_id}')

class CreatePost(LoginRequiredMixin, View):
    def get(self, request):
        post = PostForm()
        return render(request, 'createPost.html', {'form':post})
    
    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'createPost.html', {'form':form})
        filled_form = form.save(commit=False)
        filled_form.author = request.user.get_full_name()
        filled_form.save()
        
        
        return redirect("/")
