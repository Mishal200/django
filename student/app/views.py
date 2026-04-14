from django. shortcuts import render 
from django.http import HttpResponse

def students(request):
# students_list-["Ajith", "Amal", "Arjun", "Athul", "Krishna"] 
    students_list=[
        {"name": "Athul", "course": "Python","passed":True}, 
        {"name": "Krishna", "course": "python", "passed": False}, 
        {"name": "Amal", "course": 'Mern', "passed" :False}, 
        {"name": "Ajith", "course": "Flutter", "passed" : False}, 
        {"name": "Arjun", "course": "Data Science", "passed":True}
    ]
    course = "Python"
    return render (request, 'students.html',{'students': students_list, 'course': course})

def home(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')