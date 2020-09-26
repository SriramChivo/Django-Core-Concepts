from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import personForm
from .models import Person
from django.contrib import messages
from django.db.models import Q
from django.views.generic.base import TemplateView


# Create your views here.

class tempalebasedview(TemplateView):
    # pass
    template_name = "CoreApp/aboutContextBased.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['number'] = 10
    #     return context


def coreApp(request, id=None):
    obj = None
    context = {}
    if 'home' in request.get_full_path() and id == None:
        if(request.method != 'GET'):
            obj = Person.objects.all()
            context['form'] = obj
            template = 'CoreApp/main.html'
        else:
            query = request.GET.get('GetObj', 'None')
            obj = Person.objects.all()
            if query != 'None':
                print('inside query')
                obj = obj.filter(
                    Q(first_name__icontains=query) |
                    Q(last_name__icontains=query)
                )
                context['form'] = obj
                template = 'CoreApp/main.html'
            else:
                obj = Person.objects.all()
                context['form'] = obj
                template = 'CoreApp/main.html'
    if(id != None):
        if('view' in request.get_full_path()):
            obj = get_object_or_404(Person, id=id)
            context['form'] = obj
            template = 'CoreApp/first.html'
        if('update' in request.get_full_path()):
            if request.method == 'POST':
                ob = get_object_or_404(Person, id=id)
                formobj = personForm(request.POST, instance=ob)
                formobj.save(commit=True)
                message = "SuccessFully Updated....!!!"
                messages.success(request, message)
                return HttpResponseRedirect('/home/')
            else:
                ob = get_object_or_404(Person, id=id)
                formobj = personForm(instance=ob)
                context['form'] = formobj
                template = 'CoreApp/create.html'
        if('delete' in request.get_full_path()):
            ob = get_object_or_404(Person, id=id)
            ob.delete()
            message = "SuccessFully Deleted....!!!"
            messages.success(request, message)
            return HttpResponseRedirect('/home/')
    if('create' in request.get_full_path()):
        if(request.method == 'POST'):
            formobj = personForm(request.POST)
            formobj.save(commit=True)
            message = "SuccessFully Created....!!!"
            messages.success(request, message)
            return HttpResponseRedirect('/create/')
        else:
            context['form'] = personForm()
            template = 'CoreApp/create.html'
    return render(request, template, context)


# def main(request):
#     form = Person.objects.all()
#     context = {
#         'form': form
#     }
#     template = 'CoreApp/main.html'

#     return render(request, template, context)


# def first(request, id=None):
#     ll = get_object_or_404(Person, id=id)
#     # ll = Person.objects.all()
#     context = {'i': ll}
#     template = 'CoreApp/first.html'
#     return render(request, template, context)


# def create(request, id):
#     ll = get_object_or_404(Person, id=id)
#     if request.method == 'POST':
#         print('Insode post')
#         formObj = personForm(request.POST or None, instance=ll)
#         if formObj.is_valid():
#             print('Insde valis')
#             formObj.save(commit=True)
#             return HttpResponse('Submitted Successfukky....!!!!')
#     else:
#         formObj = personForm(request.POST or None, instance=ll)

#     # ob = personForm()
#     context = {'form': formObj}
#     template = 'CoreApp/create.html'
#     return render(request, template, context)
