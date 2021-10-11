# Student ID:1201200750
# Student Name: Chon Zi Kang


def main():
    print("======================================")
    print("\t      MENU")
    print("======================================")
    print("1.    Convert centimeter to meter")
    print("2.    Convert meter to centimeter")
    print("======================================")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        get_cm()

    elif choice == 2:
        get_meter()  

    else:
        print("Invalid choice")     


def cm_to_meter(centimeter):
    meter = centimeter / 100 
    return meter

def get_cm():
    cm = float(input("Please enter a value for centimeter : "))
    m = cm_to_meter(cm)
    print("{:.2f} centimeters equals to {:.2f} meters ".format(cm,m))

def get_meter():
    in_meter = float(input("Please enter a value for meter : "))
    in_centimeter = meter_to_cm(in_meter)
    print("{:.2f} meters equals to {:.2f} centimeters ".format(in_meter,in_centimeter))

def meter_to_cm(in_meter):
    in_cm = in_meter * 100
    return in_cm


main()



