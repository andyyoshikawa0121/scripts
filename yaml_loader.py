import yaml

def yaml_loader():
  with open('./config.yaml') as f:
      args = yaml.safe_load(f)
  with open('./config_local.yaml') as fl:
    args_local = yaml.safe_load(fl)

  args.update(args_local)
  return args