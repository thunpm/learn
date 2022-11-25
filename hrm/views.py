from django.shortcuts import render
from django.contrib.auth.hashers import check_password
from .models import User
from django.views.generic import FormView, CreateView, UpdateView, ListView, View, DeleteView
from django import forms
from django.http import HttpResponseRedirect, HttpResponse


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__()
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })


class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__()
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = User
        fields = ['email', 'name', 'gender', 'address']


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/hrm/user/'

    def get(self, *arg, **kwargs):
        return render(self.request, self.template_name, {'form': self.form_class})
    
    def post(self, request, *arg, **kwargs):
        form = self.form_class(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email).first()
        if user and check_password(password, user.password):
            return HttpResponseRedirect(self.success_url)
        else:
            return render(self.request, self.template_name, {'form': form, 'msg': 'Incorrect!'})


class UserListView(ListView):
    template_name = 'user_list.html'
    paginate_by = 5

    def get_queryset(self):
        list_user = User.objects.exclude(role='AD')
        return list_user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
    


class UserCreateView(CreateView):
    template_name = 'user_create.html'
    form_class = UserForm
    success_url = '/hrm/user/'

    def get(self, *arg, **kwargs):
        user_list = User.objects.exclude(role='AD')
        return render(self.request, self.template_name, {'form': self.form_class(), 'user_list': user_list})
    
    def post(self, request, *arg, **kwargs):
        name = request.POST['name']
        email = request.POST['email']
        gender = request.POST['gender']
        address = request.POST['address']
        user = User(email=email, name=name, gender=gender, address=address)
        user.save()
        return HttpResponseRedirect(self.success_url)

        # form invalid
        # form = self.form_class(request.POST)
        # if form.is_valid():
        #     instance = form.save()
        #     ser_instance = serializers.serialize('json', [instance])
        #     return JsonResponse({'instance': ser_instance}, status=200)
        # else:
        #     return JsonResponse({'error': form.errors}, status=400)
    

class UserUpdateView(UpdateView):
    # khong biet ghi de GET khi dung voi FormView
    model = User
    # class_form = User
    fields = ['email', 'name', 'gender', 'address']
    template_name = "user_update.html"
    success_url = '/hrm/user/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = context['form']
        for name in form.fields.keys():
            form.fields[name].widget.attrs.update({
                'class': 'form-control',
            })
        context['form'] = form
        return context


class UserDeleteView(View):
    # dung voi DeleteView khong duoc
    success_url = '/hrm/user/'

    def get(self, *args, **kwargs):
        pk = self.kwargs['pk']
        print(pk)
        User.objects.filter(id=pk).first().delete()
        return HttpResponse({'msg': 'Ok'}, status=200)


