import json

weekdays = {str(i): day
            for i, day in enumerate(['Sunday',
                                     'Monday',
                                     'Tuesday',
                                     'Wednesday',
                                     'Thursday',
                                     'Friday',
                                     'Saturday'
                                     ])}

# print(str(weekdays))
data = json.dumps(weekdays)
print(data)
print(type(data))