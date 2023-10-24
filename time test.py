def add_time(current_time, added_time, day = "None"):
    #extracting values
    base_time = current_time.split()
    base_time_values = base_time[0]
    base_time_components = base_time_values.split(":")
    base_time_hour = int(base_time_components[0])
    base_time_minutes = int(base_time_components[1])
    ampm = base_time[1]

    add_time = added_time.split(":")
    add_time_hour = int(add_time[0])
    add_time_minutes = int(add_time[1])
    #variables we have to keep
    elapsed_days = 0
    result_hour = 0
    minutes_sum = 0
    minutes_sum = base_time_minutes + add_time_minutes
    switch_count = 0
    new_result_hour = 0
    remainder_hour2 = 0
    final_result = ""
    #counting the days
    if add_time_hour >= 24:
        elapsed_days = elapsed_days + add_time_hour/24
        elapsed_days = round(elapsed_days)
        add_time_hour = add_time_hour%24
        
    #counting minutes and adding to hour
    if minutes_sum >= 60:
        minutes_sum = minutes_sum - 60
        remainder_hour2 = 1
    #calculating result hour
    result_hour =  remainder_hour2 + base_time_hour + add_time_hour
    #making sure it can't be more than 12 and figuring out if it switches AM or PM and how many times
    if result_hour >= 12:
        new_result_hour = result_hour%12
        switch_count = result_hour/12
        switch_count = int(switch_count)
    else:
        new_result_hour = result_hour
    #check if we add days with 
    
    if ampm == "PM" and switch_count == 2:
        elapsed_days += 1
        if new_result_hour == 0:
            new_result_hour = 12
        switch_count = 0
    
    if ampm == "AM" and switch_count == 2:
        elapsed_days += 1
        if new_result_hour == 0:
            new_result_hour = 12
    
    if ampm == "AM" and switch_count == 1:
        ampm = "PM"
        switch_count = 0
        if new_result_hour == 0:
            new_result_hour = 12
    if ampm == "PM" and switch_count == 1:
        elapsed_days += 1
        ampm = "AM"
        if new_result_hour == 0:
            new_result_hour = 12
    
    #convert minutes to str in case it is only one digit
    minutes_sum = str(minutes_sum)
    new_result_hour = str(new_result_hour)
    if len(minutes_sum) == 1:
        minutes_sum = "0"+minutes_sum
    #getting the results, if day of the week is not given
    if day == "None":
        if elapsed_days == 0:
           final_result = new_result_hour+":"+minutes_sum+" "+ampm
           return final_result
        elif elapsed_days == 1:
            final_result = new_result_hour+":"+minutes_sum+" "+ampm+" (next day)"
            return final_result
        else:
            elapsed_days = str(elapsed_days)
            final_result = new_result_hour+":"+minutes_sum+" "+ampm+" ("+elapsed_days+" days later)"
            return final_result
    #getting the results, if day of the week is given
    if day != "None":
        day = day.lower()
        day = day.capitalize()
        new_day = ""
        #I couldn't figure out if there was an efficient way to do this, but I ended up doing it one by one
        if day == "Monday":
            if elapsed_days%7 == 1:
                new_day = "Tuesday"
            elif elapsed_days%7 == 2:
                new_day = "Wednesday"
            elif elapsed_days%7 == 3:
                new_day = "Thursday"
            elif elapsed_days%7 == 4:
                new_day = "Friday"
            elif elapsed_days%7 == 5:
                new_day = "Saturday"
            elif elapsed_days%7 == 6:
                new_day = "Sunday"
            elif elapsed_days%7 == 0:
                new_day = day
        elif day == "Tuesday":
            if elapsed_days%7 == 1:
                new_day = "Wednesday"
            elif elapsed_days%7 == 2:
                new_day = "Thursday"
            elif elapsed_days%7 == 3:
                new_day = "Friday"
            elif elapsed_days%7 == 4:
                new_day = "Saturday"
            elif elapsed_days%7 == 5:
                new_day = "Sunday"
            elif elapsed_days%7 == 6:
                new_day = "Monday"
            elif elapsed_days%7 == 0:
                new_day = day
        elif day == "Wednesday":
            if elapsed_days%7 == 1:
                new_day = "Thursday"
            elif elapsed_days%7 == 2:
                new_day = "Friday"
            elif elapsed_days%7 == 3:
                new_day = "Saturday"
            elif elapsed_days%7 == 4:
                new_day = "Sunday"
            elif elapsed_days%7 == 5:
                new_day = "Monday"
            elif elapsed_days%7 == 6:
                new_day = "Tuesday"
            elif elapsed_days%7 == 0:
                new_day = day
        elif day == "Thursday":
            if elapsed_days%7 == 1:
                new_day = "Friday"
            elif elapsed_days%7 == 2:
                new_day = "Saturday"
            elif elapsed_days%7 == 3:
                new_day = "Sunday"
            elif elapsed_days%7 == 4:
                new_day = "Monday"
            elif elapsed_days%7 == 5:
                new_day = "Tuesday"
            elif elapsed_days%7 == 6:
                new_day = "Wednesday"
            elif elapsed_days%7 == 0:
                new_day = day
        elif day == "Friday":
            if elapsed_days%7 == 1:
                new_day = "Saturday"
            elif elapsed_days%7 == 2:
                new_day = "Sunday"
            elif elapsed_days%7 == 3:
                new_day = "Monday"
            elif elapsed_days%7 == 4:
                new_day = "Tuesday"
            elif elapsed_days%7 == 5:
                new_day = "Wednesday"
            elif elapsed_days%7 == 6:
                new_day = "Thursday"
            elif elapsed_days%7 == 0:
                new_day = day
        elif day == "Saturday":
            if elapsed_days%7 == 1:
                new_day = "Sunday"
            elif elapsed_days%7 == 2:
                new_day = "Monday"
            elif elapsed_days%7 == 3:
                new_day = "Tuesday"
            elif elapsed_days%7 == 4:
                new_day = "Wednesday"
            elif elapsed_days%7 == 5:
                new_day = "Thursday"
            elif elapsed_days%7 == 6:
                new_day = "Friday"
            elif elapsed_days%7 == 0:
                new_day = day
        elif day == "Sunday":
            if elapsed_days%7 == 1:
                new_day = "Monday"
            elif elapsed_days%7 == 2:
                new_day = "Tuesday"
            elif elapsed_days%7 == 3:
                new_day = "Wednesday"
            elif elapsed_days%7 == 4:
                new_day = "Thursday"
            elif elapsed_days%7 == 5:
                new_day = "Friday"
            elif elapsed_days%7 == 6:
                new_day = "Saturday"
            elif elapsed_days%7 == 0:
                new_day = day
        if elapsed_days == 0:
            final_result = new_result_hour+":"+minutes_sum+" "+ampm+", "+new_day
            return final_result
        elif elapsed_days == 1:
            final_result = new_result_hour+":"+minutes_sum+" "+ampm+", "+new_day+" (next day)"
            return final_result
        else:
            elapsed_days = str(elapsed_days)
            final_result = new_result_hour+":"+minutes_sum+" "+ampm+", "+new_day+ " ("+elapsed_days+" days later)"
            return final_result
    

x = add_time("11:59 PM", "24:05", "Wednesday")
print(x)