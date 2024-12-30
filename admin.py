

import place
import booking
import home
admin_details=[{'name':'abhi','password':'abhi'}]
class AdminLogin:
    def __init__(self,name,password):
        self.name=name
        self.password=password
    def login(self):
        for i in admin_details:
            if i.get('name')==self.name:
                print('Login Succsesfully......')
            else:
                pass
class AddServices:
    def __init__(self,new_services):
        self.new_servise=new_services
    def addService(self):
        if self.new_servise not in booking.service_list:
            booking.service_list.append(self.new_servise)
        else:
            pass
class Details:
    def registerPeoples(self):
        for i in home.l:
            print(i)
    def totalServices(self):
        for i in booking.service_list:
            print(i)
    def totalBookings(self):
        for i in booking.booking_list:
            print(i)
    def totalPlaces(self):
        for i in place.places:
            print(i)
class DeleteBooking:
    def deletebooking(self):
        dl=input('Enter the day for deleting the booking - ')
        for i in booking.booking_list:
            if dl in i:
                booking.booking_list.remove(i)
            else:
                pass
    
