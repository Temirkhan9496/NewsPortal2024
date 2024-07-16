from celery import shared_task
   from django.core.management import call_command

   @shared_task
   def send_weekly_digest():
       call_command('send_weekly_digest')