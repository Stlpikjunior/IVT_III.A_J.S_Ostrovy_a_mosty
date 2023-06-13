import tkinter as tk
import random as rd
#offset = posunutie
root = tk.Tk()
width_can = 300
height_can = 450
cw = rd.randrange(4,7) #od 4 do 6
ch = rd.randrange(3,10) # od 3 do 9
pw = 50
ph = 50
canvas = tk.Canvas(root, width = cw*pw+100, height = ch*ph, bg = 'grey')
canvas.pack()

coins = 360


field_switcher = True
water = []
islands = []

img1 = tk.PhotoImage(file='ostrov3.png')
img2 = tk.PhotoImage(file='ostrov0.png')
img3 = tk.PhotoImage(file='ostrov1.png')
img4 = tk.PhotoImage(file='ostrov2.png')
img5 = tk.PhotoImage(file ='ostrov_kruh0.png')
img6 = tk.PhotoImage(file = 'ostrov_kruh1.png')

text = canvas.create_text(cw*pw+25,25, text=coins, fill="black", font=('Helvetica 15 bold'))

def game_field():
   global water,islands
   for y in range(ch):
       for x in range(cw):
           result = rd.random() #od 0 do 1
           if result <= 0.2:
               islands.append(canvas.create_image(pw*x,ph*y, anchor ='nw',image = img2))

           else:
               water.append(canvas.create_image(pw * x, ph * y, anchor='nw', image = img1))
   canvas.create_image(cw*pw+50,0,anchor='nw',image = img5, tags='switcher')
   

def changer(e):
   global water
   global text, coins, field_switcher 
   zoz = canvas.find_overlapping(e.x,e.y, e.x+1,e.y+1)
   if len(zoz)!=0 and zoz[0]in water: # podmienka ci som vobec klikol a  v druhej skusam ci toje voda alebo pevnina
       nx = (e.x//pw)*pw
       ny = (e.y//ph)*ph

       if field_switcher == True:
           coins -=10
           if coins>=0:
            canvas.create_image(nx,ny, anchor='nw', image=img3, tag = 'bridge')
           
            canvas.itemconfig(text,text = coins)

         
       else:
           coins -=50
           if coins>=0:
            canvas.create_image(nx,ny,anchor = 'nw', image = img2, tag = 'island')
            canvas.itemconfig(text,text = coins)
           else:
             canvas.create_image(nx,ny,anchor = 'nw', image = img1)
             field_switcher = True
       canvas.delete(zoz[0])
       temp = zoz[0]
       canvas.delete(temp)
       water.remove(temp)

     
         

def spinner(e):
   zoz = canvas.find_overlapping(e.x, e.y, e.x + 1, e.y + 1)
   if canvas.itemcget(zoz[0], 'image')=='pyimage4':
       canvas.itemconfig(zoz[0], image = img3)
   elif canvas.itemcget(zoz[0],'image') =='pyimage3':
       canvas.itemconfig(zoz[0],image = img4)

def switcher(e):
   global field_switcher
   zoz = canvas.find_overlapping(e.x, e.y, e.x + 1, e.y + 1)

   if canvas.itemcget(zoz[0], 'image') == 'pyimage6':
       canvas.itemconfig(zoz[0], image=img5)
       field_switcher = True
   elif canvas.itemcget(zoz[0], 'image') == 'pyimage5':
       field_switcher = False
       canvas.itemconfig(zoz[0], image=img6)


game_field()


canvas.bind('<Button-1>', changer)
canvas.tag_bind('bridge','<Button-1>', spinner)
canvas.tag_bind('switcher','<Button-1>', switcher)
root.mainloop()

