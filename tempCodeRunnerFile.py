    mycursor.execute("SELECT * FROM "+str(row[0][6])+" WHERE id = 1")
        row = mycursor.fetchone()
        attend = list(row)[2:-1]