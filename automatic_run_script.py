# pip install python-crontab

from crontab import CronTab
import datetime
 
with open('dateInfo.txt','a') as outFile:
    outFile.write('\n' + str(datetime.datetime.now()))

my_cron = CronTab(user='hamidbh')
job = my_cron.new(command='python3 /home/hamidbh/Desktop/bh/practic/check_price_coin.py')
job.minute.every(10)

my_cron.write()

# for job in my_cron:
#     if job.comment == 'dateinfo':
#         job.hour.every(1)
#         my_cron.write()
#         print('Cron job modified successfully')
