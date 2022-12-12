import os
import random
import time
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import boto3
from main.models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout


# Create your views here.
def page_main(request):
    list_of_numbers = list(range(0, 201))
    random.shuffle(list_of_numbers)

    different_names = ["Ben", "Ann", "Susan", "Emily", "Anthony", "John"]
    # new_row = Task(name="Visited",
    #                duration_in_minutes=random.randint(10, 20))
    #
    # new_row.save()

    all_shopping_items = Shopping_item.objects.all()

    all_rows = Task.objects.all()
    for row in all_rows:
        print(row.name, row.duration_in_minutes)
    return render(request=request,
                  template_name="main/index.html",
                  context={"number": random.randint(0, 100),
                           "list_of_numbers": list_of_numbers,
                           "all_tasks": all_rows,
                           "all_shopping_items": all_shopping_items})

def page_signup(request):
    return render(request=request,
                  template_name="main/page_signup.html",
                  context={})

def page_login(request):
    # all_persons = Person.objects.all()
    # all_tasks = Task.objects.all()
    #
    # michael_tasks = Task.objects.filter(person__first_name__contains="l", person__last_name__endswith="l", name__contains="finish").order_by('-id')
    # print()

    # michael_person = Person.objects.filter(first_name='Michael')
    #
    # if len(michael_person) == 1:
    #     print(f"Found {len(michael_person)}")
    #     print(michael_person[0].first_name, michael_person[0].last_name)
    #     michael_id = michael_person[0].id
    #     print(f"The ID of Michael is {michael_id}")
    #     michael_tasks = Task.objects.filter(person_id=michael_id)
    #     print()

    # for person in all_persons:
    #     print(person.first_name, person.last_name)
    #
    # for task in all_tasks:
    #     print(task.name, task.duration_in_minutes)


    return render(request=request,
                        template_name="main/page_login.html",
                        context={})


def page_pictures(request):

    client = boto3.client('lambda',
                          aws_access_key_id=os.environ['AWS_ACCESS_KEY'],
                          aws_secret_access_key=os.environ['AWS_SECRET_KEY'],
                          )
    response = client.invoke(
        FunctionName='string',
        InvocationType='RequestResponse',
    )

    return render(request=None, template_name="main/page_pictures.html")


def page_about(request):

    p1 = Person(first_name="Susan", last_name="Sontag")
    p2 = Person(first_name="Susan", last_name="Adams")

    r = p1 == p2

    new_book = Book(title="Quiet")
    new_book.save()

    new_author = Author(first_name="Susan", last_name="Cain")
    new_author.save()

    second_author = Author(first_name="Adam", last_name="Grant")
    second_author.save()

    new_book.author.add(new_author)
    # new_author.book_set.add(new_book) THis is the same as the line above
    new_book.author.add(second_author)

    all_tasks = Task.objects.all()
    all_persons = Person.objects.all()
    all_shopping_items = Shopping_item.objects.all()

    return render(request=request, template_name="main/about.html", context={"all_persons": all_persons,
                                                                             "all_tasks": all_tasks,
                                                                             "all_shopping_items": all_shopping_items})


def ajax_say_hello(request):
    if not request.user.is_authenticated:
        return HttpResponse("You can't be here")

    user_authenticated = authenticate(request, username="arthur.gartner@gmail.com", password="password123")
    login(request, user_authenticated)

    # logout(request)
    # username = "arthur.gartner@gmail.com"
    # password = "password123"
    #
    # new_user = User.objects.create_user(username=username,
    #                          email=username,
    #                          password=password
    #                          )
    # new_user.save()
    # request.user.is_authenticated??
    # shopping_item = Shopping_item(item=request.POST.get('shopping_item'), store=request.POST.get('store'), buy_date=request.POST.get('buy_date'))
    # shopping_item.save()
    # print("Hello on the backend")
    return JsonResponse({})

# def ajax_sign_up(request):


