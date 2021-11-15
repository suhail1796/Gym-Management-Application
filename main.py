'''
GYM MANAGEMENT APPLICATION
PREPARED BY: SUHAIL SHAIKH

'''

# Creating class for super user
class super_user:
    def __init__(self):
        self.member=dict([]) # To store the gym member details
        self.regimen=dict([]) # To store the  work out regimen details
        
# Defining function for member creation
    def create_member(self,name,age,gender,mobile_no,email,BMI,membership_duration):
        
# Super user can view the gym member details by entering mobile number, hence mobile number will be key for dictionary member
        self.member[mobile_no]={}    
        self.member[mobile_no]["name"]=name
        self.member[mobile_no]["age"]=age
        self.member[mobile_no]["gender"]=gender
        self.member[mobile_no]["mobile_no"]=mobile_no
        self.member[mobile_no]["email"]=email
        self.member[mobile_no]["BMI"]=float(BMI)
        self.member[mobile_no]["membership_duration"]=int(membership_duration)

# Function for viewing the gym member details. Super user can view the gym member details by choosing the option 2 'view member'      
    def view_member(self):
        for i in self.member.keys():
            print("Full Name:",self.member[mobile_no]["name"])
            print("Age:",self.member[mobile_no]["age"])
            print("Gender:",self.member[mobile_no]["gender"])
            print("Mobile No:",self.member[mobile_no]["mobile_no"])
            print("Email ID:",self.member[mobile_no]["email"])
            print("BMI:",self.member[mobile_no]["BMI"])
            print("Membership Duration:",self.member[mobile_no]["membership_duration"])

    #For removing any gym member, we have implemented pop function, which removes the entry in dictionary.Super user can do this by choosing the option 3 'delete member'. 
    def delete_member(self,mobile_no):
        return self.member.pop(mobile_no)
    
    #Function to update the gym membership. Super user can access this by entering option 4 'update membership'  
    def update_membership(self,mobile_no,membership_duration):
        self.member[mobile_no]["membership_duration"]=membership_duration
   
# Function for creating a work out regimen.Super user can create the workout regimen by choosing the option 5 'create member'
    def create_regimen(self,BMI):
        self.regimen[BMI]={}
        if BMI<=18.5:
            self.regimen[BMI]["Mon"]="CHEST"
            self.regimen[BMI]["Tue"]="BICEPS"
            self.regimen[BMI]["Wed"]="REST"
            self.regimen[BMI]["Thu"]="BACK"
            self.regimen[BMI]["Fri"]="TRICEPS"
            self.regimen[BMI]["Sat"]="REST"
            self.regimen[BMI]["Sun"]="REST"

        elif BMI>18.5 and BMI <= 25:
            self.regimen[BMI]["Mon"]="CHEST"
            self.regimen[BMI]["Tue"]="BICEPS"
            self.regimen[BMI]["Wed"]="CARDIO/ABS"
            self.regimen[BMI]["Thu"]="BACK"
            self.regimen[BMI]["Fri"]="TRICEPS"
            self.regimen[BMI]["Sat"]="LEGS"
            self.regimen[BMI]["Sun"]="REST"

        elif BMI>25 and BMI<= 30:
            self.regimen[BMI]["Mon"]="CHEST"
            self.regimen[BMI]["Tue"]="BICEPS"
            self.regimen[BMI]["Wed"]="ABS/CARDIO"
            self.regimen[BMI]["Thu"]="BACK"
            self.regimen[BMI]["Fri"]="TRICEPS"
            self.regimen[BMI]["Sat"]="LEGS"
            self.regimen[BMI]["Sun"]="CARDIO"

        elif BMI>30 and BMI<= 35:
            self.regimen[BMI]["Mon"]="CHEST"
            self.regimen[BMI]["Tue"]="BICEPS"
            self.regimen[BMI]["Wed"]="CARDIO"
            self.regimen[BMI]["Thu"]="BACK"
            self.regimen[BMI]["Fri"]="TRICEPS"
            self.regimen[BMI]["Sat"]="CARDIO"
            self.regimen[BMI]["Sun"]="CARDIO"
            
# This function will return workout regimen of gym member.Super user can do this by entering option 6-'view regimen'           
    def view_regimen(self):
        return self.regimen
    
# This function will delete the workout regimen of gym member, super user can do this by entering option 7- 'delete regimen'   
    def delete_regimen(self,BMI):
        return self.regimen.pop(BMI)

