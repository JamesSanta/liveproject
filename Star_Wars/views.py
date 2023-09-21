from django.shortcuts import render, redirect, get_object_or_404
from .models import Character
from .forms import CharacterForm
from django.views.generic.list import ListView


def sw_home(request):
    return render(request, 'Star_Wars/sw_home.html')


def add_character(request):
    form = CharacterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
#            return redirect('sw_home')

    content = {'form': form}

    return render(request, 'Star_Wars/add_character.html', content)


#def character_view(request):
#    character_list = Character.objects.all()

#    return render(request, 'Star_Wars/character_view.html', {'character_list': character_list})


class CharacterView(ListView):
    model = Character
    paginate_by = 2
    context_object_name = 'characters'
    template_name = 'Star_Wars/character_view.html'
    ordering = ['name']
