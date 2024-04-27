from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from mycanteen.models import models
from mycanteen.models import Section
from django.contrib.auth.models import User 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.http import JsonResponse
from django.contrib import messages
from mycanteen.models import Order , AdminNotification
from django.dispatch import receiver
from django.db.models.signals import post_save
from mycanteen.models import Order

@receiver(post_save, sender=AdminNotification)
def send_order_ready_notification(sender, instance, **kwargs):
    if instance.is_ready:
        # Send notification to user
        user = instance.order.user
        order_number = instance.order.order_number
        messages.success(user, f"Your order {order_number} is ready.")

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            # Passwords don't match, handle this case as needed (e.g., show an error message)
            pass
        else:
            # Create user and save to database
            data = User.objects.create_user(username=username, password=password1)
            # Optionally, you can log in the user automatically after signup
            # login(request, user)
            data.save()
            return redirect('login')
           
    return render(request, 'signup.html')
 
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('user')  # Redirect to the home page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


@receiver(post_save, sender=AdminNotification)
def send_order_ready_notification(sender, instance, **kwargs):
    if instance.is_ready:
        # Send notification to user
        print(f"Order {instance.order.order_number} is ready. Sending notification to {instance.order.user.username}")

def get_notifications(request):
    # Retrieve notifications data from the database
    notifications = notifications.objects.all().values_list('message', flat=True)
    # Convert QuerySet to list and return as JSON response
    return JsonResponse(list(notifications), safe=False)

def user(request):
 # Retrieve all sections and their associated items
    sections = Section.objects.prefetch_related('item_set').all()

    # Debug: Print sections and associated items to console to verify data
    for section in sections:
        print(section.name)
        for item in section.item_set.all():
            print(item.name)

    # Pass sections and items to the template
    return render(request, 'user.html', {'sections': sections})

    #return render(request, 'user.html')


def menu_view(request):
    # Add logic for your menu view here
    return render(request, 'menu.html')