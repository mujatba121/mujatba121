#   variable,opraters :real life examples
#   QUESTION NO 01  FITNESS TRACKER
daily_steps=(1000,1500,2000,2500,3000,3500,4000)
distance_walked=(1,1.5,2,2.5,3,3.5,4)# distance in km
# calorie is the unit of energy
calorie_burned=(150,200,250,300,350,400,450)
average_steps_per_week=sum (daily_steps)/7
monthly_distance=sum(distance_walked)*30
print(average_steps_per_week)
print(monthly_distance)







# QUESTION NO 02    SHOPPING LIST
print("shopping list")
items=["flour","suger","salt","milk"]
quantities=[4,1.5,0.25,2]
prices=[165,135,80,200]
for item,qty,price in zip(items,quantities,prices):
    print(f"{item}:{qty}*{price}")
total_cost=(4*165)+(1.5*135)+(0.25*80)+(2*200)
budget=int(input("enter your budget"))
if budget>=total_cost:
    print(total_cost)
else:
    print("you can not buy all items")




  #QUESTION NO 03     # recipe calculater

  #ingredaint and amount
ingredaint1=3   # cup of flour
ingredaint2=2         #teaspoon of baking soda
ingredaint3=0.5      # teaspoon of suger

#number of serving
num_serving=int(input("enter num_serning"))
# calculate adjust quantities
adjust_ingredaint1=(ingredaint1/4)*num_serving(())
adjust_ingredaint2=(ingredaint2/4)*num_serving
adjust_ingredaint3=(ingredaint3/4)*num_serving

# display adjust quantities
print(f"adjust quantities for {num_serving}serving")
print(f"ingredaint1:{adjust_ingredaint1}cups")
print(f"ingredaint2:{adjust_ingredaint1}teaspoons")
print(f"ingredaint3:{adjust_ingredaint1}cups")







# question 04
user_genre=int(input("enter your prefered movie genre"))
user_rating=int(input("enter the movie prefferad ratting"))
user_release_year=int(input("enter movie release year"))
movie1={"title":"movie A","genre":"Action","ratting":8,"release_year":2020}
movie2={"title":"movie B","genre":"Drama","ratting":7,"release_year":2019}
movie3={"title":"movie C","genre":"Comedy","ratting":6,"release_year":2018}
matches=[]
#check moxie1
if user_genre.lower()==movie1["genre"].lower() and user_rating<=movie1["ratting"] and user_release_year==movie1["release_year"]:
    matches.append(movie1["title"])
# check movie2
if user_genre.lower()==movie2["genre"].lower() and user_rating<=movie2["ratting"] and user_release_year==movie2["release_year"]:
    matches.append(movie2["title"])
# check movie3
if user_genre.lower()==movie3["genre"].lower() and user_rating<=movie3["ratting"] and user_release_year==movie3["release_year"]:
    matches.append(movie3["title"])
#daily movie recomendation
if matches:
    print("recomendation movies based on your preferrece")
    for match in matches:
        print(match)
else:
    print("not matching movie founde")





#  question No 05
task1="working"
task1_duration=int(input("enter the time spent on task1{working} in hour"))
task2="reading"
task2_duration=int(input("enter time spent on task2{reading} in hour"))
task3="exercise"
task3_duration=int(input("enter time spent on task3{exercise} in hour"))
# total_time spent in each task
total_task1_time=task1_duration
total_task2_time=task2_duration
total_task3_time=task3_duration
#area for improvement
improvement_area=[]
if total_task1_time<2:
    improvement_area.append(task1)
if total_task2_time<2:
    improvement_area.append(task2)
if total_task3_time<1:
    improvement_area.append(task3)
    #display result
print("\n total time spent on {task1}:{total_task1_time}hour")
print("\n total time spent on {task2}:{total_task2_time}hour")
print("\n total time spent on {task3}:{total_task3_time}hour")

if improvement_area:
    print("\n Area for improment" )
    for area in improvement_area:
        print("speed more time om{are}")
else:
    print("keep up good work")

