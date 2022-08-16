from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from accounts.forms import UserLoginForm, RegistrationForm


# Create your views here.
def login_request(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    context = {
        'form': form,
        'title': title,
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)

        login(request, user)
        # messages.info(request, f"You are now logged in  as {user}")
        return redirect('home')
    else:
        print(form.errors)
        # messages.error(request, 'Username or Password is Incorrect! ')
    return render(request, 'login.html', context=context)


def signup_request(request):
    title = "Create Account"
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()

    context = {'form': form, 'title': title}
    return render(request, 'signup.html', context=context)


def logout_request(request):
    logout(request)
    # messages.info(request, "Logged out successfully!")
    return redirect('home')



#마이페이지
def mypage(request):
    return render(request, 'mypage.html')




# #마이페이지
# @login_required
# def userinfo(request):
#     conn_user = request.user
#     posts = Blog.objects.all().filter(create_user=conn_user).order_by('-id')
#     conn_profile = Profile.objects.get(user=conn_user)

#     if not conn_profile.profile_image:
#         pic_url = ""
#     else:
#         pic_url = conn_profile.profile_image.url
            
#     context = {
#         'id' : conn_user.username,
#         'nick' : conn_profile.nick,
#         'profile_pic' : pic_url,
#         'intro' : conn_profile.intro,
#         'posts' : posts,
#     }

#     return render(request, 'mypage.html', context=context)

# @login_required
# def user_select_info(request, writer):
#     select_profile = Profile.objects.get(nick=writer)
#     select_user = select_profile.user
#     posts = Blog.objects.all().filter(create_user=select_user).order_by('-id')

#     if not select_profile.profile_image:
#         pic_url = ""
#     else:
#         pic_url = select_profile.profile_image.url
            
#     context = {
#         'id' : select_user.username,
#         'nick' : select_profile.nick,
#         'profile_pic' : pic_url,
#         'intro' : select_profile.intro,
#         'posts' : posts,
#     }

#     return render(request, 'userpage.html', context=context)


# class ProfileUpdateView(View): 
#     def get(self, request):
#         user = get_object_or_404(User, pk=request.user.pk) 

#         if hasattr(user, 'profile'):  
#             profile = user.profile
#             profile_form = ProfileUpdateForm(initial={
#                 'nick': profile.nick,
#                 'intro': profile.intro,
#                 'profile_image': profile.profile_image,
#             })
#         else:
#             profile_form = ProfileUpdateForm()

#         return render(request, 'profile_update.html', { "profile_form": profile_form, "profile": profile})

#     def post(self, request):
#         u = User.objects.get(id=request.user.pk)       


#         if hasattr(u, 'profile'):
#             profile = u.profile
#             profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile) 
#         else:
#             profile_form = ProfileUpdateForm(request.POST, request.FILES)

#         # Profile 폼
#         if profile_form.is_valid():
#             profile = profile_form.save(commit=False) 
#             profile.user = u
#             profile.save()

#             if not profile.profile_image:
#                 pic_url = ""
#             else:
#                 pic_url = profile.profile_image.url
                    
#             context = {
#                 'id' : u.username,
#                 'nick' : profile.nick,
#                 'profile_pic' : pic_url,
#                 'intro' : profile.intro,
#             }

#             return render(request, 'mypage.html', context=context)
            
#         return redirect('mypage', pk=request.user.pk) 