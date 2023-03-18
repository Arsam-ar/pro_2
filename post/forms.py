
from django import forms
from .models import Post




class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=["title",'img',"model_post","price","category","cpu","ram", "hard", "gpu","description", "slug"]
        labels={
            'img': "عکس",
            "model_post" : "مدل",
            "price": "قیمت",
            "category":"دسته",
            "description":"توضیحات",
             "slug":"slug",
        }