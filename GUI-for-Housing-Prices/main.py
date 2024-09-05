from tkinter import *
from tkinter import ttk
import sqlite3
import pymysql
import matplotlib.pyplot as plt
import numpy as np
import random
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
import time 

connection = pymysql.connect("localhost","root","","boston_housing")
crsr = connection.cursor()


####



xdata = np.linspace(0,200,50)[:,np.newaxis]
noise = np.random.normal(20,10,xdata.shape) # (mean,stddev,shape)
ydata = 1000/(1+np.exp(-xdata/100 + 5)) + 0.6*noise

degree = 5
lw = 2
count = 0
colors = ['teal', 'yellowgreen', 'gold']
model = make_pipeline(PolynomialFeatures(degree), Ridge())
model.fit(xdata,ydata)
y_plot = model.predict(xdata)

def Regression():
    SqLab= Label(tab3,text="Input the Square area")
    SqLab_1= Entry(tab3)
    SqLab.place(x=100,y=160)
    SqLab_1.place(x=200,y=160)
    def Submit_Sq():
        a_a = np.abs(model.predict(np.array(float(SqLab_1.get())))[[0]])
        LabPredictAns = Label(tab3, text = str(a_a))
        LabPredictAns.pack()
    c = Button(tab3, text="SUBMIT", command=Submit_Sq)
    c.place(x=180, y=440 )

def GetGraph():
    plt.plot(xdata, y_plot, color=colors[count], linewidth=lw,
         label="degree %d" % degree)
    plt.scatter(xdata,ydata )
    plt.show()

####


main = Tk()
main.title('Housing Prices')
main.geometry('1000x800')

# creating the frames in the main
topFrame = Frame(main, width=1000, height=100, bg='lightgreen')
topFrame.pack(side=TOP)

bottomFrame = Frame(main, width=1000, height=700, bg='steelblue')
bottomFrame.pack(side=BOTTOM)

heading = Label(topFrame, text="Housing Prices Prediction System", font=('arial 24 bold'), fg='black', bg='lightgreen')
heading.place(x=250, y=17)

def ViewOrders():
    crsr.execute("SELECT * FROM MAINHOUSE")
    ans = crsr.fetchall()
    for i in ans:
        print(i)



def AddHouse():
    #destroyFrame()
    x = 100
    label_1= Label(tab2,text="HouseID")
    entry_1= Entry(tab2)
    label_1.place(x=10,y=120+x)
    entry_1.place(x=150,y=120+x)
    label_2= Label(tab2,text="Square Area")
    entry_2 = Entry(tab2)
    label_2.place(x=10,y=160+x)
    entry_2.place(x=150,y=160+x)
    label_3= Label(tab2,text="Price")
    entry_3 = Entry(tab2)
    label_3.place(x=10,y=200+x)
    entry_3.place(x=150,y=200+x)
    label_4 = Label(tab2, text="Contact Info")
    entry_4 = Entry(tab2)
    label_4.place(x=10, y=240 + x)
    entry_4.place(x=150, y=240 + x)
    label_5 = Label(tab2, text="Complex Name")
    entry_5 = Entry(tab2)
    label_5.place(x=10, y=280 + x)
    entry_5.place(x=150, y=280 + x)
    label_6 = Label(tab2, text="Floors")
    entry_6 = Entry(tab2)
    label_6.place(x=10, y=320 + x)
    entry_6.place(x=150, y=320 + x)
    tkvar = StringVar(tab2)
    choices = {"Allston","Back Bay","Bay Village","Beacon Hill","Brighton","Charlestown","Chinatown","Dorchester","Downtown","East Boston","Fenway Kenmore","Hyde Park",
                "Jamaica Plain","Mattapan","Mission Hill","North End","Roslindale","Roxbury","South Boston","South End","West End","West Roxbury"}
    tkvar.set('Locality')  # set the default option
    popupMenu = OptionMenu(tab2, tkvar, *choices)
    label_7 = Label(tab2, text="Locality")
    label_7.place(x=10, y=360 + x)
    popupMenu.place(x=150, y=360 + x)

    def Submit():
                crsr.execute(
                    "INSERT INTO MAINHOUSE (HouseID,AREA,PRICE,CONTACT,COMPLEX,FLOORS,LOCALITY) VALUES(%s,%s,%s,%s,%s,%s,%s)",
                    (entry_1.get(), entry_2.get(), entry_3.get(), entry_4.get(), entry_5.get(), entry_6.get(),
                     tkvar.get()))
                connection.commit()
                crsr.execute("SELECT * FROM MAINHOUSE ")
                ans = crsr.fetchall()
                for i in ans:
                    print(i)

    c = Button(tab2, text="SUBMIT", command=Submit)
    c.place(x=180, y=440 + x)


######################################################################### TABLE
sql_table_House="""CREATE TABLE IF NOT EXISTS MAINHOUSE(
HouseID INTEGER ,
AREA VARCHAR(30),
PRICE INTEGER,
CONTACT INTEGER,
COMPLEX CHAR(4),
FLOORS INTEGER,
LOCALITY CHAR(2)
)"""

crsr.execute(sql_table_House)
connection.commit()

########################################################################## MAIN GUI
note = ttk.Notebook(main)
note.place(x = 0, y = 100)
tab1 = Frame(note, width=1000, height=700, background="bisque")
tab2 = Frame(note, width=1000, height=700, background="bisque")
tab3 = Frame(note, width=1000, height=700, background="bisque")
tab4 = Frame(note, width=1000, height=700, background="bisque")


note.add(tab1, text = "     Welcome        ", compound=TOP)
note.add(tab2, text = "     ADD      ")
note.add(tab3, text = "     Predict       ")
note.add(tab4, text = "     Display Table        ")


img = PhotoImage(file = "citymap_boston_ma.gif")

labelImg=Label(tab1, image = img)
labelImg.pack(side = TOP)

#Add Tab
button1 = Button(tab2, text="Add", fg='red',compound=TOP,height=2, width=10,command=AddHouse)
button2 = Button(tab2, text="View", fg='blue', compound=TOP,height=2, width=10, command = ViewOrders)     #,command=ViewDonor)
button1.pack(side=TOP)
button2.pack(side = TOP)

############# predict

buttonReg = Button(tab3, text="Run Regression", fg='blue', compound=TOP,height=2, width=20,command=Regression)  #run training
buttonReg.place(x=100, y=200)

##################### display the table
DisplayLab = Label(tab4,text="The Curve")
DisplayLab.place(x=400, y=50)
ButtonDisp = Button(tab4, text="Get Graph", fg='blue', compound=TOP,height=2, width=20,command=GetGraph)  #show graph
ButtonDisp.place(x=400, y=100)
main.mainloop()
