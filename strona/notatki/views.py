from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NotatkaForm
from django.core.paginator import Paginator

def lista_notatek(request):
    notatki = Note.objects.all().order_by('-priorytet')
    paginator = Paginator(notatki, 5)
    page_number = request.GET.get('page')
    notes = paginator.get_page(page_number)
    return render(request, 'notatki/lista_notatek.html', {'notes': notes})

def dodaj_notatke(request):
    if request.method == 'POST':
        form = NotatkaForm(request.POST)
        if form.is_valid():
            notatka = form.save(commit=False)
            notatka.autor = request.user
            notatka.save()
            return redirect('lista_notatek')
    else:
        form = NotatkaForm()
    return render(request, 'notatki/dodaj_notatke.html', {'form': form})

def szczegoly_notatki(request, pk):
    notatka = get_object_or_404(Note, pk=pk)
    return render(request, 'notatki/szczegoly_notatki.html',
                  {'notatka': notatka})

def edytuj_notatke(request, pk):
    notatka = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NotatkaForm(request.POST, instance=notatka)
        if form.is_valid():
            form.save()
            return redirect('szczegoly_notatki', pk=notatka.pk)
    else:
        form = NotatkaForm(instance=notatka)
    return render(request, 'notatki/edytuj_notatke.html', {'form': form})