# Super user can update the workout regimen by changing the BMI of gym member, he can do this by choosing option 8-'update regi    
    def update_regimen(self,BMI,day,value):
        self.regimen[BMI][day]=value

# Creating class for gym member   
class User():
    def __init__(self,member,regimen,phone):
        self.user_profile=member[phone]
        self.user_regimen=regimen

# Function to view the user profile.This function will return user details when he/she will choose option 1-'view user profile'        
    def view_user_profile(self):
        return self.user_profile

# This function will return the corresponding workout regimen when gym member will choose option 2-'view user regimen'   
    def view_user_regimen(self):
        return self.user_regimen[self.user_profile["BMI"]]


S=super_user()
opt=True
while (opt==True):
    print("Welcome,Do you want to enter as an user or as super user")
    print("press 1 for  Super user")
    print("press 2 for user")
    val=int(input())
    if val==1:
        sup=True
        print("Congratulations You are logged in as Super User")
        while(sup==True):
            print()
            print("choose your option\n 1.Create member\n 2.View member\n 3.Delete member\n 4.Update membership\n 5.Create regimen\n 6.View regimen\n 7.Delete Regimen\n 8.Update regimen \n 9.Logout")
            num=int(input())
            if num==1:
                name=input("Enter Full Name:")
                age=int(input("Enter age:"))
                gender=input("Gender(M/F/T):")
                mobile_no=int(input("Enter mobile number:"))
                email=input("Enter your Email ID:")
                BMI=float(input("Enter your BMI(1.0-35.0):"))
                membership_duration=int(input("Enter the duration(1/3/6/12):"))
                if membership_duration in [1,3,6,12]:
                    S.create_member(name,age,gender,mobile_no,email,BMI,membership_duration)
                    S.create_regimen(BMI)
                else:
                    print("membership duration can only be 1,3,6 & 12-->Try again")
            
            elif num==2:
                print(S.view_member())

            elif num==3:
                mob=int(input("enter the mobile number of user to be deleted:"))
                S.delete_member(mob)

            elif num==4:
                mob=int(input("enter the mobile number of user to be updated:"))
                membership_duration=int(input("enter the duration upto which you want to extend:"))
                S.update_membership(mob,membership_duration)
                
            elif num==5:
                BMI_regimen=float(input("enter the BMI for regimen:"))
                S.create_regimen(BMI_regimen)

            elif num==6:
                print(S.view_regimen())

            elif num==7:
                BMI_delete=float(input("enter the BMI for regimen:"))
                try:
                    S.delete_regimen(BMI_delete)
                except:
                    print("Invalid BMI")
            elif num ==8:
                BMI_update=float(input("enter the BMI for regimen:"))
                Day=input("Enter day (Mon/Tue/Wed/Thu/Fri/Sat/Sun:)")
                value=input("Enter the Exercise name (in Capitals:)")
                try:
                    S.update_regimen(BMI_update,Day,value)
                except:
                    print("Invalid details")

            elif num==9:
                break

            else:
                print("Invalid input")
            print("Want to enter more (Y/N)?")
            sup=input()=="Y"
                  
    elif val==2:
        user1=True
        try:
            phone=int(input("please Enter the user mobile number:"))
            B=User(S.member,S.regimen,phone)
            password=input("enter password (Hint:Your full Name):")
            # Gym member should enter his first name as password
            if password == S.member[ phone]["name"]:
                print("Congratulations You are logged in as User")
                while(user1==True):
                    print("Select any :\n 1.View User Regimen \n 2.View User profile \n 3.Update Membership \n 4.Log out")
                    val=int(input())
                    if val==1:
                        try:
                            print(B.view_user_regimen())
                        except:
                            print("User regimen not present")
                    elif val==2:
                        try:
                            print(B.view_user_profile())
                        except:
                            print("User profile not present")
                    # User/Gym member can update his membership by choosing option-3 'Update Profile'        
                    elif val==3:
                        membership_duration=int(input("Enter the duration upto which you want extenxion:"))
                        try:
                            S.update_membership(phone,membership_duration)
                            print("Want to enter more (Y/N)?")
                            user1=input()=="Y"
                        except:
                            print("Invalid User Details enter again")
                    # User will be logged off after entering the option 4-Log Out
                    elif val==4:
                        break
                
                    else:
                        print("Invalid number")
            else:
                print("Invalid password")
                
        except:
            print("either user not registered or invalid entry")
            print("Want to enter more (Y/N)?")
            user1=input()=="Y"



    

