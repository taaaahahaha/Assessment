from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_exempt
from accounts.models import userProfile, Expense


@csrf_exempt
def home(request):

    print(request.user)

    if not request.user.is_authenticated:
        return redirect('/login')

    try:
        profile = userProfile.objects.get(user=request.user)
    except:
        return HttpResponse('Your Profile has not been created')

    user = userProfile.objects.get(user=request.user)

    # print(user.role,type(user.role))
    if user.role == '1':
        ins = Expense.objects.filter(created_by=user)
    else:
        ins = Expense.objects.all()

    context = {
        'expenses': ins,
        'len': len(ins)
    }
    return render(request, 'view_expense.html', context=context)


@csrf_exempt
def login(request):

    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        print(username, password)

        try:
            user = User.objects.get(username=username, password=password)
        except:
            return HttpResponse('Invalid Credentials')

        print(user)

        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            return HttpResponse('Invalid Credentials')

    context = {}
    return render(request, 'login.html', context=context)


@csrf_exempt
def logout(request):
    auth_logout(request)
    return redirect('/')


@csrf_exempt
def expense(request):

    if request.method == 'POST':
        data = {
            'name': request.POST['name'],
            'description': request.POST['description'],
            'category': request.POST['category'],
            'date_of_expense': request.POST['date_of_expense'],
            'amount': request.POST['amount'],
            'created_by': userProfile.objects.get(user=request.user)
        }

        ins = Expense.objects.create(**data)
        ins.save()

        return redirect('/')

    context = {}
    return render(request, 'create_expense.html', context=context)



@csrf_exempt
def update(request, pk):
    expense = Expense.objects.get(id=pk)
    if expense.created_by.user != request.user:
        return HttpResponse("You cannot Update or delete other's data")
    
    print(pk)
    if request.method == 'POST':
        data = {
            'name': request.POST['name'],
            'description': request.POST['description'],
            'category': request.POST['category'],
            'date_of_expense': request.POST['date_of_expense'],
            'amount': request.POST['amount'],
            'created_by': userProfile.objects.get(user=request.user)
        }

        Expense.objects.filter(id=pk).update(**data)
        return redirect('/')
    
    context = {
        'object' : Expense.objects.get(id=pk),
        'date' : Expense.objects.get(id=pk).date_of_expense.strftime("%Y-%m-%d")
    }
    print(context)
    return render(request, 'update_expense.html', context=context)




@csrf_exempt
def delete(request, pk):
    expense = Expense.objects.get(id=pk)
    if expense.created_by.user != request.user:
        return HttpResponse("You cannot Update or delete other's data")
    expense.delete()
    return redirect('/')




