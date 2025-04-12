from django.http import HttpResponse
from django.shortcuts import render
from home.models import Users
# from home.models import Fir
# from home.models import Fir_num
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt






def index(request): 
    return render(request,'home.html')


    # return HttpResponse("<h1>pawan</h1>")

def register(request):
    params={'name':'pawan','place':'jamshedpur'}
    return render(request,'register.html',params)  


def login(request):
    return render(request,'login.html')   

def user_login(request):
    if request.method == "POST":
        uemail=request.POST.get('email');
        upassword = request.POST.get('password');
        # users = Users.objects.all()
        users= Users.objects.filter(uemail=uemail, upassword=upassword).first()
        if (uemail==users.uname and upassword==users.upassword):
            return render(request,'fraud.html')
        else:
            return render(request,'login.html')
            
        # us=Users(uname=uname,uemail=uemail,upassword=upassword);
        # us.save();
# ++++++++++++++++++++++++++++++

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from imblearn.under_sampling import RandomUnderSampler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression





def fraud(request):
    return render(request,'fraud.html')


def dfraud(request):
    msg=""
    if request.method == "POST":
        income=float(request.POST.get('income'));
        customer_age=float(request.POST.get('customer_age'));
        intended_balcon_amount = float(request.POST.get('intended_balcon_amount'));
        credit_risk_score = float(request.POST.get('credit_risk_score'));
        proposed_credit_limit = float(request.POST.get('proposed_credit_limit'));
        foreign_request = float(request.POST.get('foreign_request'));
        session_length_in_minutes = float(request.POST.get('session_length_in_minutes'));
        
        df=pd.read_csv(r"C:\Users\pk525\Desktop\Djanjo\fraud\Base.csv")
        df.drop(columns=["zip_count_4w","device_os","phone_mobile_valid","source","name_email_similarity","payment_type","has_other_cards","device_fraud_count","device_distinct_emails_8w","month","velocity_4w","velocity_24h","velocity_6h","phone_home_valid",
                 "bank_months_count","housing_status","employment_status","email_is_free","date_of_birth_distinct_emails_4w","bank_branch_count_8w","days_since_request",
                "prev_address_months_count","current_address_months_count","keep_alive_session"],inplace=True)
        ru=RandomUnderSampler()
        x=df.iloc[:,:-1]
        y=df["fraud_bool"]
        ru_x,ru_y=  ru.fit_resample(x,y)
        ru_y.value_counts()
        x_train,x_test,y_train,y_test=train_test_split(ru_x,ru_y,test_size=0.3,random_state=43)
        lr=LogisticRegression(multi_class="ovr")
        lr.fit(x_train,y_train)
        lr.score(x_test,y_test)*100
        # arr=[[0.9,60,35.33754,131,1500,0,4.039]]
        arr=[[income,customer_age,intended_balcon_amount,credit_risk_score,proposed_credit_limit,foreign_request,session_length_in_minutes]]
        pre=lr.predict(arr)
        pre1=int(pre)
    
        if pre1 == 1:
           msg="There is suspect"
        else:
            msg="There is no suspect"
        
    msg1={'msg':msg}
    
    return render(request,'home.html',msg1)    






       









# def cause(request):
#     return render(request,'cause.html') 



def about(request):
    return HttpResponse("About pawan")


def insertuser(request):
    if request.method == "POST":
        uname=request.POST.get('name');
        uemail=request.POST.get('email');
        upassword = request.POST.get('password');
        us=Users(uname=uname,uemail=uemail,upassword=upassword);
        us.save();
    return render(request,'login.html')

# def insertFir(requert):
#     if requert.method == "POST":
#         name=requert.POST.get('name');
#         gender= requert.POST.get('gender');
#         age = requert.POST.get('age');
#         pincode = requert.POST.get('pincode');
#         mnumber = requert.POST.get('mobile');
#         address = requert.POST.get('address');
#         aadhaar = requert.POST.get('aadhaar');
#         poffice = requert.POST.get('post');
#         distric = requert.POST.get('district');
#         country = requert.POST.get('country');
#         us1=Fir(name=name,gender=gender,age=age,pincode=pincode,mnumber=mnumber,address=address,aadhaar=aadhaar,poffice=poffice,
#                 distric=distric,country=country);
#         us1.save();



# def insertcause(request):
#     if request.method == "POST":
#         regno=request.POST.get('regno');
#         message= request.POST.get('message');
#         img = request.POST.get('img');
#         us2=Fir_num(name=regno,message=message,img=img);
#         us2.save();
