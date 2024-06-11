from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Article, Comment


# Create your views here.

def home(request):
    # Fetch all articles adn render the home.html template
    articles = Article.objects.all()
    
    context_processors = {
        'articles': articles
    }

    return render(request, 'home.html', context_processors)

def about(request):
    return render(request, 'about.html')

# Create new article
def create(request):
    # If the request method is GET then render the create.html template
    if request.method == 'GET':
        return render(request, 'create.html')
    # If the request method is POST then create a new article
    elif request.method == 'POST':
        # Validate the request
        if request.POST['title'] and request.POST['slug'] and request.POST['body'] and request.FILES['video'] and request.FILES['image']:

            # If the title, slug, have special characters then return an error
            if not request.POST['title'].isalnum() or not request.POST['slug'].isalnum():
                return render(request, 'create.html', {'error': 'Title and slug must be alphanumeric.'})
            
            # Create a new article
            new_article = Article()
            # Set the fields of the article
            new_article.title = request.POST['title']
            new_article.slug = request.POST['slug']
            new_article.body = request.POST['body']
            new_article.video = request.FILES['video']
            new_article.image = request.FILES['image']
            new_article.thumb = request.FILES['image']
            # Save the article
            new_article.save()

            return render(request, 'create.html', {'success': 'Article created successfully.'})
        else:
            return render(request, 'create.html', {'error': 'All fields are required.'})


# Read article
def read(request, slug):
    return render(request, 'read.html')

# Update article
def update(request, slug):
    return render(request, 'update.html')

# Delete article
def delete(request, slug):
    return render(request, 'delete.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
        


def logout(request):
    # log the user out
    auth_logout(request)
    # redirect to the login page
    return render(request, 'login.html', {'success': 'Logout successful.'})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})