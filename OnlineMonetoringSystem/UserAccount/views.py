from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from UserAccount.models import *
from Activity.models import *
from Activity.forms import *
from Dictionary.models import *
from .forms import UserForm,UserProfileInfoForm
from django.template.loader import render_to_string
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import date
notification = 0
def Login(request):
    data =dict()
    notification = 0
    today =  datetime.date.today
    print(today)
    Pending_Activities_list = Pending_Activity.objects.all()
    Comments_list = Comments_Activity.objects.all()
    type = request.user.user_account.user_type
    user1 = {'user':request.user}
    obj = request.user.user_account.user_type
    obj1 = request.user.pk
    Pending_Activities_list1 = Pending_Activity.objects.all().filter(Assigned_To=obj1)
    for time in Pending_Activities_list:
        if date.today() > time.Deadline:
            time.Status = 'completed'
            time.save()


    # Comments_Activities = Comments_Activity.objects.all()
    # Pending_Activities_list2 = Comments_Activity.objects.all().filter(commented_by = request.user,comment_notification = 0 )
    x = Comments_Activity.objects.filter(comment_notification=1)
    y = Comments_Activity.objects.filter(comment_notification=0)
    if type == "administration":

        for b in x:
            if b.comment_notification_by != request.user.username:
                notification=notification+1
                print(notification)
        for a in y:
            notification=notification+1

        for p in Pending_Activities_list:
            if p.Progress !=0:
                if p.progress_notification == 0:
                    notification=notification+1
                elif p.progress_notification == 1:
                    if p.progress_notification_by != request.user.username:
                        notification=notification+1

    else:
       for p in Pending_Activities_list1:
           for q in y:
               if p.id == q.to:
                   notification=notification+1
           for s in x:
               if p.id == s.to:
                   if s.comment_notification_by != request.user.username:
                       notification=notification+1
                       print("why")

           for p in Pending_Activities_list1:
               if p.progress_notification == 0:
                   if p.progress_notification == 0:
                       notification=notification+1
                   elif p.progress_notification == 1:
                       if p.progress_notification_by != request.user.username:
                           notification=notification+1

    date_dict_normal = {'pending_activities':Pending_Activities_list1,'user1':user1}
    date_dict = {'Comments_list':Comments_list,'pending_activities':Pending_Activities_list,'pending_activities1':Pending_Activities_list1,'user1':user1,'type':type,'notification':notification,'today':today}
    # if type == 'administration':
    return render(request, 'UserAccount/home.html', date_dict)
    # else:
    #     return render(request, 'UserAccount/normal_home.html', date_dict_normal)


def control_panel(request):
    user1 = User_Account.objects.all()
    action1 = Action.objects.all()
    activity1 = Activity.objects.all()
    user2=User.objects.all()
    context = {'user1': user1,'user2': user2,'action1':action1,'activity1':activity1}
    return render(request, 'UserAccount/control_panel.html',context)

def login_redirect(request):
    return redirect('/account/login')

def save_all(request,user_form,UserProfileInfo_Form,template_name):
    data =dict()
    if request.method =='POST':
        # user_form = UserForm(request.POST)
        # UserProfileInfo_Form = UserProfileInfoForm(request.POST)
        if user_form.is_valid() or UserProfileInfo_Form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            userProfile = UserProfileInfo_Form.save(commit=False)
            userProfile.user = user
            userProfile.save()
            messages.success(request, 'User successfully registered')
            data['form_is_valid'] = True
            user1 = User_Account.objects.all()
            user2=User.objects.all()
            data['control_panel'] = render_to_string('UserAccount/user_list.html',{'user1':user1,'user2':user2})
        else:
            data['form_is_valid'] = False
            messages.error(request,'Not successfully registered')
            # return redirect('/useraccount/cp')
    # else:
    #     user_form = UserForm()
    #     UserProfileInfo_Form = UserProfileInfoForm()
    args = {'user_form':user_form,'UserProfileInfo_Form':UserProfileInfo_Form}
    data['html_form'] = render_to_string(template_name,args,request=request)
    return JsonResponse(data)


def register_user(request):
    if request.method =='POST':
        user_form = UserForm(request.POST)
        UserProfileInfo_Form = UserProfileInfoForm(request.POST)
    else:
        user_form = UserForm()
        UserProfileInfo_Form = UserProfileInfoForm()
    return save_all(request,user_form,UserProfileInfo_Form,'UserAccount/user_create.html')

def update_user(request,username,id):
    ua = User.objects.get(username=username)
    ua1 = get_object_or_404(User_Account,id=id)
    if request.method =='POST':
        user_form = UserForm(request.POST,instance=ua)
        UserProfileInfo_Form = UserProfileInfoForm(request.POST,instance=ua1)
    else:
        user_form = UserForm(instance=ua)
        UserProfileInfo_Form = UserProfileInfoForm(instance=ua1)
    return save_all(request,user_form,UserProfileInfo_Form,'UserAccount/user_update.html')

def delete_user(request,id,username):
    data = dict()
    ua1 = get_object_or_404(User_Account,id=id)
    ua = User.objects.get(username=username)
    if request.method =='POST':
        ua1.delete()
        ua.delete()
        data['form_is_valid'] = True
        user1 = User_Account.objects.all()
        user2=User.objects.all()
        data['control_panel'] = render_to_string('UserAccount/user_list.html',{'user1':user1,'user2':user2})
    else:
        args = {'ua1':ua1,'ua':ua}
        data['html_form'] = render_to_string('UserAccount/user_delete.html',args,request=request)
    return JsonResponse(data)
