from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as auth_login
from .models import Account,upimages,likefeed,dislikefeed
from itertools import chain

name = []
searched=[]
count=[]
usrid=[]
def home(request):
    searched.clear()
    if request.user.is_anonymous:
        print(request.user.is_authenticated)
        return redirect('logi')
    else:
        if(Account.objects.get(username=name[0]).following_count!=0):
            # print(Account.objects.get(username=name[0]).followings.all())
            acco=Account.objects.get(username=name[0]).followings.all()
            uacc=[]
            l=[]
            c=0
            for a in acco:
                l.append(a.username)
            for u in l:
                uacc.append(upimages.objects.filter(username=u))
                c=c+1
            uacc=list(chain.from_iterable(set(uacc)))
            print("uacc is",uacc)
            
            post={
            "acc":uacc,
            "ac":upimages.objects.filter(username=name[0]),
        
            }
            return render(request,'myapp/home1.html' ,{"post":post})
        else:
            print("in else")
            ac=upimages.objects.filter (username=name[0])
            print(ac)
            return render(request,'myapp/home.html' ,{"post":ac})
def logi(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        password=request.POST.get('password')
        usrid.append(0)
        name.append(uname)
        user=authenticate(username=uname,password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request,'myapp/login.html')
    return render(request,'myapp/login.html')

def sign(request):
    if request.method=='POST':
        u=User()
        u.email=request.POST.get('email')
        u.username=request.POST.get('username')
        u.password=request.POST.get('password')
        u.set_password(u.password)                          # Added this line
        u.save()
        name.append(u.username)
        acc=Account()
        acc.username=u.username
        acc.save()
        return redirect('home')
    return render(request,'myapp/signup.html')

def index(request):
    return render(request,'myapp/index.html')
def write(request):
    if request.method=="POST":
        
        ac=upimages()
        ac.username=name[0]
        ac.images=request.FILES['image']
        ac.text=request.POST.get('txt')
        ac.save()
    return render(request,'myapp/write.html')


def createpost(request):
    return render(request,'myapp/createpost.html')

def logou(request):
    logout(request)
    name.clear()
    count.clear()
    return render(request,'myapp/index.html')


def search(request):
    if(request.method=="POST"):
        searched.clear()
        user=request.POST.get('search')
        try:
            usersearched=Account.objects.filter(username=user)
        except Exception as e:
            return HttpResponse(e)
        searched.append(user)
        account=Account.objects.get(username=name[0])
        try:
            acc=Account.objects.get(username=user)
        except Exception as f:
            return HttpResponse(f)
        if(Account.objects.get(username=name[0])==Account.objects.get(username=user)):
            usersearched=Account.objects.filter(username=user)
            return render(request,'myapp/srchown.html',{"searched":usersearched})
        else:
            if(Account.objects.get(username=user)):
                print("trueee")
                if(account.followings.filter(id=acc.id)):
                    print("truee")
                    return render(request, 'myapp/acceptedreq.html',{"searched":usersearched})
                    return HttpResponse("Oops!...user not found")
                else :
                    print("true")
                    return render(request,'myapp/searchedusr.html',{"searched":usersearched})
            else:
                return HttpResponse("Oops!..user not found")
    return render(request,'myapp/searchedusr.html')

def accept(request):
    if request.method=="POST":
        account=Account.objects.get(username=name[0])
        account.following_count=account.following_count+1
        account.save()
        return render(request,'myapp/acceptedreq.html')
    return render(request,'myapp/acceptedreq.html')  

def send(request):
        print(searched[0])
        account=Account.objects.get(username=searched[0])
        print(account.id)
        acc=Account.objects.get(username=name[0])
        print(account)
        print(account.followers.all())
        # print(account.followers[0])
        if(account.followers.all()!=Account.objects.get(username=name[0])):
            acc.following_count=acc.following_count+1
            acc.followings.add(Account.objects.get(id=account.id))
            acc.save()
            account.follower_count=account.follower_count+1
            account.followers.add(Account.objects.get(id=acc.id))
            account.save()
            return redirect('home')
        else:
            return render(request,'myapp/acceptedreq.html')

def viewpost(request):
    ac=upimages.objects.filter(username=searched[0])
    m=[]
    m.append(ac)
    m=list(chain.from_iterable(set(m)))
    return render(request,'myapp/hom.html',{"post":m})

def unfollow(request):
    acc=Account.objects.filter(username=searched[0])
    srchacc=Account.objects.get(username=searched[0])
    ac=Account.objects.get(username=name[0])
    ac.followings.remove(srchacc)
    ac.following_count=ac.following_count-1
    srchacc.followers.remove(ac)
    srchacc.follower_count=srchacc.follower_count-1
    srchacc.save()
    ac.save()
    return render(request,'myapp/searchedusr.html',{"searched":acc})

def edipo(request):
    if request.method=="POST":
        acc=Account.objects.get(username=name[0])
        acc.image =request.FILES['fil']
        acc.username=request.POST.get('username')
        acc.text=request.POST.get('txt')
        ac=User.objects.get(username=name[0])
        ac.username=acc.username
        ac.save()
        a=upimages.objects.filter(username=name[0])
        for i in a:
            i.username=acc.username
            i.save()
        acc.save()
        return render(request,'myapp/reqsent.html')
def editpro(request):
    acc=Account.objects.filter(username=name[0])
    return render(request,'myapp/editprofile.html',{"mypro":acc})


def like(request):
    if request.method=="POST":
        likeip=request.POST.get('likeip')
        try:
            item=likefeed.objects.get(username=name[0],like_id=likeip)
            if(item.count==1):
                print("in if")
                acc=upimages.objects.get(id=likeip)
                acc.like_count=acc.like_count-1
                item.count=0
                item.save()
                acc.save()
            else:
                print("in else")
                acc=upimages.objects.get(id=likeip)
                acc.like_count=acc.like_count+1
                item.count=1
                item.save()
                acc.save()
        except Exception as e:
            print("in exception")
            likec=likefeed()
            likec.username=name[0]
            likec.like_id=likeip
            likec.count=1
            acc=upimages.objects.get(id=likeip)
            acc.like_count=acc.like_count+1
            acc.save()
            likec.save()


        


    return redirect('home')
          
def dislike(request):
    if request.method=="POST":
        likeip=request.POST.get('unlikeip')
        try:
                item=dislikefeed.objects.get(username=name[0],dislike_id=likeip)
                if(item.count==0):
                    acc=upimages.objects.get(id=likeip)
                    acc.dislike_count=acc.dislike_count+1
                    item.count=1
                    item.save()
                    acc.save()
                else:
                    acc=upimages.objects.get(id=likeip)
                    acc.dislike_count=acc.dislike_count-1
                    item.count=0
                    item.save()
                    acc.save()
        except Exception as e:
                likec=dislikefeed()
                likec.username=name[0]
                likec.dislike_id=likeip
                likec.count=1
                acc=upimages.objects.get(id=likeip)
                acc.dislike_count=acc.dislike_count+1
                acc.save()
                likec.save()
    return redirect('home')  
              


def about(request):
    return render(request,'myapp/about.html')
# Create your views here.

  