from django.shortcuts import render
from .models import Movie, Banner_Movie
from django.db.models import Q

from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def index(request):
    recommended = Movie.objects.filter(category = 'recommended')
    blockbuster = Movie.objects.filter(category = 'blockbuster')
    top_rating = Movie.objects.order_by('-rating')
    return render(request, "home/index.html", {
        "movie": Movie.objects.all(),
        "home": Banner_Movie.objects.all(),
        'recommended_row1': recommended[0:6],
        'recommended_row2': recommended[7:13],
        'blockbuster_row1': blockbuster[0:6],
        'blockbuster_row2': blockbuster[7:13],
        'top_rating_row1': top_rating[0:6],
        'top_rating_row2': top_rating[7:13],
    })
    if request.method == 'POST':
        if request.POST.get('email') and request.POST.get('password'):
            post=User()
            post.username= request.POST.get('username')
            post.password= request.POST.get('password')
            post.email= request.POST.get('email')
            post.save()
                
            return render(request, 'home/index.html')   

@csrf_protect
def register(request):
    if request.method == 'POST':
        if request.POST.get('email') and request.POST.get('password'):
            post=User()
            post.username= request.POST.get('username')
            post.password= request.POST.get('password')
            post.email= request.POST.get('email')
            post.save()
                
            return render(request, 'home/index.html') 

    else:
        return render(request,'home/index.html')

def action(request):
    action = Movie.objects.filter(Q(gener1 = 'Action')|Q(gener2 = 'Action'))
    return render(request, "home/action.html", {
        "action_row1": action[0:6],
        "action_row2": action[7:12],
        "action_row3": action[13:18],
        "action_row4": action[19:24],
        "action_row5": action[25:30],
    })


def bangla(request):
    bangla = Movie.objects.filter(language = 'Bengali')
    return render(request, "home/bangla.html", {
        "bangla_row1": bangla[0:6],
        "bangla_row2": bangla[7:12],
        "bangla_row3": bangla[13:18],
        "bangla_row4": bangla[19:24],
        "bangla_row5": bangla[25:30],
    })


def single(request):
    single = Movie.objects.get(id = 4)
    popular = Movie.objects.order_by('-rating')
    return render(request, "home/single.html", {
        'single': single,
        'popular': popular[0:7],
    })


def list(request):
    return render(request, "home/list.html", {
        "list": Movie.objects.all()
    })

