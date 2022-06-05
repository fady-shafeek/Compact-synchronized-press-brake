from tkinter import *
import time
from time import sleep
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
def newWindow():
        new_window= Toplevel(MyGui)
        new_window.geometry('400x400+10+10')
        new_window.title('Reset')
	    new_window.resizable(False,False)
       #FUNCTIONS UP
   #Right Motor up
       def uprmten():
           direction1= 16
           step1 = 12
           mymotortest1 = RpiMotorLib.A4988Nema(direction1, step1, GPIO_pins, "A4988")
           mymotortest1.motor_go(True, "Full" , 10, .005, False, .05)
       def uprmtw():
           direction1= 16
           step1 = 12
           mymotortest1 = RpiMotorLib.A4988Nema(direction1, step1, GPIO_pins, "A4988")
           mymotortest1.motor_go(True, "Full" , 20, .005, False, .05)
       def uprmfiv():
           direction1= 16
           step1 = 12
           mymotortest1 = RpiMotorLib.A4988Nema(direction1, step1, GPIO_pins, "A4988")
           mymotortest1.motor_go(True, "Full" , 50, .005, False, .05)
   #left motor up
       def uplmten():
           direction2=  20       
           step2 =  21
           mymotortest2 = RpiMotorLib.A4988Nema(direction2, step2, GPIO_pins, "A4988")
           mymotortest2.motor_go(True, "Full" , 10, .005, False, .05)
       def uplmtw():
           direction2=  20       
           step2 =  21
           mymotortest2 = RpiMotorLib.A4988Nema(direction2, step2, GPIO_pins, "A4988")
           mymotortest2.motor_go(True, "Full" , 20, .005, False, .05)
       def uplmfiv():
           direction2=  20       
           step2 =  21
           mymotortest2 = RpiMotorLib.A4988Nema(direction2, step2, GPIO_pins, "A4988")
           
           mymotortest2.motor_go(True, "Full" , 50, .005, False, .05)
   #Two Motors Up   
       def upstw():
           direction= 20, 16       
           step = 21, 12
           mymotortest1 = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")
           
           mymotortest1.motor_go(True, "Full" , 20, .005, False, .05)
       def upstw():
           direction= 20, 16       
           step = 21, 12
           mymotortest2 = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")
           
           mymotortest2.motor_go(True, "Full" , 20, .005, False, .05)
       def upsfiv():
           direction= 20, 16       
           step = 21, 12
           mymotortest1 = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")
           mymotortest1.motor_go(True, "Full" , 50, .005, False, .05)
       def upsfiv():
           direction= 20, 16       
           step = 21, 12
           mymotortest2 = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")
           mymotortest2.motor_go(True, "Full" , 50, .005, False, .05)
       def upshun():
           direction= 20, 16       
           step = 21, 12
           mymotortest1 = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")
           mymotortest1.motor_go(True, "Full" , 100, .005, False, .05)
       def upshun():
           direction= 20, 16       
           step = 21, 12
           mymotortest2 = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")
           mymotortest2.motor_go(True, "Full" , 100, .005, False, .05)
       def upstwo():
           direction= 20, 16       
           step = 21, 12
           mymotortest1 = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")
           mymotortest1.motor_go(True, "Full" , 200, .005, False, .05)
       def upstwo():
           direction= 20, 16       
           step = 21, 12
           mymotortest2 = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")
           mymotortest2.motor_go(True, "Full" , 200, .005, False, .05)
   #FUNCTIONS DOWN
  #Right Motor Down
      def downrmten():
          direction1= 16
          step1 = 12
          mymotortest1 = RpiMotorLib.A4988Nema(direction1, step1, GPIO_pins, "A4988")
          mymotortest1.motor_go(False, "Full" , 10, .005, False, .05)
      def downrmtw():
          direction1= 16
          step1 = 12
          mymotortest1 = RpiMotorLib.A4988Nema(direction1, step1, GPIO_pins, "A4988")
          mymotortest1.motor_go(False, "Full" , 20, .005, False, .05)
      def downrmfiv():
          direction1= 16
          step1 = 12
          mymotortest1 = RpiMotorLib.A4988Nema(direction1, step1, GPIO_pins, "A4988")
          mymotortest1.motor_go(False, "Full" , 50, .005, False, .05)
  #left Motor Down
      def downlmten():
          direction2=  20       
          step2 =  21
          mymotortest2 = RpiMotorLib.A4988Nema(direction2, step2, GPIO_pins, "A4988")
          mymotortest2.motor_go(False, "Full" , 10, .005, False, .05)
      def downlmtw():
          direction2=  20       
          step2 =  21
          mymotortest2 = RpiMotorLib.A4988Nema(direction2, step2, GPIO_pins, "A4988")
          mymotortest2.motor_go(False, "Full" , 20, .005, False, .05)
      def downlmfiv():
          direction2=  20       
          step2 =  21
          mymotortest2 = RpiMotorLib.A4988Nema(direction2, step2, GPIO_pins, "A4988")
          mymotortest2.motor_go(False, "Full" , 50, .005, False, .05)
  #Two Motors Down
      def downstw():
          direction= 20, 16       
          step = 21, 12
          mymotortest1 = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")
          mymotortest1.motor_go(False, "Full" , 20, .005, False, .05)
      def downstw():
          direction= 20, 16       
          step = 21, 12
          mymotortest2 = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")
          mymotortest2.motor_go(False, "Full" , 20, .005, False, .05)
      def downsfiv():
          direction= 20, 16       
          step = 21, 12
          mymotortest1 = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")
          mymotortest1.motor_go(False, "Full" , 50, .005, False, .05)
      def downsfiv():
          direction= 20, 16       
          step = 21, 12
          mymotortest2 = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")
          mymotortest2.motor_go(False, "Full" , 50, .005, False, .05)
      def downshun():
          direction= 20, 16       
          step = 21, 12
          mymotortest1 = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")
          
          mymotortest1.motor_go(False, "Full" , 100, .005, False, .05)
      def downshun():
          direction= 20, 16       
          step = 21, 12
          mymotortest2 = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")
          
          mymotortest2.motor_go(False, "Full" , 100, .005, False, .05)
      def downstwo():
          direction= 20, 16       
          step = 21, 12
          mymotortest1 = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")
          
          mymotortest1.motor_go(False, "Full" , 200, .005, False, .05)
      def downstwo():
          direction= 20, 16       
          step = 21, 12
          mymotortest2 = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")
          mymotortest2.motor_go(False, "Full" , 200, .005, False, .05)
      #HOME POSITION
      def home():
          direction= 20, 16       
          step = 21, 12
          mymotortest1 = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")
          mymotortest1.motor_go(True, "Full" , 800, .005, False, .05)
      def home():
          direction= 20, 16       
          step = 21, 12
          mymotortest2 = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")
          mymotortest2.motor_go(True, "Full" , 800, .005, False, .05)
          
      RightMotor= Label(new_window,text="Left Motor",width=15, height=2,fg="#FDF0D5",bg="#184E77").place(x=20,y=10)
      UPRightMotor= Label(new_window,text="Up",width=3, height=1,fg="#FDF0D5",bg="#457B9D",font='times 11 bold ').place(x=20,y=50)   
      Up10 = Button(new_window, width=3, height=1, text='0.5mm', bd=4,cursor='hand2',fg="#12355B",bg="#9AD1D4" ,activeforeground="#9AD1D4",activebackground='#184E77',command=uprmten).place(x=20,y=75)
      Up20 = Button(new_window, width=3, height=1, text='1mm', bd=4,cursor='hand2',fg="#12355B",bg="#9AD1D4" ,activeforeground="#9AD1D4",activebackground='#184E77',command=uprmtw).place(x=20,y=110)
      Up50 = Button(new_window, width=3, height=1, text='2.5mm', bd=4,cursor='hand2',fg="#12355B",bg="#9AD1D4" ,activeforeground="#9AD1D4",activebackground='#184E77',command=uprmfiv).place(x=20,y=145)
      DownRightMotor= Label(new_window,text="Down",width=5, height=1,fg="#FDF0D5",bg="#457B9D").place(x=93,y=50)
      Down10 = Button(new_window, width=3, height=1, text='0.5mm', bd=4,cursor='hand2',fg="#12355B",bg="#9AD1D4" ,activeforeground="#9AD1D4",activebackground='#184E77',command=downrmten).place(x=90,y=75)
      Down20 = Button(new_window, width=3, height=1, text='1mm', bd=4,cursor='hand2',fg="#12355B",bg="#9AD1D4" ,activeforeground="#9AD1D4",activebackground='#184E77',command=downrmtw).place(x=90,y=110)
      Down50 = Button(new_window, width=3, height=1,text='2.5mm', bd=4,cursor='hand2',fg="#12355B",bg="#9AD1D4" ,activeforeground="#9AD1D4",activebackground='#184E77',command=downrmfiv).place(x=90,y=145)
      
      LeftMotor= Label(new_window,text="Right Motor",width=15, height=2,fg="#FDF0D5",bg="#184E77").place(x=250,y=10)
      UPLeftMotor= Label(new_window,text="Up",width=3, height=1,fg="#FDF0D5",bg="#457B9D",font='times 11 bold ').place(x=250,y=50)
      Up10 = Button(new_window, width=3, height=1, text='0.5mm', bd=4,cursor='hand2',fg="#12355B",bg="#9AD1D4" ,activeforeground="#9AD1D4",activebackground='#184E77',command=uplmten).place(x=250,y=75)
      Up20 = Button(new_window, width=3, height=1, text='1mm', bd=4,cursor='hand2',fg="#12355B",bg="#9AD1D4" ,activeforeground="#9AD1D4",activebackground='#184E77',command=uplmtw).place(x=250,y=110)
      Up50 = Button(new_window, width=3, height=1, text='2.5mm', bd=4,cursor='hand2',fg="#12355B",bg="#9AD1D4" ,activeforeground="#9AD1D4",activebackground='#184E77',command=uplmfiv).place(x=250,y=145)
  
      DownLeftMotor= Label(new_window,text="Down",width=5, height=1,fg="#FDF0D5",bg="#457B9D").place(x=325,y=50)
      Down10 = Button(new_window, width=3, height=1, text='0.5mm', bd=4,cursor='hand2',fg="#12355B",bg="#9AD1D4" ,activeforeground="#9AD1D4",activebackground='#184E77',command=downlmten).place(x=320,y=75)
      Down20 = Button(new_window, width=3, height=1, text='1mm', bd=4,cursor='hand2',fg="#12355B",bg="#9AD1D4" ,activeforeground="#9AD1D4",activebackground='#184E77',command=downlmtw).place(x=320,y=110)
      Down50 = Button(new_window, width=3, height=1,text='2.5mm', bd=4,cursor='hand2',fg="#12355B",bg="#9AD1D4" ,activeforeground="#9AD1D4",activebackground='#184E77',command=downlmfiv).place(x=320,y=145)
      
      AllMotors= Label(new_window,text="Both Motors",width=15, height=2,fg="#FDF0D5",bg="#184E77").place(x=5,y=200)
      UPLeftMotor= Label(new_window,text="Up",width=3, height=1,fg="#FDF0D5",bg="#457B9D",font='times 11 bold ').place(x=10,y=245)
      Up20 = Button(new_window, width=3, height=1, text='1mm', bd=4,cursor='hand2',fg="#12355B",bg="#9AD1D4" ,activeforeground="#9AD1D4",activebackground='#184E77', command= upstw).place(x=50,y=245)
      Up50 = Button(new_window, width=3, height=1, text='2.5mm', bd=4,cursor='hand2',fg="#12355B",bg="#9AD1D4" ,activeforeground="#9AD1D4",activebackground='#184E77', command= upsfiv).place(x=50,y=280)
      Up100 = Button(new_window, width=3, height=1, text='5mm', bd=4,cursor='hand2',fg="#12355B",bg="#9AD1D4" ,activeforeground="#9AD1D4",activebackground='#184E77', command= upshun).place(x=115,y=245)
      Up200 = Button(new_window, width=3, height=1, text='10mm', bd=4,cursor='hand2',fg="#12355B",bg="#9AD1D4" ,activeforeground="#9AD1D4",activebackground='#184E77', command= upstwo).place(x=115,y=280)
  
  
      DownLeftMotor= Label(new_window,text="Down",width=5, height=1,fg="#FDF0D5",bg="#457B9D").place(x=200,y=245)
      Down20 = Button(new_window, width=3, height=1, text='1mm', bd=4,cursor='hand2',fg="#12355B",bg="#9AD1D4" ,activeforeground="#9AD1D4",activebackground='#184E77', command= downstw).place(x=250,y=245)
      Down50 = Button(new_window, width=3, height=1, text='2.5mm', bd=4,cursor='hand2',fg="#12355B",bg="#9AD1D4" ,activeforeground="#9AD1D4",activebackground='#184E77', command= downsfiv).place(x=250,y=280)
      Down100 = Button(new_window, width=3, height=1, text='5mm', bd=4,cursor='hand2',fg="#12355B",bg="#9AD1D4" ,activeforeground="#9AD1D4",activebackground='#184E77', command= downshun).place(x=315,y=245)
      Down200 = Button(new_window, width=3, height=1, text='10mm', bd=4,cursor='hand2',fg="#12355B",bg="#9AD1D4" ,activeforeground="#9AD1D4",activebackground='#184E77', command= downstwo).place(x=315,y=280)
      #HOME POSITION
      
      HomePosition = Button(new_window, width=10, height=2, command= home ,text='Home Position', bd=5,cursor='heart',fg='#FDF0D5',bg='#723C70',activeforeground='#FDF0D5',activebackground='#455E89').place(x=150,y=325)
  MyGui= Tk()
  MyGui.geometry('800x480+10+10')
  MyGui.title('Synchronous Press Brake ^_^')
  GPIO_pins = (14, 15, 18) 
  direction= 20, 16       
  step = 21, 12
  mymotortest1 = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")
  mymotortest2 = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")
  #Angle 80
  def Angle1():
      t0=  time.time()
      mymotortest1.motor_go(False, "Full" , 820, .005, False, .05)
      #mymotortest1.motor_go(False, "Full" , 100, .01, False, .05)
      mymotortest1.motor_go(True, "Full" , 100, .01, False, .05)
      mymotortest1.motor_go(True, "Full" , 720, .005, False, .05)
      time.sleep(1)
      t1 =  time.time() - t0
      t= Label(MyGui,text= round (t1, 2) ,width=8,height=2,bg="white", activebackground="red").place(x=710,y=215)
  
  def Angle1(): 
      t0=  time.time()
      mymotortest2.motor_go(False, "Full" , 820, .005, False, .05)
      #mymotortest2.motor_go(False, "Full" , 20, .01, False, .05)
      mymotortest2.motor_go(True, "Full" , 100, .01, False, .05)
      mymotortest2.motor_go(True, "Full" , 720, .005, False, .05)
      time.sleep(1)
      t1 =  time.time() - t0
      t= Label(MyGui,text= round (t1, 2) ,width=8,height=2,bg="white", activebackground="red").place(x=710,y=215)
      
  #Angle 90
  def Angle2():
      t0=  time.time()
      mymotortest1.motor_go(False, "Full" , 700, .005, False, .05)
      mymotortest1.motor_go(False, "Full" , 100, .01, False, .05)
      mymotortest1.motor_go(True, "Full" , 100, .01, False, .05)
      mymotortest1.motor_go(True, "Full" , 700, .005, False, .05)
      time.sleep(1)
      t1 =  time.time() - t0
      t= Label(MyGui,text= round (t1, 2) ,width=8,height=2,bg="white", activebackground="red").place(x=710,y=215)
  def Angle2():
      
      t0=  time.time()
      mymotortest2.motor_go(False, "Full" , 700, .005, False, .05)
      mymotortest2.motor_go(False, "Full" , 100, .01, False, .05)
      mymotortest2.motor_go(True, "Full" , 100, .01, False, .05)
      mymotortest2.motor_go(True, "Full" , 700, .005, False, .05)
      time.sleep(1)
      t1 =  time.time() - t0
      t= Label(MyGui,text= round (t1, 2) ,width=8,height=2,bg="white", activebackground="red").place(x=710,y=215)
  #Angle 120
  def Angle3():
      
      t0=  time.time()
      mymotortest1.motor_go(False, "Full" , 670, .005, False, .05)
      mymotortest1.motor_go(False, "Full" , 100, .01, False, .05)
      mymotortest1.motor_go(True, "Full" , 100, .01, False, .05)
      mymotortest1.motor_go(True, "Full" , 670, .005, False, .05)
      time.sleep(1)
      t1 =  time.time() - t0
      t= Label(MyGui,text= round (t1, 2) ,width=8,height=2,bg="white", activebackground="red").place(x=710,y=215)
  def Angle3():
      t0=  time.time()
      mymotortest2.motor_go(False, "Full" , 670, .005, False, .05)
      mymotortest2.motor_go(False, "Full" , 100, .01, False, .05)
      mymotortest2.motor_go(True, "Full" , 100, .01, False, .05)
      mymotortest2.motor_go(True, "Full" , 670, .005, False, .05)
      time.sleep(1)
      t1 =  time.time() - t0
      t= Label(MyGui,text= round (t1, 2) ,width=8,height=2,bg="white", activebackground="red").place(x=710,y=215)
  #first thing in row=0,column=0 SheetMaterial
  Column1= Label(text="Sheet Metal's Matrial",width=25,height=3,fg="#FDF0D5",bg="#184E77",font='times 12 bold ').place(x=10,y=10)
  Materials=["stainlessteel Sheet", "Iron Sheet", "Copper Sheet"]
  clicked= StringVar()
  clicked.set(Materials[0])
  drop= OptionMenu(MyGui, clicked, *Materials)
  drop.place(x=10,y=75)
  #second thing in row=2,column=0 SheetDimenson
  SheetDimenson= Label(text="Dimension of Sheet Metal",width=25, height=1,fg="#FDF0D5",bg="#457B9D",font='times 12 bold ').place(x=10,y=165)
  #width
  WidthDimenson= Label(text="width (cm)",width=12, height=1,fg="#12355B",bg="#A8DADC",font='times 11 bold ').place(x=10,y=210)
  Width=Scale(MyGui,width=12, length=100,from_=1, to=65, orient=HORIZONTAL)
  Width.place(x=115, y=190)
  #thickness
  ThicknessDimenson= Label(text="Thickness (mm)",width=14, height=1,fg="#12355B",bg="#A8DADC",font='times 11 bold ').place(x=10,y=247)
  Thickness=Scale(MyGui,width=12,length=100, from_=0.1, to=0.5, orient=HORIZONTAL, resolution= 0.1)
  Thickness.place(x=115, y=230)
  #third thing in row=3,column=0 Angle
  Angle= Label(text="Angle",width=25,height=1,fg="#FDF0D5",bg="#457B9D",font='times 12 bold ').place(x=10,y=290)
  Angle1= Button(text='80', width=2,height=1,command = Angle1, fg="#12355B",bg="#9AD1D4" ,activeforeground="#9AD1D4",activebackground='#184E77', bd=8,cursor='hand2').place(x=10,y=320)
  Angle2= Button(text='90', width=2,height=1, command = Angle2,fg="#12355B",bg="#9AD1D4" ,activeforeground="#9AD1D4",activebackground='#184E77', bd=8,cursor='hand2').place(x=80,y=320)
  Angle3= Button(text='120', width=2,height=1,command = Angle3, fg="#12355B",bg="#9AD1D4",activeforeground="#9AD1D4",activebackground='#184E77', bd=8,cursor='hand2').place(x=150,y=320)
  #column2
  column2= Label(text="Operating Chatractristics",width=26,height=3,fg="#FDF0D5",bg="#184E77",font='times 12 bold ').place(x=290,y=10)
  #motor speed
  MotorSpeed= Label(text="Speed Of Motors",width=17,height=1,fg="#FDF0D5",bg="#457B9D",font='times 11 bold ').place(x=290,y=110)
  #operation displacement
  OperationDisplacement= Label(text="Displacements",width=17,height=1,fg="#FDF0D5",bg="#457B9D",font='times 11 bold ').place(x=290,y=170)
  #current Angle
  Currentangle= Label(text="Current Angle",width=17,height=1,fg="#FDF0D5",bg="#457B9D",font='times 11 bold ').place(x=290,y=225)
  #Number of Steps
  Steps= Label(text="Number Of Steps",width=17,height=1,fg="#FDF0D5",bg="#457B9D",font='times 11 bold ').place(x=290,y=285)
  #column3
  column3= Label(text="Work Information",width=20,height=3,fg="#FDF0D5",bg="#184E77",font=' bold ').place(x=570,y=10)
  #torque
  Torque= Label(text="T.O.M.",width=13,height=1,fg="#FDF0D5",bg="#457B9D",font='times 11 bold ').place(x=570,y=110)
  #Force
  Force= Label(text="Force",width=13,height=1,fg="#FDF0D5",bg="#457B9D",font='times 11 bold ').place(x=570,y=170)
  #Bend Time
  BendTime= Label(text="Bend Time",width=13,height=1,fg="#FDF0D5",bg="#457B9D",font='times 11 bold ').place(x=570,y=225)
  #Bend Speed
  BendSpeed= Label(text="Bend Speed",width=13,height=1,fg="#FDF0D5",bg="#457B9D",font='times 11 bold ').place(x=570,y=285)
  #Reset Control
  ResetButton=Button(MyGui, text='Reset',width=10, height=2,fg="#FDF0D5",bg="#455E89", activeforeground='#FDF0D5',activebackground='#723C70',cursor="question_arrow",bd=5,command=newWindow).place(x=570,y=350)
  MyGui.mainloop()
