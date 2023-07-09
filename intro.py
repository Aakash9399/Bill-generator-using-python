from tkinter import*
import math,random
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing software")
        bg_color="#074463"
        title=Label(self.root,text="Billing software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #==========variable==========
        #==========grocery==========
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gel=IntVar()
        self.lotion=IntVar()
        #===========grocery==========
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.pulse=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        #===========cold drink=========
        self.maaza=IntVar()
        self.coke=IntVar()
        self.frooti=IntVar()
        self.thumbsup=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()

        #======Total product Price & Tax Variable====
        self.cosmetics_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetics_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()

        #===========Customer=======
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()



        #=========================Customer Detail Frame
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_text=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl=Label(F1,text="Phone No.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_text=Entry(F1,width=15,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_text=Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,text="Search",width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)

        #============Cosmetics Frame===============
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=325,height=400)

        bath_libl=Label(F2,text='Bath Soap',font=("times new roman",16,"bold"),bg=bg_color,fg="light green").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        face_cream_libl=Label(F2,text='Face cream',font=("times new roman",16,"bold"),bg=bg_color,fg="light green").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        face_w_libl=Label(F2,text='face wash',font=("times new roman",16,"bold"),bg=bg_color,fg="light green").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_w_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        hair_s_libl=Label(F2,text='hair spray',font=("times new roman",16,"bold"),bg=bg_color,fg="light green").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hair_s_txt=Entry(F2,width=10,textvariable=self.spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        hair_g_libl=Label(F2,text='hair gel',font=("times new roman",16,"bold"),bg=bg_color,fg="light green").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hair_g_txt=Entry(F2,width=10,textvariable=self.gel,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        body_libl=Label(F2,text='Body lotion',font=("times new roman",16,"bold"),bg=bg_color,fg="light green").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_txt=Entry(F2,width=10,textvariable=self.lotion,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #============Grocery Frame===============
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Groceries",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=180,width=325,height=400)

        g1_libl=Label(F3,text='rice',font=("times new roman",16,"bold"),bg=bg_color,fg="light green").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        g2_libl=Label(F3,text='Food oil',font=("times new roman",16,"bold"),bg=bg_color,fg="light green").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        g3_libl=Label(F3,text='pulse',font=("times new roman",16,"bold"),bg=bg_color,fg="light green").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt=Entry(F3,width=10,textvariable=self.pulse,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        g4_libl=Label(F3,text='wheat',font=("times new roman",16,"bold"),bg=bg_color,fg="light green").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        g5_libl=Label(F3,text='sugar',font=("times new roman",16,"bold"),bg=bg_color,fg="light green").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        g6_libl=Label(F3,text='tea',font=("times new roman",16,"bold"),bg=bg_color,fg="light green").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt=Entry(F3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #============Cold drink Frame===============
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drinks",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=670,y=180,width=325,height=400)

        c1_libl=Label(F4,text='Maaza',font=("times new roman",16,"bold"),bg=bg_color,fg="light green").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt=Entry(F4,width=10,textvariable=self.maaza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        c2_libl=Label(F4,text='Coke',font=("times new roman",16,"bold"),bg=bg_color,fg="light green").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt=Entry(F4,width=10,textvariable=self.coke,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        c3_libl=Label(F4,text='Frooti',font=("times new roman",16,"bold"),bg=bg_color,fg="light green").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt=Entry(F4,width=10,textvariable=self.frooti,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        c4_libl=Label(F4,text='Thumbs Up',font=("times new roman",16,"bold"),bg=bg_color,fg="light green").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt=Entry(F4,width=10,textvariable=self.thumbsup,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        c5_libl=Label(F4,text='Limca',font=("times new roman",16,"bold"),bg=bg_color,fg="light green").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt=Entry(F4,width=10,textvariable=self.limca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        c6_libl=Label(F4,text='sprite',font=("times new roman",16,"bold"),bg=bg_color,fg="light green").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt=Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #===========Bill Area==========
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=180,width=450,height=400)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #======Button Frame=====
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Billing menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=590,relwidth=1,height=200)

        m1=Label(F6,text="Total Cosmetic Price",bg=bg_color,fg="White",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetics_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        m2=Label(F6,text="Total Groceries Price",bg=bg_color,fg="White",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        m3=Label(F6,text="Total Cold drink Price",bg=bg_color,fg="White",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        c1=Label(F6,text=" Cosmetic Tax",bg=bg_color,fg="White",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.cosmetics_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=10)

        c2=Label(F6,text=" Groceries Tax",bg=bg_color,fg="White",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=10)

        c3=Label(F6,text=" Cold drink Tax",bg=bg_color,fg="White",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18,textvariable=self.cold_drink_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=10)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=650,width=680,height=150)

        total_btn=Button(btn_F,command=self.total,text="Total",bg=bg_color,bd=5,fg="black",pady=15,width=11,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=7)
        gbill_btn=Button(btn_F,text="Generate bill",command=self.bill_area,bg=bg_color,bd=5,fg="black",pady=15,width=11,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=7)
        clear_btn=Button(btn_F,text="Clear",bg=bg_color,bd=5,fg="black",pady=15,width=11,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=7)
        exit_btn=Button(btn_F,text="Exit",bg=bg_color,bd=5,fg="black",pady=15,width=11,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=7)
        self.welcome_bill()
    def total(self):

        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*120
        self.c_fw_p=self.face_wash.get()*60
        self.c_hs_p=self.spray.get()*180
        self.c_hg_p=self.gel.get()*140
        self.c_bl_p=self.lotion.get()*180

        self.total_cosmetics_price=float(
                                      self.c_s_p+
                                      self.c_fc_p+
                                      self.c_fw_p+
                                      self.c_hs_p+
                                      self.c_hg_p+
                                      self.c_bl_p
                                    )
        self.cosmetics_price.set("Rs. "+str(self.total_cosmetics_price))
        self.c_tax=round((self.total_cosmetics_price*0.05),2)
        self.cosmetics_tax.set("Rs. "+str(self.c_tax))

        self.g_r_p=self.rice.get()*60
        self.g_f_p=self.food_oil.get()*150
        self.g_d_p=self.pulse.get()*110
        self.g_w_p=self.wheat.get()*40
        self.g_s_p=self.sugar.get()*51
        self.g_t_p=self.tea.get()*400

        self.total_grocery_price=float(
                                     self.g_r_p+
                                     self.g_f_p+
                                     self.g_d_p+
                                     self.g_w_p+
                                     self.g_s_p+
                                     self.g_t_p
                                    )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.1),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))

        self.d_m_p=self.maaza.get()*60
        self.d_c_p=self.coke.get()*60
        self.d_f_p=self.frooti.get()*50
        self.d_t_p=self.thumbsup.get()*45
        self.d_l_p=self.limca.get()*40
        self.d_s_p=self.sprite.get()*70
        self.total_drinks_price=float(
                                      self.d_m_p+
                                      self.d_c_p+
                                      self.d_f_p+
                                      self.d_t_p+
                                      self.d_l_p+
                                      self.d_s_p
                                    )
        self.cold_drink_price.set("Rs. "+str(self.total_drinks_price))
        self.d_tax=round((self.total_drinks_price*0.05),2)
        self.cold_drink_tax.set("Rs. "+str(self.d_tax))

        self.Total_bill=float(self.total_cosmetics_price+self.total_grocery_price+self.total_drinks_price+self.c_tax+self.g_tax+self.d_tax)

    def welcome_bill(self):
        self.txtarea.delete("1.0",END)
        self.txtarea.insert(END,"\tWelcome to store\n")
        self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name: {self.c_name.get()}")       
        self.txtarea.insert(END,f"\n Phone Number: {self.c_phon.get()}" )
        self.txtarea.insert(END,f"\n-----------------------------------------------\n" )
        self.txtarea.insert(END,f"\tProducts\t\tQTY\t\tprice" )
        self.txtarea.insert(END,f"\n-----------------------------------------------" )

    def bill_area(self):
        
        self.welcome_bill()
        #====cosmetics========
        if self.soap.get()!=0:
            self.txtarea.insert(END,f"\n Bath Soap\t\t\t{self.soap.get()}\t\t{self.c_s_p}")
        if self.face_cream.get()!=0:
            self.txtarea.insert(END,f"\n Face Cream\t\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
        if self.face_wash.get()!=0:
            self.txtarea.insert(END,f"\n Face Wash\t\t\t{self.soap.get()}\t\t{self.c_fw_p}")
        if self.spray.get()!=0:
            self.txtarea.insert(END,f"\n Hair Spray\t\t\t{self.spray.get()}\t\t{self.c_hs_p}")
        if self.gel.get()!=0:
            self.txtarea.insert(END,f"\n Hair Gel\t\t\t{self.soap.get()}\t\t{self.c_hg_p}")
        if self.lotion.get()!=0:
            self.txtarea.insert(END,f"\n Body Lotion\t\t\t{self.soap.get()}\t\t{self.c_bl_p}")
        
        #====grocery========
        if self.rice.get()!=0:
            self.txtarea.insert(END,f"\n Rice\t\t\t{self.rice.get()}\t\t{self.g_r_p}")
        if self.food_oil.get()!=0:
            self.txtarea.insert(END,f"\n Food oil\t\t\t{self.food_oil.get()}\t\t{self.g_f_p}")
        if self.pulse.get()!=0:
            self.txtarea.insert(END,f"\n Pulse\t\t\t{self.pulse.get()}\t\t{self.g_d_p}")
        if self.wheat.get()!=0:
            self.txtarea.insert(END,f"\n Wheat\t\t\t{self.wheat.get()}\t\t{self.g_w_p}")
        if self.sugar.get()!=0:
            self.txtarea.insert(END,f"\n Sugar\t\t\t{self.sugar.get()}\t\t{self.g_s_p}")
        if self.tea.get()!=0:
            self.txtarea.insert(END,f"\n Tea\t\t\t{self.tea.get()}\t\t{self.g_t_p}")
        
        #====col drinks========
        if self.maaza.get()!=0:
            self.txtarea.insert(END,f"\n Maaza\t\t\t{self.maaza.get()}\t\t{self.d_m_p}")
        if self.coke.get()!=0:
            self.txtarea.insert(END,f"\n Coke\t\t\t{self.coke.get()}\t\t{self.d_c_p}")
        if self.frooti.get()!=0:
            self.txtarea.insert(END,f"\n Frooti\t\t\t{self.frooti.get()}\t\t{self.d_f_p}")
        if self.thumbsup.get()!=0:
            self.txtarea.insert(END,f"\n Thumbs up\t\t\t{self.thumbsup.get()}\t\t{self.d_t_p}")
        if self.limca.get()!=0:
            self.txtarea.insert(END,f"\n Limca\t\t\t{self.limca.get()}\t\t{self.d_l_p}")
        if self.sprite.get()!=0:
            self.txtarea.insert(END,f"\n sprite\t\t\t{self.sprite.get()}\t\t{self.d_s_p}")
        
        self.txtarea.insert(END,f"\n===============================================\n" )
        if self.cosmetics_tax.get()!="Rs .0.0":
            self.txtarea.insert(END,f"\nCosmetic Tax\t\t\t{self.cosmetics_tax.get()}" )
        if self.grocery_tax.get()!="Rs .0.0":
            self.txtarea.insert(END,f"\nGrocery Tax\t\t\t{self.grocery_tax.get()}" )
        if self.cold_drink_tax.get()!="Rs .0.0":
            self.txtarea.insert(END,f"\nCold drink Tax\t\t\t{self.cold_drink_tax.get()}" )
        
        self.txtarea.insert(END,f"\nTotal Bill:\t\t\tRs. {str(self.Total_bill)}" )

        self.txtarea.insert(END,f"\n===============================================" )


        
root=Tk()
obj=Bill_App(root)
root.mainloop()

  