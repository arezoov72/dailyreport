from django.shortcuts import render,redirect,HttpResponse

from .models import reportdetails
from lotus_cooperators.models import employee
from django.contrib import messages
from django.db.models import Q,F
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,authenticate
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

from .forms import TopicForm
from django.views.generic import UpdateView,DetailView
from django.views import generic

from django.contrib.auth import views as auth_views
from .filters import ReportdetailsFilter
#from .decorators import my_decorator






# Create your views here.
#home page
def home(request):
    return redirect('login/')

from django.contrib.auth import authenticate, login
from django_auth_ldap.backend import LDAPBackend
from django.conf import settings
from django.contrib import messages

from django.template import loader
def loginldap(request,username=None,password=None):
    # username = "m.zolghadr"
    # password = "F@123456"
    

    ldap_backend = LDAPBackend()
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = LDAPBackend().authenticate(request, username, password)
        if user:
            template = loader.get_template('report.html')

            return HttpResponse(template.render())

        
        else:
            messages.error(request, 'نام کاربری یا رمز عبور اشتباه است')
            return redirect('/worksheet/loginldap/')

        print (user)
        print (username, password)
    return render(request,'registration/worksheet_loginldap.html')

    
        

       
    





#from django.utils.decorators import method_decorator

#defining the dashbord of employee and managers

#@method_decorator([login_required(login_url='/worksheet/loginldap/'),my_decorator])
#@my_decorator

@login_required(login_url='/worksheet/login/')
def reportpage2(request):
    
    """Generic class-based view listing books on loan to current user."""
    #paging

    

    

    
 
    #delete repetitive rows by their workdesc
    for row in reportdetails.objects.all().reverse():
        if reportdetails.objects.filter(workdesc=row.workdesc,Date=row.Date).count() > 1:
            row.delete()
    
    if request.user.username=='admin':
        allreports=reportdetails.objects.all().order_by('-Date')
        myFilter=ReportdetailsFilter(request.GET,queryset=allreports)
        allreports=myFilter.qs
        paginator = Paginator(allreports,30)
        page = request.GET.get('page')

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)

        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        form=TopicForm()
        if request.POST:
            id = request.POST.get('id')
            edited_comment = allreports.get(id=id)
            edited_comment.public=request.POST.get('public',False) #public/private
            edited_comment.comment = request.POST.get('comment')
            edited_comment.save()
        return render(request,'report.html',{"allreports":allreports,'form': form,'page':page,'posts':posts,'myFilter':myFilter})


    
    if request.user.has_perm('lotus_cooperators.is_employee') :
        allreports=reportdetails.objects.all().filter(username_id=request.user).order_by('-Date')
        myFilter=ReportdetailsFilter(request.GET,queryset=allreports)
        allreports=myFilter.qs
        paginator = Paginator(allreports,30)
        page = request.GET.get('page')

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)

        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        form=TopicForm()
        if request.POST:
            id = request.POST.get('id')
            edited_comment = allreports.get(id=id)
            edited_comment.public=request.POST.get('public',False) #public/private
            edited_comment.comment = request.POST.get('comment')
            edited_comment.save()
        return render(request,'report.html',{"allreports":allreports,'form': form,'page':page,'posts':posts,'myFilter':myFilter})



        
    elif request.user.has_perm('lotus_cooperators.is_manager') :
        userGroup = Group.objects.get(user=request.user).name
      
        #return render(request,'report.html',{"allreports":allreports,'form': form,'page':page,'posts':posts})


        if userGroup=='تامین مالی':
            allreports=reportdetails.objects.all().filter(managerid=1).order_by('-Date')
            myFilter=ReportdetailsFilter(request.GET,queryset=allreports)
            allreports=myFilter.qs
            return render(request,'report.html',{"allreports":allreports,'myFilter':myFilter})
        elif userGroup=='مالی':
            allreports=reportdetails.objects.all().filter(managerid=3).order_by('-Date')
            myFilter=ReportdetailsFilter(request.GET,queryset=allreports)
            allreports=myFilter.qs
            paginator = Paginator(allreports,30)
            page = request.GET.get('page')

            try:
                posts = paginator.page(page)
            except PageNotAnInteger:
                posts = paginator.page(1)

            except EmptyPage:
                posts = paginator.page(paginator.num_pages)

            form=TopicForm()
            if request.POST:
                id = request.POST.get('id')
                edited_comment = allreports.get(id=id)
                edited_comment.public=request.POST.get('public',False) #public/private
                edited_comment.comment = request.POST.get('comment')
                edited_comment.save()
           
              
            print(userGroup)
            return render(request,'report.html',{"allreports":allreports,'form': form,'page':page,'posts':posts,'myFilter':myFilter})
        
        elif userGroup=='IT':
            allreports=reportdetails.objects.all().filter(managerid_id=40).order_by('-Date')
            myFilter=ReportdetailsFilter(request.GET,queryset=allreports)
            allreports=myFilter.qs
            paginator = Paginator(allreports,30)
            page = request.GET.get('page')

            try:
                posts = paginator.page(page)
            except PageNotAnInteger:
                posts = paginator.page(1)

            except EmptyPage:
                posts = paginator.page(paginator.num_pages)

            form=TopicForm()
            if request.POST:
                id = request.POST.get('id')
                edited_comment = allreports.get(id=id)
                edited_comment.public=request.POST.get('public',False) #public/private
                edited_comment.comment = request.POST.get('comment')
                edited_comment.save()
            print(userGroup) 
            return render(request,'report.html',{"allreports":allreports,'form': form,'page':page,'posts':posts,'myFilter':myFilter})
                  
    return render(request,'report.html')
            
       
       

    

    

    
