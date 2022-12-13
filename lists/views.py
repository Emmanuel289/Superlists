from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from lists.models import Item, List
# Create your views here.

def home_page(request):
    return render(request, 'home.html')


def view_delete_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'], list=list_)
        return redirect(f'/lists/{list_.id}/')
    if request.method == 'DELETE':
        list_items = Item.objects.all().filter(list=list_)
        for item in list_items:
            item.delete()
        list_.delete()
        return redirect('/')
    return render(request, 'list.html', {'list': list_})

def new_list(request):
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST['item_text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error})
    return redirect(f'/lists/{list_.id}/')


    