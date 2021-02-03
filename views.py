from django.shortcuts import render
from .models import EventModel, EnquiryModel, SignUpModel

def home(request):
    if request.method == 'GET':
        return render(request, "home.html")
    if request.method == 'POST':
        obj1 = EnquiryModel()
        obj1.email = request.POST.get('email')
        obj1.query = request.POST.get('query')

        obj1.save()

        success = True
        return render(request, "home.html", {'success': success})


def gallery(request):
    return render(request, "gallery.html")


def register(request):
    if request.method == 'GET':
        return render(request, "register.html")
    if request.method == 'POST':
        obj = EventModel()
        obj.name = request.POST.get('name')
        obj.contact = request.POST.get('contact')
        obj.email = request.POST.get('email')
        obj.date = request.POST.get('date')
        obj.event = request.POST.get('event')

        if request.POST.get('catering') is not None:
            obj.catering = request.POST.get('catering')

        else:
            obj.catering = ""


        if request.POST.get('sound') is not None:
            obj.sound = request.POST.get('sound')
        else:
            obj.sound = ""


        if request.POST.get('dec') is not None:
            obj.dec = request.POST.get('dec')

        else:
            obj.dec = ""


        if request.POST.get('venue') is not None:
            obj.venue = request.POST.get('venue')

        else:
            obj.venue = ""


        if request.POST.get('photo') is not None:
            obj.photo = request.POST.get('photo')

        else:
            obj.photo = ""

        obj.save()
        success = True

        return render(request, "register.html", {'success': success})

def admindashboard(request):

    if request.method == 'GET':
        try:
            user = EventModel.objects.all()
            return render(request,"admindashboard.html",{'user':user})
        except EventModel.DoesNotExist:
            return render(request, "login.html")

def login(request):
    if request.method =='GET':
        return render(request,"login.html")
    if request.method == 'POST':
        username = request.POST.get('username')
        password= request.POST.get('password')

        #to set session parameters
        request.session['username'] = username
        request.session['password'] = password

        #to check with database values
        try:
            user = SignUpModel.objects.get(username=username,password=password)
            data = EventModel.objects.all()
            return render(request, "admindashboard.html", {'data':data})

        except SignUpModel.DoesNotExist:
            return render(request, "login.html", {'error': True, 'error_msg':'User doesnot exist in DB'})


success = False
def signup(request):
    if request.method == 'GET':
        return render(request, "signup.html")
    if request.method == 'POST':
        obj = SignUpModel()
        obj.username = request.POST.get("username")
        obj.password = request.POST.get("password")

        obj.save()
        success=True

        return render(request, "signup.html", {'success': success})


