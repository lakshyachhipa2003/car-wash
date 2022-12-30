import place
import booking
import admin
temp=''
print('Welcome To The Car Wash Service!!!!')
print('user/admin')
mode=input()
d={}  
l=[]                                               
class SignUp:
    def __init__(self,username,email,password,confirm_password):
        self.name=username
        self.email=email
        self.password=password
        self.confirm_password=confirm_password
    def fillOut(self):
        d={}
        if self.name in d:
            pass
        else:
            d['name']=self.name
            d['email']=self.email
            d['password']=self.password
            l.append(d)
    def details(self):
        for i in range(0,len(d)):
            print(d['name'])
            print(d['email'])

class Login:
    def __init__(self,name,password):
        self.name=name
        self.password=password
    def login(self):
        for i in l:
            if i.get('name')==self.name:
                print('Login Succsesfully!!!!!!!!')
            else:
                pass
def choice():
    print('''Please enter your valid opertaions ----  1. SignUp
                                         2. Login
                                         3. Place
                                         4. Booking''')
    choice_user=int(input('Enter------->>>>>>>'))

    if choice_user==1:
        name=input('Enetr your name - ')
        email=input('Enter your Email - ')
        password=int(input('Enetr your password - '))
        confirm_password=int(input('Enetr your confirm password - '))
        s=SignUp(name,email,password,confirm_password)
        s.fillOut()
    elif choice_user==2:
        name=input('Enetr name - ')
        password=int(input('Enter your Password - '))
        l=Login(name,password)
        l.login()
    elif choice_user==3:
        place.places()
    elif choice_user==4:
        name=input('Enetr your name - ')
        vehicle_type=input('Enter your vehicle name - ')
        vehicle_nu=input('Enetr your vehicle number - ')
        day=input('Enetr day for booking - ')
        service_type=input('Enetr your servicing - ')
        b=booking.Booking(name,vehicle_type,vehicle_nu,day,service_type)
        b.booked()
    temp=input('you should exit or not........')
def ad():
    print('''Please enter your valid opertaions ----  1. AdminLogin
                                         2. Services
                                         3. Details
                                         4. DeleteBooking''')
    choice_user=int(input('Enter------->>>>>>>'))
    if choice_user==1:
        name=input('Enter your name - ')
        password=int(input('Enter your password - '))
        a=admin.AdminLogin(name,password)
        a.login()
    elif choice_user==2:
        new_service=input('Enetr new service - ')
        s=admin.AddServices(new_service)
        s.addService()
    elif choice_user==3:
        d=admin.Details()
        d.registerPeoples()
        d.totalBookings()
        d.totalPlaces()
        d.totalServices()
    elif choice_user==4:
        d=admin.DeleteBooking()
        d.deletebooking()
    temp=input('you should exit or not........')

if mode=='user':        
    choice()
    while temp!='exit':
        choice()
else:
    ad()
    while temp!='exit':
        ad()