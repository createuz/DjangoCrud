from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from .models import Users
from .forms import UsersForm


def homepage(request):
    people = Users.objects.all()
    context = {
        'request': request,
        'people': people
    }
    return render(request, 'homepage.html', context)


def add_person(request):
    context = {'request': request, 'form': UsersForm()}
    if request.method == 'POST':
        form = UsersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        context['form'] = form
        return redirect('/')
    return render(request, 'add_person.html', context)

#
# def remove_person(request, pk=None):
#     People.objects.filter(id=pk).delete()
#     return redirect('homepage')
#
#
# def edit_person(request, pk):
#     people = People.objects.get(id=pk)
#     form = PeopleForm(instance=people)
#     if request.method == 'POST':
#         form = PeopleForm(request.POST, instance=people)
#         if form.is_valid():
#             form.save()
#         return redirect('/')
#     context = {
#         'action': 'Edit',
#         'form': form,
#         'user': people
#     }
#     return render(request, 'edit_person.html', context)
