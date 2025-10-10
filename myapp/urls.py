from myapp import views
from django.urls import path
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('delete/<int:id>/',views.Delete,name='delete'),
    path('form_data/',views.form_data,name='form_data'),
    path('edit/<id>',views.Edit,name='edit')
]
