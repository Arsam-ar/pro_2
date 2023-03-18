from django.urls import path
from .views import postlistview,PostDetailView,CategoryListView,categorydetailview,create_post,PostUpdateView,PostDeleteViwe
from django.conf import settings
from django.conf.urls.static import static
app_name="post"
urlpatterns = [
    path("", postlistview, name="postlist"),
    path("post_detail/<slug:slug_f>/<int:pk>", PostDetailView.as_view(), name="postdetail"),
    path("update/<slug:slug_f>/<int:pk>", PostUpdateView.as_view(), name="update"),
    path("delete/<slug:slug_f>/<int:pk>", PostDeleteViwe.as_view(), name="delete"),
    path("category/", CategoryListView.as_view(), name="category"),
    path("category_detail/<int:i_id>", categorydetailview, name="categorydetail"),
    path("createpost/",create_post, name="create_post"),

]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
