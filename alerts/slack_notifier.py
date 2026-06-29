import urllib.request
import json
import os

def send_slack_alert(message):
    webhook_url = os.environ.get("SLACK_WEBHOOK_URL")
    if not webhook_url:
        print("[Slack] No webhook configured, skipping.")
        return
    payload = json.dumps({"text": message}).encode("utf-8")
    req = urllib.request.Request(webhook_url, data=payload, headers={"Content-Type": "application/json"})
    urllib.request.urlopen(req)
    print("[Slack] Alert sent.")
