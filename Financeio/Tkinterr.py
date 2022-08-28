from tkinter import *
import matplotlib.pyplot as plt

splash_root= Tk()
splash_root.title("Splash Screen")
splash_root.geometry("512x174+550+300")
splash_root.overrideredirect(True)

photo= PhotoImage(file="logo1.png")
lab2= Label(image=photo)
lab2.pack()


def main():
    splash_root.destroy()
    
    root = Tk()
    root.configure(background = "#fffef0")
    root.title("Financeio")
    root.iconbitmap(r'money-bag.ico')
    root.geometry('500x900+600+200')

    main_label= Label(root, text="Welcome to Financeio", font=("Stencil",18), bg = "#fffef0")
    main_label.pack(pady=20)

    totalIn= Entry(root, width=40, bg= "Teal", fg="White", bd=2, relief= "solid",font=("times",12))
    totalIn.pack(padx = 10, pady=10)
    totalIn.insert(0,"Total income")

    cliving= Entry(root, width=40, bg= "Teal", fg="White", bd=2, relief= "solid",font=("times",12))
    cliving.pack(padx = 10,pady=10)
    cliving.insert(0,"Expenditure of living")

    chealth=Entry(root, width=40, bg= "Teal", fg="White", bd=2, relief= "solid",font=("times",12))
    chealth.pack(padx = 10,pady=10)
    chealth.insert(0,"Medical expenditure")

    Centr= Entry(root, width=40, bg= "Teal", fg="White", bd=2, relief= "solid",font=("times",12))
    Centr.pack(padx = 10,pady=10)
    Centr.insert(0,"Entertainment expenditure")

    Cinv= Entry(root, width=40, bg= "Teal", fg="White", bd=2, relief= "solid",font=("times",12))
    Cinv.pack(padx = 10,pady=10)
    Cinv.insert(0,"How much do you invest?")

    Bills= Entry(root, width=40, bg= "Teal", fg="White", bd=2, relief= "solid",font=("times",12))
    Bills.pack(padx = 10,pady=10)
    Bills.insert(0,"How much do your bills cost?")

    ef= Entry(root, width=40, bg= "Teal", fg="White", bd=2, relief= "solid",font=("times",12))
    ef.pack(padx = 10,pady=10)
    ef.insert(0,"How much emergency fund do you have?")
    
    
    def saving():
        Income= int(totalIn.get())
        Living= int(cliving.get())
        Healthcare=int(chealth.get())
        Entertainment=int(Centr.get())
        Investments=int(Cinv.get())
        bills= int(Bills.get())
        Savings= Income-(Living+Healthcare+Entertainment+Investments+bills)
        lab1= Label(root, text="Total Savings: " + str(Savings), bg = "#fffef0").pack()


    def button_hover(e):
        GO["bg"]="White"
        stat_label.config(text="Submit and get savings")

    def btn_unhvr(e):
        GO["bg"]="#BBF3D0"
        stat_label.config(text="")
        


    GO= Button(root, text="GO!", command= saving, bg = "#BBF3D0")
    stat_label= Label(root, text="", bd=2, relief=SUNKEN, anchor= E)
    stat_label.pack(fill=X, side=BOTTOM, ipady=2)
    GO.bind("<Enter>", button_hover)
    GO.bind("<Leave>", btn_unhvr)
    GO.pack(pady=10)

    def chart():
        Living= int(cliving.get())
        Healthcare=int(chealth.get())
        Entertainment=int(Centr.get())
        Investments=int(Cinv.get())
        bills= int(Bills.get())
        
        activities = ['Investment', 'Bills', 'Living', 'Health', 'Entertainment']

        slices = [Investments, bills, Living, Healthcare, Entertainment]

        colors = ['r', 'y', 'g', 'b','c']

        plt.pie(slices, labels = activities, colors=colors,startangle=90, shadow= True,radius = 1.2, autopct = '%1.0f%%')

        plt.show()

        

    def buttonhvr2(e):
        Chart["bg"]= "White"
        slabel2.config(text="Get expenditure chart")

    def butnunhvr2(e):
        Chart["bg"]= "#BBF3D0"
        slabel2.config(text="")

    Chart= Button(root, text="Click to Show chart", command= chart, bg = "#BBF3D0")
    slabel2= Label(root, text="", bd=2, relief=SUNKEN, anchor= E)
    slabel2.pack(fill=X, side=BOTTOM, ipady=2)
    Chart.bind("<Enter>",buttonhvr2)
    Chart.bind("<Leave>",butnunhvr2)
    Chart.pack(pady=10)


    def savingTracker():
        Income =  int(totalIn.get())
        
        idealDistribution = Label(root, text = "The ideal distribution of your income should be: ", bg = "#fffef0", font= ("Informal Roman", 16)).pack(pady = 10)
        LE = Label(root, text = "Living expenses: " + str(0.5*Income), bg = "#fffef0").pack(pady = 3)
        savings = Label(root, text = "Savings: "  + str(0.1*Income), bg = "#fffef0").pack(pady = 3)
        invest = Label(root, text = "Investment: " + str(0.1*Income), bg = "#fffef0").pack(pady = 3)
        edu = Label(root, text = "Education: "  + str(0.1*Income), bg = "#fffef0").pack(pady = 3)
        recreation = Label(root, text = "Entertainment/ Recreation: " + str(0.1*Income), bg = "#fffef0").pack(pady = 3)
        donation = Label(root, text = "Donation: "  + str(0.05*Income), bg = "#fffef0").pack(pady = 3)
        EF = Label(root, text = "Emergency funds: " + str(0.05*Income), bg = "#fffef0").pack(pady = 3)
        Income =  int(totalIn.get())
        Living =  int(cliving.get())
        Entertainment =  int(Centr.get())
        Health =  int(chealth.get())
        Bill =  int(Bills.get())
        Investment =  int(Cinv.get())
        EmF = int(ef.get())
        saved = Income - Living - Entertainment- Health - Bill - Investment - EmF
 
        if Investment<int(0.1*Income):
            investSuggestion = Label(root, text = "Suggestion: Try to invest more",font=("Helvetica",14), bg = "#fffef0").pack(pady=10)
        if Entertainment>int(0.1*Income):
            entertainmentSuggestion= Label(root, text = "Suggestion: spend less money on entertainment",font=("Helvetica",14), bg = "#fffef0").pack(pady=15)
        if EmF < int(0.05*Income):
            efSuggestion = Label(root, text = "Suggestion: keep aside more money for emergency needs",font=("Helvetica",14), bg = "#fffef0").pack(pady=10)
        if saved < int(0.1*Income):
            savingSuggestion = Label(root, text = "Suggestion: saving a little more can be helpful", font=("Helvetica",14), bg = "#fffef0").pack(pady=10)


    def btnhvr3(e):
        report["bg"]="White"
        slb3.config(text="Get feedback report")
    def btnuhvr3(e):
        report["bg"]="#BBF3D0"
        slb3.config(text="")

        

    report = Button(root, text = "Click to get report", command = savingTracker, bg = "#BBF3D0")
    slb3= Label(root, text="", bd=2, relief=SUNKEN, anchor= E)
    slb3.pack(fill=X, side=BOTTOM, ipady=2)
    report.bind("<Enter>",btnhvr3)
    report.bind("<Leave>",btnuhvr3)
    report.pack(pady=10)
    
splash_root.after(3000,main)   
mainloop()
