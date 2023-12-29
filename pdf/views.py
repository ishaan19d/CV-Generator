from django.shortcuts import render,redirect
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
# Create your views here.
def accept(request):
    if request.method=="POST":
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        phone = request.POST.get("phone","")
        summary = request.POST.get("summary","")
        degree = request.POST.get("degree","")
        school = request.POST.get("school","")
        university = request.POST.get("university","")
        previous_work = request.POST.get("previous_work","")
        skills = request.POST.get("skills","")
        
        profile = Profile(name=name,email=email,phone=phone,summary=summary,degree=degree,school=school,university=university,previous_work=previous_work,skills=skills)
        profile.save()
        return redirect('complete',profile.pk)#(url_name,int:id)
    return render(request,'pdf/accept.html')

def view(request,id):
    user_profile=Profile.objects.get(pk=id)
    return render(request,'pdf/resume.html',{'user_profile':user_profile})

def download(request,id):
    user_profile=Profile.objects.get(pk=id)
    template=loader.get_template('pdf/resume.html')
    html = template.render({'user_profile':user_profile})
    options={
        'page-size':'Letter',
        'encoding':'UTF-8'
    }
    config=pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
    pdf=pdfkit.from_string(html,False,options=options,configuration=config)
    response=HttpResponse(pdf,content_type='application/pdf')
    filename=user_profile.name+"_resume.pdf"
    response['Content-Disposition']=f'attachment;filename={filename}'
    return response

def complete(request,id):
    return render(request,'pdf/complete.html',{'id':id})