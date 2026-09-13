phoneBook = {
 "0568323222": "Amal",
 "0522222232": "Mohammed",
 "0532335983": "Khadijah",
 "0545341144": "Abdullah",
 "0545534556": "Rawan",
 "0560664566": "Faisal",
 "0567917077": "Layla"
}
phoneNumber = input("Enter the phone number: ")

if len(phoneNumber) != 10 or not phoneNumber.isdigit():
    print("invalid number!")
elif phoneNumber in phoneBook:
    print(phoneBook[phoneNumber])
else:
    print("Sorry the number is not found")

    