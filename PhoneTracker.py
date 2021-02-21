import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

user_phone = input("Please provide phone number starting with area code: ex, +1215555555 ")
country_location = phonenumbers.parse(user_phone, "CH")
print(geocoder.description_for_number(country_location, "en"))

service_carrier = phonenumbers.parse(user_phone, "RO")
print(carrier.name_for_number(service_carrier, "en"))
