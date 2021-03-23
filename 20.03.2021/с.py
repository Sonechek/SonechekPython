minutes = int(input()) * 60
time_writing, time_sending = map(int, input().split())
messages = 0
 
minutes -= time_writing
 
if time_sending > time_writing:
    while minutes >= time_sending:
        messages += 1
        minutes -= time_sending
        
elif time_writing >= time_sending:
    while minutes >= time_sending:
        messages += 1
        minutes -= time_writing
        
 
print(messages)