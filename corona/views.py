from django.shortcuts import render,redirect
from .models import corona,update,rugi
import smtplib as s
roy = corona.objects.get(id=1)
upd = update.objects.get(id=1)
    
context = {
        'test': roy.test,
        'deth': roy.deth,
        'affected': roy.affected,
        'recovared': roy.recovared,
        'total_deth': roy.total_deth,
        'total_affected': roy.total_affected,
        'total_test': roy.total_test,
        'total_recovared': roy.totel_recovared,
        'update_news': upd.update_news
    }
def home(request):
   
    return render(request, "home.html", context)

def em(request):

    email = str(request.POST['email'])
    ob = s.SMTP("smtp.gmail.com",587)
    ob.starttls()
    ob.login("simantarr77@gmail.com","fdsa4321@")
    data = corona.objects.get(id=1)
    messeage= f"deth={data.deth} \n recovared={data.recovared}\n affected ={data.affected} \n test={data.test}\n  Stay Home stay safe  \n For Help Call Us  \n01682921257"
    listf=[email]
    
    ob.sendmail("simantarr77@gmail.com",listf,messeage)
    ob.quit
   
    
    return redirect("/")


def aff(request):
    return render(request,"aff.html")   
  
def subb(request):
    name = request.POST["name"]
    postcode = request.POST["postcode"]
    number = request.POST["number"]
    problem = request.POST["problem"]
    password = request.POST["password"]
    rugis = rugi(name=name,postcode=postcode,number=number,problem=problem,password=password)
    rugis.save()
    return redirect("/")
def cng(request):
    pnum = request.POST["lognum"]
    logpass = request.POST["logpass"]
    login = rugi.objects.get(number=int(pnum),password=logpass)
    p1= login.password 
    if logpass==p1:

        
        
        context = {
        'postcode':login.postcode,
        'name':login.name ,
        'problem':login.problem

        }
        return render(request,"login.html",context)
    else:
        return redirect("/")
def cngp(request):
    nname = request.POST["nname"]
    npostcode = request.POST["npostcode"]
    onumber = request.POST["onumber"]
    nproblem = request.POST["nproblem"]
    npassword = request.POST["npassword"]
    nnumber = request.POST["nnumber"]
    nlogin = rugi.objects.get(number=int(onumber))
    nlogin.name = nname
    nlogin.postcode = npostcode
    nlogin.password = npassword
    nlogin.problem = nproblem
    nlogin.number = nnumber
    nlogin.save()
    return redirect("/")
