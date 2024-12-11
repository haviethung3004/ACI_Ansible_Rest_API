#Import json module
import json
import yaml


def BD(filepath, output_file):
  with open(f'{filepath}', mode='r') as f:
    reader = json.load(f)
    BDs = []
    for item in reader['imdata'][0]['fvTenant']['children']:
      if 'fvBD' in item:
        bd_name =  item['fvBD']['attributes']['name']
        unicast =  item['fvBD']['attributes']['unicastRoute']
        for item in item['fvBD']['children']:
          if 'fvSubnet' in item:
            ip = item['fvSubnet']['attributes']['ip']

            BDs.append({
              'name': f"{bd_name}",
              'unicast': f"{unicast}",
              'ip': f"{ip}"
            })
    # Prepare the inventory format for Jinja template
    inventory = {
        'bds': BDs
    }
    #Output the inventory format for Jina template
    with open(output_file, 'w') as out_file:
      yaml.dump(inventory, out_file, default_flow_style=False)

# if __name__ == "__main__":


    