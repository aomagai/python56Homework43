from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

def calculation_view(request):
    result = 0
    sign = ''
    if request.method == "GET":
        return render(request, 'result.html')
    elif request.method=="POST":
        if request.POST['operation'] == "add":
            sign = "+"
            result = int(request.POST['first_number']) + int(request.POST['second_number'])
        elif request.POST['operation'] == "subtract":
            sign = "-"
            result = int(request.POST['first_number']) - int(request.POST['second_number'])
        elif request.POST['operation'] == "multiply":
            sign = "*"
            result = int(request.POST['first_number']) * int(request.POST['second_number'])
        elif request.POST['operation'] == "divide":
            sign = "/"
            result = int(request.POST['first_number']) / int(request.POST['second_number'])

        context = {
            'first_number': request.POST['first_number'],
            'second_number': request.POST['second_number'],
            'result': result,
            'sign': sign
        }
        return render(request, 'result.html', context)