# 2!!!
time = int(input('Insert time in seconds '))
if (time//3600) < 10:
    hour = '0' + str(time//3600)
else:
    hour = str(time//3600)
if ((time%3600)//60) < 10:
    min = '0' + str((time%3600)//60)
else:
    min = str(((time%3600)//60))
if ((time%3600)%60) < 10:
    sec = '0' + str((time%3600)%60)
else:
    sec = str((time%3600)%60)
print(f'{hour}:{min}:{sec}')
