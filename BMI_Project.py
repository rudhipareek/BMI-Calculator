import customtkinter
from tkinter import *
from tkinter import messagebox

#creating a window
app=customtkinter.CTk() 

#personalizing window
app.geometry("500x600")# size of window
app.title("Body Mass Index")
app.config(bg="#CDC9C9")

#creating a label and adding parameters
top=Label(app,text="BMI CALCULATOR",font=('times new roman',20,'bold'),fg="#F0FFFF",bg="#181935",width=40,height=1)
top.pack()# adding label to window

#creating height label and adding parameters
H_label=Label(app,font=('times new roman',20,'bold'),fg="#F0FFFF",bg="#181935",width=37,height=4)
H_label.place(x=10, y=80)# adding label to window

#creating height text label
H_txt=Label(app,text="Height in cm",font=('times new roman',20,'bold'),fg="#F0FFFF",bg="#181935",width=37,height=2)
H_txt.place(x=10,y=60)# adding label to window

#creating weight label and adding parameters
W_label=Label(app,font=('times new roman',20,'bold'),fg="#F0FFFF",bg="#181935",width=37,height=4)
W_label.place(x=10 ,y=310)# adding label to window

#creating weight text label
W_txt=Label(app,text="Weight in kg",font=('times new roman',20,'bold'),fg="#F0FFFF",bg="#181935",width=37,height=2)
W_txt.place(x=10,y=280)# adding label to window

#entry boxes(input) and slider
height=StringVar()
weight=StringVar()

H_value=IntVar()
W_value=IntVar()

txt=StringVar()

def get_height_value():
    return H_value.get()

def slider1(event):
    return height.set(get_height_value())

def get_weight_value():
    return W_value.get()

def slider2(event):
    return weight.set(get_weight_value())


H_entry=customtkinter.CTkEntry(app,textvariable=height,bg_color="#F0FFFF",fg_color="#FFF8DC",border_width=0,font=("times new roman",23,'bold'),text_color="#181935")
H_entry.place(x=170,y=100)

W_entry=customtkinter.CTkEntry(app,textvariable=weight,bg_color="#F0FFFF",fg_color="#FFF8DC",border_width=0,font=("times new roman",23,'bold'),text_color="#181935")
W_entry.place(x=170,y=270)


H_slider=customtkinter.CTkSlider(app,variable=H_value,from_=0,to=300,width=300,bg_color="#F0FFFF",fg_color="#F0FFFF",button_hover_color="#7FFF00",command=slider1)
H_slider.place(x=100,y=140)

W_slider=customtkinter.CTkSlider(app,variable=W_value ,from_=0,to=500,width=300,bg_color="#F0FFFF",fg_color="#F0FFFF",button_hover_color="#7FFF00",command=slider2)
W_slider.place(x=100,y=310)


def BMI():
    try:
        cm = H_entry.get()           
        w = W_entry.get()
        
        if not cm and not w:
            messagebox.showerror(title="Error", message="Please insert values for height and weight.")
            return
        elif not cm :
            messagebox.showerror(title="Error", message="Please insert values for height.")
            return
        elif not w :
            messagebox.showerror(title="Error", message="Please insert values for weight.")
            return

        #converting value in float
        cm = float(cm)
        w = float(w)       

        a = (cm / 100) # cm to m
        m = a * a
        bmi = float(format(w / m, ".2f"))

        if bmi <= 18.5:
            txt.set("Underweight")
        elif 18.5 < bmi <= 24.5:
            txt.set("Normal")
        elif 24.5 < bmi <= 29.9:
            txt.set("Overweight")
        elif 29.9 < bmi <= 34.9:
            txt.set("Obese I")
        elif 34.9 < bmi <= 39.9:
            txt.set("Obese II")
        else:
            txt.set("Obese III")
        
        result1_label=customtkinter.CTkLabel(app,text=f'BMI: {bmi}',font=("times new roman",25,'bold'))
        result1_label.place(x=170,y=460)        
        result2_label=customtkinter.CTkLabel(app,textvariable=txt,font=("times new roman",25,'bold'))
        result2_label.place(x=170,y=490)           
        

    except ValueError as e:
        messagebox.showerror(title="ERROR", message="You can only input numerical values.")
    except ZeroDivisionError as e:
        messagebox.showerror(title="ERROR", message="Height Or Weight cannot be equal to zero.")
      
#creating calulate button
calc_button=customtkinter.CTkButton(app,text="CALCULATE",command=BMI,width=170,height=20,font=("times new roman", 24,'bold'),fg_color='#3D59AB',hover_color="#483D8B")
calc_button.place(x=70,y=400)

#def clear:
def clear():
    H_entry.delete(0, END)  # Clear height entry
    W_entry.delete(0, END)  # Clear weight entry
    txt.set("")  # Clear BMI interpretation text

    # Remove previously displayed BMI result labels
    for widget in app.winfo_children():
        if isinstance(widget, customtkinter.CTkLabel):
            widget.destroy()

    # Reset sliders to minimum values
    H_slider.set(0)
    W_slider.set(0)

clear_button = customtkinter.CTkButton(app, text="Clear", command=clear, width=170, height=20, font=("times new roman", 24, 'bold'), fg_color='#3D59AB', hover_color="#483D8B")
clear_button.place(x=270, y=400) 

app.mainloop()# making window visible