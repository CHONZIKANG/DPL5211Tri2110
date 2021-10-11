# Student ID:1201200750
# Student Name: Chon Zi Kang


def main():
    width = float(input("Enter width    :"))
    length = float(input("Enter length   :"))
    r=rectangle(width, length)
    t=triangle(width, length)

    print("Rectangle area : {:.2f}".format(r))
    print("Triangle area : {:.2f}".format(t))

def rectangle(in_width, in_length):
    rec_area = in_width* in_length
    return rec_area
    
def triangle(in_width, in_length):
    tri_area = (in_width*  in_length) /2
    return tri_area





i=0
while (i<2):
    main()

    i +=1