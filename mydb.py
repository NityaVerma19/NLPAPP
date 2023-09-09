import json

class Database:

    def add_data(self, name, email, password):

        with open ("db.json", "r") as rf:
            database = json.load(rf)  #jitne bhi users ka data file mein hai, we eill load in this variable

        if email in database:  #agar pehle se email exists
            return 0   #registration nahi hoga
        else:
            database[email] = [name, password]  #database mein naya key banakar list mein name and passworf
            with open('db.json', 'w') as wf:
                json.dump(database, wf)
            return 1

    def search(self, email, password): #this function checks whether the user with that email exists and if the pass is corrext

        with open("db.json", "r") as rf:
            database = json.load(rf)
            if email in database:  #agar email match karta hai
                if database[email][1] == password:  #toh jo dictionary hai uska email wale key ka second item(password) match karta hai provided password se
                    return 1  #sahi hai login
                else:
                    return 0  #error
            else:
                return 0  #error





