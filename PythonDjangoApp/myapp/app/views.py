from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient
# mongo = MongoClient('172:17.0.2',27017) #not working
mongo = MongoClient('localhost',27017) #this line has some issues becuas eit can't find mongodb container
db = mongo['ncu_db']
collection = db['customers']
users_collection = db['users']
productList = []
def login(request):
    return render(request, 'login.html')
def register(request):
    username = request.POST['u_name']
    password = request.POST['u_password']
    useremail = request.POST['u_email']
    gender = request.POST['u_gender']
    print(gender)
    insert = users_collection.insert_one({
        "name":username,
        "password":password,
        "useremail":useremail,
        "gender":gender
    })
    if insert.acknowledged == True:
        msg = 'Registration Successful'
    else:
        msg = 'Registration Unsuccessful'
    print(msg)
    return render(request,'login.html',context={'msg':msg})

def index(request):
    username = request.POST['u_name']
    password = request.POST['u_password']
    cursor = collection.find()
    verify = users_collection.find_one(
        {
            "name":username,
            "password":password
        }
    )
    for item in cursor:
        productList.append(item)
    if verify:
        msg = 'Login successful'
    else:
        msg = "Login Failed"
    return render(request,'index.html',context={'msg':msg, 'name':username,"data":productList})