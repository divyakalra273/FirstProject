#String Formating

name="Fionna"
age=22

print("Welcome to our app",name)
print("Welcome to our app %s"%(name))

print(name,"Since you are",age,"years old.You can vote.")
print("{} Since you are {} years old.You can vote.".format(name, age))
message= "{} Since you are {} years old.You can vote.".format(name, age)

#SQL query

cid=int(input("Enter Customer Id:"))
name=input("Enter your Name:")
email=input("Enter your E-mail")

sql="insert into customer values ('{}', '{}' ,'{}')".format(cid,name,email)
print("SQL",sql)

products=[2341,6737,7879,8733,7989]
for i in range(0,len(products)):
    oldprice=products[i]
    products[i]-= 0.4*products[i]
    print("{} price reduced to {}".format(oldprice,products[i]))