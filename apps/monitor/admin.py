from django.contrib import admin

from apps.monitor.models import Websites, HistoricalStats, People, NotifyGroup


@admin.register(Websites)
class WebsitesAdmin(admin.ModelAdmin):
    list_display = ["site", "date_created"]


@admin.register(HistoricalStats)
class HistoricalStatsAdmin(admin.ModelAdmin):
    list_display = ["track", "uptime_counts", "downtime_counts", "date_created"]


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ["email_address", "date_created"]


@admin.register(NotifyGroup)
class NotifyGroupAdmin(admin.ModelAdmin):
    list_display = ["name", "notify", "date_created"]
