from django.shortcuts import render
from django.contrib.auth.hashers import check_password
from .models import User
from django.views.generic import CreateView, UpdateView, ListView, View, DeleteView
from django.shortcuts import redirect
from django.http import HttpResponseRedirect


class LoginView(View):

    def get(self, request, *arg, **kwargs):
        return render(request, 'login.html')
    
    def post(self, request, *arg, **kwargs):
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            if email and password:
                user = User.objects.filter(email=email).first()
                if user and check_password(password, user.password):
                    return redirect('/hrm/user/')
                    # return render(request, 'user_list.html')
                else:
                    return render(request, 'login.html', {'res': False, 'msg': 'Incorrect!'})
        return render(request, 'login.html')


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    

class UserUpdateView(UpdateView):
    model = User
    fields = ['email', 'name', 'gender', 'address']
    template_name = "user_update.html"
    success_url = '/hrm/user/'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.name = request.POST['name']
        self.object.gender = request.POST['gender']
        self.object.address = request.POST['address']
        self.object.save()
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genders'] = User.GENDER
        return context


# chuyen qua template confirm_delete
class UserDeleteView(DeleteView):
    model = User
    template_name = "user_confirm_delete.html"
    success_url = '/hrm/user/'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.success_url)


