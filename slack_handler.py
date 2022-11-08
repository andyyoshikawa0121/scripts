import requests
import json
import yaml


def slack(data, webhook_url):
    res = requests.post(webhook_url, data=data)
    print(res)

def process_notify(time, index, modelname):
  with open('./config.yaml') as f:
    args = yaml.safe_load(f)

    webhook_url = args['SlackHandler']['webhook_url']

    data = json.dumps({
      "text": f"Notify {modelname} Study.",
      "blocks": [
        {
          "type": "section",
          "text": {
            "type": "mrkdwn",
            "text": f"Model: {modelname}\nTime: {time} \nIteration: {index}"
          }
        },
      ]
    })
    slack(data, webhook_url)


if __name__ == '__main__':
    with open('./config.yaml') as f:
        args = yaml.safe_load(f)

    webhook_url = args['SlackHandler']['webhook_url']

    requests.post(webhook_url, data=json.dumps({
        "text": f"Test Post from Python",
    }))

    # process_notify("2022-11-08 13:46", 100, "MoCoGAN-HD")
