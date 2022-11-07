import requests
import json
import yaml


def slack(data, webhook_url):
    requests.post(webhook_url, data=data)


if __name__ == '__main__':
    with open('./config.yaml') as f:
        args = yaml.safe_load(f)

    webhook_url = args['SlackHandler']['webhook_url']

    requests.post(webhook_url, data=json.dumps({
        "text": f"Test Post from Python",
    }))
