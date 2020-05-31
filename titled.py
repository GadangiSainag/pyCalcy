
from tkinter import *

avalable_items= ("Sprite","Fizz","Candy","Monster","RedBull","Cake","Coke")
temp=[]
for x in avalable_items:
	temp.append(x)
print(temp)
shopping_cart=[]
root=Tk()

def add(item):
	shopping_cart.append(item)

def subtract(item):
	

	shopping_cart.remove(item)

def bill():
	Label(root,text=shopping_cart).grid()
	
root.geometry("500x500")

fun= {"Sprite" : lambda : add("Sprite"),
	  "Fizz": lambda : add("Fizz") ,
	  "Candy":lambda : add("Candy"),
	  "Monster":lambda : add("Monster"),
	  "RedBull":lambda : add("RedBull"),
	  "Cake":lambda : add("Cake"),
	  "Coke":lambda : add("Coke")}

fun1= {"Sprite" : lambda : subtract("Sprite"),
	  "Fizz": lambda : subtract("Fizz") ,
	  "Candy":lambda : subtract("Candy"),
	  "Monster":lambda : subtract("Monster"),
	  "RedBull":lambda : subtract("RedBull"),
	  "Cake":lambda : subtract("Cake"),
	  "Coke":lambda : subtract("Coke")}
'''
#{x : lambda:add(str(x))}
fun={"stick": 55}
for x in avalable_items:
	fun.update({x : add(x)})
'''
print(fun)

for i in avalable_items:#range(0,len(temp)):
	#shit=temp[i]
	integer=avalable_items.index(i)
	Label(root,text=i).grid(row=integer,column=0,sticky=W,padx=[0,20])
	Button(root,text="Add",command=fun[i]).grid(row=integer,column=1)

	Button(root,text="Remove",command=fun1[i]).grid(row=integer,column=2)
	Label(root, text = shopping_cart.count(i)).grid(row= integer, column= 3)

but1=Button(root,text="BIll",command=bill).grid()
root.mainloop()
'''
avalable_items= ("Sprite","Fizz","Candy","Monster","Fizz","Fizz","Fizz","Fizz","Red Bull")
shit =avalable_items.count("Fizz")
print(shit)
'''