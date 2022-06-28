
from ast import keyword
from unittest import result
from django.shortcuts import redirect, render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from .models import *
from authentication.models import *
from django.db.models import Q
from .forms import AddRoomForm, EditRoomForm,AddReviewForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .filters import RoomFilter, ProfileFilter, PreferenceFilter
from django.contrib import messages
from newsletter.forms import NewsletterForm

def index(request):

    form = NewsletterForm
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Subscribed!', extra_tags='alert alert-success')
        return redirect ('home')
    else:
        form = NewsletterForm()

    rooms = Room.objects.all()
    user_profiles= User.objects.all().filter(email_verified=True)

    context = {
        'form':form,
        'rooms': rooms,
        'user_profiles':user_profiles,
    }

    return render(request, 'iroomie/index.html', context)

@login_required()
def room_list(request): 

    

    rooms = Room.objects.all()
    room_paginator = Paginator(rooms, 2)

    page_num = request.GET.get('page')

    page = room_paginator.get_page(page_num)
    room_filter = RoomFilter(request.GET, queryset=rooms)
    
    context = {
        'rooms': rooms,
        'page': page,
        'room_filter': room_filter
    
    }

    return render(request, 'iroomie/room/room_list.html', context)

@login_required()
def room_advance_search(request): 
    rooms = Room.objects.all()
    room_filter = RoomFilter(request.GET, queryset=rooms)
    room_list = room_filter.qs

    context = {
        'rooms': rooms,
        'room_filter': room_filter,
        'room_list': room_list,
    }

    return render(request, 'iroomie/room/advance_search_result.html', context)

@login_required()
def roommates_advance_search(request): 
    user_profiles= User.objects.all() 
    profile_filter = ProfileFilter(request.GET, queryset=user_profiles)
    preference_filter = PreferenceFilter(request.GET, queryset=user_profiles)
    profile_list = profile_filter.qs
 


    context = {
        'user_profiles': user_profiles,
        'profile_filter': profile_filter,
        'profile_list': profile_list,
        'preference_filter':preference_filter,
       
    }

    return render(request, 'iroomie/roommate/advance_search_result.html', context)
    

@login_required()
def room_mate_list(request):

    rooms = Room.objects.all()
    user_profiles= User.objects.all() 
    user_profile_paginator = Paginator(user_profiles, 2)
    page_num = request.GET.get('page')
    page = user_profile_paginator.get_page(page_num)
    profile_filter = ProfileFilter(request.GET, queryset=user_profiles)
    preference_filter = PreferenceFilter(request.GET, queryset=user_profiles)


    context = {
        'rooms': rooms,
        'user_profiles':user_profiles,
        'page': page,
        'profile_filter': profile_filter,
        'preference_filter':preference_filter,
        
        
    }

    return render(request, 'iroomie/roommate/room_mate_list.html', context)

@login_required()
def preference_search(request):
    user_profiles= User.objects.all() 
    profile_filter = ProfileFilter(request.GET, queryset=user_profiles)
  
    preference_filter = PreferenceFilter(request.GET, queryset=user_profiles)
    preference_list = preference_filter.qs

    context = {
        
        'preference_filter':preference_filter,
        'user_profiles': user_profiles,
         'profile_filter': profile_filter,
        'preference_list': preference_list,
        
    }

    return render(request, 'iroomie/roommate/preference_search.html', context)


def search(request):
    rooms = Room.objects.all()

  
    school = request.GET.get("school")
    keyword = request.GET.get("keyword")
    type = request.GET.get("type")
    

    if school and keyword and type:
        query_set = rooms.filter(
            Q(address=keyword) |
            Q(school__name=school) and
            Q(type=type) 


        ).distinct()

        count = len(query_set)

    elif school and keyword :
        query_set = rooms.filter(
            Q(address=keyword) |
            Q(school__name=school) 


        ).distinct()

        count = len(query_set)

    elif school and type:
        query_set = rooms.filter(
          
            Q(school__name=school) and
            Q(type=type) 


        ).distinct()

        count = len(query_set)
    
    elif keyword and type:
        query_set = rooms.filter(
            Q(address=keyword) and
            Q(type=type) 


        ).distinct()

        count = len(query_set) 

    elif school:
        query_set = rooms.filter(
            Q(school__name=school)


        ).distinct()

        count = len(query_set)

    elif type:
        query_set = rooms.filter(
            
            Q(type__icontains=type) 


        ).distinct()

        count = len(query_set)

    elif keyword:
        query_set = rooms.filter(
            Q(address__icontains=keyword)|
             Q(description__icontains=keyword)



        ).distinct()

        count = len(query_set)  

    elif keyword == '' and school == '' and type == '':
        messages.warning(request, "Please enter a keyword or preference!", extra_tags='alert alert-')
        return redirect('home')

    else:
        query_set = rooms

    if count <= 1:
        result = 'result'
    else:
        result = 'results'
    context = {

     'rooms':rooms,   
    'school': school,
    'keyword': keyword,
    'type': type,
    'query_set': query_set,
    'count':count,
    'result': result,
        }
    return render(request, 'iroomie/search_result.html', context)

