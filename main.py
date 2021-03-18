from dbHelper import DBHelper
def main():
    db=DBHelper()
    while True:
        print("********************")
        print()
        print("press 1 to insert new user")
        print("press 2 to display all user")
        print("press 3 to delete user")
        print("press 4 to update user")
        print("press 5 to exit program")
        print()
        try:
            choice=int(input())
            if(choice==1):
                ##insert user
                uid=int(input("Enter user id:"))
                username=input("Enter user name: ")
                userphone=input("Enter user phone: ")
                db.insert_user(uid,username,userphone)
            elif choice==2:
                ##display user
                db.fetch_all()
                pass
            elif choice==3:
                ##delete user
                userid=int(input("enter user id to which you want to delete"))
                db.delete_user(userid)
            elif choice==4:
                #update user
                userid=int(input("Enter user id you want to update:"))
                username=input("Enter  new name: ")
                userphone=input("Enter  new phone: ")
                db.update_user(userid,username,userphone)


            elif choice==5:
                break
            else:
                print("INVALID TRY AGAIN")

        except Exception as e:
            print(e)
            print("Invalid Details !Try again")


if __name__== "__main__":
    main()


#main Coding
#helper=DBHelper()
##helper.insert_user(89,"Anshika","2836652")
#helper.insert_user(2,"Maneesh","9956107998")
#helper.insert_user(4,"Neelam","283665289")
#helper.insert_user(3,"Anshi","28366577772")
#helper.delete_user(89)
#helper.update_user(2,'Poonamiya','555555682')
#helper.fetch_all()