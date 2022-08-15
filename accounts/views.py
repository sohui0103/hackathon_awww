from django.shortcuts import render, redirect
from django.contrib import auth
#from backend1.awwwmember.forms import ProfileUpdateForm
from django.contrib.auth.models import User

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else: 
            return render(request, 'bad_login.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['repeat']:
            # 회원가입
            new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            # 로그인
            auth.login(request, new_user)
            # 홈 리다이렉션
            return redirect('home')
    return render(request, 'signup.html')


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