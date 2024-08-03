import tkinter
from tkinter import*
from textblob import TextBlob

root=Tk()
root.title("Spelling Checker")
root.geometry("700x400")
root.config(background="#8b3e2f")

def check_spelling():
    word=enter_text.get()
    a=TextBlob(word)
    right=str(a.correct())

    cs=Label(root,text="Correct text is:",font=("Comic Sans MS",20),bg="#8b3e2f",fg="#cdaa7d")
    cs.place(x=100,y=250)
    spell.config(text=right)

heading=Label(root,text="SPELL AND CHECK",font=("Comic Sans MS",30,"bold"),bg="#8b3e2f",fg="#cdaa7d")
heading.pack(pady=(50,0))

enter_text=Entry(root,justify="center",width=30,font=("Comic Sans MS",25),bg="white",border=2)
enter_text.pack(pady=10)
enter_text.focus()

button=Button(root,text="Check",font=("arial",20,"bold"),fg="black",bg="white",command=check_spelling)
button.pack()

spell=Label(root,font=("Comic Sans MS",20),bg="#8b3e2f",fg="#cdaa7d")
spell.place(x=350,y=250)

root.mainloop()
