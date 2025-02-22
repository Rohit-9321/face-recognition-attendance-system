from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import student

class Face_Recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")

        #first image
        img=Image.open("D:/python program/face recognization system/imgages1/one.png")
        img=img.resize((500,130),Image.Resampling.HAMMING)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)


        #second image
        img1=Image.open("D:/python program/face recognization system/imgages1/three.png")
        img1=img1.resize((500,130),Image.Resampling.HAMMING)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #third image
        img2=Image.open("D:/python program/face recognization system/imgages1/two.png")
        img2=img2.resize((500,130),Image.Resampling.HAMMING)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)
        
        #bg image
        img3=Image.open("D:/python program/face recognization system/imgages1/background.png")
        img3=img3.resize((1530,710),Image.Resampling.HAMMING)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        #student button
        img4=Image.open("D:/python program/face recognization system/imgages1/four.png")
        img4=img4.resize((220,220),Image.Resampling.HAMMING)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img, image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220) 
        
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40) 
        
        #detect face
        img5=Image.open("D:/python program/face recognization system/imgages1/facedetector.png")
        img5=img5.resize((220,220),Image.Resampling.HAMMING)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220) 
        
        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40) 
        
        #attendance
        img6=Image.open("D:/python program/face recognization system/imgages1/attendance.png")
        img6=img6.resize((220,220),Image.Resampling.HAMMING)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220) 
        
        b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40) 
        
        #help
        img7=Image.open("D:/python program/face recognization system/imgages1/helpdes.png")
        img7=img7.resize((220,220),Image.Resampling.HAMMING)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220) 
        
        b1_1=Button(bg_img,text="Help desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40) 
        
        # Train face button
        img8=Image.open("D:/python program/face recognization system/imgages1/data.png")
        img8=img8.resize((220,220),Image.Resampling.HAMMING)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=200,y=400,width=220,height=220) 
        
        b1_1=Button(bg_img,text="Train Data",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=600,width=220,height=40) 
        
        # Photo face button
        img9=Image.open("D:/python program/face recognization system/imgages1/facedata.png")
        img9=img9.resize((220,220),Image.Resampling.HAMMING)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b1.place(x=500,y=400,width=220,height=220) 
        
        b1_1=Button(bg_img,text="Photo Face",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=600,width=220,height=40) 
        
        
        # Developer
        img10=Image.open("D:/python program/face recognization system/imgages1/developer.png")
        img10=img10.resize((220,220),Image.Resampling.HAMMING)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=400,width=220,height=220) 
        
        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=600,width=220,height=40) 
        
        #Exit button
        img11=Image.open("D:/python program/face recognization system/imgages1/exit.png")
        img11=img11.resize((220,220),Image.Resampling.HAMMING)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100,y=400,width=220,height=220) 
        
        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=600,width=220,height=40) 
        
    # ==================Functions buttons=========================

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = student(self.new_window)


        
        
         



if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_system(root)
    root.mainloop()
