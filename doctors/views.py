from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def doctor_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            if user.is_staff:

                login(request, user)
                return redirect('/doctor-reports/')

            else:

                return render(
                    request,
                    'doctors/doctor_login.html',
                    {'error': 'Only doctors can login here'}
                )

        else:

            return render(
                request,
                'doctors/doctor_login.html',
                {'error': 'Invalid username or password'}
            )

    return render(
        request,
        'doctors/doctor_login.html'
    )