from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),

    #rooms
    path('search/', views.search, name='search'),
    path('rooms/advance/search/', views.room_advance_search, name='room_advance_search'),
    path('roommates/advance/search/', views.roommates_advance_search, name='roommate_advance_search'),
    path('roommates/preference/search/', views.preference_search, name='roommates_pref_search'),
    path('roomrstackrs/', views.room_mate_list, name='room_mate_list'),
   
    #roommates
    path('room_detail/<str:uuid_id>/', views.room_detail, name='room_detail'),
    path('room_edit/<str:uuid_id>/', views.edit_room, name='room_edit'),
    path('room_delete/<str:uuid_id>/', views.delete_room, name='room_delete'),
    path('rooms/', views.room_list, name='room_list'),
    path('add/room/new', views.add_new_room, name='add_new_room'),
   

    #profile
    path('profile/<profile_id>/<name_id>/<str:pk>', views.user_profile, name='user_profile_detail'),
    path('my_profile', views.my_profile, name='my_profile'),


    path('contact-us', views.contact, name='contact'),
    path('about-us/', views.about, name='about'),
    path('aaua_room_category/', views.aaua_room_category, name='aaua_room_category'),
    path('futa_room_category/', views.futa_room_category, name='futa_room_category'),
    # path('aue_room_category/', views.aue_room_category, name='aue_room_category'),
    # path('son_room_category/', views.son_room_category, name='son_room_category'),

    
   


   ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

   

handler404="iroomie.views.error_not_found"