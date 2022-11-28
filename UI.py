import handleFunc
import tkinter as tk
from PIL import ImageTk, Image
def Window(data):
    window = tk.Tk()
    window.title('MENU')
    window_width = 1000
    window_height = 850
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    titleWindow = tk.Label(window, text = 'MENU',font=('Times New Roman',20))
    titleWindow.pack(side = 'top')
    
    #Food1
    img1 = (Image.open(data[0]['picture']))
    reSizeimg1 = img1.resize((300,205), Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(reSizeimg1)
    labelim1 = tk.Label(window, image = new_image)
    labelim1.place(height=300,x = 20,y=50)
    
    
    msgif1 = 'Name: '+data[0]['name']
    msgdes1 = 'Description: '+data[0]['description']
    msgp1 =f'Price: $'+ str(data[0]['price'])
    label1 = tk.Label(window,text = msgif1,font=('Times New Roman',14))
    label1.place(height = 30 ,x = 20 , y = 310)
    des1 = tk.Label(window,text = msgdes1,font=('Times New Roman',14))
    des1.place(height =30 ,x = 20 , y = 335)
    price1 = tk.Label(window, text =msgp1 ,font=('Times New Roman',14))
    price1.place(height = 30 ,x = 20 , y = 360)
    
    
    #Food2
    img2 = (Image.open(data[1]['picture']))
    reSizeimg2 = img2.resize((300,205), Image.ANTIALIAS)
    new_image2= ImageTk.PhotoImage(reSizeimg2)
    labelim2 = tk.Label(window, image = new_image2)
    labelim2.place(height=300,x = 350,y=50)
    
    
    msgif2 = 'Name: '+data[1]['name']
    msgdes2 = 'Description: '+data[1]['description']
    msgp2 =f'Price: $'+ str(data[1]['price'])
    label2 = tk.Label(window,text = msgif2,font=('Times New Roman',14))
    label2.place(height = 30 ,x = 350 , y = 310)
    des2 = tk.Label(window,text = msgdes2,font=('Times New Roman',14))
    des2.place(height = 30 ,x = 350 , y = 335)
    price2 = tk.Label(window, text =msgp2 ,font=('Times New Roman',14))
    price2.place(height = 30 ,x = 350 , y = 360)
    
    
    #Food3
    img3 = (Image.open(data[2]['picture']))
    reSizeimg3 = img3.resize((300,205), Image.ANTIALIAS)
    new_image3= ImageTk.PhotoImage(reSizeimg3)
    labelim3 = tk.Label(window, image = new_image3)
    labelim3.place(height=300,x = 680,y=50)
    
    
    msgif3 = 'Name: '+data[2]['name']
    msgdes3 = 'Description: '+data[2]['description']
    msgp3 =f'Price: $'+ str(data[2]['price'])
    label3 = tk.Label(window,text = msgif3,font=('Times New Roman',14))
    label3.place(height = 30 ,x = 680 , y = 310)
    des3 = tk.Label(window,text = msgdes3,font=('Times New Roman',14))
    des3.place(height =30 ,x = 680 , y = 335)
    price3 = tk.Label(window, text =msgp3 ,font=('Times New Roman',14))
    price3.place(height = 30 ,x = 680 , y = 360)
    
    
    #Food4
    img4 = (Image.open(data[3]['picture']))
    reSizeimg4 = img4.resize((300,205), Image.ANTIALIAS)
    new_image4= ImageTk.PhotoImage(reSizeimg4)
    labelim4 = tk.Label(window, image = new_image4)
    labelim4.place(height=300,x = 140,y=380)
    
    
    msgif4 = 'Name: '+data[3]['name']
    msgdes4 = 'Description: '+data[3]['description']
    msgp4 =f'Price: $'+ str(data[3]['price'])
    label4 = tk.Label(window,text = msgif4,font=('Times New Roman',14))
    label4.place(height = 30 ,x = 140 , y = 640)
    des4 = tk.Label(window,text = msgdes4,font=('Times New Roman',14))
    des4.place(height =30 ,x = 140 , y = 665)
    price4 = tk.Label(window, text =msgp4 ,font=('Times New Roman',14))
    price4.place(height = 30 ,x = 140 , y = 690)
    
    
    #Food5
    img5 = (Image.open(data[4]['picture']))
    reSizeimg5 = img5.resize((300,205), Image.ANTIALIAS)
    new_image5= ImageTk.PhotoImage(reSizeimg5)
    labelim5 = tk.Label(window, image = new_image5)
    labelim5.place(height=300,x = 560,y=380)
    
    
    msgif5 = 'Name: '+data[4]['name']
    msgdes5 = 'Description: '+data[4]['description']
    msgp5 =f'Price: $'+ str(data[4]['price'])
    label5 = tk.Label(window,text = msgif5,font=('Times New Roman',14))
    label5.place(height = 30 ,x = 560 , y = 640)
    des5 = tk.Label(window,text = msgdes5,font=('Times New Roman',14))
    des5.place(height =30 ,x = 560 , y = 665)
    price5 = tk.Label(window, text =msgp5 ,font=('Times New Roman',14))
    price5.place(height = 30 ,x = 560 , y = 690)
    
    
    
    window.mainloop()
    