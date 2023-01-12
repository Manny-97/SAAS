from django.db import transaction

from apps.monitor.selectors import get_historical_stats
from apps.monitor.tasks import notify_group_of_people_via_email

import httpx
from typing import List


@transaction.atomic
def monitor_websites(websites: List[str]):

    with httpx.Client() as client:
        for website in websites:
            response, historial_stats = client.get(
                website
            ), get_historical_stats(website)

            if response.status_code == 200:

                historial_stats.uptime_counts += 1
                historial_stats.save(update_fields=["uptime_counts"])
                return f"Uptime counts has increased by 1."

            elif response.status_code in [500, 502, 503, 504]:

                historial_stats.downtime_counts += 1
                historial_stats.save(update_fields=["downtime_counts"])

                notify_group_of_people_via_email.delay(website)
                return f"Downtime counts has increased by 1."
