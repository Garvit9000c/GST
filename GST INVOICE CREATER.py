global organisation,CEO,GST_no,Address,contact_no,Email,cust_number,cust_name,product,quantity,price
#configuring and initialising graphic use interface
from tkinter import *
gui=Tk()
gui.configure(background="sky blue")
gui.title("GST INVOICE")
gui.geometry("600x600")
#------------------------------------------------------------------------------------------------------------------
confi=open("C://GST//user.txt",'r')
o=confi.readline()
l=eval(o)
organisation,CEO,GST_no,Address,contact_no,Email=l
confi.close()#
#---------------------------------------------------------------------------------------------------------------
#function for menu
def org():
    global organisation
    x=input("enter the organisation name: ")
    organisation=x
def ceo():
    global CEO
    x=input("enter the name of owner: ")
    CEO=x
def gst():
    global GST_no
    x=input("enter your gst number: ")
    GST_no=x
def address():
    global Address
    x=input("enter the address of organisation")
    Address=x
def contact():
    global contact_no
    x=input("enter owners contact number")
    contact_no=x
def email():
    global Email
    x=input("enter owners email")
    Email=x
#meubar---------------------------------------------------------------------------------------------------
menubar=Menu(gui)
gui.config(menu=menubar)
filemenu=Menu(menubar)
menubar.add_cascade(label="---CONFIGURE--",menu=filemenu)
filemenu.add_command(label="#ORGANISATION",command=org)
filemenu.add_command(label="#CEO",command=ceo)
filemenu.add_command(label="#GST_NO",command=gst)
filemenu.add_command(label="#ADDRESS",command=address)
filemenu.add_command(label="#CONTACT",command=contact)
filemenu.add_command(label="#EMAIL",command=email)
#filemenu.add_command(label="#STOP",command=gui.destroy)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#---time-date-------------------------------
import datetime
now=datetime.datetime.now()
t=str(now)
time=t[0:13]+"-"+t[14:16]+"-"+t[17:]
filename="C://GST//bills//"+time+".txt"
#--invoice-datafile-------------------------------------------------------------------------------------
invoice=open(filename,"w")
#---functions/methods----for buttons-------------------------------------------------------------------------
def Next():
    a=str(product.get())
    b=str(price.get())
    c=str(quantity.get())
    d=str(tax.get())
    in_list=[a,b,c,d]
    invoice.write(str(in_list)+"\n")
    product.set("")
    price.set("")
    quantity.set("")
    tax.set(0)
    
def done():
    global dis
    a=str(product.get())
    b=str(price.get())
    c=str(quantity.get())
    d=str(tax.get())
    in_list=[a,b,c,d]
    invoice.write(str(in_list)+"\n")
    cust_=str(cust_name.get())
    cont_=str(cust_number.get())
    it_list=[cust_,cont_]
    invoice.write(str(it_list))
    product.set("")
    price.set("")
    quantity.set("")
    tax.set(0)
    cust_name.set("")
    cust_number.set("")
    dis=int(discount.get())
    gui.destroy()
    
#-------------window gui--------------------labels and entry box-------------------------------------------
heading=Label(gui,text="GST INVOICE CREATER",font=('broadway',30),bg="sky blue").pack()
label1=Label(gui,text="CUSTOMER NAME",bg="sky blue",font=('broadway')).place(x=100,y=100)
cust_name=StringVar()
entrybox1=Entry(gui,textvariable=cust_name,width=25,bg="orange").place(x=100,y=120)

label2=Label(gui,text="CUSTOMER's CONTACT",bg="sky blue",font=('broadway')).place(x=300,y=100)
cust_number=StringVar()
entrybox2=Entry(gui,textvariable=cust_number,width=25,bg="orange").place(x=300,y=120)

label=Label(gui,text="-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",bg="sky blue").place(x=0,y=200)
X=60
label3=Label(gui,text="PRODUCT ID",bg="sky blue",font=('broadway')).place(x=100,y=350-X)
product=StringVar()
entrybox3=Entry(gui,textvariable=product,width=25,bg="orange").place(x=100,y=370-X)

label4=Label(gui,text="QUANTITY",bg="sky blue",font=('broadway')).place(x=300,y=350-X)
quantity=StringVar()
entrybox4=Entry(gui,textvariable=quantity,width=25,bg="orange").place(x=300,y=370-X)

label5=Label(gui,text="PRICE",bg="sky blue",font=('broadway')).place(x=100,y=400-X)
price=StringVar()
entrybox5=Entry(gui,textvariable=price,width=25,bg="orange").place(x=100,y=420-X)

label6=Label(gui,text="DISCOUNT(%)",bg="sky blue",font=('broadway')).place(x=100,y=530)
discount=StringVar()
entrybox6=Entry(gui,textvariable=discount,width=25,bg="orange").place(x=100,y=550)

