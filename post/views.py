from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from .models import Post,Category,ImagSlid
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.urls import reverse_lazy
from .forms import PostForm
from django.core.paginator import Paginator



class CategoryListView(ListView):
    model = Category
    paginate_by=3
    template_name = "post/categorylist.html"
    context_object_name="category_list"




def postlistview(request):
    Imgs=ImagSlid.objects.all()
    p=Paginator(Post.objects.all(),6)
    page=request.GET.get("page")
    pages=p.get_page(page)
    return render(request,"post/postlist.html",{"Imgs":Imgs,"pages":pages})
    



class PostDetailView(DetailView):
    model = Post
    template_name = "post/postdetail.html"
    context_object_name="postd_detail"

class PostUpdateView(LRM,UpdateView):
    model =Post
    template_name = "post/update.html"
    fields=["title",'img',"model_post","price","category","cpu","ram", "hard", "gpu","description"]
    

class PostDeleteViwe(LRM,DeleteView):
     model =Post
     template_name = "post/deletepost.html"
     success_url=reverse_lazy("post:postlist")






def categorydetailview(request,i_id):
    p=Paginator(Post.objects.filter(category=i_id),6)
    page=request.GET.get("page")
    pages=p.get_page(page)
    return render(request,'post/categorydetail.html',{"pages":pages})



@login_required
def create_post(request,pk=None):
    if request.method == "POST":
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect("post:postlist")
    else:
        form=PostForm()
    return render(request,"acconut/createpost.html",{"form" :form})


