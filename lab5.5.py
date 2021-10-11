# Student ID:1201200750
# Student Name: Chon Zi Kang

def main():
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("           DATA ENTRY")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    
    s_id = int(input("Enter staff id          : "))
    s_salary = float(input("Enter staff salary      : RM "))
    unit_sold = int(input("Enter total units sold  : "))

    total_bonus = get_bonus(unit_sold, s_salary)
    nett_sal = get_nett_salary(s_salary, total_bonus) 

    display(s_id, s_salary, unit_sold, total_bonus, nett_sal)

def get_bonus(in_unit_sold, in_s_salary):
    if in_unit_sold > 1000:
        bonus = in_s_salary * 0.2

    elif in_unit_sold >=501 and in_unit_sold<=1000 :
        bonus = in_s_salary * 0.1


    return bonus    

def  get_nett_salary(salary, t_bonus):
    net_salary = salary+ t_bonus
    return net_salary  

def display(dis_s_id, diss_salary, disunit_sold, distotal_bonus, disnett_sal):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("         SALARY SLIP")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Staff ID                :  ",dis_s_id)
    print("Staff salary            :  RM {:.2f}".format(diss_salary))
    print("Units sold              :  ",disunit_sold)
    print("Bonus                   :  RM {:.2f}".format(distotal_bonus))
    print("Nett Salary             :  RM {:.2f}".format(disnett_sal))
  
    








main()
