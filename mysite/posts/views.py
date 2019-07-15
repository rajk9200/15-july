from django.shortcuts import render

# Create your views here.
from .models import Posts

def add_post(request):
    if request.method=='POST':
        title1 =request.POST.get('title')
        desc1 =request.POST.get('desc')

        p=Posts()
        p.title=title1
        p.desc=desc1

        p.save()

        # p=Posts(title=title1,desc=desc1)
        # p.save()

        # Posts.objects.create(title=title1,desc=desc1)

        print('form save ho gya')

        print(title1,desc1)






    # if 'delete' in request.POST:
    #     pass
    #
    # if 'addpost' in request.POST:
    #     pass


    return render(request,'add-post.html')