# from mysql.connector import connect
#
#
#
# select = "select * from passengers where passport_number = 12345678"
# insert = "insert into passengers(name, email, passport_number, frequent_flyer_points) values ('ZGabor', 'batman@gmail.com', '1111', 0)"
# delete = "delete from passengers where  passport_number in ('1111')"
# update = "UPDATE passengers set passport_number = '87654321' where passport_number = '12345678'"
#
# def connetor():
#     connection = connect(
#         host="127.0.0.1",
#         port=3306,
#         user="root",
#         password="Forzaarsenal96$",
#         database="airportbookingsystem"
#     )
#     return connection
#
# def crud(action):
#     connection = connetor()
#     cursor = connection.cursor()
#     cursor.execute(action)
#     connection.commit()
#     if cursor.rowcount > 0:
#         print(f"cursor.rowcount: {cursor.rowcount}")
#         print("Insert successful!")
#     else:
#         print("Insert failed.")
#     cursor.close()
#     connection.close()
#
# crud(insert)
# # crud(delete)




ytup = ("az", "anyád")
print(*ytup)


mytup1 = (1,2,3)
mytup2 = (4,5,6)
mytup3 = (1,2,3)
mytup3 = (1,5,3)

set1 = {mytup1,mytup2,mytup3}
print(set1)





















