from django.shortcuts import render,redirect
from .models import Job,Person,PersonJobDetail
from .filters import PersonFilter,JobDetailFilter,JobFilter
from django.urls import reverse
from .forms import JobForm,PersonForm,PersonJobDetailForm
# Create your views here.

def show_all_persons_view(request):
    person_list=Person.objects.all()
    person_list_filter=PersonFilter(request.GET,queryset=person_list)
    context={'persons':person_list_filter,}
    return render(request,"show_all_persons.html",context)

def show_all_jobs_view(request):
    job_list=Job.objects.all()
    job_list_filter=JobFilter(request.GET,queryset=job_list)
    context={'jobs':job_list_filter,}
    return render(request,"show_all_jobs.html",context)

def show_all_personjobdetails_view(request):
    jobdetail_list=PersonJobDetail.objects.all()
    jobdetail_list_filter=JobDetailFilter(request.GET,queryset=jobdetail_list)
    context={'jobdetails':jobdetail_list_filter,}
    return render(request,"show_all_personjobdetail.html",context)

def showpersondetail_view(request,pk):
    persondetail=Person.objects.get(pk=pk)
    all_person_jobs=PersonJobDetail.objects.filter(person__id=persondetail.id)
    context={"person_Var":persondetail,
             "all_person_jobs_Var":all_person_jobs,
             }
    return render(request,'show_person_detail.html',context)



def create_person_view(request):
    if request.method=="POST":
        form=PersonForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.save()
            form=PersonForm() #this line is for clear all form fields after submitting
            return redirect(reverse('core:show_all_persons'))
    else:
        form=PersonForm()
    return render(request,'person_create.html',{'person_form':form})



def create_job_view(request):
    if request.method=="POST":
        form=JobForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.save()
            form=JobForm() #this line is for clear all form fields after submitting
            return redirect(reverse('core:show_all_jobs'))
    else:
        form=JobForm()
    return render(request,'job_create.html',{'job_form':form})




def create_personjob_view(request):
    if request.method=="POST":
        form=PersonJobDetailForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.save()
            form=PersonJobDetailForm() #this line is for clear all form fields after submitting
            return redirect(reverse('core:show_all_jobdetails'))
    else:
        form=PersonJobDetailForm()
    return render(request,'personjobdetail_create.html',{'personjobdetail_form':form})
