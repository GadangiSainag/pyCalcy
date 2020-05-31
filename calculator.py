from tkinter import *


root = Tk()
root.title("Calculator")
#borderwidth=2, padx=150,highlightcolor="red",
root.resizable(False,False)
#,relief =GROOVE
root.configure(bg= "#7B7D7D")
e =Entry(root,width=35,borderwidth=5,relief =FLAT).grid(row=0,column=0,columnspan=4,padx=10,pady=10)

but_c =Button(root,text="C", width=11,height=2,relief=GROOVE,font= ("Vanda",15)).grid(row=1,columnspan=2,column=0)

but_back=Button(root,text="<-", width=11,height=2,relief=GROOVE,font= ("Vanda",15)).grid(row=1,columnspan=2,column=2)
#padx=21,pady=34
but_7 =Button(root,text="7",width=5,height=2,relief =GROOVE,font= ("Vanda",15)).grid(row=2,column=0)
but_8 =Button(root,text="8",width=5,height=2,relief =GROOVE,font= ("Vanda",15)).grid(row=2,column=1)
but_9 =Button(root,text="9",width=5,height=2,relief =GROOVE,font= ("Vanda",15)).grid(row=2,column=2)
but_x =Button(root,text="X",width=5,height=2,relief =GROOVE,font= ("Vanda",15)).grid(row=2,column=3)

but_4 =Button(root,text="4",width=5,height=2,relief =GROOVE,font= ("Vanda",15)).grid(row=3,column=0)
but_5 =Button(root,text="5",width=5,height=2,relief =GROOVE,font= ("Vanda",15)).grid(row=3,column=1)
but_6 =Button(root,text="6",width=5,height=2,relief =GROOVE,font= ("Vanda",15)).grid(row=3,column=2)
but_s =Button(root,text="-",width=5,height=2,relief =GROOVE,font= ("Vanda",15)).grid(row=3,column=3)

but_1 =Button(root,text="1",width=5,height=2,relief =GROOVE,font= ("Vanda",15)).grid(row=4,column=0)#, RAISED, GROOVE, and .
but_2 =Button(root,text="2",width=5,height=2,relief =GROOVE,font= ("Vanda",15)).grid(row=4,column=1)
but_3 =Button(root,text="3",width=5,height=2,relief =GROOVE,font= ("Vanda",15)).grid(row=4,column=2)
but_p =Button(root,text="+",width=5,height=2,relief =GROOVE,font= ("Vanda",15)).grid(row=4,column=3)

but_mod= Button(root,text="%", width=5,height=2, relief=GROOVE,font= ("Vanda",15)).grid(row=5,column=0)
but_0  = Button(root,text="0", width=5,height=2, relief=GROOVE,font= ("Vanda",15)).grid(row=5,column=1)
but_equal= Button(root,text="=", width=11,height=2, relief=GROOVE,font= ("Vanda",15)).grid(row=5,column=2,columnspan=2)




#root.expand(False,False)
root.mainloop()


vari="32"
print(len(vari))