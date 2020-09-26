from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from .forms import AdditionInfoForm
from .forms import Signup, createForm
from .models import AdditionalUserInfo
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from .decorators import allowedusers

# Create your views here.


class register(TemplateView):
    template_name = "userCreateForm.html"

    def post(self, request, *args, **kwargs):
        username = self.request.POST.get('username', 'none')
        print(username)
        # username = username+'hello'
        email = self.request.POST.get('email', 'none')
        print(email)
        # user = User.objects.create_user(
        #     username=username, email=email, password="dummy")
        user = User.objects.create_superuser(
            username=username, email=email, password="dummy")

        # user = self.kwargs.POST('username')
        # print(user)
        return HttpResponse('Registerd')


class usercreation(FormView):
    # Should use form_class only,,otherwise it will throw nonetype object is not callable
    form_class = UserCreationForm
    template_name = "userform.html"

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            # save = form.save(commit=False)
            # print(save.username)
            # save.username = "Dafault"
            # save.save()
            # return HttpResponse('Yeah done')
            return self.form_valid(form, **kwargs)
        else:
            print('inside else')
            return self.form_invalid(form, **kwargs)

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        print('Came to this1.......')
        print(form.cleaned_data['username'])
        user = form.cleaned_data['username']
        form.instance.username = 'rajathi'
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print('Came to this.......')
        # This method is called when invalid form data has been POSTed.
        return super(usercreation, self).form_invalid(form)

    success_url = reverse_lazy('listview')


@allowedusers(['Admin'])
def ExtendedUser(request):
    context = {}
    form = Signup(request.POST or None)
    form2 = AdditionInfoForm(request.POST or None)
    if (form.is_valid() and form2.is_valid()):
        form.save()
        ins = form2.save(commit=False)
        # 1)this is one method to add the user to the another model
        # 2)Using PostSave when the user object is created,that mean sender for the post_save method is User
        # 3) Override the save method to save the user to model
        ins.user = User.objects.get(username=request.user.username)
        ins.save()
        context = AdditionalUserInfo.objects.get(
            user__username=request.user.username)  # user model and username field
        con = context.Hobby
        print('----------------')
        print(con)
        print('----------------')
        return HttpResponseRedirect('/chck/')

    context = {'form': form, 'form2': form2}
    template = "OneToONeUserform.html"
    return render(request, template, context)


def create(request):
    context = {}
    template = "create.html"
    form = createForm(request.POST or None)
    if form.is_valid():
        form1 = form.save(commit=False)
        form1.Blog = User.objects.get(username=request.user.username)
        print(form1.Item)
        print(form1.description)
        form1.save()
        return HttpResponseRedirect('/det/')
    context = {'form': form}
    return render(request, template, context)


def get(request):
    context = {}
    template = "det.html"
    print(request.user)
    use = User.objects.get(username=request.user.username)
    get = use.blog.all()
    from django.utils.translation import gettext_lazy as _
    print(type(_('Check with tme')))
    # print(get)
    # print(get.Item)
    # print(get.description)
    context = {'get': get}
    return render(request, template, context)