#submit report
@login_required(login_url='/worksheet/login/')
def details(request):
    allreports=reportdetails.objects.all()
    row=employee.objects.all()
    
    if request.user.is_authenticated:
                
        if request.method=="POST":
            username_id = request.user
            fullname =  request.user.get_full_name()
            tag=request.POST['tag']
            workdesc=request.POST['workdesc']
            Date=request.POST['Date']
            managerid_id=request.POST['managerid_id']
            otherworkdesc=request.POST['otherworkdesc']
            undonework=request.POST.get('undonework',' ')
            comment=request.POST.get('comment',' ')

            
            if otherworkdesc=='ثبت و اتمام' and undonework==' ' :
                otherworkdesc=0
                otherwork=workdesc
            elif otherworkdesc=='ادامه دارد' and undonework==' ':
                otherworkdesc=1
                otherwork=workdesc
            elif otherworkdesc=='ادامه دارد': 
                otherwork=undonework
                otherworkdesc=reportdetails.objects.filter (otherwork=undonework).filter(username_id =request.user).update(otherworkdesc=F('id'))
                otherworkdesc=1
              
            else:
                otherworkdesc=reportdetails.objects.filter(otherwork=undonework).filter(username_id =request.user).filter(otherworkdesc=1).update(otherworkdesc=F('id'))
                otherworkdesc=0
                otherwork=undonework
                

            

           

                
          
  
            report_obj=reportdetails(fullname=fullname,workdesc=workdesc,tag=tag,Date=Date,otherworkdesc=otherworkdesc,username_id=username_id,managerid_id=managerid_id,otherwork=otherwork,undonework=undonework,comment=comment)
            report_obj.save()
            messages.success(request,'درخواست با موفقیت ثبت گردید')
   
        
        return render(request,'details.html',{"row": row ,"allreports":allreports})

class edit_post(UpdateView):
    model=reportdetails
    template_name='edit.html'
    fields=['Date', 'workdesc','tag']
    allreports=reportdetails.objects.all()


           

    context={'allreports':allreports}
   
  



def edit_done(request):
    return render(request,'edit_done.html')


def search_page(request):
    allreports=reportdetails.objects.all()
    userGroup = Group.objects.get(user=request.user).name
    query=request.GET.get("q")
    if query:
        
        if request.user.has_perm('lotus_cooperators.is_employee') :
            allreports=reportdetails.objects.all().filter(username_id=request.user).filter(
                Q(fullname__icontains=query) |
                Q(Date__icontains=query) |
                Q(workdesc__icontains=query) |
                Q(otherwork__icontains=query) |
                Q(tag__icontains=query) 
            
            ).distinct().order_by('-Date')


            return render(request,'reportsearch.html',{"allreports":allreports})
        elif request.user.has_perm('lotus_cooperators.is_manager') :
            userGroup = Group.objects.get(user=request.user).name


            if userGroup=='تامین مالی':
                allreports=reportdetails.objects.all().filter(managerid=2).order_by('-Date')
                return render(request,'report.html',{"allreports":allreports})
            elif userGroup=='مالی':
                allreports=reportdetails.objects.all().filter(managerid=3).order_by('-Date')
                return render(request,'report.html',{"allreports":allreports})

            elif userGroup=='IT':
                allreports=reportdetails.objects.all().filter(managerid=40).filter(

                    Q(fullname__icontains=query) |
                    Q(Date__icontains=query) |
                    Q(workdesc__icontains=query) |
                    Q(otherwork__icontains=query) |
                    Q(tag__icontains=query) 
            
                ).distinct().order_by('-Date')

               
                return render(request,'reportsearch.html',{"allreports":allreports})
            print(query)

    
    print(userGroup)
    return render(request,'reportsearch.html',{"allreports":allreports})

class popup(generic.DetailView):
    model=reportdetails
    template_name='popup.html'
    fields=['Date', 'workdesc','otherwork','tag']
        
    allreports=reportdetails.objects.all()
    context={'allreports':allreports}


        

 
    



def test(request):



    allreports=reportdetails.objects.all()
    
  


    return render(request,'test.html',{"allreports":allreports})
            

def pdftest(request):
    if request.method=='POST':

        importpdf=request.FILES.get('importpdf',0)
    
    return render(request,'importpdf')
    
        




