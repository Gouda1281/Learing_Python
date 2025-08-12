def Day5_learning() :
    print("Day5 learning - Loops ")
    student_scores = [150,142,150,148,141,141,200,199,150,123,142,126,122,122,888]

    total_sum  =  sum(student_scores)
    print(total_sum)
    sum = 0;
    for score in student_scores:
        sum+=score;
    print(sum)

    maxscore = 0;
    for index in student_scores:
        if(index > maxscore):
            maxscore = index
            
    print(maxscore)


    # range function with for loop

    total =0 
    for index in range(1,101):  # for loop for 1 to 100 numbers - len+1 should be use in range
        total += index
        
    print(total)


    for index in range(1,101):
        if(((index % 5 )== 0) and ((index % 3 )== 0)):
         print("FizzBuzz")
        elif(index % 3 == 0):
         print("Fizz")
        elif(index % 5 == 0):
         print("Buzz")
        else:
         print(index)

