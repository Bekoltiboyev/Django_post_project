from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreatePostForm, RegisterForm, ProfileForm, CommentForm
from .models import Profil, Postmodel, ComentModel
from django.contrib.auth.models import User


def HomeView(request):
    post_yahshi = Postmodel.objects.filter(turi="yahshi")
    post_yahshi_count = Postmodel.objects.filter(turi="yahshi").count()
    post_yomon = Postmodel.objects.filter(turi='yomon')
    post_yomon_count = Postmodel.objects.filter(turi='yomon').count()

    ctx = {
        'yahshi': post_yahshi,
        'yomon': post_yomon,
        'yahshi_count': post_yahshi_count,
        'yomon_count': post_yomon_count,
    }
    
    return render(request, 'home.html', ctx)

def LoginView(request):
    if request.POST:
        userName = request.POST['username']
        userPassword = request.POST['password']
        user = authenticate(request, username=userName, password=userPassword)
        if user is not None:
            login(request, user)
            print("muofaqiyatli kirdingiz.")
            return redirect('/')
        else:
            print("afsuski login yoki parol xato!")
            
            return redirect('login')
    else:
        return render(request, 'login.html')

def LogoutView(request):
    logout(request)
    return render(request, 'home.html')
    

def RegisterView(request):
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('register')
    
    form = RegisterForm()

    return render(request, 'register.html', {"forms": form})

def ProfileView(request, pk):
    userEdit = Profil.objects.get(user_id=pk)
    if request.POST:
        form = ProfileForm(request.POST, request.FILES, instance=userEdit)
        if form.is_valid():
            
            form.save()
            # message
            return redirect('profile',pk=userEdit.user_id)
        else:
            # massage
            return redirect('profile',pk=userEdit.user_id)
    form = ProfileForm(instance=userEdit)
    ctx = {
        "form": form
    }
    return render(request, "profile.html", ctx)


def CreatePostView(request, pk):
    post_id = Profil.objects.get(user_id=pk)
    if request.POST:
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            profile_title = form.cleaned_data['title']
            profile_text = form.cleaned_data['text']
            profile_img = form.cleaned_data['post_image']
            profile_turi = form.cleaned_data['turi']
            form_data = Postmodel(profile=post_id,title=profile_title, text=profile_text,post_image=profile_img, turi=profile_turi)
            form_data.save()
        else:
            print("xato")
    form = CreatePostForm()
    ctx = {
        'form': form
    }
    return render(request, "create_post.html",ctx)


def PostsView(request, pk):
    posts = Postmodel.objects.filter(profile_id=pk)
    ctx = {
        "posts": posts
    }
    return render(request, "posts.html", ctx)


def EditPostView(request, pk):
    edit_post = Postmodel.objects.get(id=pk)
    
    if request.POST:
        form = CreatePostForm(request.POST, request.FILES, instance=edit_post)
        if form.is_valid():
            form.save()
            return redirect('posts',request.user.id)
        else:
            print("saqlanmadi")
            return redirect('edit-post',pk=edit_post.id)
    form = CreatePostForm(instance=edit_post)
    ctx = {
        "form": form,
        'pk': pk
    }
    return render(request, "edit-post.html",ctx)


def CommentsView(request, pk):
    post_yahshi = Postmodel.objects.get(id=pk)
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.save(commit=True)
            data.post = Postmodel.objects.get(id=pk)
            data.profile = Profil.objects.get(id=request.user.id)
            data.save()
            return redirect('comment',pk)
        else:
            return redirect('comment',pk)
    
    form = CommentForm()
    comment = ComentModel.objects.filter(post_id=pk)
    
    ctx = {
        "form": form,
        "posts": post_yahshi,
        "comments": comment,
    }
    
    return render(request, "comment.html",ctx)



def EditCommentView(request):
    
    
    return render(request, "edit_comments.html",{})


def DeleteCommentView(request):
    
    
    return render(request, "delete_comment.html",{})





# django  nima?
# djnago MVT Tushintirib bering?
# django ORM nima?