
from django.shortcuts import render, HttpResponseRedirect,redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django .contrib import messages

from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives
from django.http import HttpResponse

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token

from django.contrib.auth import login
from .models import User
from django.utils.encoding import force_text
from django.conf import settings
from .forms import SignUpForm


# Create your views here.



def forget_password(request):
   

    context = {
  
    }

    return render(request, 'iroomie/forget-password-page.html', context)





def register(request):
   

    context = {
  
    }

    return render(request, 'iroomie/register-page.html', context)


def usersignup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()


            # current_site = get_current_site(request)
            # subject = 'Activate Your Account'
            # message = render_to_string('iroomie/account_activation_email.html', {
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': account_activation_token.make_token(user),
               
            # })
            # user.email_user(subject, message)
            return redirect('login')

    else:
        form = SignUpForm()
    return render(request, 'iroomie/register-page.html', {'form': form})

# def activate(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)

#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None

#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.email_verified = True
#         user.save()
#         login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#         messages.warning(request, ('Account Activated'))
#         return redirect('login')
#     else:
#         messages.warning(request, ('Confirmation Link invalid'))
#         return redirect('login')







# def login_user(request):

#     next = ""

#     if request.GET:  
#         next = request.GET['next']

#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             if next == "":
#                 return HttpResponseRedirect(reverse('home'))
#             else:
#                 return HttpResponseRedirect(next)
            
#         else:
#             messages.success(request, "Invalid Login Details", extra_tags='alert alert-success')

#     context = {
#          'next':next,
#     }
#     return render(request, 'iroomie/login-page.html', context)


# def logout_user(request):

#     logout(request)
#     return HttpResponseRedirect(reverse('home'))

# def register(request):
   

#     context = {
  
#     }

#     return render(request, 'iroomie/register-page.html', context)


#  {% if next %}
#                         <form action="?next={{next}}" method="post" >
#                         {%else%}
                                        
#                         <form method="post" action="{% url 'login'%}">
#                         {% endif %}

