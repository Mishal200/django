from django. shortcuts import render 
from django.http import HttpResponse

def students(request):
# students_list-["Ajith", "Amal", "Arjun", "Athul", "Krishna"] 
    students_list=[
    {"name": "Athul", "course": "Python","passed":True, "roll_no": 1}, 
    {"name": "Krishna", "course": "python", "passed": False, "roll_no": 2}, 
    {"name": "Amal", "course": 'Mern', "passed" :False, "roll_no": 3}, 
    {"name": "Ajith", "course": "Flutter", "passed" : False, "roll_no": 4}, 
    {"name": "Arjun", "course": "Data Science", "passed":True, "roll_no": 5}
]
def students(request):
    course = "Python"
    return render (request,'students.html',{'students': students_list,'course': course})

def student_detail(request, pk):
    print(pk)
    student = None
    for s in students_list:
        if s['roll_no'] == pk:
            student = s
    return render(request, 'student_detail.html', {'student': student})
def home(request):
    if request.method == "POST":
        print(request.POST['name'])
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')