@login_required()
def room_detail(request, uuid_id):

    
    
    rooms = Room.objects.all()
    room = get_object_or_404(Room, slug=uuid_id)


    reviews = room.reviews.all()
    user_review = None
    if request.method == 'POST':
        
        form = AddReviewForm(request.POST)
        if form.is_valid():
            
            user_review = form.save(commit=False)
            user_review.Room= room
            user_review.reviewer =request.user
            user_review.save()

            return redirect('home')
    else:
        form = AddReviewForm()
   
    
    context = {
        'room': room,
        'rooms': rooms,
        'reviews': user_review,
        'reviews': reviews,
        'form': form
       
    }

    return render(request, 'iroomie/room/room_details.html', context)




@login_required()
def add_new_room(request):
    new_room = None
    if request.method == 'POST':
        
        form = AddRoomForm(request.POST, request.FILES)
        if form.is_valid():
            new_room = form.save()
            new_room.owner = request.user
            new_room.save()
            print ('Room added')
            messages.success(request, "Listing Successfully Added!", extra_tags='alert alert-success')
            return redirect('home')
    else:
        form = AddRoomForm()
        print('Unable to add room')

    context = {
        'form':form,
    }

    return render(request, 'iroomie/room/add_room.html', context)


@login_required()
def edit_room(request, uuid_id):
    room = get_object_or_404(Room, slug=uuid_id)
    if request.method == 'POST':
    
        form = EditRoomForm(request.POST, request.FILES, instance=room)
        if form.is_valid():
            form.save()
            messages.success(request, "Listing Successfully Edited!", extra_tags='alert alert-success')
            return redirect('home')
    else:
            form = EditRoomForm(instance=room)

    context = {
        'form':form,
        'room':room
    }

    return render(request, 'iroomie/room/edit_room.html', context)

@login_required()
def delete_room(request, uuid_id):
    room = get_object_or_404(Room, slug=uuid_id)
    room.delete()
    messages.success(request, "Listing Deleted!", extra_tags='alert alert-success')
    return redirect('home')
    



@login_required()
def user_profile(request, profile_id, name_id,pk):
   
   
    profile = get_object_or_404(User, first_name = profile_id, last_name= name_id, pk=pk)
    rooms = Room.objects.filter(owner= pk )

    context = {
        'profile': profile,
        'rooms': rooms,
    }

    return render(request, 'iroomie/profile.html', context)

@login_required()
def my_profile(request):
    
      context = {}
      return render(request, 'iroomie/my_profile.html', context)




def contact(request):

    context = {}

    return render(request, 'iroomie/contact-us.html', context)

def about(request):

    context = {}

    return render(request, 'iroomie/about-us.html', context)

@login_required()
def aaua_room_category(request):

    room = Room.objects.all()

    query_set = room.filter(

        Q(school__name__icontains="Adekunle Ajasin University")

    ).distinct()

    count = room.filter(

        Q(school__name__icontains="Adekunle Ajasin University")

    ).count()

    context = {
        'query_set': query_set,
        'count': count,
        'kwargs': "Adekunle Ajasin University"
    }

    return render(request, 'iroomie/room_category.html', context)

def futa_room_category(request):

    room = Room.objects.all()

    query_set = room.filter(

        Q(school__name__icontains='Federal University of Technology')

    ).distinct()
    print(query_set)

    count = room.filter(

        Q(school__name__icontains='Federal University of Technology')

    ).count()

    context = {
        room : room,
        'query_set': query_set,
        'count': count,
        'kwargs': 'Federal University of Technology'
    }

    return render(request, 'iroomie/room_category.html', context)

# def aue_room_category(request):

#     room = Room.objects.all()

#     query_set = room.filter(

#         Q(school__name__icontains='Adeyemi University of Education')

#     ).distinct()

#     count = room.filter(

#         Q(school__name__icontains='Adeyemi University of Education')

#     ).count()

#     context = {
#         'query_set': query_set,
#         'count': count,
#         'kwargs': 'Adeyemi University of Education'
#     }

#     return render(request, 'iroomie/room_category.html', context)

# def son_room_category(request):

#     room = Room.objects.all()

#     query_set = room.filter(

#         Q(school__name__icontains='School of Nursing')

#     ).distinct()

#     count = room.filter(

#         Q(school__name__icontains='School of Nursing')

#     ).count()

#     context = {
#         'query_set': query_set,
#         'count': count,
#         'kwargs': 'School of Nursing'
#     }

#     return render(request, 'iroomie/room_category.html', context)


def error_not_found(request, exception):

    return render(request, 'iroomie/404-error.html')