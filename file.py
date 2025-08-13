# postgres on docker
import psycopg2
import datetime
from flask import Flask, request, jsonify

def new_record():
        id = []
        name = []
        email = []
        phone_number = []
        id.append(input("Enter ID: "))
        name.append(input("Enter Name: "))
        email.append(input("Enter email: "))
        phone_number.append(input("Enter phone number: "))
        return id, name, email, phone_number

records = list(new_record())
for _ in records:
    id = records[0]
    name = records[1]
    email = records[2]
    phone_number = records[3]

# register for a loan
def register(id, name, email, phone_number):
    # establish a database connection
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="postgres",
            port="5432"
        )
        cursor = connection.cursor()

        # add register info to the db
        try:
            query = "INSERT INTO tbloan(id,name,email,phone_number) VALUES (%s, %s, %s, %s);"
            data = (id, name, email, phone_number)
            cursor.execute(query, data)
            connection.commit()
            print("Record Inserted Successfully")

        except (Exception, psycopg2.Error) as error:
            print("Could not insert records into database: ", error)

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error Connecting to the database: ", error)

register(id, name, email, phone_number)

# apply for a loan
def apply_loan(id):
    if id:
        print("Proceed:")
        id = id
        user_id = []
        amount = []
        status = []
        created_at = []
        updated_at = []
        user_id.append(input("Enter user_id: "))
        amount.append(input("Enter amount: "))
        status.append(input("Enter status: "))
        updated_at.append(input("Enter updated_at: "))

        loanrecords = list(apply_loan(id))
        for _ in loanrecords:
            id = id
            user_id = loanrecords[0]
            amount = loanrecords[1]
            status = loanrecords[2]
            created_at = datetime.datetime.now()
            updated_at = loanrecords[4]

        # register for a loan
        def apply(id, user_id, amount, status, created_at, updated_at):
            # apply for loan
            try:
                connection = psycopg2.connect(
                    host="localhost",
                    database="postgres",
                    user="postgres",
                    password="postgres",
                    port="5432"
                )
                cursor = connection.cursor()
                query = "INSERT INTO tbloanrequest(id,user_id,amount, status, created_at, updated_at) VALUES (%s,%s,%s %s, %s, %s);"
                data = (id, user_id, amount, status, created_at, updated_at)
                cursor.execute(query, data)
                connection.commit()
                print("Record Inserted Successfully")
            # got stuck records not getting inserted

            except (Exception, psycopg2.DatabaseError) as error:
                print(f"Error Connecting to the database: ", error)

            apply(id, user_id, amount, status, created_at, updated_at)
    else:
        print("Register First: ")
        new_record()

apply_loan(id)