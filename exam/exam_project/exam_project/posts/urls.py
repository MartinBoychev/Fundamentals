from django.urls import path, include

from exam.exam_project.posts import views

urlpatterns = [
    path('create/', views.add_post, name='add-post'),
    path('<int:post_id>/', include([
        path('details/', views.details_post, name='details-post'),
        path('edit/', views.edit_post, name='edit-post'),
        path('delete/', views.delete_post, name='delete-post'),]
    ))
]