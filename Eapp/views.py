from django.contrib import messages
from django.shortcuts import render,redirect
from Eapp.models import notedb,regdb
# Create your views here.
def indexpg(request):
    return render(request,'Index.html')
def homepg(request):
    return render(request,'Home.html')
def notepg(request):
    return render(request,'AddNote.html')
def notedbpg(request):
    if request.method=="POST":
        no=request.POST.get('note')
        nd=request.POST.get('desc')
        obj=notedb(NotesTitle=no, NotesDescription=nd)
        obj.save()
        return redirect(notepg)

def displaynote(request):
    data=notedb.objects.all()
    return render(request,'DisplayNote.html',{'data':data})
def editnote(request,dataid):
    data=notedb.objects.get(id=dataid)
    print(data)
    return render(request,'EditNote.html',{'data':data})
def updatenote(request,dataid):
    if request.method=="POST":
        no=request.POST.get('note')
        nd=request.POST.get('desc')
        notedb.objects.filter(id=dataid).update(NotesTitle=no, NotesDescription=nd)
        return redirect(displaynote)

def delnote(request,dataid):
    data=notedb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaynote)
def aboutpg(request):
    return render(request,'About.html')
def regpg(request):
    return render(request,'Registration.html')
def regpagedb(request):
    if request.method=="POST":
        na=request.POST.get('name')
        em=request.POST.get('email')
        mb=request.POST.get('mob')
        pw=request.POST.get('pwd')
        cp=request.POST.get('cpwd')
        if pw==cp:
            obj = regdb(Name=na, Email=em, MobileNumber=mb, Password=pw, ConfirmPassword=cp)
            obj.save()
            messages.success(request, "User Register Successfully")
            return redirect(logpg)
        else:
            messages.warning(request, "Sorry.... Invalid Username Or Password")
            return redirect(regpg)
    return render(request, 'Registration.html', {'msg': "sorry.... password not matched"})

def logpg(request):
    return render(request,'Login.html')


def logpgdb(request):
    if request.method=="POST":
        na=request.POST.get('name')
        pw = request.POST.get('pwd')
        if regdb.objects.filter(Name=na,Password=pw).exists():
            request.session['name']=na
            request.session['pwd']=pw
            return redirect(homepg)
        else:
            messages.warning(request, "Sorry.... Invalid Username Or Password")
    return render(request, 'Login.html')


def profilepg(request):
    data=regdb.objects.all()
    return render(request,'Profile.html',{'data':data})

def editprofile(request,dataid):
    data=regdb.objects.get(id=dataid)
    print(data)
    return render(request,'Editprofile.html',{'data':data})
def updateprofile(request,dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        mb = request.POST.get('mob')
        regdb.objects.filter(id=dataid).update(Name=na, Email=em, MobileNumber=mb)
        return redirect(profilepg)
def delprofile(request,dataid):
    data=regdb.objects.filter(id=dataid)
    data.delete()
    return redirect(profilepg)
def userlogout(request):
    del request.session['name']
    del request.session['pwd']
    return redirect(indexpg)