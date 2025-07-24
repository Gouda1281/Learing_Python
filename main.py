import Day1
import Day2
import Day3
import Day4


import enum

class Days(enum.Enum):
    DAY1 = 1
    DAY2 = 2
    DAY3 = 3
    DAY4 = 4

print("Python learning for 100 days")
print("Enter the day number to see the learning:")
Day_num_input = input()  #"Day (1-4): "

# Convert input to int safely
Day_num = Days(int(Day_num_input))

print(f"selected day number : {Day_num}")

if (Day_num == Days.DAY1):
 print("day1 print")
 Day1.Day1_learning()

elif(Day_num == Days.DAY2):
    print("day2 print")
    Day2.Day2_learning()
    Day2.BMI_calculator()
    Day2.TIP_calculator()

elif(Day_num == Days.DAY3):
     print("day3 print")
     Day3.Day3_learning()
    
elif(Day_num == Days.DAY4):
    print("day4 print")
    Day4.Day4_learning()



   
