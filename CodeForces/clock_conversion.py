# t=int(input())
# for i in range(t):
#     time=str(input())
#     # hr=int(time[0:2])
#     # if(hr>11):
#     #     print(hr-12," PM")
#     # else:
#     #     print(time,"AM")
#     print(twelve_hour_time(t))

# def twelve_hour_time(t):
#     h, m = t.split(":")
#     h = int(h)
#     if h == 0:
#         h = 12
#     elif h < 12:
#         h = str(h)
#     else:
#         h = str(h - 12)
#     if h == "0":
#         h = "12"
#     return h + ":" + m + " " + ("PM" if h != "12" else "AM")

# t=int(input())
# for i in range(t):
#     time=str(input())
#     print(twelve_hour_time(time))

# Function to convert time from 24-hour format to 12-hour format
def convert_time_to_12_hour_format(time):
    hour, minute = map(int, time.split(":"))
    
    if hour < 12:
        period = "AM"
        if hour == 0:
            hour = 12
    else:
        period = "PM"
        if hour > 12:
            hour -= 12
    
    
    hour_str = str(hour).zfill(2)
    minute_str = str(minute).zfill(2)
    
    
    return f"{hour_str}:{minute_str} {period}"


t = int(input())

for _ in range(t):
    time_24_hour = input()
    
    print(convert_time_to_12_hour_format(time_24_hour))
