from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Profile,Post,Likepost
from django.contrib.auth.decorators import login_required

# Create your views here.
def signin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        myuser=authenticate(request,username=username,password=password)
        if myuser is None:
            messages.info(request,"your username or password are incorrect")
            return redirect('signin')
        else:
            login(request,myuser)
            return redirect('homepage')
    else:
        return render(request,'signin.html')

def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1==password2:
            user=User.objects.create_user(username,email,password2)
            user.save()
            #user login to profile page
            user_login=authenticate(username=username,password=password2)
            login(request,user_login)

            user_model=User.objects.get(username=username)
            new_profile=Profile.objects.create(username=user_model,userid=user_model.id)
            new_profile.save()
            return redirect('profile')
        else:
            messages.info(request,'password and conform password are not same')
            return redirect('signup')
    else:
        return render(request,'signup.html')
@login_required(login_url='signin')
def profile(request):
    user_profile=Profile.objects.get(username=request.user)
    user_posts=Post.objects.filter(userid=user_profile.userid)
    if request.method=="POST":
        if request.FILES.get('image')==None:
            fname=request.POST.get('fname')
            lname=request.POST.get('lname')
            address=request.POST.get('address')
           
        
            user_profile.first_name=fname
            user_profile.last_name=lname
            user_profile.address=address
            
            user_profile.save()
            return redirect('profile')
        else:
            fname=request.POST.get('fname')
            lname=request.POST.get('lname')
            address=request.POST.get('address')
           
            image=request.FILES.get('image')

            user_profile.first_name=fname
            user_profile.last_name=lname
            user_profile.address=address
            
            user_profile.image=image
            user_profile.save()

            return redirect('profile')



    else:
        return render(request,'profile.html',{"user_profile":user_profile,'user_posts':user_posts})
@login_required(login_url='signin')
def homepage(request):
    user_home=Profile.objects.get(username=request.user)
    posts=Post.objects.all()
    if request.method=="POST":
        pass
    else:
        return render(request,'homepage.html',{'user_home':user_home,'posts':posts})
@login_required(login_url='signin')
def upload(request):
    user_upload=Profile.objects.get(username=request.user)
    user_id=user_upload.userid
    if request.method=="POST":
        userid=user_id
        post_name=request.POST.get('postname')
        post_image=request.FILES.get('postimage')

        new_post=Post.objects.create(userid=userid,post_name=post_name,post_image=post_image)
        new_post.save()
        return redirect('upload')
    else:
        return render(request,'upload.html',{'user_upload':user_upload})
@login_required(login_url='signin')
def like_post(request):
    post_id=request.GET.get('post_id')
    id=Post.objects.get(post_id=post_id)
    username=request.user.username
    like_filter=Likepost.objects.filter(post_id=post_id,username=username).first()
    if like_filter is None:
        new_like=Likepost.objects.create(post_id=post_id,username=username)
        new_like.save()
    
        id.no_of_likes=id.no_of_likes+1
        id.save()
        return redirect('homepage')
    else:
        like_filter.delete()
        id.no_of_likes=id.no_of_likes-1
        id.save()
        
        return redirect('homepage')



@login_required(login_url='signin')
def Logout(request):
    logout(request)
    return redirect('signin')
    