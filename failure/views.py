from django.shortcuts import render
from .models import Awaria
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import AwariaForm
from django.utils import timezone
from django.shortcuts import redirect


@login_required
# blokada dostępu dla grupy Brygadzista, Kierownik te grupy odsyła do /admin/
@user_passes_test(lambda u: u.groups.filter(name='Brygadzista').count() == 0, login_url='/loggedin/')
@user_passes_test(lambda u: u.groups.filter(name='Kierownik').count() == 0, login_url='/loggedin/')
def awarie(request):
    awarie = Awaria.objects.filter(status=1).order_by('status','-add_date')

    return render(request, 'awarie.html', {
        'awarie' : awarie
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