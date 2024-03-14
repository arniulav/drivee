import os
import tkinter
import tkintermapview
import random as ran
# create tkinter window
root_tk = tkinter.Tk()
root_tk.geometry(f"{1000}x{700}")
root_tk.title("map_view_simple_example.py")

# create map widget
map_widget = tkintermapview.TkinterMapView(root_tk, width=1000, height=700, corner_radius=0)
map_widget.pack(fill="both", expand=True)

min_lan=62000995
max_lan=62050000
min_lat=129691266
max_lat=129757461

def marker_callback(marker):
    print(marker.text)

kk=3#количество курьеров
n=9 #количество заказов


#algorithm 
import matplotlib.pyplot as plt

import random as ran
zakazy=[]
zxA=[]
zyA=[]
zxB=[]
zyB=[]


kuriery=[]
xk=[]
yk=[]


# geocoordinates_lan=[]
# geocoordinates_lat=[]
#создание заказов
for i in range(n):
    z=[]
    xa=ran.randint(min_lan,max_lan)
    ya=ran.randint(min_lat,max_lat)
    xb=ran.randint(min_lan,max_lan)
    yb=ran.randint(min_lat,max_lat)

    zxA.append(xa)
    zyA.append(ya)
    zxB.append(xb)
    zyB.append(yb)
    z.append(xa)
    z.append(ya)
    z.append(xb)
    z.append(yb)
    zakazy.append(z)
    generate_lan=xa
    generate_lat=ya
    # geocoordinates_lan.append(generate_lan)
    # geocoordinates_lat.append(generate_lat)
print('заказы=',zakazy)   

for i in range(n):    
    marker_3 = map_widget.set_marker(zxA[i]/10**6, zyA[i]/10**6, text=f"Заказ A #{i+1}", command=marker_callback)
    marker_3 = map_widget.set_marker(zxB[i]/10**6, zyB[i]/10**6, text=f"Заказ B #{i+1}", command=marker_callback)
#создание курьеров
# geocoordinates_lan_kurier=[]
# geocoordinates_lat_kurier=[]
for i in range(kk):
    k=[]
    
    xk1=ran.randint(min_lan,max_lan)
    yk1=ran.randint(min_lat,max_lat)
    
    xk.append(xk1)
    yk.append(yk1)
    k.append(xk1)
    k.append(yk1)
    
    kuriery.append(k)

    generate_lan_kurier=xk1
    generate_lat_kurier=yk1
    # geocoordinates_lan_kurier.append(generate_lan_kurier)
    # geocoordinates_lat_kurier.append(generate_lat_kurier)
print('курьеры=',kuriery)    

for i in range(3):    
    marker_3 = map_widget.set_marker(xk[i]/10**6, yk[i]/10**6, text=f"Курьер #{i+1}", command=marker_callback)
# алгоритм
list_ne_vzyatyh_zakazov=[]
for i in range(n):
    list_ne_vzyatyh_zakazov.append(i)
ind=-1

while len(list_ne_vzyatyh_zakazov)!=0:
    for j in range(kk):
        min=1000000000000
        for i in range(n):
            r=((xk[j]-zxA[i])**2+(yk[j]-zyA[i])**2)**(1/2)
            if (min > r) and (i in list_ne_vzyatyh_zakazov) : 
                min=r
                ind=i
        list_ne_vzyatyh_zakazov.remove(ind) 
        print('курьер=',j+1,'заказ=',ind+1)
        xk[j]=zxB[ind]
        yk[j]=zyB[ind]


# set initial position of map widget
map_widget.set_address("Yakutsk")
map_widget.set_zoom(13)

root_tk.mainloop()