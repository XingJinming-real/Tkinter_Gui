import tkinter as tk
import tkinter.messagebox
import os
import re

def main():
    os.chdir('C:\\Users\\邢金明\\Desktop')
    f=open('password.txt','wt')
    f.write('admin,admin')
    f.close()
    window=tk.Tk()
    window.title('Log In')
    window.geometry('494x520')

    def view_it():
        tk.messagebox.showinfo(title='Be discreet',message=var_pw.get())
        pass

    tk.Label(window,bg='yellow',text='Welcome to the Spider-Program'.center(40)).pack()
    canvas=tk.Canvas(window,width=658,height=494)
    file_img=tk.PhotoImage(file='xjm.gif')
    img=canvas.create_image(0,0,anchor='nw',image=file_img)
    canvas.pack()

    tk.Label(window,text='User name:').place(x=50,y=400)
    tk.Label(window,text='Password:').place(x=50,y=450)
    tk.Button(window,text='View it',command=view_it).place(x=295,y=450)
    var_un=tk.StringVar()
    var_pw=tk.StringVar()
    var_un.set('Example@126.com')

    t_un=tk.Entry(window,textvariable=var_un)
    t_pw=tk.Entry(window,textvariable=var_pw,show='*')
    t_un.place(x=150,y=400)
    t_pw.place(x=150,y=450)


    def login():
        f=open('password.txt','rt')
        for i in f:
            info=i.split(',')
            user_name=info[0]
            keys[user_name]=info[1]
        if t_un.get()=='':
            tk.messagebox.showwarning(title='Warning',message='Please input your account')
            
        elif t_un.get() not in keys.keys():
            k=tk.messagebox.askquestion(title='Warning',message='You have not signed up!\
     Sign up now?')
            if k=='yes':
                sign_up()
            else:
                pass
        else:   
            if not t_pw.get()==keys[t_un.get()]:
                tk.messagebox.showinfo(title='Warning',message='Password error')
            else:
                tk.messagebox.showinfo(title='Welcome',message='Logined')
                window.destroy()
                open_new()
        pass
            
    def open_new():

        window_new=tk.Tk()
        window_new.title('Console')
        window_new.geometry('600x400')
        menubar=tk.Menu(window_new)
        back_menu=tk.Menu(menubar,tearoff=0)#  待完善menubar
        menubar.add_cascade(label='Back',menu=back_menu)
        def back_step():
            k=tk.messagebox.askquestion(title='Warning',message='Are you sure to quit out?')
            if k=='yes':
                window_new.destroy()
                main()
        back_menu.add_command(label='Back to the previous step',command=back_step)
        
        #     待完善

        #     待完善

        #     待完善
        window_new.config(menu=menubar)
        pass

    def sign_up():
        su_window=tk.Tk()
        su_window.title('Sign up')
        su_window.geometry('300x400')

        def direction():#  待完善menubar
            tk.messagebox.showinfo(title='Help',message='Input randomly whatever you want !')
            pass
        def send_email():#  待完善menubar
            tk.messagebox.showinfo(title='Send Email',message='Please send your problem to xjm0801@126.com for more help!')
        menubar=tk.Menu(su_window)
        help_menu=tk.Menu(menubar,tearoff=0)#  待完善menubar
        menubar.add_cascade(label='Help',menu=help_menu)
        help_menu.add_command(label='Directions',command=direction)
        more_menu=tk.Menu(help_menu,tearoff=0)
        help_menu.add_cascade(label='More',menu=more_menu)
        more_menu.add_command(label='Send Email',command=send_email)
        help_menu.add_separator()
        help_menu.add_command(label='Exit',command=window.quit())
        su_window.config(menu=menubar)
        
        tk.Label(su_window,text='Your email address:').place(x=20,y=50)
        e_email=tk.Entry(su_window)
        e_email.place(x=140,y=50)
        tk.Label(su_window,text='Your password:').place(x=20,y=110)
        ps=tk.Entry(su_window)
        ps.place(x=140,y=110)
        tk.Label(su_window,text='Confirm password:').place(x=20,y=170)
        ps_confirm=tk.Entry(su_window)
        ps_confirm.place(x=140,y=170)
        def sign_up_check():
            if e_email.get() in keys.keys():
                tk.messagebox.showwarning(title='Warning',message='This account has already existed')
            if not re.match(r'\w+@\w{3,8}\.com',e_email.get()):
                tk.messagebox.showerror(title='Error',message='Please rectify the pattern of your email \
    address!')
                su_window.destroy()
                sign_up()
            else:
                pass
            
            if not ps_confirm.get()==ps.get():
                tk.messagebox.showerror(title='Error',message='Please make sure your password is \
    same!')
                su_window.destroy()
                sign_up()
            else:
                keys[e_email.get()]=ps_confirm.get()
                tk.messagebox.showinfo(title='Welcome',message='Welcome '+e_email.get()+' !')
                
                f=open('password.txt','at')
                f.write('\n')
                f.write(e_email.get()+','+ps.get())
                f.close()
                open_new()
                su_window.destroy()
                window.destroy()
        check_b=tk.Button(su_window,text='Sign up',bg='yellow',command=sign_up_check)
        check_b.place(x=220,y=350)
        pass


    keys={}
    b_login=tk.Button(window,text='Log in',command=login)
    b_sign_up=tk.Button(window,text='Sign up',command=sign_up)
    b_login.place(x=350,y=480)
    b_sign_up.place(x=420,y=480)
    menubar=tk.Menu(window)
    back_menu=tk.Menu(menubar,tearoff=0)#  待完善menubar
    menubar.add_cascade(label='Back',menu=back_menu)
    def back_step():
        k=tk.messagebox.askquestion(title='Warning',message='Are you sure to quit out?')
        if k=='yes':
            window.destroy()
    back_menu.add_command(label='Back to the previous step',command=back_step)
    window.config(menu=menubar)
    window.mainloop()
main()
