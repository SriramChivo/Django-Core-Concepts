from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import login, FormModel
from .forms import loginForm, Formclass, FormclassModel
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.contrib import messages
from django.utils.text import slugify
from django.views.generic.edit import FormView, UpdateView, CreateView
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
# Create your views here.


class tempview(TemplateView):
    # template_name = 'classBasedCoreApp/TemplateBasics.html'
    template_name = 'classBasedCoreApp/tempinherit.html'
    # context = {'obj': 'Hello'} this line wont effect anything ! this not function based view to send context like this
    #  #we should send context data to the templateview using function get_context_data() method only

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # temp = '''

        #         <b>
        #             yes i am Bold
        #         </b>
        # '''
        # floati = 12.34567
        # liVal = ['first', 'second']
        # messages = [x for x in range(0, 102)]
        # context = {'obj': temp, 'float': floati,
        #            'value': liVal, 'messages': messages}
        context = {'hello': 'Hello World', 'Inheritvalue': [
            'first', 'second'], 'Inheritobj': "<b>Inherited from the next template</b>", 'InheritFloat': 12.34567, 'emptyforloop': []}
        return context


def functionForm(request):
    context = {}
    # form = FormclassModel(initial={'firstname': request.user.username})
    form = FormclassModel(usertext='default')
    context['form'] = form
    template = 'classBasedCoreApp/FormCreate.html'
    # print('onget')
    # print(request.GET)

    if request.method == 'POST':
        print('-------------------------------------')
        print(request.POST)
        form = FormclassModel(data=request.POST, usertext='default')
        print(form)
        if form.is_valid():
            print('Inside postttttttttt--------------')
            obj = form.save(commit=False)
            print('before--------------')
            print(form.save())
            print(obj)
            print(obj.Age)
            print('After--------------')
            obj.Age = 12
            print(form.instance.firstname)
            print(form.instance.lastname)
            form.save(commit=True)  # or obj.save()
            messages.success(request, 'Created Succesfuly!!!')
            return HttpResponseRedirect('/listview/')
        else:
            context['form'] = form
    return render(request, template, context)


class projectForm(FormView):
    model = FormModel
    # form.forms and form view to validate the form records and saving into models
    # usually form.forms will not have save() method to save the form fields to the db(models) for that we need to use forms.Modelform
    # so but we acheived the saving the form view fields to db using below metho
    form_class = Formclass
    # form_class = FormclassModel #if we use modeform as form_class we can use form.save methos to populate fields auto
    # fields=['firstname','lastname','Age']
    success_url = reverse_lazy('listview')
    template_name = 'classBasedCoreApp/FormCreate.html'

    # def form_valid(self, form=form_class):
    #     form.save()   #this form submitting viamodeform sos much work not needed
    #     return super().form_valid(form)
    def get(self, request, *args, **kwargs):
        print('Inside GET Guys')
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        print(dir(form))
        if(form.is_valid()):
            # model1 = model()
            # print(dir(model1))
            print('yes')
            model1 = self.model()
            # model1 = model() will throw an error that model is not defined o we need to set as argument to function model=model
            # print(self.model()) or model=model()
            # print(dir(model1))
            print('yes')
            print('Inside POST Guys')
            # model = self.model  # we need to instantiate the model to an object
            model1.firstname = form.cleaned_data.get(
                'firstname', 'none')
            print('--------------')
            print(model1.firstname)  # Adding fields to model
            model1.lastname = slugify(
                form.cleaned_data.get('lastname', 'none'))
            model1.Age = form.cleaned_data.get('Age', 'none')
            model1.save(self)
            return HttpResponse('nothing')

    # def form_valid(self, form, model=model, *args, **kwargs):
    #     # return self.form_invalid(form)  # to show the invalid form again to the user should use this line
    #     # self.model.lastname = slugify(un)
    #     # un = form.cleaned_data.get('lastname', 'none')
    #     # print(self.model.lastname)
    #     model = model()  # we need to instantiate the model to an object
    #     model.firstname = form.cleaned_data.get(
    #         'firstname', 'none')
    #     print('--------------')
    #     print(model.firstname)  # Adding fields to model
    #     model.lastname = slugify(form.cleaned_data.get('lastname', 'none'))
    #     model.Age = form.cleaned_data.get('Age', 'none')
    #     model.save(self)  # save the model
    #     return super().form_valid(form)

    def get_initial(self, model=FormModel):
        initial = super(projectForm, self).get_initial()
        initial['firstname'] = self.request.user.username
        return initial


