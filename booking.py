booking_list=[]
service_list=['washing','Engine services']
dict_booking={}
class Booking:
    def __init__(self,name,vehicle_type,vehicle_nu,day,service_type):
        self.name=name
        self.vehicle_type=vehicle_type
        self.vehicle_nu=vehicle_nu
        self.day=day
        self.service_type=service_type
    def booked(self):
        dict_booking={}
        if self.day in dict_booking:
            pass
        else:
            dict_booking['name']=self.name
            dict_booking['vehicle_type']=self.vehicle_type
            dict_booking['vehicle_nu']=self.vehicle_nu
            dict_booking['day']=self.day
            if self.service_type not in service_list:
                dict_booking['service_type']=self.service_type
            else:
                pass
            booking_list.append(dict_booking)
        