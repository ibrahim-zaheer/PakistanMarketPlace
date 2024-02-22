from django.shortcuts import render,get_object_or_404,redirect
from .models import Category,Item
#add this so login will be require to use certain view function
from django.contrib.auth.decorators import login_required
from .forms import newItemForm
# Create your views here.

def detail(request,pk):
    item = get_object_or_404(Item,pk= pk)
    # to show related objects of the same category and we use [0:3] to display three items at a time
    related_items = Item.objects.filter(category = item.category,is_sold = False).exclude(pk = pk)[0:3]
    return render(request,'detail.html',{'item':item,'related_items':related_items})

@login_required
def new(request):
    if request.method == 'POST':
        form = newItemForm(request.POST,request.FILES)

        if form.is_valid:
            #since we are going to store an image as well we fist save the formn and then save database
            item = form.save(commit= False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail',pk = item.id)
    else:
        form = newItemForm()
    return render(request,'form.html',{'form':form,'title':'new Item'})
