from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from lists.forms import ItemForm
from lists.models import Item, List
# Create your views here.

def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})

def view_delete_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    error = None
    if request.method == 'POST':
        try:
            item = Item.objects.create(text=request.POST['text'], list=list_)
            item.full_clean()
            item.save()
            return redirect(list_)
        except ValidationError:
            item.delete()
            error = "You can't have an empty list item"
    if request.method == 'DELETE':
        list_items = Item.objects.all().filter(list=list_)
        for item in list_items:
            item.delete()
        list_.delete()
        return redirect('/')
    return render(request, 'list.html', {'list': list_, 'error': error})

def new_list(request):
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST['text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        item.delete()
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error})
    return redirect(list_)