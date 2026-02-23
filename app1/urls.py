from django.urls import path
from .import views

urlpatterns =[
   path('',views.home,name='home'),
   path('about/',views.about,name='about'),
   path('contact/',views.contact,name='contact'),
   path('ViewBook/',views.ViewBook,name='ViewBook'),    
   path('addbook/',views.addbook,name='addbook'),
   path('updatebook/<int:id>',views.update_book,name='updatebook'),
   path('delete/<int:id>',views.delete_book,name='deletebook'),
   path('register/',views.register,name='register')
]