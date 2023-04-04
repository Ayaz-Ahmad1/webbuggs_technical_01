# import time
# from datetime import datetime, time, timezone, timedelta
# from accounts.utils import set_inactive_users
# from sched import scheduler
# import sched
# from django.core.management import call_command
# from django_apscheduler.jobstores import register_job

# @register_job("interval", seconds=60)
# def job(): 
#     # Set the scheduled time to today's date at 12AM UTC
#     scheduled_time = datetime.combine(datetime.utcnow().date() + timedelta(days=1), time(hour=0), tzinfo=timezone.utc)

#     # Calculate the number of seconds until the scheduled time
#     time_delta = (scheduled_time - datetime.now(timezone.utc)).total_seconds()

#     # Create the scheduler and schedule the job to repeat daily
#     scheduler = sched.scheduler(timezone.utc.timestamp, time.sleep)
#     scheduler.enter(time_delta, 1, set_inactive_users, ())
#     scheduler.run()


from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .utils import set_inactive_users

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(set_inactive_users, 'interval', seconds=60*60*24)
    scheduler.start()
    




