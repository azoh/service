from django.shortcuts import render
from .models import Awaria
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import AwariaForm
from django.utils import timezone
from django.shortcuts import redirect
from django.core.paginator import Paginator


@login_required
# blokada dostępu dla grupy Brygadzista, Kierownik te grupy odsyła do /admin/
@user_passes_test(lambda u: u.groups.filter(name='Brygadzista').count() == 0, login_url='/loggedin/')
@user_passes_test(lambda u: u.groups.filter(name='Kierownik').count() == 0, login_url='/loggedin/')
def awarie(request):
    awarie_list = Awaria.objects.filter(status=1).order_by('status','-add_date')

    paginator = Paginator(awarie_list,5)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        awarie = paginator.page(page)
    except(EmptyPage, InvalidPage):
        awarie = paginator.page(paginator.num_pages)

    return render(request, 'awarie.html', {
        'awarie' : awarie
        })
        
@login_required
def awarie_all(request):
    awarie_all_list = Awaria.objects.all().order_by('status','-add_date')

    paginator = Paginator(awarie_all_list,5)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        awarie_all = paginator.page(page)
    except(EmptyPage, InvalidPage):
        awarie_all = paginator.page(paginator.num_pages)

    return render(request, 'awarie_all.html', {
        'awarie_all' : awarie_all
        })


def awarie_new(request):
    if request.method == "POST":
        form = AwariaForm(request.POST)
        if form.is_valid():
            awarie = form.save(commit=False)
            awarie.user = request.user
            awarie.add_date = timezone.now()
            awarie.sur = ""
            awarie.save()
            return redirect('/loggedin/')
    else:
        form = AwariaForm()
    return render(request, 'awarie_edit.html', {'form': form})