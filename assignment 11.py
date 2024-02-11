

# LOGIC PROBLEMS
#   question 01
for i in range(1,4):
    n=int(input("enter n number"))
    if n>0:
        print("positive")
    elif n<0:
       print("negative")
    elif n==0:
       print("zero")



# question 02
age=int(input("enter your age"))
if age<=10:
    print("child")
elif age>10 and age<18:
    print("adult")
elif age>=18 and age<40:
    print("teenager")
else:
    print("senior")


#question 03
x=int(input("enter x number"))
y=int(input("enter y number"))
if x>y:
    print("x is greater",x)
else:
    print("y is greater",y)


#question 04
year=int(input("enter year"))
if (year%4==0 and year!=100) or (year%400==0):
    print("its is leap year")
else:
    print("its is not leap year")



# question 05
num1=int(input("enter num1"))
num2=int(input("enter num2"))
num3=int(input("enter num3"))
maximum=max(num1,num2,num3)
print(maximum)
minimum=min(num1,num2,num3)
print(minimum)



#question 06
marks=int(input("enter your marks"))
if marks>=90 and marks<=100:
    print("A grade")
elif marks>=80 and marks<=89:
    print("B grade")
elif marks>=70 and marks<=79:
    print("C grade")
if marks>=60 and marks<=69:
    print("D grade")
elif marks<60:
    print("Fail")





# simple practical problems
# question 01
price=int(input("enter the price"))
quantity=int(input("enter the quantity"))
total_cost=price*quantity
# total_cost is greater then 1000 apply 10% discount
if total_cost>1000:
    discount=0.1
    total_cost=total_cost-(total_cost*0.1)
    print(total_cost)


#question  02
temperature=int(input("enter the tempreature"))
if temperature<20:
    print("wear the jacket")
else:
    print("not wear the jacket")


# question 03
side1=int(input("enter side1"))
side2=int(input("enter side2"))
side3=int(input("enter side3"))
if (side1==side2==side3):
    print("equilateral")
elif (side1==side2) or (side2==side3) or (side1==side3):
    print("isosceles")
elif (side1!=side2!=side3):
    print("scalene")



#question 04
pin=input("Enter your PIN")
blance=1500
if pin=="4321":
    amount=int(input("enter withdrawal your amount"))
    if amount<=blance:
        blance=blance-amount
        print("withdrawal is succesfull",blance)
    else:
        print("insufficient funds")
else:
    print("invild PIN")





# question  05
month=int(input("emter the month in numbers"))
if month in [1,3,5,7,8,10,12]:
    print("31 days")
elif month in [4,6,9,11]:
    print("30 days")
elif month==2:
    print("28 or 29 days(leap year)")
else:
    print("invild month")




#question 06
year=int(input("enter the year"))
month=int(input("emter the month in numbers"))
if month==2:
    if (year%4==0 and year!=100) or (year%400==0):
        print("29 days (leap year)")
    else:
        print("28 days")
elif month in [1,3,5,7,8,10,12]:
    print("31 days")
elif month in [4,6,9,11]:
    print("30 days")
else:
    print("invild month")



# healthy  life style
#question no 01
def calculate_calorie_goal(age,weight,activity_level):
    based_calories=2000
    if activity_level=="sendentry":
        calorie_goal=based_calories*1.2
    elif activity_level=="moderate":
        calorie_goal=based_calories*1.5
    elif activity_level=="active":
        calorie_goal=based_calories*1.8
    else:
        print("inviled activity_level")
    print("your daily actovity_goal")
age=int(input("enter your age"))
weight=int(input("enter your weight in kg"))
activity_level=input("enter your activity_level(sedentry,moderate,active)")
calculate_calorie_goal(age, weight, activity_level)




#question no 02
def calculate_sleep_duration(bedtime,wakeup_time):
    sleep_duration=(wakeup_time-bedtime+24)%24
    return sleep_duration
def evaluate_sleep_quality(sleep_duration,recommend_sleep):
    if sleep_duration>=recommend_sleep:
        print("you had a good nights sleeep")
    else:
        print("considering getting more sleep for better healtg")
bedtime=int(input("enter your bedtime in( 24 hour ,22.4 for 10:30)"))
wakeup_time=int(input("enter your bedtime in 24 hour"))
recommended_sleep=7
sleep_duration=calculate_sleep_duration(bedtime, wakeup_time)
evaluate_sleep_quality(sleep_duration,recommended_sleep)




# question 03
def suggest_water_intake(weight,activity_level):
    base_intake=30
    if activity_level=="light":
        water_intake=base_intake*weight
    elif activity_level=="moderate":
        water_intake=base_intake*1.5*weight
    elif activity_level=="intense":
        water_intake=base_intake*2*weight
    else:
        print("invilid activity_level")
weight=int(input("enter your weight in kg"))
activity_level=input("enter your activity_level(light,moderate,intense)")
suggest_water_intake(weight, activity_level)




# TIME MANAGEMENT
#question 02
def pomodoro_timer(total_cycles):
    for cycle in range(total_cycles):
        print("work session srarts.focus for 25 minutes")
        time.sleep(1500)  # 25*60==1500seconds
        # 5 minutes break
        print("take 5 minutes for break")
        time.sleep(300)  # 5*60=300
    print("all total cycles")
total_cycles=int(input("enter numbers of  total_cycles of pomodoro"))
pomodoro_timer(total_cycles)



#question 03
def find_common_metting_time(availability):
    common_time_slots=set(availability[0])
    for user_availability in availability[1:]:
        common_time_slots=common_time_slots.intersection((set(user_availability)))
        if not common_time_slots:
            print("no common metting time found")
        else:
            print(f"common_metting_slots:{common_time_slots}")
user_count=int(input("enter numbers of users"))
availability=[]
for i in range(user_count):
    user_availability=int(input("enter anailability for user{i+1}(common_separated time slots):")
anailability.append(user_availability)
find_common_metting_time(availability)





