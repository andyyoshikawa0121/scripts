import requests
import json
import yaml
import datetime


def slack(data, webhook_url):
    res = requests.post(webhook_url, data=data)
    print(res)

def process_notify(time, index, modelname):
  with open('./config.yaml') as f:
    args = yaml.safe_load(f)

    webhook_url = args['SlackHandler']['webhook_url']

    data = json.dumps({
      "attachments": [
        {
          "pretext": f"{modelname} Study Notification.",
          "color": "#AAFFAA",
          "fields": [
            {
              "title": "Parameters\n",
              "short": False,
            },
            {
              "value": f"Iterations: {index}",
              "short": False,
            },
            {
              "value": f"Time: {time}",
              "short": False,
            },
          ]
        }
      ]
    })
    slack(data, webhook_url)


if __name__ == '__main__':
    # with open('./config.yaml') as f:
    #     args = yaml.safe_load(f)

    # webhook_url = args['SlackHandler']['webhook_url']

    # requests.post(webhook_url, data=json.dumps({
    #     "text": f"Test Post from Python",
    # }))

    # process_notify(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 100, "MoCoGAN-HD")
