
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),
    path('list/', views.ListView.as_view(), name = 'list'),
    path('detail/<int:class_id>/', views.DetailView.as_view(), name = 'detail'),
    path('create/', views.CreateView.as_view(), name = 'create'),
    path('login/', TokenObtainPairView.as_view(), name="login"),
    path('update/<int:class_id>/', views.UpdateView.as_view(), name = 'update'),
    path('<int:class_id>/delete/', views.DeleteView.as_view(), name = 'delete'),

]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
