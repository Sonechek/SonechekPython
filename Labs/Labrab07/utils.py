st = str(input())
n = int(input())
count = 0
chas = int(st[0:2])
minutes = int(st[3:5])
seconds = int(st[6:8])
seconds += n
if seconds >= 60:
    while seconds >= 60:
        seconds -= 60
        count += 1
    minutes += count
    count = 0
if minutes >= 60:
    while minutes >= 60:
        minutes -=60
        count += 1
    chas += count
ch = str(chas)
minu = str(minutes)
sec = str(seconds)
if len(minu) < 2:
    m = '0' + minu
if len(sec) < 2:
    s = '0' + sec
time = ch + ':' + m + ':' + s
if len(time) == 7:
    time = '0' + time
print(time)