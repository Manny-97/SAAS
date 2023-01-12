from django.db import models

from apps.monitor.helpers.object_tracker import ObjectTracker


class Websites(ObjectTracker):

    site = models.URLField(unique=True)

    def __str__(self):
        return str(self.site)

    class Meta:
        db_table = "websites"
        verbose_name_plural = "Websites"


class HistoricalStats(ObjectTracker):

    track = models.OneToOneField(Websites, on_delete=models.CASCADE)
    uptime_counts = models.PositiveBigIntegerField(default=0)
    downtime_counts = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f"{self.track.site}'s historical stats"

    class Meta:
        db_table = "historical_stats"
        verbose_name_plural = "Historial Stats"


class People(ObjectTracker):

    email_address = models.EmailField(unique=True)

    def __str__(self):
        return self.email_address

    class Meta:
        db_table = "people"
        verbose_name_plural = "People"


class NotifyGroup(ObjectTracker):

    name = models.CharField(max_length=30, unique=True)
    notify = models.ForeignKey(Websites, on_delete=models.CASCADE)
    emails = models.ManyToManyField(People, related_name="people_notify_group")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "notify_group"
        verbose_name_plural = "Notify Group"
