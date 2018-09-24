from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from Activity.models import Pending_Activity,Comments_Activity
from .forms import ActivitiesForm,Dashboard_Comment_Form,ProgressForm
from django.template.loader import render_to_string
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect


# Create your views here.
ACTIVITY_TYPE = [
('pending','Pending'),
('ongoing','Ongoing'),
('completed','Completed'),
('submitted','Submitted'),
]
notification = 0
def Login(request):
    data =dict()
    Pending_Activities_list = Pending_Activity.objects.all()
    date_dict = {'pending_activities':Pending_Activities_list}
    return render(request, 'Dashboard/dashboard.html', date_dict)

def save_all_activitiess(request,activities_form,template_name):
    Pending_Activities_list = Pending_Activity.objects.all()
    activities_form.instance.Assigned_By = request.user.username

    data = dict()
    if request.method =='POST':
        request.POST = request.POST.copy()
        if activities_form.is_valid():
            activities_form.save()
            data['form_is_valid'] = True
            data['control_panel'] = render_to_string('Activities/pending_list.html',{'pending_activities':Pending_Activities_list,'pending_activities1':Pending_Activities_list})
        else:
            data['form_is_valid'] = False

    args = {'activities_form':activities_form}
    data['html_form'] = render_to_string(template_name,args,request=request)
    return JsonResponse(data)


def register_activitiess(request):
    if request.method =='POST':
        activities_form = ActivitiesForm(request.POST)
    else:
        activities_form = ActivitiesForm()
    return save_all_activitiess(request,activities_form,'Activities/activities_create.html')


def update_activitiess(request,id):
    ua1 = get_object_or_404(Pending_Activity,id=id)
    if request.method =='POST':
        activities_form = ActivitiesForm(request.POST,instance=ua1)
    else:
        activities_form = ActivitiesForm(instance=ua1)
    return save_all_activitiess(request,activities_form,'Activities/activities_update.html')


def delete_activitiess(request,id):
    data = dict()
    ua1 = get_object_or_404(Pending_Activity,id=id)
    if request.method =='POST':
        ua1.delete()
        data['form_is_valid'] = True
        Pending_Activities_list = Pending_Activity.objects.all()
        data['control_panel'] = render_to_string('Activities/pending_list.html',{'pending_activities':Pending_Activities_list})
    else:
        args = {'ua1':ua1}
        data['html_form'] = render_to_string('Activities/activities_delete.html',args,request=request)
    return JsonResponse(data)



def save_all_comments(request,dashboard_form,comments_form,template_name):
    notification =0
    type = request.user.user_account.user_type
    Comments_list = Comments_Activity.objects.all()
    Progress_list = Pending_Activity.objects.all()
    print(request.user.user_account.image)
    data = dict()
    if request.method =='POST':
        if comments_form.is_valid():
            comments_form.instance.to = dashboard_form.instance.id
            comments_form.instance.commented_by = request.user
            comments_form.instance.image = request.user.user_account.image
            comments_form.save()
            print("Saved")
            data['form_is_valid'] = True
            data['control_panel'] = render_to_string('Dashboard/comments_list.html',{'dashboard_form':dashboard_form,'comments_form':comments_form,'Comments_list':Comments_list})
        else:
            data['form_is_valid'] = False
    args = {'dashboard_form':dashboard_form,'comments_form':comments_form,'Comments_list':Comments_list,'Progress_list':Progress_list,'type':type}
    data['html_form'] = render_to_string(template_name,args,request=request)
    return JsonResponse(data)

def show_dashboard(request,id):
    ua3 = get_object_or_404(Pending_Activity,id=id)
    if request.method =='POST':
        dashboard_form = ActivitiesForm(request.POST,instance=ua3)
        comments_form = Dashboard_Comment_Form(request.POST)
    else:
        dashboard_form = ActivitiesForm(instance=ua3)
        comments_form = Dashboard_Comment_Form()
    return save_all_comments(request,dashboard_form,comments_form,'Dashboard/show_dashboard.html')



