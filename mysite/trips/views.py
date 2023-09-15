from django.shortcuts import render, redirect
from django.urls import reverse
import sqlite3

# Create your views here.
def menu(request):
    area = request.POST.get('area')
    print(area)

    Type = request.POST.get('type')
    print(Type)

    budget = request.POST.get('budget')
    if budget != None and budget != "全部":
        budget = budget.split("-")
    print(budget)

    open_hour = request.POST.get('open hour')
    if open_hour != None and open_hour != "全部":
        open_hour = open_hour.split("-")
    print(open_hour)

    comment = request.POST.get('comment')
    print(comment)

    db = sqlite3.connect('db.sqlite3')
    cursor = db.cursor()

    req =""
    if area != None:
        if area != "全部":
            if len(req) ==0:
                req += " where "
            else:
                req += " and "
            req += "Area='" +area + "'"
        #res1 = cursor.execute("SELECT * FROM [trips_Positions] WHERE Area='" +area + "'")
        #print(res1.fetchall())
    if Type != None :
        if Type != "全部":
            if len(req) ==0:
                req += " where "
            else:
                req += " and "
            req += "style='" +Type + "'"
        #res2 = cursor.execute("SELECT * FROM [trips_Food_Type] WHERE style='" +Type + "'")
        #print(res2.fetchall())
    if budget != None :
        if budget != "全部":
            if len(req) ==0:
                req += " where "
            else:
                req += " and "
            req += "Avg_charge >='" +budget[0] + "' and Avg_charge <='" +budget[1]+"'"
        #res3 = cursor.execute("SELECT * FROM [trips_Prices] WHERE Avg_charge >='" +budget[0] + "' and Avg_charge <='" +budget[1]+"'")
        #print(res3.fetchall())
    if open_hour != None :
        if  open_hour != "全部":
            if len(req) ==0:
                req += " where "
            else:
                req += " and "
            req += "not (START_Time >'" +open_hour[1] + "' or Close_Time <'" +open_hour[0]+"')"
        #res4 = cursor.execute("SELECT * FROM [trips_Infos] WHERE not (START_Time >'" +open_hour[1] + "' or Close_Time <'" +open_hour[0]+"')")
        #print(res4.fetchall())
    if comment != None:
        if  comment != "全部":
            if len(req) ==0:
                req += " where "
            else:
                req += " and "
            req += "CP >='" +comment + "' and Service >='" +comment+ "' and Delicious_level >='" +comment+ "' and Clean >='" +comment+"'"
        #res5 = cursor.execute("SELECT * FROM [trips_Comment] WHERE CP >='" +comment + "' and Service >='" +comment+ "' and Delicious_level >='" +comment+ "' and Clean >='" +comment+"'")
        #print(res5.fetchall())
    # print(req)
    #res = cursor.execute("SELECT * FROM ([trips_Positions] natural join trips_Food_Type natural join trips_Prices natural join trips_Infos natural join trips_Comment] "+req)
    res = cursor.execute("SELECT * FROM [trips_Positions] natural join [trips_Food_Type] natural join [trips_Prices] natural join [trips_Infos] natural join [trips_Comment] "+req)
    
    if area != None:
        
        if request.method == 'POST':
            f=[]
            form = res.fetchall()
           # print('form ',form)
            for i in form:
                n = list(i)
                
                for cnt, nn in enumerate(n):
                    if nn is None:
                        n[cnt]=''
                        
                f.append(n)
            #print(res.fetchall())
            
            if area != None:
                return render(request, 'order_finish.html', context = {'form':f})
            
    return render(request, 'index.html')
