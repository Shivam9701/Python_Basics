import mysql.connector
from flask import request, make_response


class user_model:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="flask_tutorial",
            )
            self.cur = self.con.cursor(dictionary=True)
            print("Connection Successful")

        except mysql.connector.Error as e:
            print(e)
            return {"message": "Connection Failed"}

    def user_getall_model(self):
        self.cur.execute("SELECT * FROM user")
        result = self.cur.fetchall()

        if len(result) > 0:
            res = make_response(result, 200)
            res.headers["Access-Control-Allow-Origin"] = "*"
            return res

        return make_response({"message": "No Data Found"}, 204)

    def user_addone_model(self, data):
        print(data)

        query = f'INSERT INTO user (Name, Email, Password, Role, Phone) VALUES ("{data["name"]}", "{data["email"]}", "{data["password"]}", "{data["role"]}", "{data["phone"]}")'

        self.cur.execute(query)
        self.con.commit()

        return make_response({"message": "Data Added Successfully"}, 201)

    def user_update_model(self, data):
        query = f'UPDATE user SET Name="{data["name"]}", Email="{data["email"]}", Password="{data["password"]}", Role="{data["role"]}", Phone="{data["phone"]}" WHERE UserID={data["id"]}'

        self.cur.execute(query)
        self.con.commit()

        if self.cur.rowcount > 0:
            return make_response({"message": "Data Updated Succesfully"}, 200)

        return make_response({"message": "No Data Found"}, 202)

    def user_delete_model(self, data):
        query = f'DELETE FROM user WHERE UserID={data["id"]}'

        self.cur.execute(query)
        self.con.commit()

        if self.cur.rowcount > 0:
            return {"message": "Data Deleted Successfully"}

        return {"message": "No Data Found"}