class loginupdateview(UpdateView):
    model = login
    fields = ['username', 'description', 'about', 'remarks']
    template_name_suffix = '_update_view'


class loginformview(FormView):
    model = login
    form_class = loginForm
    success_url = '/listview/'
    template_name = 'classBasedCoreApp/login_formview.html'

    def form_valid(self, form):
        return super().form_valid(form)


class loginCreateView(SuccessMessageMixin, CreateView):
    model = login
    # fields = ['username', 'description', 'about']
    form_class = loginForm
    success_url = '/listview/'

    success_message = "User was created successfully"

    # def get_success_message(self, cleaned_data):
    #     return self.success_message % dict(
    #         cleaned_data,
    #         calculated_field=self.object.username,
    #     )

    def form_valid(self, form, model=model):
        print(model)
        print(self.fields)
        print(form)
        print('------------------------')
        print(form.instance)
        print('------------------------')
        un = form.cleaned_data.get('username', 'none')
        # print(str(self.request.user.username) + 'USername')
        form.instance.about = slugify(form.instance.about)
        # print(un)
        return super().form_valid(form)


class loginDetailView(DetailView):
    model = login
    # pk_url_kwarg = 'id'

    def get_queryset(self, model=model):
        # qs = model.objects.filter(username__icontains='c')  #restrict by showing only detailview for matched fields , show404 fot unmatched
        qs = model.objects.filter(pk=self.kwargs.get('pk'))
        # usual django return this querset filter by id given thru url no customization
        # print(qs)
        return qs

    # not needed to give this context until you dont need to pass other texts or objects with django object to render on template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print('---------------------')
        # print(context)
        # i am showing extra field to render in my template
        context['dummy'] = 'dummy'
        return context

    # def get_context_data(self, model=model, ** kwargs):
    #     print('------------------')
    #     # print(context)
    #     print('------------------')
    #     context = {'login': model.objects.filter(
    #         pk=self.kwargs.get('pk'))}
    #     print('-----------------')
    #     print(context)
    #     print(context['login'])
    #     return context


class loginListView(ListView):
    model = login
    # queryset = model.objects.all().order_by('username')

    def get_queryset(self, model=model):
        # self.kwargs.get('orderby','username')
        order = self.request.GET.get('orderby', 'username')
        filter_val = self.request.GET.get('filter', '')
        # print(model.objects.all())
        # print(order)
        # print(filter_val)
        if(order == 'Descendingbyid'):
            new_context = self.model.objects.all().filter(
                Q(username__icontains=filter_val) |
                Q(description__icontains=filter_val) | Q(about__icontains=filter_val)).order_by('-id')
        elif(order == 'updateTime'):
            new_context = self.model.objects.all().filter(
                Q(username__icontains=filter_val) |
                Q(description__icontains=filter_val) | Q(about__icontains=filter_val)).order_by('-updateTime')
        elif(order == 'publishedTime'):
            new_context = self.model.objects.all().filter(
                Q(username__icontains=filter_val) |
                Q(description__icontains=filter_val) | Q(about__icontains=filter_val)).order_by('-publishedTime')
        else:
            new_context = self.model.objects.all().filter(
                Q(username__icontains=filter_val) |
                Q(description__icontains=filter_val) | Q(about__icontains=filter_val)).order_by(order)
        return new_context

    # def get_queryset(self):
    #     return self.model.objects.all().filter(username='Sriram')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["object_list"] = self.model.objects.all().filter(
    #         username__icontains='c')
    #     print(context["object_list"])
    #     return context