tax=IntVar()
label6=Label(gui,text="TAX CATEGORY",bg="sky blue",font=('broadway')).place(x=300,y=400-X)
Radiobutton(gui,text="3%",variable=tax,value=3,bg="sky blue",font=("bold")).place(x=300,y=420-X)
Radiobutton(gui,text="5%",variable=tax,value=5,bg="sky blue",font=("bold")).place(x=350,y=420-X)
Radiobutton(gui,text="12%",variable=tax,value=12,bg="sky blue",font=("bold")).place(x=400,y=420-X)
Radiobutton(gui,text="18%",variable=tax,value=18,bg="sky blue",font=("bold")).place(x=450,y=420-X)
Radiobutton(gui,text="28%",variable=tax,value=28,bg="sky blue",font=("bold")).place(x=500,y=420-X)
#---------------------------------------------------buttons---------------------------------------------------------------------------------------------------
button1=Button(gui,text='NEXT',command=Next).place(x=100,y=450)
button2=Button(gui,text='DONE',command=done).place(x=300,y=450)
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#-gui loop closing---
gui.mainloop()
invoice.close()
l=[organisation,CEO,GST_no,Address,contact_no,Email]
confi=open("C://GST//user.txt",'w')
confi.write(str(l))
confi.close()
#
#
#
#___________till this part we have collected all the inform and store in user and datetime file-----
global org_,own,gno,ad,co,em
from PIL import Image,ImageDraw
from PIL import ImageFont
owner=open("C://GST//user.txt","r")
cust=open(filename,"r")
bill=Image.new("RGB",(1000,1000),color='white')
#---------------------------------------------------------------------------------------------------------------------------------------------------------
def f(char,x,y,size):
    draw=ImageDraw.Draw(bill)
    font_path="C:/WINDOWS/Fonts/ALGER.TTF"
    font=ImageFont.truetype(font_path,size)
    draw.text((x,y),char,(0,0,0),font=font)
#--------------------------------------------------------------------------------------------------------------------------------------------------------
def trunk8(x):
    l=10
    if len(x)==l:
        return x
    if len(x)>l:
        return x[0:l]
    if len(x)<l:
        while not(len(x)==l):
            x=x+" "
        return x
#---------------------------------------------------------------------------------------------------------------------------------------------------------
def extractor(x):
    global org_,own,gno,ad,co,em
    s=x.readline()
    p=s.strip()
    l=eval(p)
    a,b,c,d,e,f=l
    org_,own,gno,ad,co,em=a.upper(),b.upper(),c.upper(),d.upper(),e.upper(),f.upper()
extractor(owner)
f(org_,0,0,40)
f(ad,0,50,20)
f("_________________________________________________________________________________________",0,60,50)
f("GST NUMBER:"+gno,600,70,25)
f(own,0,70,25)
f(co,600,110,20)
f(em,600,130,20)
f("---------------------------------------------------------------------------------------------------------------------------------------------------------",0,140,50)
f("PRODUCT                           |quantity   |PRICE      |GST |CGST  |SGST   |TOTAL|",10,190,25)
f("--------------------------------------------------------------------------------------------------------------------------------",10,210,30)
#___________________________________________________________________________________________________________________
def extractor2(x):
    l=x.readlines()
    s=l[len(l)-1]
    p=eval(s)
    f("customer:"+ p[0] +"/"+p[1],0,120,20)
    List=[]
    total=0
    total_tax=0
    for i in range(0,len(l)-1):
        List.append(str(i+1))
    for j in range(0,len(l)-1):
        h=eval(l[j])
        f(List[j]+"."+trunk8(h[0]),10,230+j*40,30)
        f(h[2],300,230+j*40,30)
        f(h[1],400,230+j*40,30)
        f(h[3]+"%",550,230+j*40,30)
        a=str(int(h[3])/2)+"%"
        f(a+"  "+a,620,230+j*40,25)
        q=100+int(h[3])
        y=q/100
        u=int(h[1])
        t=y*u*int(h[2])
        w=(q-100)/100
        z=u*w*int(h[2])
        total=total+t
        total_tax=total_tax+z
        f(str(int(t)),800,230+j*40,30)
    t_=((100-dis)*total)/100
    f("*************************************************************************************************************************************************************************",0,230+(len(l)-2)*40+20,30)
    f("TOTAL",0,230+(len(l)-2)*40+50,30)
    f(str(int(total-total_tax))+"Rs",380,230+(len(l)-2)*40+50,30)
    f(str(int(total_tax))+"Rs",550,230+(len(l)-2)*40+50,30)
    f(str(int(total))+"Rs",800,230+(len(l)-2)*40+50,30)
    f("after discount"+"("+str(int(dis))+"%)",670,230+(len(l)-2)*40+90,30)
    f(str(int(t_))+"Rs",800,230+(len(l)-2)*40+120,30)
    f("***************************************************************************************************************************************************************************",0,230+(len(l)-2)*40+70,30)
    f("HAPPY PURCHASING",400,230+(len(l)-2)*80+100,20)
extractor2(cust)
#_______________________________________________________________________________________________________________
    

bill.save("C://GST//invoice//"+time+".png")
bill.show("C://GST//invoice//"+time+".png")
