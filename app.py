from tkinter import *
from mydb import Database
from tkinter import messagebox, Entry
from myapi import API
import threading

class NLPApp:



    def __init__(self):

        #create db object
        self.dbo = Database()
        self.apio = API()

        
        self.root = Tk() 
        self.root.title("NLP APP")
        self.root.iconbitmap("Resources/favicon.ico")
        self.root.geometry("400x600")
        self.root.configure(bg="#C4006E")

        self.login_gui()

        self.root.mainloop()  # GUI ko hold karke rakhta hai screen par

    
    def login_gui(self):
        self.clear() #everything on the screen will be cleared
        heading = Label(self.root, text="NLP APP", bg="#C4006E", fg="black")

        heading.pack(pady=(30, 30))  # pack displays the text on the gui
     
        heading.configure(font=("Times New Roman", 24, "bold"))

        label1 = Label(self.root, text="ENTER EMAIL", bg="#C4006E", fg="black")
        label1.pack(pady=(20, 20))

        self.email_input = Entry(self.root, width=35)  
        self.email_input.pack(pady=(5, 10), ipady =3) #ipady - internal padding in y direction(vertical)

        label2 = Label(self.root, text="ENTER PASSWORD", bg="#C4006E", fg="black")
        label2.pack(pady=(20, 20))

        self.pass_input = Entry(self.root, width=35, show = "*")  # class which helps the user to input
        self.pass_input.pack(pady=(5, 10), ipady=3)  


        login_but = Button(self.root, text = 'Login', width = 30, height = 1, command = self.perform_login) #button ko height de sakte hai, text ko nahi
        login_but.pack(pady = (10,10))

        label3 = Label(self.root, text = 'Not a member?')
        label3.pack(pady = (20,10))

        redirect_but = Button(self.root, text = "Register now", command = self.register_gui)
        redirect_but.pack(pady = (5,5))

        #redirecting to register page
    def register_gui(self):
        self.clear()

        heading = Label(self.root, text="NLP APP", bg="#C4006E", fg="black")

        heading.pack(pady=(30, 30))  
        heading.configure(font=("Times New Roman", 24, "bold", "underline"))

        label1 = Label(self.root, text="ENTER NAME", bg="#C4006E", fg="black")
        label1.pack(pady=(20, 20))

        self.name_input = Entry(self.root, width=35)  
        self.name_input.pack(pady=(5, 10), ipady=3) 

        label1 = Label(self.root, text="ENTER EMAIL", bg="#C4006E", fg="black")
        label1.pack(pady=(20, 20))

        self.email_input = Entry(self.root, width=35)  
        self.email_input.pack(pady=(5, 10), ipady=3)  

        label2 = Label(self.root, text="ENTER PASSWORD", bg="#C4006E", fg="black")
        label2.pack(pady=(20, 20))

        self.pass_input = Entry(self.root, width=35, show="*") 
        self.pass_input.pack(pady=(5, 10), ipady=3) 

        #will jump to registration function
        reg_but = Button(self.root, text='Register', width=30, height=1, command = self.perform_registration)  # button ko height de sakte hai, text ko nahi
        reg_but.pack(pady=(10, 10))

        label3 = Label(self.root, text='Already a member?')
        label3.pack(pady=(20, 10))

        redirect_but = Button(self.root, text="Login now", command=self.login_gui)
        redirect_but.pack(pady=(5, 5))


    def clear(self): 
        for i in self.root.pack_slaves():  # fetching all the slaves
            i.destroy()  


    def perform_registration(self):
        #fetch data from the gui
        name = self.name_input.get()    

        email = self.email_input.get()
        password = self.pass_input.get()

        response = self.dbo.add_data(name, email, password)

        if response:
            messagebox.showinfo("Success", "Registration successful. You can login now")
        else:
            messagebox.showinfo("Error","Email already exits")


    def perform_login(self):

        email = self.email_input.get()
        password = self.pass_input.get()

        response = self.dbo.search( email, password)

        if response:
            messagebox.showinfo("Success", "Login Successful")
            self.home_gui()
        else:
            messagebox.showinfo("Error", "Incorrect email/password"
                                )

    def home_gui (self):
        self.clear()
        #we will keep the heeding as "NLP"
        heading = Label(self.root, text="NLP APP", bg="#C4006E", fg="black")

        heading.pack(pady=(30, 30))
        heading.configure(font=("Times New Roman", 24, "bold", "underline"))

        sentiment_btn = Button(self.root , text = "Sentiment Analysis" , width = 42 , height = 5 , command =self.sentiment_gui)
        sentiment_btn.pack(pady=(35,35))

        ner_btn = Button(self.root, text="Named Entity Recognition", width=42, height=5, command=self.ner_gui)
        ner_btn.pack(pady=(35, 35))

        emotion_btn = Button(self.root, text="Emotion Prediction", width=42, height=5, command=self.emo_gui)
        emotion_btn.pack(pady=(35, 35))

        logout_but = Button(self.root, text="Logout", command=self.login_gui)
        logout_but.pack(pady=(5, 5))

        #gui for sentiment analysis page
    def sentiment_gui(self):

        self.clear()
        heading = Label(self.root, text="NLP APP", bg="#C4006E", fg="black")

        heading.pack(pady=(30, 30))
        heading.configure(font=("Times New Roman", 24, "bold", "underline"))


        heading2 = Label(self.root, text = "Sentiment Analysis", bg ="#C4006E" , fg = "black" )
        heading2.pack(pady = (20,20))
        heading2.configure(font = ("Times New Roman" , 20 ))

        label1 = Label(self.root, text = "Enter the text")
        label1.pack(pady = (10,10))

        self.sentiment_input = Entry(self.root, width=50)
        self.sentiment_input.pack(pady=(5, 10), ipady=10)

        sentiment_but = Button(self.root, text='Analyze sentiment', width=30, height=1, command=self.do_sentiment_analysis)
        sentiment_but.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root, text='',bg='#C4006E',fg='black')
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.configure(font=('Times New Roman', 11))


        goback_btn = Button(self.root, text='Go Back', command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

        #analyzing and generating results
    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)

        txt = ' '
        for i in result['sentiment']:
            txt = txt+  i+ ' -> ' + str(result['sentiment'][i]) + '\n'
            print(i, result['sentiment'][i])

        self.sentiment_result['text'] = txt

        #gui for the named entity recognition
    def ner_gui(self):

        self.clear()

        heading = Label(self.root, text = "NLP APP", bg="#C4006E" , fg = "black")
        heading.pack(pady = (30,30))
        heading.configure(font =( "Times New Roman", 24 , "bold", "underline"))

        heading2 = Label(self.root, text="Named Entity Recognition", bg="#C4006E", fg="black")
        heading2.pack(pady=(20, 20))
        heading2.configure(font=("Times New Roman", 20))

        label1 = Label(self.root, text = "Enter the text")
        label1.pack(pady=(10,10))

        self.ner_input = Entry(self.root, width = 50)
        self.ner_input.pack(pady=(5, 10), ipady=10)

        ner_but = Button(self.root, text = "Analyze text", width=30, height=1, command=self.do_ner_analysis)
        ner_but.pack(pady=(10, 10))

        self.ner_result = Label(self.root, text='', bg='#C4006E', fg='black')
        self.ner_result.pack(pady=(10, 10), ipady = 50)
        self.ner_result.configure(font=('Times New Roman', 11))

        goback_btn = Button(self.root, text='Go Back', command=self.home_gui)
        goback_btn.pack(pady=(10, 10))


        #Analyzing the texts
    def do_ner_analysis(self):
        text = self.ner_input.get()
        result = self.apio.ner_analysis(text)

        ner_results_text = []  # Create a list to store the NER results

        for dicti in result["entities"]:
            for key in dicti:
                values = dicti[key]
                ner_results_text.append(f'{key} -> {str(values)}')

        self.ner_result['text'] = '\n'.join(ner_results_text)


        #Emotion analysis page
    def emo_gui(self):

        self.clear()

        heading = Label(self.root, text = "NLP APP", bg="#C4006E" , fg = "black")
        heading.pack(pady = (30,30))
        heading.configure(font =( "Times New Roman", 24 , "bold", "underline"))

        heading2 = Label(self.root, text="Emotion Analysis", bg="#C4006E", fg="black")
        heading2.pack(pady=(20, 20))
        heading2.configure(font=("Times New Roman", 20))

        label1 = Label(self.root, text = "Enter the text")
        label1.pack(pady=(10,10))

        self.emo_input = Entry(self.root, width = 50)
        self.emo_input.pack(pady=(5, 10), ipady=10)

        ner_but = Button(self.root, text = "Analyze emotion", width=30, height=1, command=threading.Thread(target=self.do_emo_analysis).start )
        ner_but.pack(pady=(10, 10))

        self.emo_result = Label(self.root, text='', bg='#C4006E', fg='black')
        self.emo_result.pack(pady=(10, 10), ipady = 50)
        self.emo_result.configure(font=('Times New Roman', 11))

        #Function for performing emotion analysis on a text
    def do_emo_analysis(self):

        text = self.emo_input.get()
        result = self.apio.emo_analysis(text)

        txt = ' '
        for i in result['emotion']:
            txt = txt + i + ' -> ' + str(result['emotion'][i]) + '\n'
            #print(txt)

        self.emo_result['text'] = txt

nlp = NLPApp()



