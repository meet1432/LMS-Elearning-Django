from django.shortcuts import redirect,render


def Base(request):
    return render(request, 'base.html')

def Home(request):
    return render(request, 'Main/home.html')

def Single_Course(request):
    return render(request, 'Main/single_course.html')

def About_Us(request):
    return render(request, 'Main/about_us.html')

def Contact_Us(request):
    return render(request, 'Main/contact_us.html')