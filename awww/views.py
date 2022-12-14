from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse
from awww.models import Blog
from awww.forms import BlogUpdate, CommentForm, BlogModelForm

#메인 페이지
#플레이리스트 추천
def home(request):
    blogs = Blog.objects.order_by('-id')
    blog_list = Blog.objects.all().order_by('-id')
    paginator = Paginator(blog_list,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'home.html', {'blogs':blogs,'posts':posts}) 

#music talk
def musictalk(request):
    blogs = Blog.objects.order_by('-id')
    blog_list = Blog.objects.all().order_by('-id')
    paginator = Paginator(blog_list,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'musictalk.html', {'blogs':blogs,'posts':posts}) 

    # page = request.GET.get('page', '1')  # 페이지
    # paginator = Paginator(blog_list, 5)  # 페이지당 5개씩 보여주기
    # page_obj = paginator.get_page(page)
    # context = {'blog_list': page_obj}

    # return render(request,'musictalk.html', context) 

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    comment_form = CommentForm()
    return render(request, 'detail.html',{'blog': blog_detail}, {'comment_form':comment_form})


def create_comment(request, blog_id):
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():
        finished_form  = filled_form.save(commit=False) 
        finished_form.post = get_object_or_404(Blog, pk=blog_id) 
        finished_form.save()

        return redirect('detail.html', blog_id)

def create1(request):
    if(request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.save()
    return redirect('home')

def create(request):
    return render(request, 'create.html')

def postcreate(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/awww/detail/' + str(blog.id))

def update(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    if request.method =='POST':
        form = BlogUpdate(request.POST)
        if form.is_valid():
            blog.title = form.cleaned_data['title']
            blog.body = form.cleaned_data['body']
            blog.pub_date=timezone.now()
            blog.save()
            return redirect('/awwwapp/detail/' + str(blog.id))
    else:
        form = BlogUpdate(instance = blog) 
 
        return render(request,'update.html', {'form':form})

def delete(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect('/')

def new(request):
    return render(request, 'new.html')

def search(request):
    blogs = Blog.objects.all().order_by('-id')

    q = request.POST.get('q', "")

    if q:
        blogs = blogs.filter(title__icontains=q)
        return render(request, 'search.html',{'blogs' : blogs, 'q' : q})
    
    else:
        return render(request, 'search.html')

#좋아요
def BlogPostLike(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('blogpost_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('blogpost-detail', args=[str(pk)]))

def modelformcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid(): #만약 유효하다면
            form.save()
            return redirect('home')

# class BlogPostDetailView(detail):
#     model = Blog
#     # template_name = MainApp/BlogPost_detail.html
#     # context_object_name = 'object'

#     def get_context_data(self, **kwargs):
#         data = super().get_context_data(**kwargs)

#         likes_connected = get_object_or_404(Blog, id=self.kwargs['pk'])
#         liked = False
#         if likes_connected.likes.filter(id=self.request.user.id).exists():
#             liked = True
#         data['number_of_likes'] = likes_connected.number_of_likes()
#         data['post_is_liked'] = liked
#         return data


#유저 플레이리스트
def userplaylist(request):
    return render(request, 'userplaylist.html')

#뮤직 플레이리스트 생성
def makeplaylist(request):
    return render(request, 'makeplaylist.html')

