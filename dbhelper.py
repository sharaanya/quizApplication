import mysql.connector

class DB:
    def __init__(self):
        # connect to the database
        try:
            self.conn=mysql.connector.connect(host="localhost", user="root", password="", database="quiz")
            self.mycursor=self.conn.cursor( )
            print("Database connection succesfull")
        except:
            print("Not connected")

    def checklogin(self,username,password):
        query ="SELECT * FROM users WHERE username LIKE '{}' AND pswd LIKE '{}'".format(username,password)
        self.mycursor.execute(query)
        data=self.mycursor.fetchall()

        return data

    def performRegistration(self,email, username, fname,lname, gender,age,password):

        query="INSERT INTO users (email_id, username, f_name,l_name, gender,age,pswd) VALUES ('{}','{}','{}','{}','{}',{},'{}')".format(
            email, username, fname,lname, gender,age,password)

        try:
            self.mycursor.execute(query)
            self.conn.commit( )
            return 1
        except:
            return 0


    def editProfile(self, age, username,password, user_id):

        query = "UPDATE users SET age={},username='{}',pswd='{}' WHERE user_id={}".format(age, username,password,
                                                                                                 user_id)
        try:
            self.mycursor.execute(query)
            self.conn.commit()
            return 1
        except:
            return 0

    def add_score(self,username,score):

        query="SELECT * FROM leaderboard WHERE username LIKE '{}' ".format(username)
        self.mycursor.execute(query)
        data=self.mycursor.fetchall( )
        if len(data)>0:
            if data[0][2]<score:
                query="UPDATE leaderboard SET score={} WHERE username='{}' ".format(score,username)
                self.mycursor.execute(query)
                self.conn.commit()
                return 1

            else:
                return 0
        else:
            query="INSERT INTO leaderboard (username, score) VALUES ('{}',{})".format(username, score)
            try:
                self.mycursor.execute(query)
                self.conn.commit( )
                return 1
            except:
                return 0


    def retrive_leaderboard_names(self):
        query="SELECT * FROM leaderboard"
        self.mycursor.execute(query)
        data=self.mycursor.fetchall( )

        return data