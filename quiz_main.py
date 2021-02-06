from tkinter import *
from tkinter import messagebox, ttk
import time
from dbhelper import DB
from quiz_app import m


class Quiz_gui:
    def __init__(self):

        self.db = DB()
        self.m = Tk()
        self.m.title("quiz")
        self.m.minsize(500, 500)
        self.m.configure(bg='#0a3d62')
        self.login()
        self.m.mainloop()

    def colors(self):
        self.color1 = '#0a3d62'
        self.button_color = '#079992'
        self.button_color1 = '#ffffff'
        self.font1 = 'white'
        self.font2 = 'black'
        # 0a3d62
        # 182C61

    def login(self):
        self.clear()
        self.colors()

        self.label_1 = Label(self.m, text='QUIZ GAME', bg=self.color1, fg='white', font=('Times New Roman', 20))
        self.label_1.pack(pady=(42, 92))

        self.user_Frame = Frame(self.m, bg=self.color1)
        self.user_Frame.pack(pady=(15, 15))
        self.username = Label(self.user_Frame, text='Username', bg=self.color1, fg='white', font=('Arial', 10))
        self.username.grid(sticky='NW')

        self.user_input = Entry(self.user_Frame, width=40, font=('Arial', 8, 'bold'))
        self.user_input.grid(sticky='s')
        self.pswd_Frame = Frame(self.m, bg=self.color1)
        self.pswd_Frame.pack(pady=(0, 25))
        self.password = Label(self.pswd_Frame, text='Password', bg=self.color1, fg='white', font=('Arial', 10)).grid(
            sticky='NW')
        self.password_input = Entry(self.pswd_Frame, show='*', width=40, font=('Times', 9, 'bold'))
        self.password_input.grid(sticky='s')

        self.frame3 = Frame(self.m, bg=self.color1)
        self.frame3.pack()
        self.loginbutton = Button(self.frame3, text='Login', bg=self.button_color, padx=21, pady=1, fg='#ffffff',
                                  font=('Times New Roman', 12), command=lambda: self.dologin())
        self.loginbutton.pack(padx=(10, 20), side=LEFT)
        self.sign_in_button = Button(self.frame3, text='Sign in', bg=self.button_color, padx=21, pady=1, fg='#ffffff',
                                     font=('Times New Roman', 12), command=lambda: self.registration())
        self.sign_in_button.pack(side=RIGHT, padx=15)

    def dologin(self):
        self.user_name = self.user_input.get()
        print(self.user_name)
        password = self.password_input.get()
        # send this data to database llambda :land check( if user exists or not
        self.data = self.db.checklogin(self.user_name, password)
        if len(self.data) > 0:
            # print the GUI
            self.user_id = self.data[0][0]
            self.homegui()
        else:
            messagebox.showerror("Error", "Incorrect credentials")

    def clear(self):
        for i in self.m.pack_slaves():
            i.destroy()

    def registration(self):
        self.clear()
        self.label_1 = Label(self.m, text='QUIZ GAME', bg=self.color1, fg='white', font=('Arial', 20, 'bold')).pack(
            pady=(42, 22))

        self.frame2 = Frame(self.m, bg=self.color1, relief='raised')
        self.frame2.pack(pady=(5, 20))

        # email id
        self.email_Frame = Frame(self.frame2, bg=self.color1)
        self.email_Frame.pack(padx=(30, 30), pady=15)
        self.email = Label(self.email_Frame, text='Email ID', bg=self.color1, fg='white',
                           font=('Arial', 10)).grid(
            sticky='NW')
        self.email_input = Entry(self.email_Frame, width=60, font=('Times', 9, 'bold'))
        self.email_input.grid()

        # username
        self.username_Frame = Frame(self.frame2, bg=self.color1)
        self.username_Frame.pack(padx=(30, 30), pady=15)
        self.username = Label(self.username_Frame, text='Username', bg=self.color1, fg='white', font=('Arial', 10))
        self.username.grid(sticky='NW')
        self.username_input = Entry(self.username_Frame, width=60, font=('Arial', 8, 'bold'))
        self.username_input.grid()

        # first name
        self.First_Name_Frame = Frame(self.frame2, bg=self.color1)
        self.First_Name_Frame.pack(padx=(30, 30), pady=15)
        self.first_name = Label(self.First_Name_Frame, text='First Name', bg=self.color1, fg='white',
                                font=('Arial', 10))
        self.first_name.grid(sticky='NW')
        self.first_name_input = Entry(self.First_Name_Frame, width=60, font=('Arial', 8, 'bold'))
        self.first_name_input.grid(sticky='s')

        # last name
        self.Last_Name_Frame = Frame(self.frame2, bg=self.color1)
        self.Last_Name_Frame.pack(padx=(30, 30), pady=15)
        self.Last_Name = Label(self.Last_Name_Frame, text='Last Name', bg=self.color1, fg='white',
                               font=('Arial', 10)).grid(
            sticky='NW')
        self.Last_Name_input = Entry(self.Last_Name_Frame, width=60, font=('Times', 9, 'bold'))
        self.Last_Name_input.grid(sticky='s')

        # Gender
        self.gender_frame = Frame(self.frame2, bg=self.color1)
        self.gender_frame.pack(padx=(30, 30), pady=15)
        self.gender = Label(self.gender_frame, text='Gender', bg=self.color1, fg='white', font=('Arial', 10))
        self.gender.grid(sticky='NW')
        self.gender_input = ttk.Combobox(self.gender_frame, width=57, values=('Male', 'Female', 'Transgender'))
        self.gender_input.grid(sticky='s')

        # Age
        self.age_frame = Frame(self.frame2, bg=self.color1)
        self.age_frame.pack(padx=(30, 30), pady=15)
        self.age = Label(self.age_frame, text='Age', bg=self.color1, fg='white', font=('Arial', 10)).grid(sticky='NW')
        self.age_input = Spinbox(self.age_frame, width=57, from_=8, to=101)
        self.age_input.grid(sticky='s')

        # setting password
        set_pwd = Frame(self.frame2, bg=self.color1)
        set_pwd.pack(pady=15)
        self.new_password = Label(set_pwd, text='Password', bg=self.color1, fg='white', font=('Arial', 10)).grid(
            sticky='NW')
        self.new_password_input = Entry(set_pwd, show='*', width=60)
        self.new_password_input.grid(sticky='s')

        re_set_pwd = Frame(self.frame2, bg=self.color1)
        re_set_pwd.pack(pady=15)
        self.re_password = Label(re_set_pwd, text='Re-enter Password', bg=self.color1, fg='white',
                                 font=('Arial', 10)).grid(sticky='NW')
        self.re_password_input = Entry(re_set_pwd, show='*', width=60)
        self.re_password_input.grid(sticky='s')
        register = Button(self.frame2, text='Register', bg=self.button_color, fg='white', font=('Times New Roman', 12),
                          command=lambda: self.do_registration())
        register.pack(pady=(15, 8))
        go_back = Button(self.frame2, text='Go back', bg=self.button_color, fg='white', font=('Times New Roman', 12),
                         command=lambda: self.login())
        go_back.pack(pady=(4, 10))

    def do_registration(self):
        # gathering data from registration form
        email = self.email_input.get()
        username = self.username_input.get()
        fname = self.first_name_input.get()
        lname = self.Last_Name_input.get()
        gender = self.gender_input.get()
        age = self.age_input.get()
        if self.new_password_input.get() == self.re_password_input.get():
            password = self.new_password_input.get()
            response = self.db.performRegistration(email, username, fname, lname, gender, age,
                                                   password)  # sending data to database
            if (response == 0):
                messagebox.showerror("Error", "User already exists")

            else:
                messagebox.showinfo("Registration Successful", "Successfully Registered")
                time.sleep(1)
                self.login()
        else:
            messagebox.showerror(' ', 'Password does not match !')

    def homegui(self):
        self.clear()
        self.colors()

        logout = Button(self.m, text='Log out', bg=self.color1, relief='flat', padx=10, activebackground=self.color1,
                        activeforeground=self.font1, fg=self.font1, font=('Times New Roman', 12),
                        command=lambda: self.login())
        logout.pack(anchor='ne', side=RIGHT)

        editprofile = Button(self.m, text='Edit Profile', bg=self.color1, relief='flat', padx=5, pady=2,
                             activebackground=self.color1,
                             activeforeground=self.font1, fg=self.font1, font=('Times New Roman', 12),
                             command=lambda: self.editprofileGUI())
        editprofile.pack(anchor='nw', side=LEFT)

        self.label_1 = Label(self.m, text='QUIZ GAME', bg=self.color1, fg='white', font=('Times New Roman', 20))
        self.label_1.pack(pady=(42, 92), padx=(0, 12))

        self.frame4 = Frame(self.m, bg=self.color1)
        self.frame4.pack()
        self.quiz_button = Button(self.frame4, text='Take Quiz', bd=5, bg=self.button_color1, padx=49, pady=1,
                                  fg=self.font2, relief='raised', font=('Times New Roman', 14),
                                  command=lambda: self.topics())
        self.quiz_button.pack(pady=(10, 25))
        self.leaderboard_button = Button(self.frame4, text='Leaderboard', bg=self.button_color1, bd=5, padx=41, pady=1,
                                         fg=self.font2, relief='raised', font=('Times New Roman', 14),
                                         command=lambda: self.show_leaderboard())
        self.leaderboard_button.pack(pady=(25, 35))

    def show_leaderboard(self):
        self.clear()

        logout = Button(self.m, text='Log out', bg=self.color1, relief='flat', padx=10, activebackground=self.color1,
                        activeforeground=self.font1, fg=self.font1, font=('Times New Roman', 12),
                        command=lambda: self.login())
        logout.pack(anchor='ne')

        title = Label(self.m, text='Leaderboard', bg=self.color1, fg='white', font=('Times New Roman', 30))
        title.pack(pady=(20, 25))

        # reading name from leaderboard
        lframe = Frame(self.m, bd=5, relief='raised', padx=5)
        lframe.pack(expand=1)
        leadernames = self.db.retrive_leaderboard_names()
        string = "ID" + "  " + "Username" + ((23 - len("Username")) * " ") + "score  "
        Label(lframe, text=string, font=('Times New Roman', 13)).pack(pady=(0, 5))

        # displaying names on window
        for i in leadernames:
            string = str(i[0]) + ".     " + i[1] + ((30 - len(i[1])) * " ") + str(i[2]) + " \n"
            Label(lframe, text=string, font=('Times New Roman', 13)).pack()

        # home button
        home_button = Button(self.m, text='Home', bg=self.color1, fg=self.font1, relief='flat',
                             font=('Times New Roman', 20), command=lambda: self.homegui())
        home_button.pack(pady=(25, 15))

    def topics(self):
        self.clear()
        self.colors()

        logout = Button(self.m, text='Log out', bg=self.color1, relief='flat', padx=10, activebackground=self.color1,
                        activeforeground=self.font1, fg=self.font1, font=('Times New Roman', 12),
                        command=lambda: self.login())
        logout.pack(anchor='ne')

        # title
        self.label_1 = Label(self.m, text='QUIZ GAME', bg=self.color1, fg='white', font=('Times New Roman', 20))
        self.label_1.pack(pady=(16, 92))

        # quiz topics
        self.frame4 = Frame(self.m, bg=self.color1)
        self.frame4.pack()
        self.history = Button(self.frame4, text='History', bd=5, bg=self.button_color1, padx=49, pady=1,
                              fg=self.font2, relief='raised',
                              font=('Times New Roman', 14), command=lambda: self.start_quiz(1))
        self.history.pack(pady=(10, 25))
        self.GK = Button(self.frame4, text='GK', bg=self.button_color1, bd=5, padx=64, pady=1,
                         fg=self.font2, relief='raised',
                         font=('Times New Roman', 14), command=lambda: self.start_quiz(2))
        self.GK.pack(pady=(25, 35))

        # home button

        home_button = Button(self.m, text='Home', bg=self.color1, fg=self.font1, relief='flat',
                             font=('Times New Roman', 20),
                             command=lambda: self.homegui())
        home_button.pack(pady=(25, 15))

    # retrieving question and answer from file
    def start_quiz(self, flag):
        self.clear()
        self.response = m(flag)
        self.index, self.r = 0, 0
        # starting the quiz part
        self.start()

    # displaying question
    def display_question(self, r):
        # self.frame1=Frame(self.m,bg='#8B008B',width=1500,height=200)
        # self.frame1.pack(expand=False,fill=None)
        # 8B008B

        # question label
        Label(self.m, bg='#0a3d62', fg='#ffffff', text=r.questions, font=('Times New Roman', 19)).pack(pady=50)

        self.var = StringVar()
        # options for the question
        b1 = Radiobutton(self.m, bg='#0a3d62', fg='#ffffff', text=r.answers[0], variable=self.var,
                         value=r.answers[0], command=lambda: self.check(r))
        b2 = Radiobutton(self.m, text=r.answers[1], bg='#0a3d62', fg='#ffffff', variable=self.var,
                         value=r.answers[1], command=lambda: self.check(r))
        b3 = Radiobutton(self.m, text=r.answers[2], variable=self.var, bg='#0a3d62', fg='#ffffff',
                         value=r.answers[2], command=lambda: self.check(r))
        b4 = Radiobutton(self.m, text=r.answers[3], variable=self.var, value=r.answers[3], bg='#0a3d62',
                         fg='#ffffff', command=lambda: self.check(r))
        b1.pack(pady=10)
        b2.pack(pady=10)
        b3.pack(pady=10)
        b4.pack(pady=(10, 20))

        # quit button
        Button(self.m, text='Quit', padx=20, relief='raised', bd=3, font=('Times New Roman', 12),
               command=lambda: self.topics() if messagebox.askquestion('.',
                                                                       'Do you want to quit the Quiz ?') == 'yes' else print(
                   'hey works')).pack(pady=10)

    # checking whether the answer is correct
    def check(self, r):
        l1 = Label(self.m)
        l1.pack()
        if self.var.get() == r.correct_answer:
            self.r += 1
            l1.configure(text='Right')
            l1.after(800, self.change())
        else:
            l1.configure(text='Wrong')
            l1.after(800, self.change())

    # jumps to next question
    def change(self):
        self.clear()

        self.start()

    # starts the quiz
    def start(self):
        fr1 = Frame(self.m, bg=self.color1)
        # if all questions are attempted then display a message
        if self.index == len(self.response):
            result = 'Your score is ' + str(self.r) + ' out of ' + str(
                len(self.response)) + '\n\n' + 'Thank you for attending the quiz.'
            Label(self.m, text=result, bd=5, pady=15, font=('Times New Roman', 12), relief='groove').pack(
                pady=(200, 90), ipadx=50)
            fr1.pack(pady=25)

            # home button
            Button(fr1, text='Home', padx=38, bg=self.button_color1, font=('Times New Roman', 12),
                   command=lambda: self.homegui()).pack(side=LEFT, padx=15)

            # leaderboard button
            Button(fr1, text='Leaderboard', padx=19, bg=self.button_color1, font=('Times New Roman', 12),
                   command=lambda: self.show_leaderboard()).pack(side=RIGHT, padx=15)

            # storing the score in database
            res = self.db.add_score(self.user_name, self.r)


        # show next question if question are remaining
        else:
            self.display_question(self.response[self.index])
            self.index += 1

    def editprofileGUI(self):
        self.clear()

        self.label_1 = Label(self.m, text='QUIZ GAME', bg=self.color1, fg='white', font=('Times New Roman', 20))
        self.label_1.pack(pady=(42, 72))

        self.ageLabel = Label(self.m, text="Set New Age:", bg=self.color1, fg='white')
        self.ageLabel.pack(padx=(10, 210))

        self.ageInput = Entry(self.m, width=45, font=('Arial', 8, 'bold'))
        self.ageInput.pack(pady=(0, 23))

        self.usernameLabel = Label(self.m, text="Enter New Username:", bg=self.color1, fg='white')
        self.usernameLabel.pack(padx=(10, 166))

        self.usernameInput = Entry(self.m, width=45, font=('Arial', 8, 'bold'))
        self.usernameInput.pack(pady=(0, 23))

        self.passwordLabel = Label(self.m, text="Enter New Password:", bg=self.color1, fg='white')
        self.passwordLabel.pack(padx=(10, 167))

        self.passwordInput = Entry(self.m, show='*', width=45, font=('Arial', 8, 'bold'))
        self.passwordInput.pack(pady=(0, 23))

        self.re_passwordLabel = Label(self.m, text="Confirm Your New Password: ", bg=self.color1, fg='white')
        self.re_passwordLabel.pack(padx=(10, 121))

        self.passwordInput = Entry(self.m, show='*', width=45, font=('Arial', 8, 'bold'))
        self.passwordInput.pack(pady=(0, 40))

        self.editBtn = Button(self.m, text="Submit", font=('Times New Roman', 12), command=lambda: self.editProfile())
        self.editBtn.pack(pady=15, ipadx=14)
        # home button
        back_button = Button(self.m, text='Home', bg=self.color1, fg=self.font1, relief='flat',
                             font=('Times New Roman', 20),
                             command=lambda: self.homegui())
        back_button.pack(pady=(25, 15))

    def editProfile(self):
        age = self.ageInput.get()
        username = self.usernameInput.get()
        password = self.passwordInput.get()
        response = self.db.editProfile(age, username, password, self.user_id, )
        if response == 1:
            messagebox.showinfo("Success", "Profile updated successfully")
        else:
            messagebox.showerror("Error", "Some error occured")


run = Quiz_gui()
