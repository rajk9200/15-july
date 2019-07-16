from django.shortcuts import render
from django.contrib import messages
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
        messages.success(request, f'{title1}, Post save successfully...')
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


def show_posts(request):
    # post =Posts.objects.all()
    post =Posts.objects.all().order_by('-pk')
    # post =Posts.objects.all().last()
    dic ={
        'post':post
    }
    return render(request,'show-posts.html',dic)


"""

queryset =use loop

Posts.objects.all()    return Queryset [<obj>]
Posts.objects.filter() return Queryset [<obj>]

Posts.objects.first()  return <obj>
Posts.objects.last()  return <obj>
Posts.objects.count()  return <obj>
Posts.objects.get()  return <obj>



"""