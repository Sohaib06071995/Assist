from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from Dictionary.models import *
from .forms import ActionsForm,ActivitiesForm
from django.template.loader import render_to_string
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect

# here are codes for Dictionary




def save_all_actions(request,action_form,template_name):
    action1 = Action.objects.all()
    data =dict()
    if request.method =='POST':
        if action_form.is_valid():
            action_form.save()
            data['form_is_valid'] = True
            data['control_panel'] = render_to_string('Dictionary/actions.html',{'action1':action1})
        else:
            data['form_is_valid'] = False
    args = {'action_form':action_form}
    data['html_form'] = render_to_string(template_name,args,request=request)
    return JsonResponse(data)

def register_action(request):
    if request.method =='POST':
        action_form = ActionsForm(request.POST)
    else:
        action_form = ActionsForm()
    return save_all_actions(request,action_form,'Dictionary/action_create.html')


def delete_action(request,id):
    data = dict()
    ua1 = get_object_or_404(Action,id=id)
    if request.method =='POST':
        ua1.delete()
        data['form_is_valid'] = True
        action1 = Action.objects.all()
        data['control_panel'] = render_to_string('Dictionary/actions.html',{'action1':action1})
    else:
        args = {'ua1':ua1}
        data['html_form'] = render_to_string('Dictionary/action_delete.html',args,request=request)

    return JsonResponse(data)




def save_all_activities(request,activity_form,template_name):
    activity1 = Activity.objects.all()
    data =dict()
    if request.method =='POST':
        if activity_form.is_valid():
            activity_form.save()
            data['form_is_valid'] = True
            data['control_panel'] = render_to_string('Dictionary/activities.html',{'activity1':activity1})
        else:
            data['form_is_valid'] = False
    args = {'activity_form':activity_form}
    data['html_form'] = render_to_string(template_name,args,request=request)
    return JsonResponse(data)

def register_activity(request):
    if request.method =='POST':
        activity_form = ActivitiesForm(request.POST)
    else:
        activity_form = ActivitiesForm()
    return save_all_activities(request,activity_form,'Dictionary/activity_create.html')


def delete_activity(request,id):
    data = dict()
    ua1 = get_object_or_404(Activity,id=id)
    if request.method =='POST':
        ua1.delete()
        data['form_is_valid'] = True
        activity1 = Activity.objects.all()
        data['control_panel'] = render_to_string('Dictionary/activities.html',{'activity1':activity1})
    else:
        args = {'ua1':ua1}
        data['html_form'] = render_to_string('Dictionary/activity_delete.html',args,request=request)

    return JsonResponse(data)
