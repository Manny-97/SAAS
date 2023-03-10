import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "saas.settings")

app = Celery("saas")

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "sync_items_to_db": {
        "task": "apps.monitor.tasks.monitor_websites_up_x_downtimes",
        "schedule": crontab(minute="*/15"),
    },
}