def update_status(request,id):
    data = dict()
    ua1 = get_object_or_404(Pending_Activity,id=id)
    if request.method =='GET':
        status_form = ActivitiesForm(request.POST,instance=ua1)
        Comments_list = Comments_Activity.objects.all()
        comments_form = Dashboard_Comment_Form(request.POST)
        ua1.Status ='ongoing'
        print(ua1.Status)
        ua1.save()
        data['form_is_valid'] = True
        data['control_panel'] = render_to_string('Dashboard/comments_list.html',{'Comments_list':Comments_list})
    else:
        data['form_is_valid'] = False
    args = {'status_form':status_form,'comments_form':comments_form,'Comments_list':Comments_list}
    data['html_form'] = render_to_string('Dashboard/comments_list.html',args,request=request)
    return JsonResponse(data)

# pregress

def save_progress(request,progress_form,dashboard_form,template_name):
    Progress_list = Pending_Activity.objects.all()
    data = dict()
    if request.method =='POST':
        if progress_form.is_valid():
            progress_form.instance.progress_notification = 0
            progress_form.instance.progress_notification_by = ''
            progress_form.instance.progress_by = request.user
            progress_form.save()
            print("Saved")
            data['form_is_valid'] = True
            data['width'] = dashboard_form.instance.Progress
            data['control_panel'] = render_to_string('Dashboard/progress.html',{'progress_form':progress_form,'dashboard_form':dashboard_form,'Progress_list':Progress_list})
        else:
            data['form_is_valid'] = False
    args = {'progress_form':progress_form}
    data['html_form'] = render_to_string(template_name,args,request=request)
    return JsonResponse(data)

def progress_create(request,id):
    ua3 = get_object_or_404(Pending_Activity,id=id)
    dashboard_form = ActivitiesForm(request.POST,instance=ua3)
    if request.method =='POST':
        progress_form = ProgressForm(request.POST,instance=ua3)
    else:
        progress_form = ProgressForm(instance=ua3)
        dashboard_form = ActivitiesForm(instance=ua3)
    return save_progress(request,progress_form,dashboard_form,'Dashboard/progress_form.html')

def update_progress_notification(request,id):
    data = dict()
    ua1 = get_object_or_404(Pending_Activity,id=id)
    if request.method =='GET':
        commentProgress_form = ActivitiesForm(request.POST,instance=ua1)
        Comments_list = Comments_Activity.objects.all()
        comments_form = Dashboard_Comment_Form(request.POST)
        ua1.progress_notification = ua1.progress_notification + 1
        ua1.progress_notification_by = request.user.username
        print(ua1.progress_notification)
        ua1.save()
        data['form_is_valid'] = True
        data['control_panel'] = render_to_string('Dashboard/comments_list.html',{'Comments_list':Comments_list})
    else:
        data['form_is_valid'] = False
    args = {'commentProgress_form':commentProgress_form,'comments_form':comments_form,'Comments_list':Comments_list}
    data['html_form'] = render_to_string('Dashboard/comments_list.html',args,request=request)
    return JsonResponse(data)

def update_comment_notification(request,id):
    data = dict()
    ua1 = get_object_or_404(Comments_Activity,id=id)
    if request.method =='GET':
        commentProgress_form = ActivitiesForm(request.POST)
        Comments_list = Comments_Activity.objects.all()
        comments_form = Dashboard_Comment_Form(request.POST,instance=ua1)
        ua1.comment_notification = ua1.comment_notification + 1
        ua1.comment_notification_by = request.user.username
        print(ua1.comment_notification)
        ua1.save()
        data['form_is_valid'] = True
        data['control_panel'] = render_to_string('UserAccount/notification.html',{'Comments_list':Comments_list})
    else:
        data['form_is_valid'] = False
    args = {'commentProgress_form':commentProgress_form,'comments_form':comments_form,'Comments_list':Comments_list}
    data['html_form'] = render_to_string('base.html',args,request=request)
    return JsonResponse(data)
