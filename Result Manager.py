import tkinter as tk
from tkinter import messagebox 

class ResultManager:
    def __init__(self,root):
        self.root=root
        self.root.title(' Result Manager')
        self.root.geometry('550x500')
        self.root.configure(bg="#fff3be")

        self.title_lb=tk.Label(self.root,text='Student Manager App',font=('Arial',15,'bold'),bg='#fff3be',fg='black')
        self.title_lb.pack(pady=10)

        self.btns_frame=tk.Frame(self.root,bg='#fff3be')
        self.btns_frame.pack(pady=10)

        self.add_btn=tk.Button(self.btns_frame,text='Add',font=('Arial',13,'bold'),bg="#4498be",fg='black',command=self.add)
        self.add_btn.pack(side='left',padx=10,pady=10)

        self.view_btn=tk.Button(self.btns_frame,text='view',font=('Arial',13,'bold'),bg="#4498be",fg='black',command=self.view)
        self.view_btn.pack(side='left',padx=10,pady=10)

        self.result_btn=tk.Button(self.btns_frame,text='check result',font=('Arial',13,'bold'),bg="#4498be",fg='black',command=self.check_result)
        self.result_btn.pack(side='left',padx=10,pady=10)

        self.name_lb=tk.Label(self.root,text='Student Name:',font=('Arial',12),bg='#fff3be')
        self.name_entry=tk.Entry(self.root,font=('Arial',12),width=27)

        self.marks_lb=tk.Label(self.root,text='Student Marks:',font=('Arial',12),bg='#fff3be')
        self.marks_entry=tk.Entry(self.root,font=('Arial',12),width=27)

        self.save_btn=tk.Button(self.root,text='Save',font=('Arial',13,'bold'),bg="#ee7f3e",fg='white',command=self.Save_student)
        
        self.view_text=tk.Text(self.root,bg="#cadfc2",font=('Arial',12),fg='black',width=50)

        self.Check_btn=tk.Button(self.root,text='Check',font=('Arial',13),bg='#ee7f3e',fg='white',command=self.check)
        

        self.student={}

    def view(self):
        self.name_lb.pack_forget()
        self.name_entry.pack_forget()

        self.marks_lb.pack_forget()
        self.marks_entry.pack_forget()
        self.save_btn.pack_forget()
        self.Check_btn.pack_forget()

        self.view_text.pack(pady=40,padx=20)
        if not self.student:
            messagebox.showinfo('NotFound','No Student Found!')
            self.view_text.pack_forget()

        else:
            self.view_text.delete(1.0,tk.END)

            for name,marks in self.student.items():
                self.view_text.insert('end',f'{name} : {marks}\n')

        self.view_text.pack(pady=40,padx=20)

        

    def add(self):
        self.Check_btn.pack_forget()
        self.view_text.pack_forget()

        self.name_lb.pack(pady=5)
        self.name_entry.pack(pady=5)

        self.marks_lb.pack(pady=5)
        self.marks_entry.pack(pady=5)
        self.save_btn.pack(pady=10)

        self.name_entry.focus()
        

    def Save_student(self):
        name=self.name_entry.get().strip()
        marks=self.marks_entry.get().strip()

        if not name or not marks:
            messagebox.showwarning('Invalid','pls enter both name and marks')
            return

        try:
            marks_int=int(marks)
            self.student[name]=marks_int

            self.name_entry.delete(0,tk.END)
            self.marks_entry.delete(0,tk.END)

            self.name_lb.pack_forget()
            self.name_entry.pack_forget()
            self.marks_lb.pack_forget()
            self.marks_entry.pack_forget()
            self.save_btn.pack_forget()

            messagebox.showinfo('Status','Student: added Successful')

        except ValueError:
            pass

    def check_result(self):
        self.view_text.pack_forget()
        self.marks_entry.pack_forget()
        self.marks_lb.pack_forget()
        self.save_btn.pack_forget()

        self.name_lb.pack(pady=5)
        self.name_entry.pack(pady=5)

        self.Check_btn.pack(pady=10)

    def check(self):
        entered_name=self.name_entry.get().strip()

        if entered_name in self.student:
            marks=self.student[entered_name]

            if marks>=40:
                messagebox.showinfo('Result','You Passed The Exam')
                
            else:
                messagebox.showinfo('Result','You Failed The Exam')
                

        else:
            messagebox.showinfo('NotFound','Student Not Found')

        self.name_lb.pack_forget()
        self.name_entry.pack_forget()
        self.Check_btn.pack_forget()



if __name__=="__main__":
    window=tk.Tk()
    app=ResultManager(window)
    window.mainloop()
